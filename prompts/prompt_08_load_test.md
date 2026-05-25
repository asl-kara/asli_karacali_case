# Prompt 08 — Load Test Scenarios (Locust)

## Goal
Write Locust load test scenarios for the n11.com search module — covering both happy path and unhappy path cases with realistic user behavior simulation.

## Context provided
- Target: `https://www.n11.com` search module
- Tool: Locust (Python)
- Search endpoint: `/arama?q=<keyword>`
- 1 user is sufficient per case study requirements
- Need both happy path and unhappy path scenarios

## Prompt
"n11.com arama modülü için Locust load test yaz. Happy path ve unhappy path senaryoları olsun."

## Output evaluation

### Scenarios accepted
| Scenario | Type | Decision |
|---|---|---|
| Basic keyword search — high frequency | Happy path | Accepted — `@task(3)` weight reflects real traffic distribution |
| Basic keyword search — low frequency | Happy path | Accepted — `@task(1)` for less common searches |
| Search with pagination | Happy path | Accepted — simulates user browsing page 1 then random page 2-5 |
| Empty search (`q=`) | Unhappy path | Accepted — server should handle gracefully, not crash |
| No-results keyword (`xkqzwpvmjr9999`) | Unhappy path | Accepted — expects valid "no results" page, not 5xx |
| Extremely long keyword (500 chars) | Unhappy path | Accepted — boundary test for query string length |

### Design decisions
- `name=` parameter used on all requests → groups results in Locust UI by scenario type, not raw URL
- `User-Agent` and `Accept-Language` headers added → prevents bot detection blocking requests
- `wait_time = between(1, 3)` → simulates realistic think time between requests
- Turkish keywords used for high/low frequency lists → realistic for n11.com's user base

## Iteration notes
- Task weights (`@task(3)` vs `@task(1)`) model real search frequency distribution — high-volume keywords should fire more often
- Pagination implemented as two sequential requests within one task — matches actual user flow
- `name=` grouping is critical for readable Locust reports; without it every unique URL appears as a separate entry
