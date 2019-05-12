from selenium.webdriver.common.by import By

from pages.base_bage import BasePage
# from pages.dashboard_page import DashboardPage
from utils import helpers


class IssuePage(BasePage):
    PROJECT_FIELD = (By.ID, "project-name-val")
    ISSUETYPE_FIELD = (By.ID, "type-val")
    SUMMARY_INPUT = (By.ID, "summary-val")
    DESCRIPTION_INPUT = (By.ID, "description-val")
    MORE_DROPDOWN=(By.ID,"opsbar-operations_more")
    DELETE_BUTTON =(By.ID,"delete-issue")
    CONFIRM_DELETE_BUTTON = (By.ID, "delete-issue-submit")

    # delete - issue
    def get_project(self):
        return helpers.get_text(self.driver,self.PROJECT_FIELD, 10)

    def get_issue_type(self):
        return helpers.get_text(self.driver,self.ISSUETYPE_FIELD, 10)

    def get_summary(self):
        return helpers.get_text(self.driver,self.SUMMARY_INPUT, 10)

    def get_description(self):
        return helpers.get_text(self.driver,self.DESCRIPTION_INPUT, 10)

    def delete_issue(self):
        helpers.click(self.driver, self.MORE_DROPDOWN, 10)
        helpers.click(self.driver, self.DELETE_BUTTON, 10)
        helpers.submit(self.driver, self.CONFIRM_DELETE_BUTTON, 10)



