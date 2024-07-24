from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from element import BasePageElement
from locators import LoginPageLocators, ProfilesPageLocators, HomePageLocators

class UsernameElement(BasePageElement):
    """This class gets the username text from the specified locator"""
    locator = "username"

class PasswordElement(BasePageElement):
    """This class gets the password text from the specified locator"""
    locator = "password"

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

class LoginPage(BasePage):
    """Login page action methods come here"""

    username_element = UsernameElement()
    password_element = PasswordElement()

    def enter_username(self, username):
        element = self.driver.find_element(*LoginPageLocators.USERNAME)
        element.send_keys(username)

    def enter_password(self, password):
        element = self.driver.find_element(*LoginPageLocators.PASSWORD)
        element.send_keys(password)
        element.send_keys(Keys.ENTER)

class ProfilesPage(BasePage):
    """Profiles page action methods come here"""
    
    def click_profile(self):
        element = self.driver.find_element(*ProfilesPageLocators.PROFILE_IDENTITY)
        element.click()

class HomePage(BasePage):
    """Home page action methods come here"""
    
    def is_search_bar_present(self):
        try:
            self.driver.find_element(*HomePageLocators.SEARCH_BAR)
            return True
        except NoSuchElementException:
            return False
