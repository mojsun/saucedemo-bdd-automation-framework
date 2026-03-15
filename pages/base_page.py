"""Base page with reusable WebDriver methods and explicit waits."""
import os
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Allow imports from project root
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.config_reader import get_config
from utils.logger import get_logger

logger = get_logger()


class BasePage:
    def __init__(self, driver, base_url=None):
        self.driver = driver
        config = get_config()
        self.base_url = base_url or config["base_url"]
        self.wait = WebDriverWait(driver, config["explicit_wait"])

    def open(self, path=""):
        url = self.base_url if path.startswith("http") else f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"
        self.driver.get(url)
        logger.info("Opened %s", url)

    def find(self, locator_tuple, timeout=None):
        wait = WebDriverWait(self.driver, timeout or get_config()["explicit_wait"])
        return wait.until(EC.presence_of_element_located(locator_tuple))

    def find_clickable(self, locator_tuple, timeout=None):
        wait = WebDriverWait(self.driver, timeout or get_config()["explicit_wait"])
        return wait.until(EC.element_to_be_clickable(locator_tuple))

    def find_visible(self, locator_tuple, timeout=None):
        wait = WebDriverWait(self.driver, timeout or get_config()["explicit_wait"])
        return wait.until(EC.visibility_of_element_located(locator_tuple))

    def find_all(self, locator_tuple, timeout=None):
        self.wait.until(EC.presence_of_element_located(locator_tuple))
        return self.driver.find_elements(*locator_tuple)

    def click(self, locator_tuple):
        self.find_clickable(locator_tuple).click()

    def send_keys(self, locator_tuple, text):
        el = self.find(locator_tuple)
        el.clear()
        el.send_keys(text)

    def get_text(self, locator_tuple):
        return self.find_visible(locator_tuple).text

    def is_displayed(self, locator_tuple, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator_tuple))
            return True
        except Exception:
            return False

    def current_url(self):
        return self.driver.current_url
