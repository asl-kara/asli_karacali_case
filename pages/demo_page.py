from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class DemoPage:
    _URL = "https://insiderone.com/request-a-demo/"
    _COOKIE_BTN = (By.ID, "wt-cli-accept-btn")
    _FORM = (By.CSS_SELECTOR, "#expandable-form form.hs-form")
    _FIRST_NAME = (By.CSS_SELECTOR, "#expandable-form input[name='firstname']")
    _LAST_NAME = (By.CSS_SELECTOR, "#expandable-form input[name='lastname']")
    _EMAIL = (By.CSS_SELECTOR, "#expandable-form input[name='email']")
    _JOB_TITLE = (By.CSS_SELECTOR, "#expandable-form input[name='jobtitle']")
    _COMPANY = (By.CSS_SELECTOR, "#expandable-form input[name='company']")
    _HOW_DID_YOU_HEAR = (By.CSS_SELECTOR, "#expandable-form input[name='how_did_you_hear_about_us_']")
    _PHONE = (By.CSS_SELECTOR, "#expandable-form input[type='tel']")
    _SUBMIT_BTN = (By.CSS_SELECTOR, "#expandable-form input[type='submit']")
    _ERROR_MSGS = (By.CSS_SELECTOR, "#expandable-form .hs-error-msg")
    _EMAIL_ERROR = (By.CSS_SELECTOR, "#expandable-form .hs-email .hs-error-msg")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self) -> None:
        self.driver.get(self._URL)
        try:
            btn = self.wait.until(EC.element_to_be_clickable(self._COOKIE_BTN))
            btn.click()
        except TimeoutException:
            pass
        self.wait.until(EC.visibility_of_element_located(self._FORM))

    def verify_form_elements_visible(self) -> None:
        self.wait.until(EC.visibility_of_element_located(self._FORM))
        self.wait.until(EC.visibility_of_element_located(self._FIRST_NAME))
        self.wait.until(EC.visibility_of_element_located(self._EMAIL))
        self.wait.until(EC.visibility_of_element_located(self._SUBMIT_BTN))

    def _fill_field(self, locator: tuple, value: str) -> None:
        field = self.wait.until(EC.visibility_of_element_located(locator))
        field.clear()
        field.send_keys(value)

    def fill_first_name(self, value: str) -> None:
        self._fill_field(self._FIRST_NAME, value)

    def fill_last_name(self, value: str) -> None:
        self._fill_field(self._LAST_NAME, value)

    def fill_email(self, value: str) -> None:
        self._fill_field(self._EMAIL, value)

    def fill_job_title(self, value: str) -> None:
        self._fill_field(self._JOB_TITLE, value)

    def fill_company(self, value: str) -> None:
        self._fill_field(self._COMPANY, value)

    def fill_how_did_you_hear(self, value: str) -> None:
        self._fill_field(self._HOW_DID_YOU_HEAR, value)

    def fill_phone(self, value: str) -> None:
        self._fill_field(self._PHONE, value)

    def submit_form(self) -> None:
        btn = self.wait.until(EC.element_to_be_clickable(self._SUBMIT_BTN))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
        btn.click()

    def get_error_count(self) -> int:
        return len(self.get_error_texts())

    def get_error_texts(self) -> list[str]:
        try:
            errors: list[WebElement] = self.wait.until(
                EC.visibility_of_all_elements_located(self._ERROR_MSGS)
            )
            return [e.text for e in errors]
        except TimeoutException:
            return []

    def is_email_error_visible(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(self._EMAIL_ERROR))
            return True
        except TimeoutException:
            return False
