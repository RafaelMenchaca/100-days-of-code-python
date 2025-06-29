from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.signin_button = (By.CSS_SELECTOR, '[data-testid="loginButton"]')
        self.username_field = (By.NAME, "text")
        self.next_button = (By.XPATH, '//button[.//span[text()="Next"]]')
        self.password_field = (By.CSS_SELECTOR, '[name="password"]')
        self.submit_button = (By.CSS_SELECTOR, '[data-testid="LoginForm_Login_Button"]')


    def click_signin_button(self, timeout=10):
        WebDriverWait(self.driver,timeout).until(
            EC.element_to_be_clickable(self.signin_button)
        ).click()

    def enter_username(self, username, timeout=10):
        field = WebDriverWait(self.driver,timeout).until(
            EC.visibility_of_element_located(self.username_field)
        )
        field.clear()
        field.send_keys(username)

    def click_next_button(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.next_button)
        ).click()

    def enter_password(self, password, timeout=10):
        field = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.password_field)
        )
        field.clear()
        field.send_keys(password)

    def click_submit_button(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.submit_button)
        ).click()


