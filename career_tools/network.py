"""
Manages networking tasks such as messaging contacts on LinkedIn to establish connections or seek referrals.
"""

import time
import utils.linkedin as linkedin
from utils.user import User
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def network():
    # Initialize selenium webdriver
    driver = webdriver.Chrome()

    # Go to linkedin.com/feed (Homepage)
    driver.get("https://www.linkedin.com/feed")

    roey = User("Roey", "Mevorach", "roeymevorach7@gmail.com", "roey2000")

    # Log in to LinkedIn
    search_bar = linkedin.sign_in(driver, roey)

    # Go to job postings page (software engineer in NYC)
    # In the future include user input and don't go directly to the URL, doing this now so I could start using it quicker
    driver.get("https://www.linkedin.com/jobs/search/?f_PP=102571732&f_TPR=r86400&geoId=90000070&keywords=software%20engineer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R")

    linkedin.get_open_positions(driver)
    # linkedin.get_position_details(driver)

    driver.close()