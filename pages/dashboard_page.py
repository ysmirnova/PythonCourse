from selenium.webdriver.common.by import By

from pages.base_bage import BasePage
from utils import helpers


class DashboardPage(BasePage):
    LOGIN_INPUT = (By.ID, "login-form-username")
    PASSWORD_INPUT = (By.ID, "login-form-password")
    LOGIN_BUTTON = (By.ID, "login-form-password")

