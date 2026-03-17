import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorMainPage:
    """
    Класс для страницы калькулятора.
    Содержит методы для взаимодействия с полем ввода задержки,
    кнопками калькулятора и полем вывода результата.
    """
    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор класса CalculatorMainPage для инициализации
        страницы калькулятора.

        :param driver: WebDriver - объект драйвера для управления браузером.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.delay_input = (By.CSS_SELECTOR, '#delay')
        self.result_screen = (By.CSS_SELECTOR, 'div.screen')

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """
        Открывает страницу калькулятора.
        Ожидает загрузку поля ввода задержки.
        """
        base_url = "https://bonigarcia.dev"
        path = "/selenium-webdriver-java/slow-calculator.html"
        self.driver.get(base_url + path)
        self.wait.until(EC.presence_of_element_located(self.delay_input))

    @allure.step("Установить задержку: {seconds} секунд")
    def set_delay(self, seconds: str) -> None:
        """
        Устанавливает время задержки в поле ввода
        для выполнения операций на калькуляторе.

        :param delay: str - время задержки в секундах.
        """
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(seconds)

    @allure.step("Нажать кнопки: {buttons} на калькуляторе")
    def click_buttons(self, buttons: list) -> None:
        """
        Последовательно нажимает указанные кнопки калькулятора.

        :param buttons: list[str] - список текстов на нажимаемых кнопках.
        """
        for button_text in buttons:
            button_locator = (By.XPATH, f'//span[text()="{button_text}"]')
            button = self.driver.find_element(*button_locator)
            button.click()

    @allure.step("Ожидать результат: '{expected_result}'")
    def wait_for_result(self, expected_result: str) -> str:
        """
        Ожидает появление ожидаемого результата на экране калькулятора.

        :param expected_result: str - ожидаемое значение результата.

        :return: str - фактический результат после ожидания.
        """
        wait = WebDriverWait(self.driver, 50)
        wait.until(EC.text_to_be_present_in_element(
            self.result_screen, expected_result
            ))
        return self.get_result()

    @allure.step("Получить результат с экрана калькулятора")
    def get_result(self) -> str:
        """
        Возвращает полученный результат с экрана калькулятора.

        :return: str - текст результата в окне.
        """
        result_field = self.driver.find_element(*self.result_screen)
        return result_field.text
