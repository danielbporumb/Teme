from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class WishList(BasePage):

    WISHLIST_PAGE_URL = "https://demo.nopcommerce.com/wishlist"
    WISHLIST_MESSAGE = By.CLASS_NAME, "no-data"
    CELL_PHONE = By.CLASS_NAME, "product-name"

    def navigate_to_wishlist_page(self):
        self.driver.get(self.WISHLIST_PAGE_URL)

    def is_empty_wishlist_message_displayed(self):
        return self.is_element_displayed(self.WISHLIST_MESSAGE)

    def get_empty_wishlist_message_text(self):
        return self.get_element_text(self.WISHLIST_MESSAGE)

    def is_a_cell_phone_in_the_wishlist(self):
        return self.is_element_present(self.CELL_PHONE)

    def get_cell_phone_name(self):
        return self.get_element_text(self.CELL_PHONE)


