"""
Load Test Scenarios — n11.com Search Module
============================================

Happy Path:

Scenario 1: Basic Keyword Search
  - User sends a GET request to the search endpoint with a keyword.
  - Verifies the results page loads successfully (HTTP 200).

Scenario 2: Search with Pagination
  - User searches for a keyword on page 1.
  - Then navigates to page 2 of results.
  - Simulates a user browsing through search results.

Scenario 3: Multi-Keyword Search (weighted)
  - Multiple popular keywords are searched with realistic frequency.
  - High-volume keywords are assigned higher task weights.

Unhappy Path:

Scenario 4: Empty Search
  - User submits a search with an empty query (q=).
  - Site should handle gracefully without error.

Scenario 5: Nonsense / No-Result Search
  - User searches for a random string that returns no results.
  - Site should return a valid "no results" page, not an error.

Scenario 6: Extremely Long Keyword
  - User sends a 500-character query string.
  - Site should not crash or return a 5xx error.
"""

import random

from locust import HttpUser, between, task

SEARCH_TERMS_HIGH = ["telefon", "laptop", "ayakkabı", "elbise", "kulaklık"]
SEARCH_TERMS_LOW = ["kitap", "oyuncak", "saat", "parfüm", "çanta"]

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "tr-TR,tr;q=0.9",
}


class N11SearchUser(HttpUser):
    host = "https://www.n11.com"
    wait_time = between(1, 3)

    # Scenario 1 & 3 — basic search, high-frequency keywords weighted higher
    @task(3)
    def search_high_frequency_keyword(self):
        term = random.choice(SEARCH_TERMS_HIGH)
        self.client.get(
            f"/arama?q={term}",
            headers=HEADERS,
            name="/arama?q=[high-freq-keyword]",
        )

    # Scenario 3 — low-frequency keywords
    @task(1)
    def search_low_frequency_keyword(self):
        term = random.choice(SEARCH_TERMS_LOW)
        self.client.get(
            f"/arama?q={term}",
            headers=HEADERS,
            name="/arama?q=[low-freq-keyword]",
        )

    # Scenario 4 — empty search
    @task(1)
    def search_empty_query(self):
        self.client.get(
            "/arama?q=",
            headers=HEADERS,
            name="/arama?q=[empty]",
        )

    # Scenario 5 — nonsense keyword, expects no-results page not an error
    @task(1)
    def search_no_results(self):
        self.client.get(
            "/arama?q=xkqzwpvmjr9999",
            headers=HEADERS,
            name="/arama?q=[no-results]",
        )

    # Scenario 6 — extremely long keyword
    @task(1)
    def search_long_keyword(self):
        long_term = "a" * 500
        self.client.get(
            f"/arama?q={long_term}",
            headers=HEADERS,
            name="/arama?q=[long-keyword]",
        )

    # Scenario 2 — search then paginate
    @task(2)
    def search_and_paginate(self):
        term = random.choice(SEARCH_TERMS_HIGH)
        self.client.get(
            f"/arama?q={term}",
            headers=HEADERS,
            name="/arama?q=[keyword] page=1",
        )
        page = random.randint(2, 5)
        self.client.get(
            f"/arama?q={term}&pg={page}",
            headers=HEADERS,
            name="/arama?q=[keyword] page=N",
        )
