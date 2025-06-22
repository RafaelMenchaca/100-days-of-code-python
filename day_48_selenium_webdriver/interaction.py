from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


WIKI_URL = "https://en.wikipedia.org/wiki/Main_Page"
APP_WREBERY = "https://secure-retreat-92358.herokuapp.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(APP_WREBERY)

# article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# article_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
# print(article_count.text)
# article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# search_click_fake = driver.find_element(By.XPATH, value='//*[@id="p-search"]/a')
# search_click_fake.click()
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("python")
# search.send_keys(Keys.ENTER)
# search_click = driver.find_element(By.XPATH, value='//*[@id="searchform"]/div/button')
# search_click.click()

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Rafael")

last_name =  driver.find_element(By.NAME, value="lName")
last_name.send_keys("Menchaca")

email_address = driver.find_element(By.NAME, value="email")
email_address.send_keys("arafael.menchaca@gmail.com")

sing_up = driver.find_element(By.CSS_SELECTOR, value="form button")
sing_up.click()



driver.quit()  #Close all windows
