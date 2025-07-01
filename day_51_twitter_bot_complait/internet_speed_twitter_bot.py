from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

SPEED_TEST_URL = "https://www.speedtest.net/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(SPEED_TEST_URL)


class InternetSpeedTwitterBot:

    def __init__(self, driver):
        self.driver = driver
        self.go_button = (By.CSS_SELECTOR, "a.js-start-test")
        self.up = ""
        self.down = ""


    def click_go_button(self, timeout=1):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self.go_button)
        )
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.go_button)
        )
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.go_button)
        ).click()



    def get_internet_speed(self):
        pass

    def tweet_at_provider(self):
        pass


internet_speed = InternetSpeedTwitterBot(driver)
internet_speed.click_go_button()

wait = WebDriverWait(driver, 10)
# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.download-speed")))
# wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.download-speed")))
# wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.download-speed"), "."))
# presence → visibility → large timeout for “not empty”
WebDriverWait(driver,  5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.download-speed")))
WebDriverWait(driver,  5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.download-speed")))
WebDriverWait(driver, 60).until(lambda d: d.find_element(By.CSS_SELECTOR, "span.download-speed").text != "")

down = driver.find_element(By.CSS_SELECTOR, value="span.download-speed")
print(down.text)