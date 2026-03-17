import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """
    Класс для оформления заказа на сайте интернет-магазина.
    Содержит методы для заполнения формы данными
    (имя, фамилия, почтовый индекс) и проверки итоговой стоимости.
    """
    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор класса CheckoutPage для инициализации
        страницы оформления заказа.

        :param driver: WebDriver - объект драйвера для управления браузером.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.first_name_input = (By.CSS_SELECTOR, '#first-name')
        self.last_name_input = (By.CSS_SELECTOR, '#last-name')
        self.postal_code_input = (By.CSS_SELECTOR, '#postal-code')
        self.continue_button = (By.CSS_SELECTOR, '#continue')
        self.total_label = (By.CSS_SELECTOR, 'div.summary_total_label')

    @allure.step("Ожидать загрузку формы оформления заказа")
    def wait_for_checkout_form(self) -> None:
        """Ожидает загрузку формы ввода данных покупателя."""
        self.wait.until(EC.presence_of_element_located(self.first_name_input))

    @allure.step("Ввести имя: {first_name}")
    def enter_first_name(self, first_name: str) -> None:
        """
        Вводит имя покупателя в соответствующее поле.

        :param first_name: str - имя покупателя.
        """
        first_name_field = self.driver.find_element(*self.first_name_input)
        first_name_field.clear()
        first_name_field.send_keys(first_name)

    @allure.step("Ввести фамилию: {last_name}")
    def enter_last_name(self, last_name: str) -> None:
        """
        Вводит фамилию покупателя в соответствующее поле.

        :param last_name: str - фамилия покупателя.
        """
        last_name_field = self.driver.find_element(*self.last_name_input)
        last_name_field.clear()
        last_name_field.send_keys(last_name)

    @allure.step("Ввести почтовый индекс: {postal_code}")
    def enter_postal_code(self, postal_code: str) -> None:
        """
        Вводит почтовый индекс покупателя в соответствующее поле.

        :param postal_code: str - почтовый индекс покупателя.
        """
        postal_code_field = self.driver.find_element(*self.postal_code_input)
        postal_code_field.clear()
        postal_code_field.send_keys(postal_code)

    @allure.step("Нажать кнопку Continue")
    def click_continue(self) -> None:
        """Нажимает кнопку Continue для продолжения оформления заказа."""
        button = self.driver.find_element(*self.continue_button)
        button.click()

    @allure.step("Ожидать отображение итоговой суммы")
    def wait_for_total(self) -> None:
        """Ожидает появление итоговой суммы на странице."""
        self.wait.until(EC.presence_of_element_located(self.total_label))

    @allure.step("Получить итоговую сумму заказа")
    def get_total(self) -> str:
        """
        Возвращает итоговую сумму заказа.

        :return: str - итоговая сумма в формате "$XX.XX"
        """
        total_element = self.driver.find_element(*self.total_label)
        total_text = total_element.text
        total_price = total_text.split()[1]
        return total_price
