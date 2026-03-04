from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.inventory_list = (By.CSS_SELECTOR, 'div.inventory_list')
        self.cart_button = (By.CSS_SELECTOR, 'a.shopping_cart_link')

    def wait_for_inventory_page(self):
        self.wait.until(EC.presence_of_element_located(self.inventory_list))

    def add_items(self, items_id):
        for item_id in items_id:
            self.driver.find_element(By.CSS_SELECTOR, f'#{item_id}').click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()
