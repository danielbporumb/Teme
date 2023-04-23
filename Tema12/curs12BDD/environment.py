from browser import Browser
from pages.cellphones_page import CellPhones
from pages.login_page import LoginPage
from pages.wishlist_page import WishList


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.wishlist_page = WishList()
    context.cellphones_page = CellPhones()

def after_all(context):
    context.browser.close()