"""Login page object for SauceDemo."""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger()


class LoginPage(BasePage):
    USERNAME = (By.CSS_SELECTOR, "#user-name")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def open_login(self):
        self.open("")

    def login(self, username, password):
        self.send_keys(self.USERNAME, username)
        self.send_keys(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
        logger.info("Login submitted for user: %s", username)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def error_is_displayed(self):
        return self.is_displayed(self.ERROR_MESSAGE)
