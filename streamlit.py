import streamlit as st


# --- PAGE SETUP ---
home_page = st.Page(
    "Views/home_page.py",
    title="Home PAGE",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    "Views/buzz_finder.py",
    title="Buzz Topic Finder",
    icon=":material/bar_chart:",
)
contact_page = st.Page(
    "Views/contact.py",
    title="Contact",
    icon=":material/smart_toy:",
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [home_page],
        "Projects": [project_1_page],
        "Contact":[contact_page],
    }
)


# --- SHARED ON ALL PAGES ---
st.logo("Assets/logo.png")
st.sidebar.markdown("Made with ❤️ by [ACHRAF]")


# --- RUN NAVIGATION ---
pg.run()