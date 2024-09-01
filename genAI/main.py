import streamlit as st

from app import chatbotApp
from job_des_ui import jobDescriptionApp
from resume_analyzer_ui import resumeAnlayzerApp
# from resume_analayzer.resume_analyzer import ResumeAnalyzer
# from job_description.job_description_ai import jobDescriptionAI

# Set the page configuration
st.set_page_config(page_title="Smart Recruitment App", page_icon=":rocket:", layout="centered")

# Title of the main page
st.title("Welcome to the Smart Recruitment App")

# Sidebar or Main Page Navigation
st.sidebar.title("Navigation")
option = st.sidebar.radio("Go to", ("Job Description", "Resume Analyzer", "Chatbot"))

# Conditional rendering based on user selection
if option == "Job Description":
    jobDescriptionApp()
elif option == "Resume Analyzer":
    resumeAnlayzerApp() # Call the function from resume_analyzer_app
elif option == "Chatbot":
    chatbotApp()  # Call the function from chatbot_app
