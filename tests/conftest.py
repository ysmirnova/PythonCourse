import pytest
from pytest_variables.plugin import variables

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager as Chrome_driver_manager


@pytest.yield_fixture()
def driver():
    driverq = webdriver.Chrome(executable_path=Chrome_driver_manager().install())
    driverq.get("https://jira.hillel.it/login.jsp")
    yield driverq
    driverq.quit()

