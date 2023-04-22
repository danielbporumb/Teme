import time
from unittest import TestCase

from Teme.Tema11.pages.login_page import LoginPage
from Teme.Tema11.pages.secure_page import SecurePage
from Teme.Tema11.utils.driverfactory import DriverFactory


class TestSecurePage(TestCase):

    CORRECT_USERNAME = "tomsmith"
    CORRECT_PASSWORD = "SuperSecretPassword!"
    SUCCESS_LOGIN_MESSAGE = "You logged into a secure area!"
    SUCCESS_LOGOUT_MESSAGE = "You logged out of the secure area!"

    def setUp(self):
        self.driver = DriverFactory.get_driver()

    def tearDown(self):
        self.driver.quit()

    def test_login_successful(self):
        login_page = LoginPage(self.driver)
        secure_page = SecurePage(self.driver)
        login_page.navigate_to_login_page()
        login_page.username_type(self.CORRECT_USERNAME)
        login_page.password_type(self.CORRECT_PASSWORD)
        login_page.click_on_login_button()
        # time.sleep(3)

        self.assertTrue(secure_page.is_success_message_displayed(), "Error, message is not displayed")
        # print(f"\n{secure_page.get_success_message_text()}")
        self.assertIn(self.SUCCESS_LOGIN_MESSAGE, secure_page.get_success_message_text(), "Error, messages do not match")

    def test_logout(self):
        self.test_login_successful()
        secure_page = SecurePage(self.driver)
        login_page = LoginPage(self.driver)
        secure_page.click_on_logout_button()
        time.sleep(1)

        self.assertTrue(login_page.is_message_displayed(), "Error, message is not displayed")
        # print(f"\n{login_page.get_message_text()}")
        self.assertIn(self.SUCCESS_LOGOUT_MESSAGE, login_page.get_message_text(), "Error, messages do not match")

    def test_close_flash_message(self):
        self.test_login_successful()
        time.sleep(1)
        secure_page = SecurePage(self.driver)
        secure_page.close_message()
        secure_page.wait_for_message_to_be_absent()
        # sta un pic cam mult dupa ce da x la mesaj, incerc sa imi dau seama de ce
        # print(secure_page.is_message_present())
        assert not secure_page.is_message_present(), "Error, message is still displayed"
