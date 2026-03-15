"""Step definitions for checkout feature."""
from behave import when, then
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@when('I proceed to checkout')
def step_proceed_checkout(context):
    if not hasattr(context, "cart_page"):
        context.cart_page = CartPage(context.driver)
    context.cart_page.click_checkout()
    context.checkout_page = CheckoutPage(context.driver)


@when('I fill checkout information with first name "{first}" last name "{last}" postal code "{zip}"')
def step_fill_checkout(context, first, last, zip):
    context.checkout_page.fill_info(first, last, zip)


@when('I finish the checkout')
def step_finish_checkout(context):
    context.checkout_page.finish_checkout()


@then('I should see the order confirmation message "{message}"')
def step_see_confirmation(context, message):
    header = context.checkout_page.get_confirmation_header()
    assert message in header, f"Expected '{message}' in confirmation, got: {header}"


@then('the confirmation header should contain "{text}"')
def step_confirmation_contains(context, text):
    header = context.checkout_page.get_confirmation_header()
    assert text in header, f"Expected '{text}' in header, got: {header}"
