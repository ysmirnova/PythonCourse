from selenium.webdriver.common.by import By

from utils import helpers


class BasePage:
    driver = None
    DASHBOARDS_MENU = (By.ID, "home_link")
    SYSTEM_DASHBOARDS = (By.ID, "dash_lnk_system_lnk")


    def __init__(self, driver):
        self.driver = driver

    def is_page_opened(self, title):
        return helpers.wait_page_title(self.driver, title, 10)

    def open_dashboard(self):
        helpers.click(self.driver, self.DASHBOARDS_MENU, 10)
        helpers.click(self.driver, self.SYSTEM_DASHBOARDS, 10)


