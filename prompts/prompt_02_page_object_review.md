# Prompt 02 — Page Object Code Review and Refactoring

## Goal
Review all four page objects for correctness, Selenium best practices, and PEP 8 compliance — then fix every issue found.

## Context provided
- Four page objects: `home_page.py`, `careers_page.py`, `jobs_page.py`, `job_detail_page.py`
- Existing code had mixed quality: some locators inline, some asserts inside page objects, some brittle XPath
- Real HTML from insiderone.com provided for locator verification

## Prompt
`/code-review @pages/home_page.py` (repeated for each file)

## Output evaluation

### home_page.py
Issues found and fixed:
- Asserts inside `verify_page()` moved to test file → replaced with getter methods (`is_navbar_visible()`, `is_hero_visible()`, etc.)
- Locators updated to stable selectors using real HTML (`By.ID` for navbar and footer)
- `navigate_to_careers()` kept as JS click — native click failed due to confirmed overlay on insiderone.com

### careers_page.py
Issues found and fixed:
- Magic number `window.scrollBy(0, -300)` replaced with `scrollIntoView` on the actual QA department element
- Brittle XPath for "See all teams" button replaced with CSS attribute selector
- QA link locator changed from hardcoded full URL to `href*=` partial match

### jobs_page.py
Issues found and fixed:
- `get_all_job_details()` re-fetches postings on each loop iteration to prevent stale element references
- Department retrieved via `preceding-sibling` XPath — CSS cannot traverse upward in the DOM; XPath kept intentionally
- `filter_by_location()` and `filter_by_team()` default parameters removed (values passed explicitly from test)

### job_detail_page.py
Issues found and fixed:
- `verify_page()` assert for `len(btns) > 0` kept — this is a precondition guard, not a test assertion
- `element_to_be_clickable` added before `btns[index].click()` to handle slow environments

## Iteration notes
- Assertions in page objects vs tests: page objects may contain precondition guards, never outcome assertions
- `presence_of_element_located` vs `visibility_of_element_located`: use visibility for elements the user interacts with
- JS click vs native click: always prefer native; only use JS when an overlay is confirmed
- Stale element prevention: re-fetch the element list inside the loop rather than caching it
