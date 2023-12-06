import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

search_field = driver.find_element(By.NAME, 'q')
search_field.send_keys('while')
search_field.submit()


time.sleep(5)
driver.quit()