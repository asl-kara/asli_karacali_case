from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class JobsPage:
    _POSTING = (By.CSS_SELECTOR, "div.posting")
    _APPLY_BTN = (By.CSS_SELECTOR, "[data-qa='btn-apply'] a")
    _POSTING_NAME = (By.CSS_SELECTOR, "[data-qa='posting-name']")
    _POSTING_DEPARTMENT = (By.CSS_SELECTOR, ".posting-category-title")
    _POSTING_LOCATION = (By.CSS_SELECTOR, ".sort-by-location")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def verify_page(self) -> None:
        self.wait.until(EC.url_contains("lever.co"))

    def get_job_postings(self) -> list[WebElement]:
        return self.wait.until(
            EC.presence_of_all_elements_located(self._POSTING)
        )

    def _apply_filter(self, btn_xpath: str, option_text: str, url_keyword: str) -> None:
        filter_btn: WebElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, btn_xpath)))
        filter_btn.click()
        option: WebElement = self.wait.until(
            EC.presence_of_element_located((By.XPATH, f"//a[contains(@class,'category-link') and normalize-space(text())='{option_text}']"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option)
        option.click()
        self.wait.until(EC.url_contains(url_keyword))

    def filter_by_location(self, location: str = "Istanbul") -> None:
        self._apply_filter(
            "//div[@role='button' and contains(@aria-label,'Filter by Location') and not(contains(@aria-label,'type'))]",
            location,
            "location="
        )

    def filter_by_team(self, team: str = "Quality Assurance") -> None:
        self._apply_filter(
            "//div[@role='button' and contains(@aria-label,'Filter by Team')]",
            team,
            "team="
        )

    def verify_job_listings(self) -> int:
        try:
            postings: list[WebElement] = self.get_job_postings()
            return len(postings)
        except TimeoutException:
            return 0

    def click_apply_for_job(self, index: int) -> None:
        postings: list[WebElement] = self.get_job_postings()
        postings[index].find_element(*self._APPLY_BTN).click()
        self.wait.until(EC.url_contains("lever.co/insiderone/"))

    def get_all_job_details(self) -> list[dict]:
        count = len(self.get_job_postings())
        result = []
        for i in range(count):
            posting = self.get_job_postings()[i]
            result.append({
                "position": posting.find_element(*self._POSTING_NAME).text,
                "department": posting.find_element(By.XPATH, "preceding-sibling::div[contains(@class,'posting-category-title')]").text,
                "location": posting.find_element(*self._POSTING_LOCATION).text,
            })
        return result
