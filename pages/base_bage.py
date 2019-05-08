from utils import helpers


class BasePage:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def is_page_opened(self, title: object) -> object:
        return helpers.wait_page_title(self.driver, title, 10)
