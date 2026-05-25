# Prompt 05 — Write Test Skill Creation

## Goal
Create a reusable slash command that guides structured test generation — gathering requirements before writing any code.

## Context provided
- Project already has a working `/code-review` skill as reference
- Tests must follow project conventions: POM, WebDriverWait, conftest fixture, PEP 8
- Needed a skill that asks for missing information instead of making assumptions

## Prompt
"Bir tane skill yaratmak istiyorum test case yazan. Hangi datalar lazımsa onu istesin."

## Output evaluation
Skill created at `~/.claude/commands/write-test.md` with two phases:
- **Step 1**: Asks 5 questions before writing any code (page/URL, scenario, test data, expected result, existing page object?)
- **Step 2**: Writes page object first, then test file — following all project conventions

Accepted as-is. No iterations needed.

## Iteration notes
- "Hangi datalar lazımsa onu istesin" → Step 1 requirement gathering prevents writing tests with wrong locators or missing data
- Skill asks only what it doesn't already know — if context is provided upfront, it skips directly to Step 2
- Complements `/code-review`: write with `/write-test`, then review with `/code-review`
