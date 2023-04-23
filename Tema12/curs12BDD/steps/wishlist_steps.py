from behave import *


@given('I am on the Wishlist page')
def step_impl(context):
    context.wishlist_page.navigate_to_wishlist_page()


@then('The Wishlist text is displayed')
def step_impl(context):
    assert context.wishlist_page.is_empty_wishlist_message_displayed()


@then('The Wishlist text contains "{message}"')
def step_impl(context, message):
    assert message in context.wishlist_page.get_empty_wishlist_message_text()


@given('I am on the Cell-Phones page')
def step_impl(context):
    context.cellphones_page.navigate_to_cell_phones_page()


@then('I add to Wishlist the "HTC One Mini Blue"')
def step_impl(context):
    context.cellphones_page.click_on_htc_one_mini_add_to_wishlist_button()


@then('The successful adding to Wishlist message is displayed')
def step_impl(context):
    assert context.cellphones_page.is_wishlist_successful_added_message_displayed()


@then('The successful message contains "{message}"')
def step_impl(context, message):
    assert message in context.cellphones_page.get_successful_added_to_wishlist_message_text()


@then('I click on "Wishlist" button')
def step_impl(context):
    context.wishlist_page.click_on_wishlist_button()


@then('I actually am on "{expected_url}"')
def step_impl(context, expected_url):
    assert context.wishlist_page.is_url_correct(expected_url)


@then('The "{expected_phone}" is actually in the Wishlist')
def step_impl(context, expected_phone):
    assert expected_phone in context.wishlist_page.get_cell_phone_name()