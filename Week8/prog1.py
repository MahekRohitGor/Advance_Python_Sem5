# Import the BeautifulSoup library
from bs4 import BeautifulSoup
# HTML content to be parsed
html_content = "<div id='content'><p>Hello World I am Mahek</p></div>"
# Create a BeautifulSoup object to parse the HTML content using the "html.parser" parser
soup = BeautifulSoup(html_content, "html.parser")
# Find the <div> element with the id "content" in the parsed HTML
div = soup.find("div", id="content")
# Access the <p> element within the found <div> element and extract its text
paragraph_text = div.p.text
# Print the extracted text
print(paragraph_text)