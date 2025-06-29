from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
from dotenv import load_dotenv

load_dotenv()

URL = "https://www.x.com"
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

sleep(5)
sing_in = driver.find_element(By.CSS_SELECTOR, value='[data-testid="loginButton"]')
sing_in.click()

sleep(5)
send_user = driver.find_element(By.CSS_SELECTOR, value='[name="text"]')
send_user.send_keys(USER)
click_next = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
click_next.click()

sleep(3)
send_password = driver.find_element(By.CSS_SELECTOR, value='[name="password"]')
send_password.send_keys(PASSWORD)
click_login = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
click_login.click()

