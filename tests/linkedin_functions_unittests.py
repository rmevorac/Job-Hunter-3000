import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from utils.linkedin import linkedin_login
from utils.user import User

class TestLinkedInLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # or any WebDriver of your choice
        self.user = User(first_name="John", last_name="Doe", username="johndoe@example.com", password="password123")
        self.driver.get("https://www.linkedin.com")

    def test_successful_login_already_signed_in(self):
        # Simulate already signed in scenario
        self.driver.find_element(By.CLASS_NAME, "search-global-typeahead__input").is_displayed = lambda: True
        search_bar = linkedin_login(self.driver, self.user)
        self.assertIsNotNone(search_bar)

    def test_successful_login_saved_profile_click(self):
        # Simulate saved profile click scenario
        self.driver.find_element(By.CLASS_NAME, "profile__identity").click()
        search_bar = linkedin_login(self.driver, self.user)
        self.assertIsNotNone(search_bar)

    def test_successful_login_manual_login(self):
        # Simulate manual login scenario
        try:
            self.driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
        except NoSuchElementException:
            self.driver.find_element(By.ID, "username").send_keys(self.user.username)
            self.driver.find_element(By.ID, "password").send_keys(self.user.password, Keys.ENTER)
        search_bar = self.driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
        self.assertIsNotNone(search_bar)

    def test_unsuccessful_login_saved_profile_not_found(self):
        # Simulate saved profile not found scenario
        with self.assertRaises(SystemExit):
            linkedin_login(self.driver, self.user)

    def test_unsuccessful_login_incorrect_credentials(self):
        # Simulate incorrect credentials scenario
        self.user.password = "wrongpassword"
        with self.assertRaises(SystemExit):
            linkedin_login(self.driver, self.user)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
