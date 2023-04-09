from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Teme.Tema11.pages.home_page import HomePage


class LoginPage(HomePage):

    LOGIN_PAGE_URL = "https://the-internet.herokuapp.com/login"
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "fa-sign-in")
    MESSAGE = (By.ID, "flash")

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def navigate_to_login_page(self):
        self.click_on_form_authentication()

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def username_type(self, username):
        self.type(self.USERNAME_INPUT, username)

    def password_type(self, password):
        self.type(self.PASSWORD_INPUT, password)

    def click_on_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def get_element_text(self, locator):
        return self.find(locator).text

    def get_message_text(self):
        return self.get_element_text(self.MESSAGE)

    def wait_for_element_to_be_present(self, element_locator, time):
        wait = WebDriverWait(self.driver, time)
        return wait.until(EC.presence_of_element_located(element_locator))

    def is_message_displayed(self):
        return self.wait_for_element_to_be_present(self.MESSAGE, 5)

    def wait_for_element_to_be_absent(self, element_locator, time):
        wait = WebDriverWait(self.driver, time)
        return wait.until(EC.none_of(EC.presence_of_element_located(element_locator)))

    def is_element_present(self, locator):
        return len(self.driver.find_elements(*locator)) > 0