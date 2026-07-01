# main.py
import streamlit as st

# Define individual pages
home_page = st.Page("Eda.py", title="Data & AI Job Market")
analytics_page = st.Page("app.py", title="AI Career Advisor")

# Create the navigation menu
pg = st.navigation([home_page, analytics_page])

# Run the selected page
pg.run()
