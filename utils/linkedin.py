"""
Contains functions for automating tasks on LinkedIn, such as login, profile management, and messaging.
"""

import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .scraping import wait_for_content_change

def sign_in(driver, user):
    """
    Logs into LinkedIn using the provided WebDriver instance.
    
    Checks if the user is already signed in by attempting to find the search bar element.
    If the search bar element is not found, prompts the user to log in either by clicking a saved profile
    or entering email/phone and password.

    Args:
        driver (WebDriver): The Selenium WebDriver instance used to interact with the browser.
        user (User): User class instance

    Returns:
        search_bar (WebElement): The search bar element if login is successful.

    Raises:
        NoSuchElementException: If login fails due to missing saved profile or incorrect credentials.
    """
    search_bar = None

    try:
        # Try to find search bar (checking if already logged in)
        search_bar = driver.find_element(By.CLASS_NAME, 'search-global-typeahead__input')

    except NoSuchElementException:
        try:
            # Attempt to log in with saved profile
            profile = driver.find_element(By.CLASS_NAME, 'profile__identity')
            profile_name = profile.text.strip()
            
            if profile_name == user.full_name.strip():
                profile.click()

                try:
                    # Try to find search bar again after login attempt
                    search_bar = driver.find_element(By.CLASS_NAME, 'search-global-typeahead__input')
                
                except NoSuchElementException:
                    print("Sign in was unsuccessful after clicking saved profile")
                    driver.close()
                    sys.exit()

            else:
                driver.find_element(By.XPATH, )
                raise NoSuchElementException("Saved profile does not match user's full name.")

        except NoSuchElementException:
            # If saved profile not found, log in using credentials
            driver.find_element(By.XPATH, "//input[@id='username']").send_keys(user.username)
            driver.find_element(By.XPATH, "//input[@id='password']").send_keys(user.password, Keys.ENTER)

            try:
                # Try to find search bar after login attempt
                search_bar = driver.find_element(By.CLASS_NAME, 'search-global-typeahead__input')
            
            except NoSuchElementException:
                print("Sign in was unsuccessful with provided credentials")
                driver.close()
                sys.exit()

    return search_bar


def get_open_positions(driver):
    """
    Gets all hiring companies and associated info on a single page.
    """
    max_positions = 30
    max_attempts = 3
    old_content = None

    for i in range(max_positions):
        attempts = 0

        while attempts < max_attempts:
            try:
                # Fetch all clickable job cards
                hiring_companies = WebDriverWait(driver, 5).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, 'job-card-container--clickable'))
                )

                # Click on the ith job card
                WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable(hiring_companies[i])
                ).click()

                # Wait for the job details content to load and change
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, 'jobs-details__main-content'))
                )

                all_position_details = wait_for_content_change(driver, 'jobs-details__main-content', old_content, 5)
                
                if all_position_details:
                    position = get_position_details(all_position_details)
                    position['apply_link'] = get_apply_link(driver, all_position_details, position.get('position_linkedin_URL'))
                    print_position_details(position)
                    old_content = all_position_details
                    break  # Exit the retry loop if successful

            except (StaleElementReferenceException, TimeoutException) as e:
                attempts += 1
                if attempts >= max_attempts:
                    print(f"Failed to interact with element after several attempts: {e}")
                    break
                print(f"Encountered {e.__class__.__name__}, retrying ({attempts}/{max_attempts})...")

            except IndexError:
                print("No more elements to interact with.")
                return


