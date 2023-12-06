import requests
from bs4 import BeautifulSoup

sub_pages = ["python-language-advantages-applications", "download-and-install-python-3-latest-version", "python-3-basics", "python-keywords"]

for page in sub_pages:
    url=f"https://www.geeksforgeeks.org/{page}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    print(">>>>>>Paragraphs>>>>>>>>>")
    para = soup.find_all("p")
    for paras in para:
        print(paras.text)
    print(f"\n>>>>> Headings >>>>>")
    headings=soup.find_all("h1")
    for heading in headings:
        print(heading.text)
    print(f"Scraping done for url {page}")