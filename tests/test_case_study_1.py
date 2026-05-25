from selenium.webdriver.remote.webdriver import WebDriver

from pages.home_page import HomePage, EXPECTED_SECTION_CLASSES
from pages.careers_page import CareersPage
from pages.jobs_page import JobsPage
from pages.job_detail_page import JobDetailPage
from pages.application_form_page import ApplicationFormPage


def verify_and_apply_for_jobs(driver: WebDriver, jobs: JobsPage, location_label: str) -> None:
    count = jobs.verify_job_listings()
    if count == 0:
        print(f"⚠ No listings found for '{location_label}' — skipping")
        return
    print(f"✓ {count} job listing(s) found for {location_label}")

    for i, job in enumerate(jobs.get_all_job_details()):
        pos = job["position"].lower()
        assert "quality assurance" in pos or "qa" in pos, \
            f"Job {i+1}: Position '{job['position']}' does not contain 'Quality Assurance' or 'QA'"
        assert "quality assurance" in job["department"].lower(), \
            f"Job {i+1}: Department '{job['department']}' does not contain 'Quality Assurance'"
        assert location_label.lower() in job["location"].lower(), \
            f"Job {i+1}: Location '{job['location']}' does not contain '{location_label}'"
    print(f"✓ All jobs verified: Position, Department contain 'Quality Assurance' and Location contains '{location_label}'")

    for i in range(count):
        jobs.click_apply_for_job(i)
        detail = JobDetailPage(driver)
        detail.verify_page()
        detail.click_top_apply_button()
        ApplicationFormPage(driver).verify_page()
        driver.back()
        detail.verify_page()
        detail.click_bottom_apply_button()
        ApplicationFormPage(driver).verify_page()
        driver.back()
        detail.verify_page()
        driver.back()
        jobs.get_job_postings()

    print(f"✓ All Apply buttons verified — form page loaded for each job in {location_label}")


def test_insider_career_page_qa_jobs(driver):
    home = HomePage(driver)
    home.open()
    home.accept_cookies()
    assert "insiderone.com" in home.get_current_url()
    assert home.is_title_correct()
    assert home.is_navbar_visible()
    assert home.is_hero_visible()
    assert home.is_footer_visible()
    for expected in EXPECTED_SECTION_CLASSES:
        assert any(expected in cls for cls in home.get_section_classes()), \
            f"Expected section not found: {expected}"
    print("✓ Homepage loaded: URL, title, navbar, hero, all main sections, footer verified")

    home.navigate_to_careers()

    careers = CareersPage(driver)
    careers.verify_page()
    print("✓ Careers page navigation successful")

    careers.click_see_all_teams()
    print("✓ 'See all teams' clicked")

    careers.navigate_to_qa_positions()
    print("✓ Quality Assurance department selected")

    jobs = JobsPage(driver)
    jobs.verify_page()

    jobs.filter_by_location("Istanbul")
    print("✓ Location filter set to Istanbul")
    jobs.filter_by_team("Quality Assurance")
    print("✓ Team filter set to Quality Assurance")
    verify_and_apply_for_jobs(driver, jobs, "Istanbul")

    jobs.filter_by_location("Istanbul, Turkiye")
    print("✓ Location filter set to Istanbul, Turkiye")
    verify_and_apply_for_jobs(driver, jobs, "Istanbul, Turkiye")
