# Prompt 04 — Test Generation and Debugging

## Goal
Generate a page object and test file for the Get a Demo form validation scenario, following existing project conventions.

## Context provided
- Target URL: https://insiderone.com/request-a-demo/
- Form is HubSpot-embedded — fields rendered dynamically by JavaScript (not in static HTML)
- Two forms on the page: main demo form (`#expandable-form`) and footer newsletter form
- Field names discovered via browser console: `firstname`, `lastname`, `email`, `jobtitle`, `company`, `phone` (tel), `how_did_you_hear_about_us_`, `industry_dropdown`

## Prompt
`/write-test` — "Get a Demo form validation testi yaz, gerekli dataları sor"

Field discovery prompt (browser console):
```javascript
document.querySelectorAll('input, select, textarea').forEach(el =>
  console.log(el.name, el.type, el.id, el.placeholder))
```

## Output evaluation

### First version — issues found
- `get_error_count()` used `presence_of_all_elements_located` → **false positive**: HubSpot pre-renders hidden error elements in the DOM before any submit; tests passed without any real interaction

### Second version — accepted
- Changed to `visibility_of_all_elements_located` → only counts errors that are actually visible on screen
- Added `scrollIntoView` before submit button click to ensure the button is in view
- Scoped all locators to `#expandable-form` to avoid targeting the footer newsletter form

## Iteration notes
- `presence_of` vs `visibility_of`: always use `visibility_of` when asserting user-facing state
- HubSpot forms pre-populate the DOM with hidden error elements — a common source of false positives
- Two forms on the same page require scoped locators; `By.NAME` alone would match both forms
