"""Behave hooks: driver lifecycle, screenshot on failure, logging."""
import os
import sys
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from utils.config_reader import get_config
from utils.logger import get_logger

logger = get_logger()
driver = None
config = None


def get_driver():
    global driver, config
    if config is None:
        config = get_config()
    if driver is None:
        options = webdriver.ChromeOptions()
        use_headless = config.get("headless") or os.environ.get("CI") == "true"
        if use_headless:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(config["implicit_wait"])
        driver.set_page_load_timeout(config["page_load_timeout"])
        logger.info("Browser started (headless=%s)", use_headless)
    return driver


def before_all(context):
    context.config = get_config()
    logger.info("Test run starting")


def before_scenario(context, scenario):
    # Fresh driver per scenario so cart/login state doesn't leak between scenarios
    global driver
    if driver is not None:
        try:
            driver.quit()
        except Exception:
            pass
        driver = None
    context.driver = get_driver()
    logger.info("Scenario: %s", scenario.name)


def after_scenario(context, scenario):
    if scenario.status == "failed":
        logger.warning("Scenario failed: %s", scenario.name)
        if context.config.get("screenshot_on_failure", True):
            screenshots_dir = os.path.join(PROJECT_ROOT, "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            name = scenario.name.replace(" ", "_")[:50]
            path = os.path.join(screenshots_dir, f"failure_{name}_{timestamp}.png")
            try:
                context.driver.save_screenshot(path)
                context.embed(path, "image/png", "Screenshot on failure")
                logger.info("Screenshot saved: %s", path)
            except Exception as e:
                logger.warning("Could not save screenshot: %s", e)
    else:
        logger.info("Scenario passed: %s", scenario.name)
    # Quit driver after each scenario to avoid cleanup_error and state leakage
    global driver
    if driver is not None:
        try:
            driver.quit()
        except Exception:
            pass
        driver = None


def after_all(context):
    global driver
    if driver is not None:
        try:
            driver.quit()
        except Exception:
            pass
        driver = None
        logger.info("Test run finished")
