import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox"],
        help="Browser to run tests on: chrome (default) or firefox",
    )


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture
def driver(browser):
    if browser == "firefox":
        drv = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
    else:
        drv = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )

    drv.maximize_window()
    yield drv
    drv.quit()
