"""Burger menu page object for SauceDemo (logout, etc.)."""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MenuPage(BasePage):
    MENU_BUTTON = (By.CSS_SELECTOR, "#react-burger-menu-btn")
    LOGOUT_LINK = (By.CSS_SELECTOR, "#logout_sidebar_link")

    def open_menu(self):
        self.click(self.MENU_BUTTON)

    def logout(self):
        self.find_clickable(self.LOGOUT_LINK).click()
