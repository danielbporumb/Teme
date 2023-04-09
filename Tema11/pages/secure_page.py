from selenium import webdriver
from selenium.webdriver.common.by import By

from Teme.Tema11.pages.login_page import LoginPage


class SecurePage(LoginPage): # mostenim din LoginPage doar, pt ca LoginPage la randul ei mosteneste din HomePage

    SECURE_PAGE_URL = "https://the-internet.herokuapp.com/secure"
    LOGOUT_BUTTON = (By.CLASS_NAME, "icon-signout")
    CLOSE_MESSAGE_BUTTON = (By.CLASS_NAME, "close")

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def click_on_logout_button(self):
        self.click(self.LOGOUT_BUTTON)

    def close_message(self):
        self.click(self.CLOSE_MESSAGE_BUTTON)

    def get_success_message_text(self):
        return self.get_message_text()

    def wait_for_message_to_be_absent(self):
        self.wait_for_element_to_be_absent(self.MESSAGE, 3)

    def is_message_present(self):
        return self.is_element_present(self.MESSAGE)