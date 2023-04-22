import time
from unittest import TestCase

from Teme.Tema11.pages.home_page import HomePage
from Teme.Tema11.pages.login_page import LoginPage
from Teme.Tema11.pages.secure_page import SecurePage
from Teme.Tema11.utils.driverfactory import DriverFactory


class TestLoginPage(TestCase):

    CORRECT_USERNAME = "tomsmith"
    CORRECT_PASSWORD = "SuperSecretPassword!"
    WRONG_USERNAME = "daniel"
    WRONG_PASSWORD = "password"
    WRONG_PASSWORD_MESSAGE = "Your password is invalid!"
    WRONG_USERNAME_MESSAGE = "Your username is invalid!"

    def setUp(self):
        self.driver = DriverFactory.get_driver()

    def tearDown(self):
        self.driver.quit()

    def test_login_with_correct_username_password(self):
        login_page = LoginPage(self.driver)
        secure_page = SecurePage(self.driver) # am initializat si un obiect din SecurePage pt a verifica cu URL-ul ei, declarat acolo
        home_page = HomePage(self.driver)
        home_page.navigate_to_home_page()
        home_page.click_on_form_authentication()
        # login_page.navigate_to_login_page()
        # pot sa ajung pe login_page si direct cu link, dar si folosindu-ma de functiile din home_page
        login_page.username_type(self.CORRECT_USERNAME)
        login_page.password_type(self.CORRECT_PASSWORD)
        login_page.click_on_login_button()
        time.sleep(3)

        self.assertEqual(secure_page.SECURE_PAGE_URL, self.driver.current_url, "The Login was not made successfully")

    def test_login_with_correct_username_and_wrong_password(self):
        login_page = LoginPage(self.driver)
        login_page.navigate_to_login_page()
        login_page.username_type(self.CORRECT_USERNAME)
        login_page.password_type(self.WRONG_PASSWORD)
        login_page.click_on_login_button()

        self.assertTrue(login_page.is_message_displayed(), "Error, message is not displayed")
        # print(f"\n{login_page.get_message_text()}")
        self.assertIn(self.WRONG_PASSWORD_MESSAGE, login_page.get_message_text(), "Error message text do not match")

    def test_login_with_incorrect_username(self):
        login_page = LoginPage(self.driver)
        login_page.navigate_to_login_page()
        login_page.username_type(self.WRONG_USERNAME)
        login_page.click_on_login_button()

        self.assertTrue(login_page.is_message_displayed(), "Error, message is not displayed")
        # print(f"\n{login_page.get_message_text()}")
        self.assertIn(self.WRONG_USERNAME_MESSAGE, login_page.get_message_text(), "Error message text do not match")

