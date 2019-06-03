import allure
import pytest
from rest.rest_actions import RestActions
from utils import json_actions as JA


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
    marker = item.get_closest_marker("ui")
    if marker:
        if rep.when == "call" and rep.failed:
            try:
                allure.attach(item.instance.driver.get_screenshot_as_png(),
                              name=item.name,
                              attachment_type=allure.attachment_type.PNG)
            except Exception as e:
                print(e)


@pytest.fixture(scope="function")
def rest_actions():
    yield RestActions('https://jira.hillel.it', 'YuliiaSmirnova', 'YuliiaSmirnova')


@pytest.fixture(scope="function")
def create_issue_id(rest_actions):
    path = '/rest/api/2/issue'
    status_code, key_issue, id_issue, error = rest_actions.create_issue_rest(path, JA.json_file_to_string('issue_json/issue_required_field.json'))
    assert status_code == 201
    yield id_issue


