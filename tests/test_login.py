import allure

from pages.login_page import LoginPage


class TestLogin:
    driver = None
    @allure.title("Successful login")
    def test_login(self, driver, variables):
        self.driver = driver
        self.login_page = LoginPage(driver)

        # self.login_page.is_page_opened(variables["title_login"])
        # self.login_page.login(variables["username"], variables["password"])
        with allure.step("Open login page"):
            self.login_page.open("https://jira.hillel.it/login.jsp")
            assert self.login_page.is_page_opened("Log in - Hillel IT School JIRA")

        with allure.step("login to Jira"):
            self.dashboard_page = self.login_page.login("YuliiaSmirnova", "YuliiaSmirnova")

        with allure.step("System dashboard page is opened"):
            assert self.dashboard_page.is_page_opened("System Dashboard - Hillel IT School JIRA")

    @allure.title("Login with invalid username")
    def test_login_invalid_username(self, driver, variables):
        self.driver = driver
        self.login_page = LoginPage(driver)
        # self.login_page.is_page_opened(variables["title_login"])
        # self.login_page.login(variables["username"], variables["password"])
        with allure.step("Open login page"):
            self.login_page.open("https://jira.hillel.it/login.jsp")
            assert self.login_page.is_page_opened("Log in - Hillel IT School JIRA")

        with allure.step("Login with invalid username"):
            self.login_page.login("invalid", "YuliiaSmirnova")

        with allure.step("Error message appears"):
            assert "Sorry, your username and password are incorrect - please try again." in self.login_page.get_error_message()

    @allure.title("Login with invalid password")
    def test_login_invalid_password(self, driver, variables):
        self.driver = driver
        self.login_page = LoginPage(driver)
        # self.login_page.is_page_opened(variables["title_login"])
        # self.login_page.login(variables["username"], variables["password"])
        with allure.step("Open login page"):
            self.login_page.open("https://jira.hillel.it/login.jsp")
            assert self.login_page.is_page_opened("Log in - Hillel IT School JIRA")

        with allure.step("Login with invalid password"):
            self.login_page.login("YuliiaSmirnova", "invalid")

        with allure.step("Error message appears"):
            assert "fff." in self.login_page.get_error_message()

