import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage:
    """
    Класс для страницы авторизации на сайте интернет-магазина.
    Содержит методы для ввода логина и пароля и для нажатия кнопки входа.
    """
    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор класса AuthPage для инициализации
        страницы авторизации.

        :param driver: WebDriver - объект драйвера для управления браузером.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.auth_field = (By.CSS_SELECTOR, 'div.login_wrapper-inner')
        self.username_input = (By.CSS_SELECTOR, '#user-name')
        self.password_input = (By.CSS_SELECTOR, '#password')
        self.login_button = (By.CSS_SELECTOR, '#login-button')

    @allure.step("Открыть страницу авторизации")
    def open(self) -> None:
        """
        Открывает страницу авторизации интернет-магазина.
        Ожидает загрузку формы авторизации.
        """
        self.driver.get('https://www.saucedemo.com/')
        self.wait.until(EC.presence_of_element_located(self.auth_field))

    @allure.step("Ввести имя пользователя: {username}")
    def enter_username(self, username: str) -> None:
        """
        Вводит имя пользователя в поле логина.

        :param username: str - имя пользователя.
        """
        username_field = self.driver.find_element(*self.username_input)
        username_field.clear()
        username_field.send_keys(username)

    @allure.step("Ввести пароль: {password}")
    def enter_password(self, password: str) -> None:
        """
        Вводит пароль в поле пароля.

        :param password: str - пароль.
        """
        password_field = self.driver.find_element(*self.password_input)
        password_field.clear()
        password_field.send_keys(password)

    @allure.step("Нажать кнопку Login")
    def click_login(self) -> None:
        """Нажимает кнопку входа в систему."""
        button = self.driver.find_element(*self.login_button)
        button.click()
