import streamlit as st
from scrape import (
    scrape_website,
    split_dom_content,
    clean_body_content,
    extract_body_content,
)

st.title("Job Web Scraper")
url = st.text_input("Enter a website URL: ")

# url = "https://en.wikipedia.org/wiki/List_of_Greek_mathematicians"