"""
Contains functions for automating tasks on LinkedIn, such as login, profile management, and messaging.
"""

import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

def linkedin_login(driver):
    """
    Logs into LinkedIn using the provided WebDriver instance.
    
    Checks if the user is already signed in by attempting to find the search bar element.
    If the search bar element is not found, prompts the user to log in either by clicking a saved profile
    or entering email/phone and password.

    Args:
        driver (WebDriver): The Selenium WebDriver instance used to interact with the browser.

    Returns:
        search_bar (WebElement): The search bar element if login is successful.

    Raises:
        NoSuchElementException: If login fails due to missing saved profile or incorrect credentials.
    """
    # Check if user is already signed in
    try:
        # Try to find search bar
        search_bar = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")

    except NoSuchElementException:
        # If search bar element doesn't exist, the user needs to log in
        identity = "Roey Mevorach" #input("Enter your first and last name as it appears on your LinkedIn profile: ")

        try:
            # Try to find if the user already has an account saved in this browser and click it if it exists
            driver.find_element(By.CLASS_NAME, "profile__identity").click()

            try:
                # Try to find search bar
                search_bar = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
            
            except NoSuchElementException:
                print("Login was unsuccessful: saved profile not found")
                sys.exit()  # End the program

        except NoSuchElementException:
            # If the user's account isn't saved in the brower, need to log in with email/phone and password
            username = "roeymevorach7@gmail.com" #input("Enter your LinkedIn email/phone: ")
            password = "roey2000" #input("Enter your LinkedIn password: ")

            driver.find_element(By.XPATH, "//input[@id='username']").send_keys(username)
            driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password, Keys.ENTER)

            try:
                # Try to find search bar
                search_bar = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
            
            except NoSuchElementException:
                print("Login was unsuccessful: email/phone or password were incorrect")
                sys.exit()  # End the program

    return search_bar


def get_user_job_preferences():
    return

