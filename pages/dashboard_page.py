from selenium.webdriver.common.by import By

from pages.base_bage import BasePage
from pages.create_issue_page import CreateIssuePage
from pages.issue_page import IssuePage
from utils import helpers


class DashboardPage(BasePage):
    CREATE_BUTTON = (By.ID, "create_link")
    MESSAGE_CONTAINER = (By.XPATH, "//div[contains(@class, 'aui-message-success')]")
    ISSUE_LINK = (By.XPATH, "//a[contains(@data-issue-key, 'WEBINAR-')]")
    QUICK_ISSUE_SEARCH_INPUT = (By.ID, "quickSearchInput")
    FIND_ISSUE_LINK = (By.XPATH, "(//li[@class='quick-search-result-item'][1]/a)[1]")
    FIND_ISSUE_NOT_FOUND = (By.CLASS_NAME, "quick-search-no-results")

    def open_create_issue_page(self):
        helpers.click(self.driver, self.CREATE_BUTTON, 10)
        return CreateIssuePage(self.driver)

    def get_create_issue_message(self):
        return helpers.get_text(self.driver, self.MESSAGE_CONTAINER, 10)

    def get_create_issue_number(self):
        return helpers.get_text(self.driver, self.ISSUE_LINK, 10)

    def open_new_issue(self):
        helpers.click(self.driver, self.ISSUE_LINK, 10)
        return IssuePage(self.driver)

    def search_issue(self, issue_number):
        helpers.input_value(self.driver, self.QUICK_ISSUE_SEARCH_INPUT, issue_number, 10)

    def get_search_result(self):
        return helpers.get_text(self.driver, self.FIND_ISSUE_LINK, 10)

    def open_found_issue(self):
        helpers.click(self.driver, self.FIND_ISSUE_LINK, 10)
        return IssuePage(self.driver)

    def get_not_found_issue_message(self):
        return helpers.get_text(self.driver, self.FIND_ISSUE_NOT_FOUND, 10)


