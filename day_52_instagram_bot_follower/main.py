from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv

load_dotenv()

# Credentials and constants
USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")
TARGET = "chefsteps"
INSTA_URL = "https://www.instagram.com/accounts/login/"
MODAL_XPATH = "/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]"

# setting the webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# open the page here
driver.get(INSTA_URL)


# class to follow pp on insta
class InstaFollower:

    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.CSS_SELECTOR, '[name="username"]')
        self.password_field = (By.CSS_SELECTOR, '[name="password"]')
        self.login_button = (By.CSS_SELECTOR, '[type="submit"]')
        self.save_login_prompt = (By.XPATH, "//div[contains(text(), 'Not now')]")
        self.notifications_prompt = (By.XPATH, "// button[contains(text(), 'Not Now')]")
        self.modal = (By.XPATH, MODAL_XPATH)
        self.followers_button = (By.CSS_SELECTOR, f'[href="/{TARGET}/followers/"]')




    def login(self, username, password,  timeout=10):
        username_field = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.username_field)
        )
        username_field.clear()
        username_field.send_keys(username)

        password_field = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.password_field)
        )
        password_field.clear()
        password_field.send_keys(password)

        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

        if self.save_login_prompt:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(self.save_login_prompt)
            ).click()

        # if self.notifications_prompt:
        #     WebDriverWait(self.driver, timeout).until(
        #         EC.element_to_be_clickable(self.notifications_prompt)
        #     ).click()

    def find_followers(self, timeout=10):
        sleep(5)
        self.driver.get(f"https://www.instagram.com/{TARGET}/")
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.followers_button)
        ).click()
        sleep(3)
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", self.modal)
            sleep(2)



    def follow(self):
        pass



bot_follower = InstaFollower(driver)
bot_follower.login(USERNAME, PASSWORD)
bot_follower.find_followers()