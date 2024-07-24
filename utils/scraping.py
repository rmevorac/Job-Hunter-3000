"""
Provides functions for web scraping tasks, including data extraction, parsing, and handling web pages.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def wait_for_content_change(driver, element, old_content, timeout=10):
    start_time = time.time()
    while time.time() - start_time < timeout:
        # Refresh the element or re-find it to get the updated content
        new_content = driver.find_element(By.ID, element.id).text
        if new_content != old_content:
            return True
        time.sleep(0.5)  # Check every 0.5 seconds
    return False