def get_position_details(all_position_details):
    position = {}

    try:
        main_position_details = all_position_details.find_element(By.CLASS_NAME, 'job-details-jobs-unified-top-card__container--two-pane')
        
        details_div = main_position_details.find_element(By.CLASS_NAME, 'job-details-jobs-unified-top-card__company-name')
        details_a_tag = details_div.find_element(By.TAG_NAME, 'a')

        position['company_name'] = details_a_tag.text
        position['company_linkedin_URL'] = details_a_tag.get_attribute('href')

        details_div = main_position_details.find_element(By.CLASS_NAME, 'job-details-jobs-unified-top-card__job-title')
        details_a_tag = details_div.find_element(By.XPATH, 'h1/a')

        position['position'] = details_a_tag.text
        position['position_linkedin_URL'] = details_a_tag.get_attribute('href')

        details_div = main_position_details.find_element(By.CLASS_NAME, 'job-details-jobs-unified-top-card__primary-description-container')
        position['position_location'] = details_div.find_element(By.XPATH, 'div/span').text

        details_div = main_position_details.find_elements(By.CLASS_NAME, 'job-details-jobs-unified-top-card__job-insight')

        position['position_salary'] = details_div[0].find_element(By.XPATH, 'span/span').text.split(" · ", 1)[0]
        position['company_size'] = details_div[1].find_element(By.TAG_NAME, 'span').text.split(" · ", 1)[0]

        if "$" not in position['position_salary']:
            position['position_salary'] = None

        position['hirer'], position['hirer_URL'] = get_hirer_details(all_position_details)
        position['position_description'] = all_position_details.find_element(By.CLASS_NAME, 'jobs-description-content__text').text

    except NoSuchElementException:
        print("Some elements could not be found")
    
    return(position)


def get_apply_link(driver, position_details, position_url):
    apply_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(position_details.find_element(By.CLASS_NAME, 'jobs-apply-button--top-card'))
    )

    # Optionally, handle new windows/tabs if that's how the site works
    if apply_button.text == "Apply":
        apply_button.click()

        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[1])
            apply_link = driver.current_url
            driver.close()  # Close the new tab if you don't need it open
            driver.switch_to.window(driver.window_handles[0])  # Switch back to the original tab

    else:
        # If the button leads to a new page in the same tab
        apply_link = position_url

    return apply_link


def get_hirer_details(position_details):
    try:
        hirer_info = position_details.find_element(By.CLASS_NAME, 'hirer-card__hirer-information')

        hirer_name = hirer_info.find_element(By.TAG_NAME, 'a').text.split("\n", 1)[0]
        hirer_URL = hirer_info.find_element(By.TAG_NAME, 'a').get_attribute('href')

        return (hirer_name, hirer_URL)

    except NoSuchElementException:
        print("No hirer details available")
        return (None, None)


def print_position_details(position):
    # Build the output string with formatting
    details = (
        f"Company Name: {position.get('company_name', 'N/A')}\n"
        f"Company LinkedIn URL: {position.get('company_linkedin_URL', 'N/A')}\n"
        f"Company Size: {position.get('company_size', 'N/A')}\n"
        f"Position Title: {position.get('position', 'N/A')}\n"
        f"Position URL: {position.get('position_linkedin_URL', 'N/A')}\n"
        f"Position Description: {position.get('position_description', 'N/A')}\n"
        f"Location: {position.get('position_location', 'N/A')}\n"
        f"Salary: {position.get('position_salary', 'N/A')}\n"
        f"Apply Link: {position.get('apply_link', 'N/A')}\n"
        f"Hirer: {position.get('hirer', 'N/A')}\n"
        f"Hirer URL: {position.get('hirer_URL', 'N/A')}\n"
    )
    
    # Print the detailed string
    print(details)









# IMPLEMENT LATER!!!!

# def sign_out(driver: webdriver):
#     try:
#         # Click on the "Me" button to open the dropdown menu
#         me_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.global-nav__primary-link-me-menu-trigger'))
#         )
#         me_button.click()

#         # Wait for the dropdown menu to be visible
#         dropdown_menu = WebDriverWait(driver, 10).until(
#             EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.global-nav__me-content'))
#         )

#         # Click on the "Sign out" button
#         sign_out_button = WebDriverWait(dropdown_menu, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'logout')]"))
#         )
#         sign_out_button.click()

#     except NoSuchElementException as e:
#         print("An element was not found:", e)
#     except Exception as e:
#         print("An error occurred:", e)

# def search(driver, user):
#     # Need to write function that searches in LinkedIn using the user.job_preferences
#     return