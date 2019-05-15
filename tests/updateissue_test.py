import random
import string
from os.path import join

import allure
import pytest

from pages.login_page import LoginPage


@allure.feature("Update issue")
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
    def issue(self, variables):
        self.create_issue_page = self.dashboard_page.open_create_issue_page()
        assert self.create_issue_page.is_page_opened(variables["title_create_issue"])
        issue_data = variables["issue_data"]
        self.create_issue_page.create_issue(issue_data)
        assert "Story summary has been successfully created." in self.dashboard_page.get_create_issue_message()
        num = self.dashboard_page.get_create_issue_number()
        self.issue_number = num[:num.find(" ")]
        self.dashboard_page.search_issue(self.issue_number)
        self.issue_page = self.dashboard_page.open_found_issue()
        yield
        self.issue_page.delete_issue()

    @allure.title("Update issue summary")
    def test_update_issue_summary(self, setup, issue):
        with allure.step("Update issue summary"):
            self.issue_page.change_summary("summary is updated")
        with allure.step("Check updated issue summary"):
            self.issue_page.open_dashboard()
            self.dashboard_page.search_issue(self.issue_number)
            self.issue_page = self.dashboard_page.open_found_issue()
            assert "summary is updated" in self.issue_page.get_summary()

