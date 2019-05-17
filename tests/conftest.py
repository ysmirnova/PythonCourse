import allure
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager as Chrome_driver_manager


@pytest.fixture(scope="function")
def driver():
    _driver = webdriver.Chrome(executable_path=Chrome_driver_manager().install())
    _driver.fullscreen_window()
    yield _driver
    _driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        try:
            allure.attach(item.instance.driver.get_screenshot_as_png(),
                          name=item.name,
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(e)
