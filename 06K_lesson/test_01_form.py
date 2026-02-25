from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    service = Service("C:/Users/79046/Desktop/edgedriver/msedgedriver.exe")
    driver = webdriver.Edge(service=service)

    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html'
               )

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'form')))

    fields = {
        'input[name="first-name"]': 'Иван',
        'input[name="last-name"]': 'Петров',
        'input[name="address"]': 'Ленина, 55-3',
        'input[name="e-mail"]': 'test@skypro.com',
        'input[name="phone"]': '+7985899998787',
        'input[name="city"]': 'Москва',
        'input[name="country"]': 'Россия',
        'input[name="job-position"]': 'QA',
        'input[name="company"]': 'SkyPro'
    }

    for selector, value in fields.items():
        driver.find_element(By.CSS_SELECTOR, selector).send_keys(value)

    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    zip_code_class = driver.find_element(By.CSS_SELECTOR,
                                         '#zip-code').get_attribute('class')
    assert 'alert py-2 alert-danger' in zip_code_class

    green_fields = ["#first-name", "#last-name",
                    "#address", "#e-mail", "#phone",
                    "#city", "#country", "#job-position", "#company"]

    for id_field in green_fields:
        field_class = driver.find_element(By.CSS_SELECTOR,
                                          id_field).get_attribute('class')
    assert 'alert py-2 alert-success' in field_class

    driver.quit()
