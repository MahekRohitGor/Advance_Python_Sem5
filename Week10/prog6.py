from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.pdpu.ac.in/")
driver.save_screenshot("screenshot.png")