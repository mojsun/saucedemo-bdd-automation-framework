"""Step definitions for login feature."""
from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.test_data import USERS


@given('I am on the login page')
def step_on_login_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open_login()


@when('I log in with username "{username}" and password "{password}"')
def step_login(context, username, password):
    context.login_page.login(username, password)


@when('I log in as "{user_key}"')
def step_login_by_key(context, user_key):
    user = USERS.get(user_key, USERS["standard_user"])
    context.login_page.login(user["username"], user["password"])


@given('I am logged in as "{user_key}"')
def step_logged_in(context, user_key):
    user = USERS.get(user_key, USERS["standard_user"])
    context.login_page = LoginPage(context.driver)
    context.login_page.open_login()
    context.login_page.login(user["username"], user["password"])
    context.inventory_page = InventoryPage(context.driver)


@then('I should be on the inventory page')
def step_on_inventory(context):
    context.inventory_page = InventoryPage(context.driver)
    assert "/inventory.html" in context.inventory_page.current_url(), \
        f"Expected inventory URL, got {context.inventory_page.current_url()}"


@then('the inventory page should display products')
def step_inventory_has_products(context):
    count = context.inventory_page.get_product_count()
    assert count > 0, f"Expected at least one product, got {count}"


@then('an error message should be displayed')
def step_error_displayed(context):
    assert context.login_page.error_is_displayed(), "Expected login error message to be visible"


@then('the error message should contain "{text}"')
def step_error_contains(context, text):
    msg = context.login_page.get_error_message()
    assert text.lower() in msg.lower(), f"Expected error to contain '{text}', got: {msg}"


@given('I am on the inventory page')
def step_on_inventory_page(context):
    if not hasattr(context, "inventory_page"):
        context.inventory_page = InventoryPage(context.driver)
    assert "/inventory.html" in context.inventory_page.current_url(), "Not on inventory page"
