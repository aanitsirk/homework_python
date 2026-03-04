from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.first_name_input = (By.CSS_SELECTOR, '#first-name')
        self.last_name_input = (By.CSS_SELECTOR, '#last-name')
        self.postal_code_input = (By.CSS_SELECTOR, '#postal-code')
        self.continue_button = (By.CSS_SELECTOR, '#continue')
        self.total_label = (By.CSS_SELECTOR, 'div.summary_total_label')

    def wait_for_checkout_form(self):
        self.wait.until(EC.presence_of_element_located(self.first_name_input))

    def enter_first_name(self, first_name):
        first_name_field = self.driver.find_element(*self.first_name_input)
        first_name_field.clear()
        first_name_field.send_keys(first_name)

    def enter_last_name(self, last_name):
        last_name_field = self.driver.find_element(*self.last_name_input)
        last_name_field.clear()
        last_name_field.send_keys(last_name)

    def enter_postal_code(self, postal_code):
        postal_code_field = self.driver.find_element(*self.postal_code_input)
        postal_code_field.clear()
        postal_code_field.send_keys(postal_code)

    def click_continue(self):
        button = self.driver.find_element(*self.continue_button)
        button.click()

    def wait_for_total(self):
        self.wait.until(EC.presence_of_element_located(self.total_label))

    def get_total(self):
        total_element = self.driver.find_element(*self.total_label)
        total_text = total_element.text
        total_price = total_text.split()[1]
        return total_price
