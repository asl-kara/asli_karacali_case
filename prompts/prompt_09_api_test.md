# Prompt 09 — API Test Scenarios (Petstore)

## Goal
Write CRUD API tests for the Petstore Swagger `/pet` endpoint covering positive and negative scenarios using Python `requests` and pytest.

## Context provided
- Target API: `https://petstore.swagger.io/v2`
- Endpoint: `/pet`
- Tool: Python `requests` library + pytest
- Need: positive (happy path) and negative scenarios

## Prompt
"Petstore Swagger API'nin pet endpointi için CRUD testleri yaz. Positive ve negative senaryolar olsun."

## Output evaluation

### Positive scenarios — `TestPetPositive`
| Test | Decision |
|---|---|
| `test_create_pet` — POST, verify id/name/status returned | Accepted |
| `test_read_pet` — GET by id, verify correct pet returned | Accepted |
| `test_update_pet` — PUT with changed name/status, verify response | Accepted |
| `test_delete_pet` — DELETE then GET, verify 404 | Accepted |

### Negative scenarios — `TestPetNegative`
| Test | Decision |
|---|---|
| `test_get_nonexistent_pet` — GET non-existent id → 404 | Accepted |
| `test_get_invalid_id_format` — GET with string id → 404 | Accepted |
| `test_delete_nonexistent_pet` — DELETE non-existent id → 404 | Accepted |
| `test_create_pet_with_invalid_content_type` — POST with `text/plain` → 400 or 415 | Accepted — `in [400, 415]` used because API behavior varies |

### Design decisions
- `created_pet` fixture handles setup and teardown — creates pet before test, deletes after via `yield`
- `VALID_PET` constant at module level — single source of truth for test data
- `BASE_URL` constant — not hardcoded in each request
- Tests grouped into `TestPetPositive` and `TestPetNegative` classes for organized output

## Iteration notes
- `created_pet` fixture prevents test order dependency — each test that needs an existing pet gets a fresh one
- `test_create_pet` cleans up manually (no fixture) since it's testing the creation itself
- `assert response.status_code in [400, 415]` — Petstore API is inconsistent on invalid content type; both are acceptable server rejections
