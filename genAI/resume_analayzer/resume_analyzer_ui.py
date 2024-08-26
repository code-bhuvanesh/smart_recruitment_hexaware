import streamlit as st
from langchain.document_loaders import PyPDFLoader
import tempfile
import os
from resume_analyzer import ResumeAnalyzer
# Title of the app
st.title("PDF File Uploader")

# File uploader for PDFs
resume_pdf = st.file_uploader("Choose a PDF file", type="pdf")
job_description = st.text_area("Job Description")
skills_required = st.text_area("Skills Required")

# Check if a file has been uploaded
if resume_pdf is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(resume_pdf.read())
        temp_file_path = tmp_file.name
    # Display the file name
    st.write(f"Uploaded file: {resume_pdf.name}")
    
    # Read the PDF file
    pages = PyPDFLoader(temp_file_path).load()

    analyzing = st.empty()
    analyzing.write("Anaylizing resume....")

    resumeAnalyzer = ResumeAnalyzer()
    result = resumeAnalyzer.analyze(pages[0].page_content, job_description, skills_required)

    analyzing.write("Complete")

    st.write(result)

    # Clean up the temporary file if needed
    os.remove(temp_file_path)

else:
    st.write("Please upload a PDF file to analyze.")
