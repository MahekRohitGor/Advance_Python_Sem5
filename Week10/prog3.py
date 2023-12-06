import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.bstackdemo.com")
dropdown = Select(driver.find_element(By.CSS_SELECTOR, "Select"))
dropdown.select_by_value("lowestprice")
time.sleep(5)
driver.quit()