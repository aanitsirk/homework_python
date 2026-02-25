import pytest
from selenium import webdriver
from shop_pages.auth_page import AuthPage
from shop_pages.inventory_page import InventoryPage
from shop_pages.cart_page import CartPage
from shop_pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(driver):
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
