from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CellPhones(BasePage):

    CELLPHONES_PAGE_URL = "https://demo.nopcommerce.com/cell-phones"
    HTC_ONE_MINI_WISHLIST_BUTTON = (By.XPATH, "//a[text()='HTC One Mini Blue']/following::button[text()='Add to wishlist'][1]")
    WISHLIST_MESSAGE = (By.CLASS_NAME, "success")
    HTC_ONE_MINI_ADD_TO_CART_BUTTON = (By.XPATH, "//div[text()='HTC One and HTC One Mini now available in bright blue hue']/following::button[text()='Add to cart'][1]")


    def navigate_to_cell_phones_page(self):
        self.driver.get(self.CELLPHONES_PAGE_URL)

    def click_on_htc_one_mini_add_to_wishlist_button(self):
        self.click(self.HTC_ONE_MINI_WISHLIST_BUTTON)

    def click_on_htc_one_mini_add_to_cart_button(self):
        self.click(self.HTC_ONE_MINI_ADD_TO_CART_BUTTON)

    def is_wishlist_successful_added_message_displayed(self):
        return self.is_element_present(self.WISHLIST_MESSAGE)

    def get_successful_added_to_wishlist_message_text(self):
        return self.get_element_text(self.WISHLIST_MESSAGE)
