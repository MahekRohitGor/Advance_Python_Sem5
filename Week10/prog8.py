import time
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://www.techbeamers.com/selenium-webdriver-waits-python/")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
page_source = driver.page_source

soup = BeautifulSoup(page_source, "html.parser")
print("Title: ", soup.title.text)