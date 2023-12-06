from bs4 import BeautifulSoup
html_content ="<ol><li> Python </li> <li> Java </li>"
soup=BeautifulSoup(html_content,"html.parser")

d=soup.ol
for p in d.find_all("li"):
    print(p.text)

