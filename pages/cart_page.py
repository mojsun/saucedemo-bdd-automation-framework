"""Cart page object for SauceDemo."""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button.cart_button")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "#checkout")

    def get_cart_item_count(self):
        return len(self.find_all(self.CART_ITEMS))

    def remove_first_item(self):
        remove_buttons = self.find_all(self.REMOVE_BUTTON)
        if remove_buttons:
            self.find_clickable(self.REMOVE_BUTTON)
            remove_buttons[0].click()

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
