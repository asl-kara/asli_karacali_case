from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CareersPage:
    _SEE_ALL_TEAMS_BTN = (By.CSS_SELECTOR, "a.inso-btn.see-more")
    _DEPARTMENT_ITEM = (By.CSS_SELECTOR, "[data-department]")
    _QA_DEPARTMENT = (By.CSS_SELECTOR, "[data-department='Quality Assurance']")
    _QA_LINK = (By.CSS_SELECTOR, "[data-department='Quality Assurance'] .insiderone-icon-cards-grid-item-btn")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def verify_page(self) -> None:
        self.wait.until(EC.url_contains("careers"))
        self.wait.until(EC.title_contains("Careers"))

    def click_see_all_teams(self) -> None:
        see_all_btn: WebElement = self.wait.until(
            EC.element_to_be_clickable(self._SEE_ALL_TEAMS_BTN)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'instant'});", see_all_btn)
        see_all_btn.click()
        self.wait.until(EC.presence_of_element_located(self._DEPARTMENT_ITEM))
        self.wait.until(lambda d: d.execute_script(
            "return document.querySelector(\"[data-department='Quality Assurance']\").getBoundingClientRect().bottom < 0"
        ))

    def navigate_to_qa_positions(self) -> None:
        qa_link: WebElement = self.wait.until(
            EC.element_to_be_clickable(self._QA_LINK)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', behavior: 'instant'});", qa_link
        )
        # Scrolling triggers intersection observer which resets href to "#";
        # wait for the lever.co API to restore the correct href before clicking.
        qa_link = WebDriverWait(self.driver, 15).until(
            lambda d: (lambda el: el if "lever.co" in (el.get_attribute("href") or "") else False)(
                d.find_element(*self._QA_LINK)
            )
        )
        qa_link.click()
        self.wait.until(EC.url_contains("lever.co"))
