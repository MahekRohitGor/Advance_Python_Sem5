from bs4 import BeautifulSoup
import requests

url = "https://www.wikipedia.org/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# Extract and print the page title
print("Page Title: ", soup.title.text)

d = soup.div
for p in d.find_all("h1"):
    print(p.text)

data1 = soup.find("span", class_="central-textlogo__image sprite svg-Wikipedia_wordmark")
print(data1.text)