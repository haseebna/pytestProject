from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData


class LoginPage(BasePage):
    EMAIL_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    BUTTON = (By.ID, "login-button")
    NOTIFICATION = (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')

    def __init__(self, driver):
        super().__init__(driver)
        url = TestData.BASE_URL
        self.driver.get(url)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL_FIELD, username)
        self.do_send_keys(self.PASSWORD_FIELD, password)
        self.do_click(self.BUTTON)

    def get_current_url(self,url):
        return self.get_url(url)

    def get_error_msg(self):
        return self.get_element_text(self.NOTIFICATION)
