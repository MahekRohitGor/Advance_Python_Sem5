from bs4 import BeautifulSoup

html_content = "<ul><li>Milk</li><li>Bread</li><li>Fruits</li></ul>"

html_content_1 = "<table border=1><tr><th>Subjects </th><th> Marks </th></tr><tr><td> Advance Python </td><td> 41.5 </td></tr><tr><td> Information Security </td><td> 46 </td></tr><tr><td> Web Technology </td><td> 46 </td></tr></table>"

soup = BeautifulSoup(html_content, "html.parser")
soup_1 = BeautifulSoup(html_content_1, "html.parser")

items = soup.find_all("li")
items_1 = soup_1.find_all("table")

for item in items:
    print(item.text)

for item_1 in items_1:
    print(item_1.text + "\n")