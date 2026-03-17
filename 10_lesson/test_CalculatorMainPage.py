import pytest
import allure
from selenium import webdriver
from CalculatorMainPage import CalculatorMainPage


@pytest.fixture
def driver():
    """Фикстура для создания и закрытия драйвера браузера."""
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Тест калькулятора")
@allure.description("Проверка сложения 7 + 8 с задержкой 45 секунд")
def test_CalculatorMainPage(driver):
    """
    Тест на проверку сложения двух чисел с учетом заданной задержки.

    :param: driver - фикстура с экземпляром WebDriver.
    """
    calc = CalculatorMainPage(driver)
    calc.open()
    calc.set_delay('45')
    calc.click_buttons(['7', '+', '8', '='])
    calc.wait_for_result('15')
    result = calc.get_result()
    assert result == '15'
