from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorMainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.delay_input = (By.CSS_SELECTOR, '#delay')
        self.result_screen = (By.CSS_SELECTOR, 'div.screen')

    def open(self):
        base_url = "https://bonigarcia.dev"
        path = "/selenium-webdriver-java/slow-calculator.html"
        self.driver.get(base_url + path)
        self.wait.until(EC.presence_of_element_located(self.delay_input))

    def set_delay(self, seconds):  # поле ввода задержки
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(seconds)

    def click_buttons(self, buttons):  # кнопки калькулятора
        for button_text in buttons:
            button_locator = (By.XPATH, f'//span[text()="{button_text}"]')
            button = self.driver.find_element(*button_locator)
            button.click()

    def wait_for_result(self, expected_result):  # ожидание рез-та
        wait = WebDriverWait(self.driver, 50)
        wait.until(EC.text_to_be_present_in_element(
            self.result_screen, expected_result
            ))
        return self.get_result()

    def get_result(self):  # поле вывода результата
        result_field = self.driver.find_element(*self.result_screen)
        return result_field.text
