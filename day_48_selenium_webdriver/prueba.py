# from os.path import split
# #
# # lista = ['Cursor\n18\n1', 'Grandma\n100']
# #
# # print(lista)
# #
# # # lista = lista[0].split("\n")
# # # print(lista)
# # # print(lista[1])
#
# dict = {
#     0: 'Cursor\n15\n100',
#     1: 'Grandma\n100\n40',
#     2: 'Farm\n250\n3',
#     3: 'Mine\n500\n1',
# }
# new_dict = {}
#
# for n in range(len(dict)):
#     new_dict[n] = {
#         dict[n].split("\n")[0]: dict[n].split("\n")[1]
#     }
#
#
# print(dict)
# print(new_dict)
#
#
#
# # event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
# # event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
# # events = {}
# #
# # for n in range(len(event_times)):
# #     events[n] = {
# #         "time": event_times[n].text,
# #         "name": event_names[n].text,
# #     }
# #
# # print(events)
#

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time

# Setup Chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://ozh.github.io/cookieclicker/")

# Wait for page to load just in case
sleep(3)

# Handle initial popups (cookies consent does not have to be clicked, but language does)
print("Looking for language selection...")
try:
    # Select English language
    language_button = driver.find_element(by=By.ID, value="langSelect-EN")
    print("Found language button, clicking...")
    language_button.click()
    sleep(3) # more loading
except NoSuchElementException:
    print("Language selection not found")

# Wait for everything to settle
sleep(2)

# Find the big cookie to click
cookie = driver.find_element(by=By.ID, value="bigCookie")

# Get all store items (products 0-17)
item_ids = [f"product{i}" for i in range(18)]

# Set timers
wait_time = 5
timeout = time() + wait_time  # Check for purchases every 5 seconds
five_min = time() + 60 * 5  # Run for 5 minutes

while True:
    cookie.click()

    # Every 5 seconds, try to buy the most expensive item we can afford
    if time() > timeout:
        try:
            # Get current cookie count
            cookies_element = driver.find_element(by=By.ID, value="cookies")
            cookie_text = cookies_element.text
            # Extract number from text like "123 cookies"
            cookie_count = int(cookie_text.split()[0].replace(",", ""))

            # Find all available products in the store
            products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")

            # Find the most expensive item we can afford
            best_item = None
            for product in reversed(products):  # Start from most expensive (bottom of list)
                # Check if item is available and affordable (enabled class)
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break

            # Buy the best item if found
            if best_item:
                best_item.click()
                print(f"Bought item: {best_item.get_attribute('id')}")

        except (NoSuchElementException, ValueError):
            print("Couldn't find cookie count or items")

        # Reset timer
        timeout = time() + wait_time

    # Stop after 5 minutes
    if time() > five_min:
        try:
            cookies_element = driver.find_element(by=By.ID, value="cookies")
            print(f"Final result: {cookies_element.text}")
        except NoSuchElementException:
            print("Couldn't get final cookie count")
        break
