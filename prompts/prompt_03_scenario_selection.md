# Prompt 03 — AI Sub-Scenario Selection

## Goal
Choose a meaningful additional UI test scenario to generate with AI assistance — one that demonstrates real QA thinking, not just page navigation.

## Context provided
- Existing suite already covers: homepage structure, careers navigation, job filters, Apply button
- Constraint: must be verifiable through UI only (no backend/email/inbox access)
- Site: insiderone.com

## Prompt
"insiderone.com için mevcut test suite'ine ek, anlamlı bir UI test senaryosu öner"

## Output evaluation
| Scenario | Decision | Reason |
|---|---|---|
| Language switcher (TR/EN) | Rejected | Pages appeared identical in both languages — no observable difference to assert |
| Get a Demo form validation | Accepted | Clear, deterministic criteria: required field errors and email format validation |
| Platform menu navigation | Not evaluated | Not needed after selecting form validation |
| Cookie consent | Not evaluated | Not needed after selecting form validation |

## Iteration notes
- Language tests require observable content differences between locales — absent here
- Form validation is a universally understood test type with binary outcomes (error visible / not visible)
- Chosen sub-scenarios: empty submit shows required field errors + invalid email shows format error
