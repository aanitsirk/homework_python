from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.auth_field = (By.CSS_SELECTOR, 'div.login_wrapper-inner')
        self.username_input = (By.CSS_SELECTOR, '#user-name')
        self.password_input = (By.CSS_SELECTOR, '#password')
        self.login_button = (By.CSS_SELECTOR, '#login-button')

    def open(self):
        self.driver.get('https://www.saucedemo.com/')
        self.wait.until(EC.presence_of_element_located(self.auth_field))

    def enter_username(self, username):
        username_field = self.driver.find_element(*self.username_input)
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(*self.password_input)
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        button = self.driver.find_element(*self.login_button)
        button.click()
