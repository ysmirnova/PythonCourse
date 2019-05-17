import random
import string
from os.path import join

import allure
import pytest

from pages.login_page import LoginPage


@allure.feature("Search issue")
@allure.tag("ui")
class TestSearchIssue:
    driver = None
    dashboard_page = None
    issue_number = None

    @pytest.fixture()
    def setup(self, driver, variables):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.login_page.open(variables["url"])
        self.login_page.is_page_opened(variables["title_login"])
        self.dashboard_page = self.login_page.login(variables["username"], variables["password"])
        assert self.dashboard_page.is_page_opened(variables["title_dashboard"])

    @pytest.fixture()
    def create_issue(self, variables):
        self.create_issue_page = self.dashboard_page.open_create_issue_page()
        assert self.create_issue_page.is_page_opened(variables["title_create_issue"])
        issue_data = variables["issue_data"]
        self.create_issue_page.create_issue(issue_data)
        assert "Story summary has been successfully created." in self.dashboard_page.get_create_issue_message()
        num = self.dashboard_page.get_create_issue_number()
        self.issue_number = num[:num.find(" ")]
        yield
        self.issue_page = self.dashboard_page.open_found_issue()
        self.issue_page.delete_issue()

    @allure.title("Search issue by number")
    def test_search_exist_issue(self, setup, create_issue):
        with allure.step("Fill issue number in search field"):
            self.dashboard_page.search_issue(self.issue_number)
        with allure.step("Check that issue found"):
            assert self.issue_number in self.dashboard_page.get_search_result()

    @allure.title("Search issue “no results”")
    def test_search_not_exist_issue(self, setup):
        with allure.step("Fill not exist issue number in search field"):
            self.dashboard_page.search_issue("F-0987763")
        with allure.step("Check that 'No results' message appears"):
            assert "No results" in self.dashboard_page.get_not_found_issue_message()
