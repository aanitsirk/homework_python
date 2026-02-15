from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/login')

sleep(3)

username_input = driver.find_element(By.ID, 'username')
username_input.send_keys('tomsmith')

sleep(3)

password_input = driver.find_element(By.ID, 'password')
password_input.send_keys('SuperSecretPassword!')

button = driver.find_element(By.CSS_SELECTOR, 'button.radius')
button.click()

sleep(3)

success_message = driver.find_element(By.ID, 'flash')
message_text = success_message.text

print("Текст с плашки: ", message_text)

driver.quit()
