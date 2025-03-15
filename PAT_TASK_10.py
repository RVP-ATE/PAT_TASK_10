#Import necessary modules from the Selenium library

# WebDriver module to control the browser (e.g., Chrome, Firefox, etc.)
from selenium import webdriver
# By class is used to locate elements on the page
from selenium.webdriver.common.by import By
# WebDriverWait is used to wait for a specific condition to occur
from selenium.webdriver.support.ui import WebDriverWait
# Expected Conditions (EC) is a set of predefined conditions to be used with WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Keys module is used to send keyboard inputs (like pressing keys such as ENTER, TAB, etc.)
from selenium.webdriver.common.keys import Keys
# time module is used for waiting or sleeping during script execution
import time


# Define the InstagramBot class to automate Instagram login, search, and profile extraction
class InstagramBot:

    # Constructor to initialize the bot with username and password
    def __init__(self, username, password):
        # Store the username and password provided to the bot
        self.username = username
        self.password = password

        # Initialize the Chrome WebDriver to interact with Instagram's website
        self.driver = webdriver.Chrome()

    # Function to log in to Instagram using the provided credentials
    def login(self):
        # Navigate to Instagram's login page
        self.driver.get('https://www.instagram.com/accounts/login/')

        # Wait for the page to load fully
        time.sleep(5)

        # Maximize the browser window for better visibility
        self.driver.maximize_window()

        # Wait for an additional 20 seconds (can be reduced or replaced by more reliable waits)
        time.sleep(2)

        # Locate the username and password input fields using their HTML 'name' attributes
        username_input = self.driver.find_element(By.NAME, 'username')
        password_input = self.driver.find_element(By.NAME, 'password')

        # Enter the username and password into the respective fields
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)

        # Simulate pressing the "Enter" key to submit the login form
        password_input.send_keys(Keys.RETURN)

        # Wait for 5 seconds to allow the login process to complete
        time.sleep(5)

    # Function to close the "Save your password" prompt after logging in
    def notnow_close(self):
        # Wait until the "Save your password" prompt becomes visible (using WebDriverWait)
        save_your_password = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@aria-label="Save your password"]'))
        )

        # Find the "Close" button to dismiss the prompt
        close_button = save_your_password.find_element(By.XPATH, "//*[@aria-label='Close']")

        # Click the close button to dismiss the prompt
        close_button.click()

    # Function to search for a user by their username
    def search_user(self, username):
        # Find the search input field by its placeholder text
        search_input = self.driver.find_element(By.XPATH, '//input[@placeholder="Search"]')

        # Enter the username into the search bar to start the search
        search_input.send_keys(username)

        # Wait for 3 seconds to allow suggestions to appear
        time.sleep(3)

        # Press "Enter" to initiate the search for the user
        search_input.send_keys(Keys.RETURN)

        # Wait for 3 seconds for the results to load (this can be adjusted)
        time.sleep(3)

    # Function to navigate to the profile of the given username
    def navigate_to_profile(self, username):
        # Find the profile link based on the username in the URL
        profile_link = self.driver.find_element(By.XPATH, f'//a[@href="/{username}/"]')

        # Click the profile link to open the user's profile page
        profile_link.click()

        # Wait for 10 seconds to ensure the profile page has loaded completely
        time.sleep(10)

    # Function to extract and print the number of followers and following of the profile
    def get_followers_and_following(self):
        try:
            # Locate the followers count and extract the text
            followers = self.driver.find_element(By.XPATH, '//a[contains(@href, "/followers")]/span')
            followers_count = followers.text
            print(f"Followers: {followers_count}")

            # Locate the following count and extract the text
            following = self.driver.find_element(By.XPATH, '//a[contains(@href, "/following")]/span')
            following_count = following.text
            print(f"Following: {following_count}")

        except Exception as e:
            # If there is an error while extracting the follower/following count, print the error message
            print(f"Error extracting follower/following count: {e}")

    # Function to close the browser window once the tasks are completed
    def close_browser(self):
        # Close the WebDriver (the browser window)
        self.driver.quit()


# Main execution block
if __name__ == "__main__":
    # Initialize the bot with Instagram username and password
    bot = InstagramBot('rvpkumar100', 'Pavan@223')

    # Log in to Instagram
    bot.login()

    # Close the "Save your password" prompt if it appears
    bot.notnow_close()

    # Search for the user 'guviofficial'
    bot.search_user('virat.kohli')

    # Navigate to the 'guviofficial' profile
    bot.navigate_to_profile('virat.kohli')

    # Extract and print the follower and following counts of the 'guviofficial' profile
    bot.get_followers_and_following()
