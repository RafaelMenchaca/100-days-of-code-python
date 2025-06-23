from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Game URL
URL = "https://ozh.github.io/cookieclicker/"

# Keep browser open after script finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Start driver
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Max wait time for elements
wait = WebDriverWait(driver, 10)

# ✅ Function to handle cookie banner if it appears
def accept_cookies():
    try:
        # Wait until the cookie banner is visible
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cc_btn_accept_all")))
        # Find and click the accept button
        accept_button = driver.find_element(By.CSS_SELECTOR, value=".cc_btn_accept_all")
        if accept_button.is_displayed() and accept_button.is_enabled():
            print("🟢 Accepting cookies...")
            accept_button.click()
    except:
        print("🟡 No cookie banner found or already accepted.")

# ✅ First cookie banner (on initial page load)
accept_cookies()

# ✅ Wait for language selector to show up
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "langSelectButton")))

# ✅ Choose English language
language_selector = driver.find_element(By.ID, value="langSelect-EN")
language_selector.click()

# ✅ Second cookie banner (reappears after selecting language)
accept_cookies()

# ✅ Wait for big cookie to appear
wait.until(EC.element_to_be_clickable((By.ID, 'bigCookie')))

# ✅ Find the cookie and start clicking
big_cookie = driver.find_element(By.ID, "bigCookie")
print("🍪 Starting to click the cookie...")

# ✅ Click the cookie for 10 seconds
timeout = 60
end_time = sleep_start = sleep(0) or time() + timeout
while time() < end_time:
    big_cookie.click()


number_of_cookies = driver.find_element(By.ID, value="cookies")
int_number_of_cookies = int(number_of_cookies.text.split()[0])
print(f"number of cookies: {int_number_of_cookies}")


price_cursor = driver.find_element(By.ID, value="productPrice0")
int_price_cursor = int(price_cursor.text)
print(f"price cursor: {int_price_cursor}")

if int_number_of_cookies >= int_price_cursor:
    cursor = driver.find_element(By.ID, value="product0")
    cursor.click()
    print("cursor purchased")

products = driver.find_elements(By.CSS_SELECTOR, value="#products .product.enabled")
enabled_products = {}

for n in range(len(products)):
    enabled_products[n] = products[n].text

print(enabled_products)




# ✅ Close the browser
# driver.quit()
