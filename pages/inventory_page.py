"""Inventory / products page object for SauceDemo."""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    PRODUCT_ITEMS = (By.CSS_SELECTOR, ".inventory_item")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn_inventory")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")

    def get_product_count(self):
        return len(self.find_all(self.PRODUCT_ITEMS))

    def add_first_product_to_cart(self):
        buttons = self.find_all(self.ADD_TO_CART_BUTTON)
        if buttons:
            self.find_clickable(self.ADD_TO_CART_BUTTON)
            buttons[0].click()

    def add_product_by_index(self, index):
        buttons = self.find_all(self.ADD_TO_CART_BUTTON)
        if 0 <= index < len(buttons):
            self.find_clickable(self.ADD_TO_CART_BUTTON)
            buttons[index].click()

    def remove_product_by_index(self, index):
        remove_buttons = self.driver.find_elements(By.CSS_SELECTOR, "button.btn_inventory")
        remove_count = 0
        for btn in remove_buttons:
            if btn.text.strip().lower() == "remove":
                if remove_count == index:
                    btn.click()
                    return
                remove_count += 1

    def get_cart_badge_count(self):
        if not self.is_displayed(self.CART_BADGE):
            return 0
        return int(self.get_text(self.CART_BADGE))

    def open_cart(self):
        self.click(self.CART_LINK)
