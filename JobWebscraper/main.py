import requests
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd

from scrape import scrape_website

st.title("Job Web Scraper")
url = st.text_input("Enter a website URL: ")

# url = "https://en.wikipedia.org/wiki/List_of_Greek_mathematicians"

if st.button("Scrape Site"):
    st.write("Scraping the website...")
    result = scrape_website(url)
    print(result)