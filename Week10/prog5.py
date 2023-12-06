from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.hyrtutorials.com/p/frames-practice.html")

wait = WebDriverWait(driver, 10)
iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@id='frm1']")))
driver.switch_to.frame(iframe)

dropdown = Select(driver.find_element(By.CSS_SELECTOR, "select#selectnav2.selectnav"))
dropdown.select_by_value("https://www.hyrtutorials.com/p/contactus.html")

sleep(5)

driver.switch_to.default_content()
