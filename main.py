# main.py
import streamlit as st

# Define individual pages
home_page = st.Page("Eda.py", title="Data & AI Job Market", icon=":woman_technologist:")
analytics_page = st.Page("analytics.py", title="Analytics", icon=":brain:")

# Create the navigation menu
pg = st.navigation([home_page, analytics_page])

# Run the selected page
pg.run()
