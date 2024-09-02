import streamlit as st

from job_des_ui import jobDescriptionApp
from resume_analyzer_ui import resumeAnlayzerApp
from chatbot_ui import ChatBotApp
from streamlit_option_menu import option_menu   
# from resume_analayzer.resume_analyzer import ResumeAnalyzer
# from job_description.job_description_ai import jobDescriptionAI

st.set_page_config(page_title="Smart Recruitment App", page_icon=":rocket:", layout="centered")

st.title("Smart Recruitment App")


with st.sidebar:
    selected = option_menu(
        menu_title="",
        options=["Job Description", "Resume Analyzer","Chatbot"],
        icons=["bi bi-file-earmark-text-fill", "bi bi-bar-chart-line-fill","bi bi-chat-fill"],
        menu_icon="",
        default_index=0,
    )

if selected == "Job Description":
    jobDescriptionApp()

if selected == "Resume Analyzer":
    resumeAnlayzerApp()

if selected == "Chatbot":
    ChatBotApp()