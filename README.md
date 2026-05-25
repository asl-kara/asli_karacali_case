# QA Engineer Assessment Project 

A complete QA automation project covering UI end-to-end tests, API tests, and load tests, built for the QA Engineer Assessment.

---

## Project Structure

```
├── pages/                          # Page Object Model classes (Selenium UI)
│   ├── home_page.py                # Insider One homepage
│   ├── careers_page.py             # Careers page — teams & QA navigation
│   ├── jobs_page.py                # Lever.co jobs listing page
│   ├── job_detail_page.py          # Individual job detail page
│   ├── application_form_page.py    # Lever application form page
│   └── demo_page.py                # Request a Demo form page (AI sub-scenario)
├── tests/                          # UI test scenarios (Selenium + pytest)
│   ├── test_case_study_1.py        # Task 1 — Careers page E2E test
│   └── test_demo_form_validation.py # Task 1 AI Sub-Scenario — Demo form validation
├── api_tests/                      # API test scenarios (requests + pytest)
│   └── pet/
│       └── test_pet.py             # Task 3 — Petstore CRUD tests
├── load_tests/                     # Load test scenarios (Locust)
│   ├── n11_search/
│   │   └── locustfile.py           # Task 2 — n11.com search load test
│   └── requirements.txt            # Load test dependencies (locust)
├── prompts/                        # AI collaboration documentation (one file per iteration)
│   ├── prompt_01_scenario_selection.md
│   ├── prompt_02_page_object_review.md
│   ├── prompt_03_scenario_selection.md
│   ├── prompt_04_test_generation.md
│   ├── prompt_05_write_test_skill.md
│   ├── prompt_06_test_iteration.md
│   ├── prompt_07_demo_test_code_review.md
│   ├── prompt_08_load_test.md
│   └── prompt_09_api_test.md
├── conftest.py                     # Pytest fixtures — browser driver setup/teardown
├── requirements.txt                # UI & API test dependencies
├── AI_USAGE.md                     # AI collaboration reflection (4 questions)
└── README.md
```

---

## Requirements

- Python 3.10+
- Google Chrome or Firefox (latest)
- ChromeDriver / GeckoDriver — installed automatically via `webdriver-manager`

---

## Setup

```bash
# 1. Clone the repository
git clone <repo-url>
cd practice-project-1

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install UI & API test dependencies
pip install -r requirements.txt

# 4. Install load test dependencies (only needed for Task 2)
pip install -r load_tests/requirements.txt
```

---

## Running Tests

### Task 1 — UI Tests (Selenium)

Run all UI tests on Chrome (default):

```bash
pytest tests/ -v
```

Run on Firefox:

```bash
pytest tests/ -v --browser=firefox
```

Run only the main careers test:

```bash
pytest tests/test_case_study_1.py -v
```

Run only the AI sub-scenario (demo form validation):

```bash
pytest tests/test_demo_form_validation.py -v
```

### Task 3 — API Tests

```bash
pytest api_tests/ -v
```

### Task 2 — Load Tests (Locust)

Headless run with 1 user for 30 seconds:

```bash
locust -f load_tests/n11_search/locustfile.py --headless -u 1 -r 1 --run-time 30s
```

Interactive web UI (open `http://localhost:8089` after running):

```bash
locust -f load_tests/n11_search/locustfile.py
```

---

## Test Scenarios

### Task 1 — UI: Careers Page E2E (`tests/test_case_study_1.py`)

Tests the full user journey on [insiderone.com](https://insiderone.com):

| Step | What is verified |
|------|-----------------|
| 1 | Homepage loads — URL contains `insiderone.com`, correct title, navbar, hero, footer all visible |
| 2 | All expected section blocks are present (hero, social proof, capabilities, AI, channels, case study, analyst, integrations, resources, CTA) |
| 3 | Navigate to Careers page via navbar — URL and title verified |
| 4 | Click "See all teams" — all department cards appear |
| 5 | Navigate to Quality Assurance open positions — redirects to Lever jobs page |
| 6 | Filter jobs by Location: **Istanbul** and Team: **Quality Assurance** |
| 7 | All job listings verified: Position contains "Quality Assurance", Department contains "Quality Assurance", Location contains "Istanbul" |
| 8 | Filter by Location: **Istanbul, Turkiye** — same verifications repeated |
| 9 | Click "Apply" on each job — Lever application form page opens |
| 10 | Top and bottom Apply buttons both verified per job listing |

### Task 1 — UI: AI Sub-Scenario — Demo Form Validation (`tests/test_demo_form_validation.py`)

AI-generated test scenario: validates the "Request a Demo" form at [insiderone.com/request-a-demo](https://insiderone.com/request-a-demo/).

| Test | Description |
|------|-------------|
| `test_demo_form_shows_errors_on_empty_submit` | Submitting an empty form shows at least one validation error |
| `test_demo_form_treats_whitespace_as_empty` | Whitespace-only inputs still trigger validation errors |
| `test_demo_form_shows_email_error[invalid_format]` | Invalid email format (`notanemail`) triggers email error |
| `test_demo_form_shows_email_error[non_business_domain]` | Non-business email (`test@test.com`) triggers email error |

### Task 3 — API: Petstore CRUD (`api_tests/pet/test_pet.py`)

CRUD operations against [petstore.swagger.io](https://petstore.swagger.io/) `/pet` endpoints:

| Test | Scenario |
|------|----------|
| Create pet | Positive — 200 OK, pet ID in response |
| Read pet by ID | Positive — retrieved pet matches created data |
| Update pet | Positive — updated fields reflect in GET response |
| Delete pet | Positive — 200 OK, subsequent GET returns 404 |
| Get non-existent pet | Negative — 404 Not Found |
| Get invalid ID format | Negative — 400 Bad Request |
| Delete non-existent pet | Negative — 404 Not Found |
| Create with invalid content type | Negative — 415 Unsupported Media Type |

### Task 2 — Load: n11.com Search Module (`load_tests/n11_search/locustfile.py`)

Load test scenarios for the search module at [n11.com](https://www.n11.com/):

| Scenario | Weight | Type |
|----------|--------|------|
| Basic keyword search — high frequency ("laptop") | 3 | Happy path |
| Basic keyword search — low frequency ("kamera") | 2 | Happy path |
| Search with pagination (page 2) | 1 | Happy path |
| Empty search query | 1 | Unhappy path |
| No-results keyword ("xyzxyzxyz999") | 1 | Unhappy path |
| Extremely long keyword (500 chars) | 1 | Unhappy path |

---

## AI-Augmented Sub-Scenario

The demo form validation test (`tests/test_demo_form_validation.py`) was generated with Claude (Claude Code) as the AI assistant.

- See `/prompts/` for all prompt iterations with goals, context provided, output evaluations, and iteration notes.
- See `AI_USAGE.md` for reflection on context, prompt, skill, and agent concepts, validation approach, AI weaknesses encountered, and when manual coding was preferred.

---

## Notes

- The UI tests accept all cookies via the browser's cookie consent banner automatically. This is required for the Lever.co API to set job listing links dynamically on the careers page.
- All tests are designed to run end-to-end without manual intervention beyond the initial `pip install`.
- AI was **not** used for Task 2 (Load Tests) or Task 3 (API Tests). This is noted in the `/prompts/` directory.
