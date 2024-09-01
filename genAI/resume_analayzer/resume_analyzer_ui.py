import streamlit as st
from langchain.document_loaders import PyPDFLoader
import tempfile
import os
from resume_analyzer import ResumeAnalyzer
# Title of the app
st.title("Resume Analyzer")

# File uploader for PDFs
resume_pdf = st.file_uploader("Choose a PDF file", type="pdf")
skills_required = st.text_input("Skills Required")
job_description = st.text_area("Job Description")

if st.button("analyze"):

    # Check if a file has been uploaded
    if resume_pdf is not None and job_description != "" and skills_required != "":
        analyzing = st.empty()
        analyzing.write("Anaylizing resume....")
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(resume_pdf.read())
            temp_file_path = tmp_file.name

        
        # Read the PDF file
        pages = PyPDFLoader(temp_file_path).load()

        

        resumeAnalyzer = ResumeAnalyzer()
        result = resumeAnalyzer.analyze(pages[0].page_content, job_description, skills_required)

        analyzing.empty()
        total_score = 0
        for k in result.keys():
            st.write(f"{k} : {result[k]}/10")
            total_score += result[k]
        
        st.write(f"total score : {total_score/4}/10")

        # Clean up the temporary file if needed
        os.remove(temp_file_path)

    else:
        st.write("Please upload a PDF file to analyze.")

test = '''
We are looking for a senior Software Engineer with experience in Python, Django, and React.js.
The ideal candidate should have at least 50 years of experience in software development, 
familiarity with CI/CD pipelines, and a strong understanding of web technologies.

python, django, react
'''