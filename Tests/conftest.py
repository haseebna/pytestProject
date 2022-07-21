import pytest
from selenium import webdriver
from Config.config import TestData
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    chrome_path = TestData.CHROME_EXECUTABLE_PATH
    firefox_path = TestData.FIREFOX_EXECUTABLE_PATH

    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
        request.cls.driver = web_driver
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        request.cls.driver = web_driver
    yield
    web_driver.close()
