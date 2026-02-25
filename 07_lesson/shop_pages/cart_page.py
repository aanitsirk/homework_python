from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.cart_list = (By.CSS_SELECTOR, 'div.cart_list')
        self.cart_item_names = (By.CSS_SELECTOR, 'div.inventory_item_name')
        self.checkout_button = (By.CSS_SELECTOR, '#checkout')

    def wait_for_cart_page(self):
        self.wait.until(EC.presence_of_element_located(self.cart_list))

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
