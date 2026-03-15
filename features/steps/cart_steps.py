"""Step definitions for cart feature."""
from behave import given, when, then
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@when('I add the first product to the cart')
def step_add_first(context):
    context.inventory_page.add_first_product_to_cart()


@when('I add the second product to the cart')
def step_add_second(context):
    context.inventory_page.add_product_by_index(1)


@when('I remove the first product from the cart')
def step_remove_first_from_inventory(context):
    context.inventory_page.remove_product_by_index(0)


@then('the cart badge should show "{count}" item')
def step_badge_count_singular(context, count):
    step_badge_count_plural(context, count)


@then('the cart badge should show "{count}" items')
def step_badge_count_plural(context, count):
    expected = int(count)
    actual = context.inventory_page.get_cart_badge_count()
    assert actual == expected, f"Expected cart badge {expected}, got {actual}"


@then('the cart badge should not be visible')
def step_badge_not_visible(context):
    count = context.inventory_page.get_cart_badge_count()
    assert count == 0, f"Expected no badge, got badge count {count}"


@when('I open the cart')
def step_open_cart(context):
    context.inventory_page.open_cart()
    context.cart_page = CartPage(context.driver)


@when('I remove the first item from the cart')
def step_remove_first_in_cart(context):
    context.cart_page.remove_first_item()


@then('the cart should have "{count}" items')
def step_cart_item_count(context, count):
    expected = int(count)
    actual = context.cart_page.get_cart_item_count()
    assert actual == expected, f"Expected {expected} items in cart, got {actual}"
