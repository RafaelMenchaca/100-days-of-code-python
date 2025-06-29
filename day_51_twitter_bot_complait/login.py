from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.login_button = (By.CSS_SELECTOR, '[data-testid="loginButton"]')
        self.username_field = (By.NAME, "text")
        self.next_button = (By.XPATH, '//button[.//span[text()="Next"]]')

    def click_sing_in(self, timeout=10):
        pass

    def enter_username(self, username, timeout=10):
        pass

    def click_next(self, timeout=10):
        pass

