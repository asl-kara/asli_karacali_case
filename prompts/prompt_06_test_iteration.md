# Prompt 06 — Test Flow Update and New Test Cases

## Goal
Improve the demo form test by starting from the homepage (realistic E2E flow), and expand coverage with additional test scenarios.

## Context provided
- Initial test opened `/request-a-demo/` directly — not realistic, skips homepage navigation
- Screenshot showed "Get a demo" button in navbar with `href="/request-a-demo/"` and class `btn btn-primary`
- Screenshot showed a new validation: form rejects non-business email domains (e.g. test@test.com)

## Prompt
"Test demo form yanlış yerden başlıyor. Homepage'den başlamalı, sonra Get a demo butonuna basıp form sayfasına geçmeli, form elementleri görünür mü kontrol etmeli, sonra submit etmeli."

## Changes made

### Flow update
- Added `_GET_DEMO_BTN` locator and `click_get_demo()` to `HomePage`
- Added `verify_form_elements_visible()` to `DemoPage` — checks form, firstname, email, submit visible
- Test now: `home.open()` → `home.accept_cookies()` → `home.click_get_demo()` → `demo.verify_form_elements_visible()`

### New test cases added
| Test | Reason |
|---|---|
| `test_demo_form_treats_whitespace_as_empty` | Edge case: whitespace-only input should not bypass required field validation |
| `test_demo_form_rejects_non_business_email_domain` | Discovered live: form rejects test.com, gmail.com etc. — business emails only |

## Output evaluation
- Flow change: accepted immediately
- Whitespace test: accepted — all 7 text fields filled with spaces
- Non-business email test: accepted — `NON_BUSINESS_EMAIL = "test@test.com"` constant added

## Iteration notes
- Realistic E2E flow is more valuable than direct URL tests for a case study — shows full navigation path
- Edge cases discovered by manually interacting with the form, not from requirements
- Two separate email error tests identified as parametrize candidates → addressed in prompt_07
