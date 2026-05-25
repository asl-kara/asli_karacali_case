import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2"

VALID_PET = {
    "id": 99991234,
    "name": "TestDog",
    "photoUrls": ["https://example.com/dog.jpg"],
    "status": "available",
}


@pytest.fixture
def created_pet():
    response = requests.post(f"{BASE_URL}/pet", json=VALID_PET)
    assert response.status_code == 200
    pet = response.json()
    yield pet
    requests.delete(f"{BASE_URL}/pet/{pet['id']}")


# ─── Positive Scenarios ───────────────────────────────────────────────────────

class TestPetPositive:
    def test_create_pet(self):
        response = requests.post(f"{BASE_URL}/pet", json=VALID_PET)
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == VALID_PET["id"]
        assert data["name"] == VALID_PET["name"]
        assert data["status"] == VALID_PET["status"]
        requests.delete(f"{BASE_URL}/pet/{VALID_PET['id']}")

    def test_read_pet(self, created_pet):
        response = requests.get(f"{BASE_URL}/pet/{created_pet['id']}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == created_pet["id"]
        assert data["name"] == VALID_PET["name"]

    def test_update_pet(self, created_pet):
        updated = {**VALID_PET, "name": "UpdatedDog", "status": "sold"}
        response = requests.put(f"{BASE_URL}/pet", json=updated)
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "UpdatedDog"
        assert data["status"] == "sold"

    def test_delete_pet(self, created_pet):
        pet_id = created_pet["id"]
        delete_response = requests.delete(f"{BASE_URL}/pet/{pet_id}")
        assert delete_response.status_code == 200
        get_response = requests.get(f"{BASE_URL}/pet/{pet_id}")
        assert get_response.status_code == 404


# ─── Negative Scenarios ───────────────────────────────────────────────────────

class TestPetNegative:
    def test_get_nonexistent_pet(self):
        response = requests.get(f"{BASE_URL}/pet/999999999999")
        assert response.status_code == 404

    def test_get_invalid_id_format(self):
        response = requests.get(f"{BASE_URL}/pet/invalid-id")
        assert response.status_code == 404

    def test_delete_nonexistent_pet(self):
        response = requests.delete(f"{BASE_URL}/pet/999999999999")
        assert response.status_code == 404

    def test_create_pet_with_invalid_content_type(self):
        response = requests.post(
            f"{BASE_URL}/pet",
            data="not valid json",
            headers={"Content-Type": "text/plain"},
        )
        assert response.status_code in [400, 415]
