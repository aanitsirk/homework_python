import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    """
    Класс для главной страницы интернет-магазина.
    Содержит методы для добавления товаров в корзину и перехода в корзину.
    """
    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор класса InventoryPage для инициализации
        страницы с товарами.

        :param driver: WebDriver - объект драйвера для управления браузером.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.inventory_list = (By.CSS_SELECTOR, 'div.inventory_list')
        self.cart_button = (By.CSS_SELECTOR, 'a.shopping_cart_link')

    @allure.step("Ожидать загрузку страницы с товарами")
    def wait_for_inventory_page(self) -> None:
        """Ожидает загрузку списка товаров на странице."""
        self.wait.until(EC.presence_of_element_located(self.inventory_list))

    @allure.step("Добавить товары в корзину: {items_id}")
    def add_items(self, items_id: list) -> None:
        """
        Добавляет указанные товары в корзину по ID.

        :param items_id: list[str] - список ID кнопок для добавления товаров.
        """
        for item_id in items_id:
            self.driver.find_element(By.CSS_SELECTOR, f'#{item_id}').click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """Переходит на страницу корзины."""
        self.driver.find_element(*self.cart_button).click()
