from Tests.test_base import test_base
from Pages.LoginPage import LoginPage
from Config.config import TestData


class Test_login(test_base):

    def test_login_page_tile(self):
        self.loginPage = LoginPage(self.driver)
        page_title = TestData.Login_page_title
        expected_title = self.loginPage.get_title(page_title)
        assert expected_title == page_title

    def test_login_standard_user(self):
        self.loginPage = LoginPage(self.driver)
        valid_username = TestData.valid_username_1
        expected_url_after_login = TestData.expected_URL
        password = TestData.valid_password
        self.loginPage.do_login(valid_username, password)
        actual_url_after_login = self.loginPage.get_current_url(expected_url_after_login)
        assert actual_url_after_login == expected_url_after_login

    def test_login_problem_user(self):
        self.loginPage = LoginPage(self.driver)
        valid_username = TestData.valid_username_3
        expected_url_after_login = TestData.expected_URL
        password = TestData.valid_password
        self.loginPage.do_login(valid_username, password)
        actual_url_after_login = self.loginPage.get_current_url(expected_url_after_login)
        assert actual_url_after_login == expected_url_after_login

    def test_login_performance_glitch_user(self):
        self.loginPage = LoginPage(self.driver)
        valid_username = TestData.valid_username_4
        expected_url_after_login = TestData.expected_URL
        password = TestData.valid_password
        self.loginPage.do_login(valid_username, password)
        actual_url_after_login = self.loginPage.get_current_url(expected_url_after_login)
        assert actual_url_after_login == expected_url_after_login

    def test_login_locked_out_user(self):
        self.loginPage = LoginPage(self.driver)
        valid_username = TestData.valid_username_2
        password = TestData.valid_password
        expected_error_msg = TestData.Error_msg_locked_user
        self.loginPage.do_login(valid_username, password)
        actual_error_msg = self.loginPage.get_error_msg()
        print(actual_error_msg)
        assert expected_error_msg == actual_error_msg

    def test_login_valid_username_and_invalid_password(self):
        self.loginPage = LoginPage(self.driver)
        valid_username = TestData.valid_username_1
        password = TestData.invalid_password
        expected_error_msg = TestData.Error_msg_invalid_username_password
        self.loginPage.do_login(valid_username, password)
        actual_error_msg = self.loginPage.get_error_msg()
        print(actual_error_msg)
        assert expected_error_msg == actual_error_msg

    def test_login_invalid_username_and_valid_password(self):
        self.loginPage = LoginPage(self.driver)
        valid_username = TestData.invalid_username
        password = TestData.valid_password
        expected_error_msg = TestData.Error_msg_invalid_username_password
        self.loginPage.do_login(valid_username, password)
        actual_error_msg = self.loginPage.get_error_msg()
        print(actual_error_msg)
        assert expected_error_msg == actual_error_msg

    def test_login_invalid_username_and_invalid_password(self):
        self.loginPage = LoginPage(self.driver)
        valid_username = TestData.invalid_username
        password = TestData.invalid_password
        expected_error_msg = TestData.Error_msg_invalid_username_password
        self.loginPage.do_login(valid_username, password)
        actual_error_msg = self.loginPage.get_error_msg()
        print(actual_error_msg)
        assert expected_error_msg == actual_error_msg
