from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_element(driver, locator, timeout):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator))


def wait_page_title(driver, title, timeout):
    return WebDriverWait(driver, timeout).until(
        EC.title_contains(title))


def input_value(driver, locator, value, timeout):
    elem = wait_element(driver, locator, timeout)
    elem.clear()
    elem.send_keys(value)


def submit(driver, locator, timeout):
    elem = wait_element(driver, locator, timeout)
    elem.submit()


def get_text(driver, locator, timeout):
    elem = wait_element(driver, locator, timeout)
    return elem.text
