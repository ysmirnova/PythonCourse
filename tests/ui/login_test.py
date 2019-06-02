import allure
import pytest

from pages.login_page import LoginPage


@allure.feature("Login")
@allure.tag("ui")
@pytest.mark.skip
class TestLogin:
    driver = None
    login_page = None

    @pytest.fixture()
    def setup(self, driver, variables):
        self.driver = driver
        self.login_page = LoginPage(driver)

    @allure.title("Successful login")
    def test_login(self, setup, variables):
        with allure.step("Open login page"):
            self.login_page.open(variables["url"])
            self.login_page.is_page_opened(variables["title_login"])

        with allure.step("login to Jira"):
            self.dashboard_page = self.login_page.login(variables["username"], variables["password"])

        with allure.step("System dashboard page is opened"):
            assert self.dashboard_page.is_page_opened(variables["title_dashboard"])

    @allure.title("Login with invalid username")
    def test_login_invalid_username(self, setup, variables):
        with allure.step("Open login page"):
            self.login_page.open(variables["url"])
            self.login_page.is_page_opened(variables["title_login"])

        with allure.step("login with invalid username"):
            self.login_page.login("invalid", variables["password"])

        with allure.step("Error message appears"):
            assert "Sorry, your username and password are incorrect - please try again." \
                   in self.login_page.get_error_message()

    @allure.title("Login with invalid password")
    def test_login_invalid_password(self, setup, variables):
        with allure.step("Open login page"):
            self.login_page.open(variables["url"])
            self.login_page.is_page_opened(variables["title_login"])

        with allure.step("Login with invalid password"):
            self.login_page.login(variables["username"], "invalid")

        with allure.step("Error message appears"):
            assert "Sorry, your username and password are incorrect - please try again." \
                   in self.login_page.get_error_message()

