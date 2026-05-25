from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class JobDetailPage:
    _APPLY_BTN = (By.CSS_SELECTOR, "a.postings-btn.template-btn-submit")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def verify_page(self) -> None:
        self.wait.until(EC.url_contains("lever.co/insiderone/"))
        self.wait.until(EC.presence_of_element_located(self._APPLY_BTN))

    def _click_apply_button(self, index: int) -> None:
        btns: list[WebElement] = self.wait.until(
            EC.presence_of_all_elements_located(self._APPLY_BTN)
        )
        assert len(btns) > 0, "No Apply buttons found on job detail page"
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btns[index])
        self.wait.until(EC.element_to_be_clickable(btns[index]))
        btns[index].click()
        self.wait.until(EC.url_contains("/apply"))

    def click_top_apply_button(self) -> None:
        self._click_apply_button(0)

    def click_bottom_apply_button(self) -> None:
        self._click_apply_button(-1)
