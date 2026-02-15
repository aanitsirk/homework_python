from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/inputs')

sleep(3)

search_input = 'input[type="number"]'
text_input = driver.find_element(By.CSS_SELECTOR, search_input)

text = 'Sky'
text_input.send_keys(text)

sleep(3)

text_input.clear()

text = 'Pro'
text_input.send_keys(text)

sleep(3)

driver.quit()
