
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


class TestLogin:

    def test_login(self, driver, variables):
        self.login_page = LoginPage(driver)
        # self.login_page.is_page_opened(variables["title_login"])
        # self.login_page.login(variables["username"], variables["password"])
        assert self.login_page.is_page_opened("Log in - Hillel IT School JIRA")
        self.main_page = self.login_page.login("YuliiaSmirnova", "YuliiaSmirnova")
        assert self.main_page.is_page_opened("System Dashboard - Hillel IT School JIRA")

    def test_login_invalid_username(self, driver, variables):
        self.login_page = LoginPage(driver)
        # self.login_page.is_page_opened(variables["title_login"])
        # self.login_page.login(variables["username"], variables["password"])
        assert self.login_page.is_page_opened("Log in - Hillel IT School JIRA")
        self.login_page.login("invalid", "YuliiaSmirnova")
        assert "Sorry, your username and password are incorrect - please try again." in self.login_page.get_error_message()

    def test_login_invalid_password(self, driver, variables):
        self.login_page = LoginPage(driver)
        # self.login_page.is_page_opened(variables["title_login"])
        # self.login_page.login(variables["username"], variables["password"])
        assert self.login_page.is_page_opened("Log in - Hillel IT School JIRA")
        self.login_page.login("YuliiaSmirnova", "invalid")
        assert "Sorry, your username and password are incorrect - please try again." in self.login_page.get_error_message()

