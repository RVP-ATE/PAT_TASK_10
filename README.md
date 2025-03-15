Instagram Follower and Following Count Fetcher
This Python program automates the process of logging into Instagram, searching for a user by their username, navigating to their profile, and extracting the number of followers and following. The script uses the Selenium library to interact with Instagram's website through a web browser.

Requirements
Python 3.x
Selenium
Chrome WebDriver (or another browser driver like Firefox WebDriver)
Required Libraries
selenium
time
You can install the required libraries by running the following command:

bash
Copy
pip install selenium
Additionally, you will need the Chrome WebDriver (or the corresponding WebDriver for your browser). You can download it from the following link:

ChromeDriver
Setup
Download the WebDriver:

Ensure that you download the appropriate version of the WebDriver for your browser. If you're using Chrome, for example, download the correct version of ChromeDriver.
Extract the WebDriver and ensure the executable file is accessible from your Python script.
Configure Instagram Credentials:

Open the InstagramBot class and input your Instagram username and password in the bot = InstagramBot('your_username', 'your_password') line.
How to Run
Clone or download this repository to your local machine.
Open a terminal and navigate to the directory containing the Python script.
Run the script with the following command:
bash
Copy
python instagram_bot.py
The bot will:

Log into Instagram using the provided credentials.
Close any "Save Your Password" prompts.
Search for the user profile you specify.
Navigate to that user's profile.
Extract and display the number of followers and following.
Code Breakdown
Login: Logs in to Instagram using the provided username and password.
Close "Save Password" prompt: Closes any prompt asking to save your password after login.
Search User: Searches for the user profile by entering the username in the search bar.
Navigate to Profile: Clicks on the user profile to open it.
Extract Followers and Following Count: Retrieves the number of followers and following for the user profile.
Example Output
text
Copy
Followers: 2000
Following: 150
Notes
The script currently uses the Chrome WebDriver for automation. If you're using a different browser, you must configure the script accordingly (e.g., Firefox WebDriver).
Always be cautious with automating interactions on social media platforms. Instagram may limit or ban accounts for suspicious activity or bot-like behavior. 
