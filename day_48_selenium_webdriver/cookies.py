from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://ozh.github.io/cookieclicker/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

wait = WebDriverWait(driver, 10)

wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "langSelectButton")))
language_selector = driver.find_element(By.ID, value="langSelect-EN")
language_selector.click()

wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/a[1]')))
accept_cookies = driver.find_element(By.XPATH, value='/html/body/div[1]/div/a[1]')
accept_cookies.click()

wait.until(EC.element_to_be_clickable((By.ID, 'bigCookie')))
click_cookie = driver.find_element(By.XPATH, value='//*[@id="bigCookie"]')
click_cookie.click()

driver.quit()  #Close all windows
