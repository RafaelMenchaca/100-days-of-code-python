from selenium import webdriver
from day_51_twitter_bot_complait.internet_speed_twitter_bot import InternetSpeedTwitterBot

SPEED_TEST_URL = "https://www.speedtest.net/"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(SPEED_TEST_URL)

internet_speed = InternetSpeedTwitterBot(driver)
internet_speed.click_go_button()
