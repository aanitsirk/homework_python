from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/classattr')

sleep(3)

button_locator = 'button.btn-primary'
blue_button = driver.find_element(By.CSS_SELECTOR, button_locator)

blue_button.click()
sleep(3)

alert = driver.switch_to.alert
alert.accept()

driver.quit()
