from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
import csv

# rxTTw
driver = webdriver.Chrome()
driver.get("https://timesofindia.indiatimes.com/")

element = driver.find_element(By.CLASS_NAME, "rxTTw")
element.click()
time.sleep(10)
response = requests.get("https://timesofindia.indiatimes.com/explainers")
soup = BeautifulSoup(response.content, "html.parser")
links = soup.find_all("a")

with open("data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(['Links'])
        for link in links:
            writer.writerow(link['href'])
driver.quit()