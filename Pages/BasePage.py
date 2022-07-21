from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

""""It contains all methods and utilities for all pages"""


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, location):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(location)).click()

    def do_send_keys(self, location, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(location)).send_keys(text)

    def get_element_text(self, location):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(location))
        return element.text

    def is_enable(self, location):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(location))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def get_url(self, url):
        WebDriverWait(self.driver, 20).until(EC.url_to_be(url))
        return self.driver.current_url


