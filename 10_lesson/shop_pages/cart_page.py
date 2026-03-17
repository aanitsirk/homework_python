import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """
    Класс для страницы корзины на сайте интернет-магазина.
    Содержит методы для нажатия кнопки Checkout и проверки содержимого корзины.
    """
    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор класса CartPage для инициализации
        страницы корзины.

        :param driver: WebDriver - объект драйвера для управления браузером.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.cart_list = (By.CSS_SELECTOR, 'div.cart_list')
        self.cart_item_names = (By.CSS_SELECTOR, 'div.inventory_item_name')
        self.checkout_button = (By.CSS_SELECTOR, '#checkout')

    @allure.step("Ожидать загрузку страницы корзины")
    def wait_for_cart_page(self) -> None:
        """Ожидает загрузку списка товаров в корзине."""
        self.wait.until(EC.presence_of_element_located(self.cart_list))

    @allure.step("Нажать кнопку Checkout")
    def click_checkout(self) -> None:
        """Нажимает кнопку для перехода к оформлению заказа."""
        self.driver.find_element(*self.checkout_button).click()
