from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

EXPECTED_SECTION_CLASSES: list[str] = [
    "homepage-hero",
    "homepage-social-proof",
    "homepage-capabilities",
    "homepage-insider-one-ai",
    "homepage-channels",
    "homepage-case-study",
    "homepage-analyst",
    "homepage-integrations",
    "homepage-resources",
    "homepage-call-to-action",
]


class HomePage:
    _URL = "https://insiderone.com/"
    _COOKIE_BTN = (By.ID, "wt-cli-accept-all-btn")
    _COOKIE_OVERLAY = (By.CSS_SELECTOR, ".cli-popupbar-overlay")
    _NAVBAR = (By.ID, "navigation")
    _HERO = (By.CSS_SELECTOR, ".homepage-hero-content-title h1")
    _SECTIONS = (By.TAG_NAME, "section")
    _FOOTER = (By.ID, "footer")
    _CAREERS_LINK = (By.CSS_SELECTOR, 'a[href="/careers/"]')
    _GET_DEMO_BTN = (By.CSS_SELECTOR, 'a.btn.btn-primary[href="/request-a-demo/"]')

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self) -> None:
        self.driver.get(self._URL)

    def accept_cookies(self) -> None:
        try:
            btn = self.wait.until(EC.element_to_be_clickable(self._COOKIE_BTN))
            btn.click()
            self.wait.until(EC.invisibility_of_element_located(self._COOKIE_OVERLAY))
        except TimeoutException:
            pass

    def get_current_url(self) -> str:
        return self.driver.current_url

    def is_title_correct(self) -> bool:
        self.wait.until(EC.title_contains("Insider"))
        return True

    def is_navbar_visible(self) -> bool:
        self.wait.until(EC.visibility_of_element_located(self._NAVBAR))
        return True

    def is_hero_visible(self) -> bool:
        self.wait.until(EC.visibility_of_element_located(self._HERO))
        return True

    def get_section_classes(self) -> list[str]:
        sections: list[WebElement] = self.wait.until(
            EC.presence_of_all_elements_located(self._SECTIONS)
        )
        return [s.get_attribute("class") for s in sections]

    def is_footer_visible(self) -> bool:
        self.wait.until(EC.visibility_of_element_located(self._FOOTER))
        return True

    def click_get_demo(self) -> None:
        btn: WebElement = self.wait.until(EC.element_to_be_clickable(self._GET_DEMO_BTN))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
        btn.click()
        self.wait.until(EC.url_contains("request-a-demo"))

    def navigate_to_careers(self) -> None:
        link: WebElement = self.wait.until(
            EC.element_to_be_clickable(self._CAREERS_LINK)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'instant'});", link)
        link.click()
        self.wait.until(EC.url_contains("careers"))
