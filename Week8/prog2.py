# Import the BeautifulSoup library
from bs4 import BeautifulSoup
# HTML content to be parsed
html_content = "<div><p>Paragraph 1</p><p>Paragraph 2</p></div>"
# Create a BeautifulSoup object to parse the HTML content using the "html.parser" parser
soup = BeautifulSoup(html_content, "html.parser")
# Find the <div> element in the parsed HTML
d = soup.div  # This allows you to navigate from the <div> element
# Iterate through all <p> elements within the <div> element
for p in d.find_all("p"):
    # Print the text content of each <p> element
    print(p.text)