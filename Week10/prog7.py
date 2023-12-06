import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(11)
driver.get("https://google.com")
Element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "APjFqb"))
)
Element = driver.find_element(By.ID, "APjFqb")
Element.send_keys("Mahek R. Gor")
Element.submit()
time.sleep(5)