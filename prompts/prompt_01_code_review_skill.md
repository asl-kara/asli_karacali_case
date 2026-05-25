# Prompt 01 — Code Review Skill Creation

## Goal
Create a reusable AI slash command that performs consistent, opinionated code reviews on Python Selenium test automation code.

## Context provided
- Project uses Python, Selenium, pytest, Page Object Model
- Needed a repeatable review process covering: test design, Selenium best practices, code quality, naming conventions, reliability, security
- Claude Code supports custom slash commands via `~/.claude/commands/`

## Prompt
"Bir tane skill yaratmak istiyorum code review yapan. Python Selenium test automation ile ilgili nelere bakılması gerekiyorsa onlara bakmalı, bir test automation lead gibi review yapmalı"

## Output evaluation
First version accepted with the following additions requested:
- PEP 8 naming conventions section added (PascalCase, snake_case, UPPER_SNAKE_CASE, _private_underscore)
- Output format changed from prose to numbered list for easier issue tracking
- Added closing question: "Sorunları tek tek çözelim mi?" to drive iterative fixing

## Iteration notes
- Skill file must be in `~/.claude/commands/`, not `~/.claude/skills/` (wrong path on first attempt)
- Output format matters: numbered list made it easy to work through issues one by one
- The skill carried context across all page object reviews, producing consistent findings
