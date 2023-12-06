#Home-assignment task for any NEWS-related website:
# 1. Scrape the titles and links of articles from the news website and save the data to a CSV file.
# 2. Scrape images from the website and save them in a folder.
# 3. Scrape data from multiple pages of the website
import requests
import csv
import os
import re
from bs4 import BeautifulSoup

def scrape_titles_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    titles = soup.find_all("div", class_ = "WavNE")
    links = soup.find_all('a', href=True)

    with open("news_title_links.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Links'])
        for titles,links in zip(titles,links):
            writer.writerow([titles.text, links['href']])

def scrape_titles_links1(url):
    csv_exists = os.path.exists("news_title_links_multiple_pages.csv")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    div_elements = soup.find_all("div", class_="pZFl7")
    
    for div_element in div_elements:
        h1_element = div_element.find("h1", class_="HNMDR")
            
        if h1_element:
            span_element = h1_element.find("span")
            if span_element:
                title = span_element.text
            else:
                print("No <span> element found within the <h1>.")
        else:
            print("No <h1> element found within the <div>.")
        link = url 
    
    with open("news_title_links_multiple_pages.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if not csv_exists:  # Write headers only if the file is newly created
            writer.writerow(['Title', 'Links'])
            csv_exists = True  
        writer.writerow([title, link])

def clean_filename(filename):
    # Use regular expressions to remove invalid characters from the filename
    clean_filenames = re.sub(r'[\\/:*?"<>|]', '', filename)
    return clean_filenames

def scrape_images(url, path_to_folder):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    img = soup.find_all("img", src=True)
    if not os.path.exists(path_to_folder):
        os.makedirs(path_to_folder)
    
    for imgs in img:
        img_url = imgs["src"]
        img_filename = clean_filename(img_url.split("/")[-1])
        img_res = requests.get(img_url)
        with open(os.path.join(path_to_folder, img_filename), "wb") as file:
            file.write(img_res.content)

def scrape_multiple_pages(url):
    # Sub pages within TOI/india
    pages = ["stand-in-solidarity-with-israel-at-this-difficult-hour-pm-modi/articleshow/104241034.cms",
         "pm-modi-chairs-meeting-to-review-steps-for-implementation-of-independence-day-announcements/articleshow/104237612.cms",
         "israel-palestine-conflict-india-issues-advisory-for-its-nationals-in-israel/articleshow/104236885.cms"]
    for page in pages:
        full_url = url + page
        scrape_titles_links1(full_url)
        image_folder = "images"
        scrape_images(full_url, image_folder)


if __name__ == "__main__":
    scrape_multiple_pages("https://timesofindia.indiatimes.com/india/")
    scrape_titles_links("https://timesofindia.indiatimes.com/india/")
    scrape_images("https://timesofindia.indiatimes.com/india/", "images")