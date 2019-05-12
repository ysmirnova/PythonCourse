from selenium.webdriver.common.by import By

from pages.base_bage import BasePage
# from pages.dashboard_page import DashboardPage
from utils import helpers


class CreateIssuePage(BasePage):
    PROJECT_FIELD = (By.ID, "project-field")
    ISSUETYPE_FIELD = (By.ID, "issuetype-field")
    SUMMARY_INPUT = (By.ID, "summary")
    DESCRIPTION_FRAME = (By.ID, "mce_7_ifr")
    DESCRIPTION_INPUT = (By.ID, "tinymce")
    PRIORITY_FIELD = (By.ID, "priority-field")
    ASSIGNEE_FIELD = (By.ID, "assignee-field")
    CREATE_ISSUE_BUTTON = (By.ID, "create-issue-submit")
    ERROR_MESSAGE = (By.CLASS_NAME, "error")

    def create_issue(self, project, issuetype, summary, description=None, priority=None, assignee=None):
        helpers.click(self.driver, self.PROJECT_FIELD, 2)
        helpers.input_value(self.driver, self.PROJECT_FIELD, project, 5)
        helpers.submit(self.driver, self.PROJECT_FIELD, 2)

        helpers.click(self.driver, self.ISSUETYPE_FIELD, 2)
        helpers.input_value(self.driver, self.ISSUETYPE_FIELD, issuetype, 5)
        helpers.submit(self.driver, self.ISSUETYPE_FIELD, 2)

        helpers.click(self.driver, self.SUMMARY_INPUT, 2)
        helpers.input_value(self.driver, self.SUMMARY_INPUT, summary, 5)

        if description is not None:
            helpers.frame_switch(self.driver, self.DESCRIPTION_FRAME, 5)
            helpers.click(self.driver, self.DESCRIPTION_INPUT, 2)
            helpers.input_value(self.driver, self.DESCRIPTION_INPUT, description, 5)
            helpers.frame_switch_default(self.driver)

        if priority is not None:
            helpers.click(self.driver, self.PRIORITY_FIELD, 2)
            helpers.input_value(self.driver, self.PRIORITY_FIELD, priority, 5)

        if priority is not None:
            helpers.click(self.driver, self.ASSIGNEE_FIELD, 2)
            helpers.input_value(self.driver, self.ASSIGNEE_FIELD, assignee, 5)

        helpers.submit(self.driver, self.CREATE_ISSUE_BUTTON, 2)
        # return DashboardPage(self.driver)

    def get_error_message(self):
        return helpers.get_text(self.driver, self.ERROR_MESSAGE, 10)
