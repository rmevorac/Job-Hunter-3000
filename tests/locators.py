from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    """A class for login page locators. All login page locators should come here"""

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")

class ProfilesPageLocators(object):
    """A class for profiles page locators. All profiles page locators should come here"""

    PROFILE_IDENTITY = (By.CLASS_NAME, "profile__identity")

class HomePageLocators(object):
    """A class for home page locators. All home page locators should come here"""

    SEARCH_BAR = (By.CLASS_NAME, "search-global-typeahead__input")