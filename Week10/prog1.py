from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

#Locate an element by ID
element_by_id = driver.find_element(By.ID,"id-search-field")
print(element_by_id)

# Locate an element by Class
element_by_class = driver.find_element(By.CLASS_NAME, "main-header")
print(element_by_class)

driver.close()