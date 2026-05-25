from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ApplicationFormPage:
    _FORM = (By.CSS_SELECTOR, "form#application-form")
    _NAME_INPUT = (By.CSS_SELECTOR, "[data-qa='name-input']")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def verify_page(self) -> None:
        self.wait.until(EC.url_contains("/apply"))
        self.wait.until(EC.presence_of_element_located(self._FORM))
        self.wait.until(EC.presence_of_element_located(self._NAME_INPUT))
