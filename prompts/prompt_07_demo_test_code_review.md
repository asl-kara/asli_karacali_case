# Prompt 07 — Demo Page and Test Code Review

## Goal
Review `demo_page.py` and `test_demo_form_validation.py` for code quality, duplication, and best practices using the `/code-review` skill.

## Context provided
- Both files freshly written — first review pass
- `/code-review` skill used (see prompt_01 for skill definition)

## Prompt
`/code-review @pages/demo_page.py`
`/code-review @tests/test_demo_form_validation.py`

## Output evaluation

### demo_page.py — 3 issues found and fixed
| Issue | Fix |
|---|---|
| `open()` used `presence_of` for form | Changed to `visibility_of` — form may be in DOM before JS renders it visually |
| `get_error_count()` and `get_error_texts()` duplicated DOM query | `get_error_count()` now delegates to `get_error_texts()`: `return len(self.get_error_texts())` |
| 7 `fill_*` methods repeated same pattern | Extracted `_fill_field(locator, value)` private helper — each fill method is now one line |

### test_demo_form_validation.py — 3 issues found and fixed
| Issue | Fix |
|---|---|
| Same 6-line setup repeated in all 4 tests | Extracted `demo_form` pytest fixture — setup runs once, returned as `DemoPage` instance |
| Test 3 and 4 identical structure, different email only | Merged into one parametrized test with `@pytest.mark.parametrize` and `pytest.param` IDs |
| `print()` statements left in test code | Removed — were debug artifacts from false positive investigation |

## Iteration notes
- `presence_of` vs `visibility_of`: always use `visibility_of` for HubSpot forms — JS renders elements progressively
- Private `_fill_field` helper: reduces 21 lines to 7 — each public method stays named and readable
- Fixture vs repeated setup: fixture is re-created per test by default in pytest — tests stay independent
- `pytest.param` with `id=`: keeps test names readable in output (`[invalid_format]`, `[non_business_domain]`) instead of raw values
