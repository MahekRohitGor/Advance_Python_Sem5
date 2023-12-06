import requests
from bs4 import BeautifulSoup

url = "https://www.geeksforgeeks.org/playfair-cipher-with-examples/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
img = soup.find("img")
src = img["src"]
alt = img["alt"]
print(f"Source of image is : {src}")
print(f"Alternate text for image is: {alt}")