import requests
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd

st.title("Job Web Scraper")
url = st.text_input("Enter a website URL: ")

# url = "h ttps://en.wikipedia.org/wiki/List_of_Greek_mathematicians"

if st.button("Scrape Site"):
    st.write("Scraping the website...")

# Set up url, paege, soup

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

# List all names
all_col_divs = soup.findAll("div", class_="div-col")

# print(all_col_divs)

name_section = all_col_divs[0]

if name_section:
    links = name_section.find_all("a")

    # print(links)
    # print("\n")

    for name in links:
        if "title" in name.attrs:
            st.write(name.get("title"))
else:
    st.write("No such section.")