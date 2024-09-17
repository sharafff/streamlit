import streamlit as st 



st.title("Scrap it ALL")

url = st.text_input("Enter a URL")

if st.button("Scraping website"):
    st.write("yeees")
    