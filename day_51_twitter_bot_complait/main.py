from selenium import webdriver
import os
from dotenv import load_dotenv
from day_51_twitter_bot_complait.login import Login

load_dotenv()

TWITTER_URL = "https://www.x.com"
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(TWITTER_URL)

login = Login(driver)
login.click_signin_button()
login.enter_username(USER)
login.click_next_button()
login.enter_password(PASSWORD)
login.click_submit_button()
