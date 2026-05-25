import pytest
from pages.demo_page import DemoPage
from pages.home_page import HomePage

INVALID_EMAIL = "notanemail"
NON_BUSINESS_EMAIL = "test@test.com"


@pytest.fixture
def demo_form(driver):
    home = HomePage(driver)
    home.open()
    home.accept_cookies()
    home.click_get_demo()
    demo = DemoPage(driver)
    demo.verify_form_elements_visible()
    return demo


def test_demo_form_shows_errors_on_empty_submit(demo_form):
    demo_form.submit_form()
    assert len(demo_form.get_error_texts()) > 0, "No validation errors shown after empty form submit"


def test_demo_form_treats_whitespace_as_empty(demo_form):
    demo_form.fill_first_name("   ")
    demo_form.fill_last_name("   ")
    demo_form.fill_email("   ")
    demo_form.fill_job_title("   ")
    demo_form.fill_company("   ")
    demo_form.fill_how_did_you_hear("   ")
    demo_form.submit_form()
    assert len(demo_form.get_error_texts()) > 0, "Whitespace-only input should trigger validation errors"


@pytest.mark.parametrize("email,description", [
    pytest.param(INVALID_EMAIL, "invalid format", id="invalid_format"),
    pytest.param(NON_BUSINESS_EMAIL, "non-business domain", id="non_business_domain"),
])
def test_demo_form_shows_email_error(demo_form, email, description):
    demo_form.fill_email(email)
    demo_form.submit_form()
    assert demo_form.is_email_error_visible(), (
        f"No email error shown for {description} email '{email}'"
    )
