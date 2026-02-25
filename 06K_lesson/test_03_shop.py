from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    driver.get('https://www.saucedemo.com/')

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#user-name')))

    driver.find_element(By.CSS_SELECTOR,
                        '#user-name').send_keys('standard_user')
    driver.find_element(By.CSS_SELECTOR,
                        '#password').send_keys('secret_sauce')

    driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               '.inventory_list')))

    driver.find_element(By.CSS_SELECTOR,
                        '#add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.CSS_SELECTOR,
                        '#add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.CSS_SELECTOR,
                        '#add-to-cart-sauce-labs-onesie').click()

    driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.cart_list')))
    driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               '.checkout_info')))
    driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys('Kristina')
    driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys('Maslova')
    driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('192288')

    driver.find_element(By.CSS_SELECTOR, '#continue').click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                               '.summary_total_label')))
    total_label = driver.find_element(By.CSS_SELECTOR,
                                      '.summary_total_label').text
    total_price = total_label.split()[1]

    expected_total = '$58.29'
    assert total_price == expected_total

    driver.quit()
