from time import sleep,strftime, gmtime
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")
sleep(5)

driver.get("http://www.aajtak.com")
driver.back()
sleep(5)
driver.forward()
sleep(5)
driver.quit()