from selenium import webdriver
from selenium.webdriver.common.by import By

from Teme.Tema11.pages.base_page import BasePage


class SecurePage(BasePage):

    SECURE_PAGE_URL = "https://the-internet.herokuapp.com/secure"
    LOGOUT_BUTTON = (By.CLASS_NAME, "icon-signout")
    SUCCESS_MESSAGE = (By.ID, "flash")
    CLOSE_MESSAGE_BUTTON = (By.CLASS_NAME, "close")

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def click_on_logout_button(self):
        self.click(self.LOGOUT_BUTTON)

    def close_message(self):
        self.click(self.CLOSE_MESSAGE_BUTTON)

    def get_success_message_text(self):
        return self.get_element_text(self.SUCCESS_MESSAGE)

    def wait_for_message_to_be_absent(self):
        self.wait_for_element_to_be_absent(self.SUCCESS_MESSAGE, 3)

    def is_message_present(self):
        return self.is_element_present(self.SUCCESS_MESSAGE)

    def is_success_message_displayed(self):
        return self.wait_for_element_to_be_present(self.SUCCESS_MESSAGE, 5)