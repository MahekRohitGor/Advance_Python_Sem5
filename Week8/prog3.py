# Import the BeautifulSoup library for parsing HTML content
from bs4 import BeautifulSoup
# Define the HTML content as a string
html_content = "<a href='https://example.com'>Visit Example</a>"
# Create a BeautifulSoup object and specify the parser (in this case, "html.parser")
soup = BeautifulSoup(html_content, "html.parser")
# Extract the 'a' (anchor) element from the HTML content
link = soup.a
# Print the text within the 'a' element (in this case, "Visit Example")
print("Link Text: ", link.text)
# Print the value of the 'href' attribute within the 'a' element (in this case, "https://example.com")
print("Link URL: ", link["href"])