"""Checkout (information and overview) page objects for SauceDemo."""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger()


class CheckoutPage(BasePage):
    FIRST_NAME = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME = (By.CSS_SELECTOR, "#last-name")
    POSTAL_CODE = (By.CSS_SELECTOR, "#postal-code")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#continue")
    FINISH_BUTTON = (By.CSS_SELECTOR, "#finish")
    CONFIRMATION_HEADER = (By.CSS_SELECTOR, ".complete-header")
    CONFIRMATION_MESSAGE = (By.CSS_SELECTOR, ".complete-text")

    def fill_info(self, first_name, last_name, postal_code):
        self.send_keys(self.FIRST_NAME, first_name)
        self.send_keys(self.LAST_NAME, last_name)
        self.send_keys(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE_BUTTON)
        logger.info("Checkout info submitted")

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)
        logger.info("Checkout finished")

    def get_confirmation_header(self):
        return self.get_text(self.CONFIRMATION_HEADER)

    def get_confirmation_message(self):
        return self.get_text(self.CONFIRMATION_MESSAGE)
