"""
Provides functions for web scraping tasks, including data extraction, parsing, and handling web pages.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

def wait_for_content_change(driver, class_name, old_content, timeout=10):
    """
    Waits for a content change and returns the new element, else returns None.
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            new_content = driver.find_element(By.CLASS_NAME, class_name)
            if new_content.text != old_content:
                return new_content
        except StaleElementReferenceException:
            pass
        time.sleep(0.5)  # Check every 0.5 seconds
    return None