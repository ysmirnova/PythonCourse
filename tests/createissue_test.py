import json
import random
import string

import allure
import pytest

from pages.login_page import LoginPage


@allure.feature("Create issue")
@allure.tag("ui")
class TestCreateIssue:
    driver = None
    dashboard_page = None
    delete_issue = True

    # @pytest.fixture()
    # def setup(self, driver, variables):
    #     self.driver = driver
    #     self.login_page = LoginPage(driver)
    #     self.login_page.open(variables["url"])
    #     self.login_page.is_page_opened(variables["title_login"])
    #     self.dashboard_page = self.login_page.login(variables["username"], variables["password"])
    #     assert self.dashboard_page.is_page_opened(variables["title_dashboard"])
    #     yield
    #     if self.delete_issue:
    #         self.issue_page.delete_issue()

    @pytest.fixture()
    def setup(self, driver, variables):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.login_page.open("https://jira.hillel.it/login.jsp")
        # variables["url"])
        # self.login_page.is_page_opened(variables["title_login"])
        # self.dashboard_page = self.login_page.login(variables["username"], variables["password"])
        self.dashboard_page = self.login_page.login("YuliiaSmirnova", "YuliiaSmirnova")
        # assert self.dashboard_page.is_page_opened(variables["title_dashboard"])
        yield
        if self.delete_issue:
            self.issue_page.delete_issue()

    @allure.title("Create issue with all fields")
    def test_create_issue_full(self, setup, variables):
        with allure.step("Open Create issue page"):
            self.create_issue_page = self.dashboard_page.open_create_issue_page()
            assert self.create_issue_page.is_page_opened(variables["title_create_issue"])

        with allure.step("Fill issue data"):
            issue_data = variables["issue_data_full"]
            self.create_issue_page.create_issue(issue_data)

        with allure.step("Check that issue was created"):
            assert "Story summary has been successfully created." in self.dashboard_page.get_create_issue_message()

        with allure.step("Check that issue field is correct"):
            self.issue_page = self.dashboard_page.open_new_issue()
            assert issue_data["project"] in self.issue_page.get_project()
            assert issue_data["issue_type"] in self.issue_page.get_issue_type()
            assert issue_data["summary"] in self.issue_page.get_summary()
            assert issue_data["description"] in self.issue_page.get_description()

    @allure.title("Create issue with only required fields")
    def test_create_issue(self, setup, variables):
        with allure.step("Open Create issue page"):
            self.create_issue_page = self.dashboard_page.open_create_issue_page()
            assert self.create_issue_page.is_page_opened(variables["title_create_issue"])
        with allure.step("Fill issue data"):
            issue_data = variables["issue_data"]
            self.create_issue_page.create_issue(issue_data)
        with allure.step("Check that issue was created"):
            assert "Story summary has been successfully created." in self.dashboard_page.get_create_issue_message()

        with allure.step("Check that issue field is correct"):
            self.issue_page = self.dashboard_page.open_new_issue()
            assert issue_data["project"] in self.issue_page.get_project()
            assert issue_data["issue_type"] in self.issue_page.get_issue_type()
            assert issue_data["summary"] in self.issue_page.get_summary()

    @allure.title("Create issue with parameter text length, longer than supported")
    def test_create_issue_with_error(self, setup, variables):
        with allure.step("Open Create issue page"):
            self.create_issue_page = self.dashboard_page.open_create_issue_page()
            assert self.create_issue_page.is_page_opened(variables["title_create_issue"])
        with allure.step("Fill issue data"):
            issue_data = variables["issue_data"]
            issue_data["summary"] = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
                              for x in range(260))
            self.create_issue_page.create_issue(issue_data)
        with allure.step("Error message appears"):
            assert "Summary must be less than 255 characters." in self.create_issue_page.get_error_message()
        self.delete_issue = False
