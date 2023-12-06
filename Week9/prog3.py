import requests
from bs4 import BeautifulSoup

url = "https://morth.nic.in/motor-vehicles-act-1988"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find("table")
for row in table.find_all("tr")[0:]:
    columns = row.find_all("td")
    data1 = columns[0].text
    data2 = columns[1].text
    print(f"Data-1: {data1}")
    print(f"Data-2: {data2}")