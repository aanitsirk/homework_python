import pytest
from selenium import webdriver
from CalculatorMainPage import CalculatorMainPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_CalculatorMainPage(driver):
    calc = CalculatorMainPage(driver)
    calc.open()
    calc.set_delay('45')
    calc.click_buttons(['7', '+', '8', '='])
    calc.wait_for_result('15')
    result = calc.get_result()
    assert result == '15'
