from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
URL = "https://www.linkedin.com/jobs/search-results/?distance=50&eBP=NON_CHARGEABLE_CHANNEL&f_AL=true&geoId=103644278&keywords=maintenance%20technician&origin=JOBS_HOME_SEARCH_BUTTON&refId=QI7ypX1E23QzOl2c8eMKNQ%3D%3D&trackingId=5y63UZk6imeYVhCjUVPhIg%3D%3D"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

wait = WebDriverWait(driver, 10)

sleep(3)

login_user = driver.find_element(By.ID, value="username")
login_user.click()
login_user.send_keys(USER)

login_password = driver.find_element(By.ID, value="password")
login_password.click()
login_password.send_keys(PASSWORD)
# login_password.send_keys(Keys.ENTER)

login_button = driver.find_element(By.CLASS_NAME, value="from__button--floating")
login_button.click()


wait.until(EC.visibility_of_element_located((By.ID, "jobs-apply-button-id")))
click_apply_job = driver.find_element(By.ID, value="jobs-apply-button-id")
click_apply_job.click()


# ember4034
#
# ember4034

