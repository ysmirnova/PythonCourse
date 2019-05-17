from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_element_visibility(driver, locator, timeout):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator))


def wait_element_to_be_clickable(driver, locator, timeout):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator))


def wait_page_title(driver, title, timeout):
    return WebDriverWait(driver, timeout).until(
        EC.title_contains(title))


def input_value(driver, locator, value, timeout):
    elem = wait_element_visibility(driver, locator, timeout)
    # elem.clear()
    elem.send_keys(value)


def submit(driver, locator, timeout):
    elem = wait_element_visibility(driver, locator, timeout)
    elem.submit()


def get_text(driver, locator, timeout):
    elem = wait_element_visibility(driver, locator, timeout)
    return elem.text


def click(driver, locator, timeout):
    elem = wait_element_to_be_clickable(driver, locator, timeout)
    elem.click()


def frame_switch(driver, locator, timeout):
    elem = wait_element_visibility(driver, locator, timeout)
    driver.switch_to.frame(elem)


def frame_switch_default(driver):
    driver.switch_to.default_content()


def select_by_text(driver, locator, value, timeout):
    elem = driver.find_element(*locator)
    select = Select(elem)
    select.select_by_visible_text(value)


