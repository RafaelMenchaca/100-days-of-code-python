from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

AMAZON_URL = "https://www.amazon.com/acer-Gaming-Laptop-GeForce-Backlit/dp/B0DZH5WTQJ/?_encoding=UTF8&pd_rd_w=eSVd8&content-id=amzn1.sym.255b3518-6e7f-495c-8611-30a58648072e%3Aamzn1.symc.a68f4ca3-28dc-4388-a2cf-24672c480d8f&pf_rd_p=255b3518-6e7f-495c-8611-30a58648072e&pf_rd_r=AFS7N31CHASN5P6KKJCS&pd_rd_wg=8geXK&pd_rd_r=a4c95859-79ec-4ce1-876f-525a23826c78&ref_=pd_hp_d_atf_ci_mcx_mr_ca_hp_atf_d&th=1"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

# wait = WebDriverWait(driver, 10)
# wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "a-button-text")))

# a-button-text
#
# click_button = driver.find_element(By.CLASS_NAME, value="a-button-text")
# click_button.click()
#
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
#
# print(f"The price is {price_dollar.text}.{price_cents.text}")

# sear_bar = driver.find_element(By.NAME, value="q")
# print(sear_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)




# driver.close() #Close 1 window
driver.quit()  #Close all windows

