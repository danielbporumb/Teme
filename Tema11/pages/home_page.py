from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage:

    HOME_PAGE_URL = "https://the-internet.herokuapp.com/"
    FORM_AUTHENTICATION_LINK = (By.LINK_TEXT, "Form Authentication")
    DROPDOWN_LINK = (By.LINK_TEXT, "Dropdown")
    JAVASCRIPT_ALERTS_LINK = (By.PARTIAL_LINK_TEXT, "Alerts")
    CONTEXT_MENU_LINK = (By.LINK_TEXT, "Context Menu")

    def __init__(self, driver: webdriver):
        self.driver = driver

    def navigate_to_home_page(self):
        self.driver.get(self.HOME_PAGE_URL)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        return self.find(locator).click()

    def click_on_form_authentication(self):
        return self.click(self.FORM_AUTHENTICATION_LINK)

    def click_on_dropdown(self):
        return self.click(self.DROPDOWN_LINK)

    def click_on_js_alerts(self):
        return self.click(self.JAVASCRIPT_ALERTS_LINK)

    def click_on_context_menu(self):
        return self.click(self.CONTEXT_MENU_LINK)

