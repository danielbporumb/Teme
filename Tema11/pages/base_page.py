from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver: webdriver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        return self.find(locator).click()

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def get_element_text(self, locator):
        return self.find(locator).text

    def wait_for_element_to_be_present(self, element_locator, time):
        wait = WebDriverWait(self.driver, time)
        return wait.until(EC.presence_of_element_located(element_locator))

    def wait_for_element_to_be_absent(self, element_locator, time):
        wait = WebDriverWait(self.driver, time)
        return wait.until(EC.none_of(EC.presence_of_element_located(element_locator)))

    def is_element_present(self, locator):
        return len(self.driver.find_elements(*locator)) > 0