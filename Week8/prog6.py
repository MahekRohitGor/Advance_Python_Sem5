from bs4 import BeautifulSoup
html_content = "<html><head><title>Python</title></head><body> <p> Hello World This is Mahek Gor </p></body></html>"

soup = BeautifulSoup(html_content, "html.parser")
print("Title: ", soup.text)
print("Paragraph: ", soup.p.text)