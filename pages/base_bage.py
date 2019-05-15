from selenium.webdriver.common.by import By

from utils import helpers


class BasePage:
    driver = None
    LOGO = (By.XPATH, "//*[contains(@href,'Dashboard.jspa')]")

    def __init__(self, driver):
        self.driver = driver

    def is_page_opened(self, title):
        return helpers.wait_page_title(self.driver, title, 10)

    def open_dashboard(self):
        helpers.click(self.driver, self.LOGO, 10)


