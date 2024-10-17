import requests
from bs4 import BeautifulSoup
import pandas as pd

current_page = 1

proceed = True

# Set up url, paege, soup
url = "https://en.wikipedia.org/wiki/List_of_Greek_mathematicians"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

# Print title of article / webpage
# print(soup.title.text)

# List all names
all_col_divs = soup.findAll("div", class_="div-col")

# print(all_col_divs)
#ag = ancient greek

name_section = all_col_divs[0]

if name_section:
    links = name_section.find_all("a")

    print(links)
    print("\n")

    for name in links:
        if "title" in name.attrs:
            print(name.get("title"))
else:
    print("No such section")
