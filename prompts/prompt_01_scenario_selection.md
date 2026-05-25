# Prompt 01 — Test Scenario Selection

## Goal
Identify a meaningful AI-augmented UI test scenario for insiderone.com that goes beyond the existing test suite.

## Context provided
- Existing suite covers: careers page QA job listings, filters, Apply button navigation
- Site: insiderone.com
- Constraint: scenario must be verifiable purely through UI (no backend/email access)

## Prompt
"insiderone.com için mevcut test suite'ine ek, anlamlı bir UI test senaryosu öner"

## Output evaluation
Candidates proposed by AI:
| Scenario | Decision | Reason |
|---|---|---|
| Language switcher | Rejected | TR/EN pages appeared identical — no observable difference to assert |
| Get a Demo form validation | Accepted | Clear pass/fail criteria: required field errors, email format validation |
| Platform menu navigation | Not needed | Get a Demo already selected |
| Cookie consent | Not needed | Get a Demo already selected |

## Iteration notes
- Language-based tests require observable content differences between locales — not present here
- Form validation is a classic, well-understood test type with deterministic outcomes
- Chosen scenario: **required field errors on empty submit** + **email format validation error**
