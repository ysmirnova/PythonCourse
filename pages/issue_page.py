from selenium.webdriver.common.by import By

from pages.base_bage import BasePage
# from pages.dashboard_page import DashboardPage
from utils import helpers


class IssuePage(BasePage):
    PROJECT_FIELD = (By.ID, "project-name-val")
    ISSUETYPE_FIELD = (By.ID, "type-val")
    SUMMARY_VAl = (By.ID, "summary-val")
    SUMMARY_INPUT = (By.ID, "summary")
    DESCRIPTION_VAL = (By.ID, "description-val")
    PRIORITY_VAL = (By.ID, "priority-val")
    PRIORITY_INPUT = (By.ID, "priority-field")
    ASSIGNEE_VAL = (By.ID, "assignee-val")
    ASSIGNEE_INPUT = (By.ID, "assignee-field")
    MORE_DROPDOWN=(By.ID,"opsbar-operations_more")
    DELETE_BUTTON =(By.ID,"delete-issue")
    CONFIRM_DELETE_BUTTON = (By.ID, "delete-issue-submit")
    UPDATE_BUTTON = (By.CSS_SELECTOR, ".aui-button.submit")

    def get_project(self):
        return helpers.get_text(self.driver,self.PROJECT_FIELD, 10)

    def get_issue_type(self):
        return helpers.get_text(self.driver,self.ISSUETYPE_FIELD, 10)

    def get_summary(self):
        return helpers.get_text(self.driver, self.SUMMARY_VAl, 10)

    def get_description(self):
        return helpers.get_text(self.driver,self.DESCRIPTION_VAL, 10)

    def get_priority(self):
        return helpers.get_text(self.driver, self.PRIORITY_VAL, 10)

    def get_assignee(self):
        return helpers.get_text(self.driver, self.ASSIGNEE_VAL, 10)

    def delete_issue(self):
        helpers.click(self.driver, self.MORE_DROPDOWN, 10)
        helpers.click(self.driver, self.DELETE_BUTTON, 10)
        helpers.submit(self.driver, self.CONFIRM_DELETE_BUTTON, 10)

    def change_summary(self, summary_text):
        helpers.click(self.driver, self.SUMMARY_VAl, 10)
        helpers.input_value(self.driver, self.SUMMARY_INPUT, summary_text, 10)
        helpers.submit(self.driver, self.SUMMARY_INPUT, 10)

    def change_priority(self, priority_text):
        helpers.click(self.driver, self.PRIORITY_VAL, 10)
        helpers.input_value(self.driver, self.PRIORITY_INPUT, priority_text, 10)
        helpers.submit(self.driver, self.PRIORITY_INPUT, 10)

    def change_assignee(self, assignee_text):
        helpers.click(self.driver, self.ASSIGNEE_VAL, 10)
        helpers.input_value(self.driver, self.ASSIGNEE_INPUT, assignee_text, 10)
        helpers.submit(self.driver, self.ASSIGNEE_INPUT, 10)





