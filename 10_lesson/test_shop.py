import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from shop_pages.auth_page import AuthPage
from shop_pages.inventory_page import InventoryPage
from shop_pages.cart_page import CartPage
from shop_pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    """Фикстура для инициализации и завершения работы драйвера Firefox."""
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест на оформление заказа в магазине")
@allure.description("""
    Проверка полного сценария покупки товаров:
    1. Авторизация на сайте
    2. Добавление трех товаров в корзину
    3. Переход в корзину
    4. Оформление заказа
    5. Проверка итоговой суммы
""")
def test_shop(driver: WebDriver) -> None:
    """
    Тест проверяет полный сценарий покупки товаров в интернет-магазине.

    :param driver: WebDriver - объект драйвера для управления браузером.
    """
    auth_page = AuthPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    auth_page.open()
    auth_page.enter_username('standard_user')
    auth_page.enter_password('secret_sauce')
    auth_page.click_login()

    inventory_page.wait_for_inventory_page()
    items_id = [
            'add-to-cart-sauce-labs-backpack',
            'add-to-cart-sauce-labs-bolt-t-shirt',
            'add-to-cart-sauce-labs-onesie'
        ]
    inventory_page.add_items(items_id)

    inventory_page.go_to_cart()
    cart_page.wait_for_cart_page()
    cart_page.click_checkout()

    checkout_page.wait_for_checkout_form()
    checkout_page.enter_first_name('Kristina')
    checkout_page.enter_last_name('Maslova')
    checkout_page.enter_postal_code('192288')
    checkout_page.click_continue()

    checkout_page.wait_for_total()
    total = checkout_page.get_total()
    assert total == '$58.29'
