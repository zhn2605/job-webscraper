import streamlit as st
from scrape import (
    scrape_website,
    split_dom_content,
    clean_body_content,
    extract_body_content,
)

from parse import parse_with_ollama

st.title("Job Web Scraper")
url = st.text_input("Enter a website URL: ")

# url = "https://en.wikipedia.org/wiki/List_of_Greek_mathematicians"

if st.button("Scrape Site"):
    st.write("Scraping the website...")
    result = scrape_website(url)
    
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    # Expanding to view more content
    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height = 300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("What do you wish to parse?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")

            # Grab chunks to pass into llm
            dom_chunks = split_dom_content(st.session_state.dom_content)

            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)
