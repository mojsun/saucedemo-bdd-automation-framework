"""Step definitions for navigation and logout."""
from behave import when, then
from pages.inventory_page import InventoryPage
from pages.menu_page import MenuPage


@when('I open the side menu')
def step_open_side_menu(context):
    context.menu_page = MenuPage(context.driver)
    context.menu_page.open_menu()


@when('I click logout')
def step_click_logout(context):
    context.menu_page.logout()


@then('I should be on the login page')
def step_on_login_page(context):
    assert "saucedemo.com" in context.driver.current_url and "inventory" not in context.driver.current_url, \
        f"Expected login page, got {context.driver.current_url}"
