from selenium.webdriver.common.by import By

from pages.base_bage import BasePage
from pages.dashboard_page import DashboardPage
from utils import helpers


class LoginPage(BasePage):
    LOGIN_INPUT = (By.ID, "login-form-username")
    PASSWORD_INPUT = (By.ID, "login-form-password")
    LOGIN_BUTTON = (By.ID, "login-form-password")
    ERROR_MESSAGE = (By.CLASS_NAME, "aui-message")

    def login(self, username, password):
        helpers.input_value(self.driver, self.LOGIN_INPUT, username, 10)
        helpers.input_value(self.driver, self.PASSWORD_INPUT, password, 10)
        helpers.submit(self.driver, self.LOGIN_BUTTON, 10)
        return DashboardPage(self.driver)

    def get_error_message(self):
        return helpers.get_text(self.driver,self.ERROR_MESSAGE, 10)
