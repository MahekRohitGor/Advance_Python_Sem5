# Import the BeautifulSoup library for parsing HTML content
from bs4 import BeautifulSoup
# Define the HTML content as a string
html_content = "<div class='hello'><p class='text'>Hello World!</p><p class='text'>Hello Mahek!</p></div>"
# Create a BeautifulSoup object and specify the parser (in this case, "html.parser")
soup = BeautifulSoup(html_content, "html.parser")
# Find the first 'p' element with the class attribute "text"
para1 = soup.find("p", class_="text")
# Print the text within the first 'p' element found (in this case, "Hello World!")
print(para1.text)  # Only the text within the first 'p' element with class "text" is considered