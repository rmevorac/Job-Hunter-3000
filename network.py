"""
Manages networking tasks such as messaging contacts on LinkedIn to establish connections or seek referrals.
"""

import time
import functions.linkedin_functions as linkedin
from selenium import webdriver

def network():
    # Initialize selenium webdriver
    driver = webdriver.Chrome()

    # Go to linkedin.com/feed (Homepage)
    driver.get("https://www.linkedin.com/feed")

    # Log in to LinkedIn
    search_bar = linkedin.linkedin_login(driver)

    time.sleep(7)

if __name__ == "__main__":
    network()