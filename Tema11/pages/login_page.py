from selenium import webdriver
from selenium.webdriver.common.by import By

from Teme.Tema11.pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_PAGE_URL = "https://the-internet.herokuapp.com/login"
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "fa-sign-in")
    MESSAGE = (By.ID, "flash")

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def navigate_to_login_page(self):
        self.driver.get(self.LOGIN_PAGE_URL)

    def username_type(self, username):
        self.type(self.USERNAME_INPUT, username)

    def password_type(self, password):
        self.type(self.PASSWORD_INPUT, password)

    def click_on_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def get_message_text(self):
        return self.get_element_text(self.MESSAGE)

    def is_message_displayed(self):
        return self.wait_for_element_to_be_present(self.MESSAGE, 5)

