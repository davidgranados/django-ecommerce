import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def chrome_browser_instance(request):
    """
    Provide a selenium webdriver instance
    """
    options = Options()
    options.headless = True
    browser = webdriver.Remote(
        command_executor="http://selenium-chrome:4444/wd/hub", options=options
    )
    yield browser
    browser.close()
