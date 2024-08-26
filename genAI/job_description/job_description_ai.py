from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from datetime import datetime, timedelta
import json
import os

load_dotenv()
api_key = os.getenv("AISTUDIO_API_KEY")
model = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)

today_date = datetime.now()
deadline_date = today_date + timedelta(days=7)
formatted_deadline = deadline_date.strftime("%d/%m/%Y")

def generate_job_description(msg):
    messages = [
        SystemMessage(content=f"Generate a job description for the following in JSON format only. Job Title, Job Description,Department, Job Location, Employment Type,Salary Range (starting with 'RS'), Application Deadline (use {formatted_deadline} in DD/MM/YYYY format), Required Qualifications, Preferred Qualifications, Responsibilities. Do not include json word at beggining."),
        HumanMessage(content="senior software devloper role for backend devloper in django 5 plus years experience salary of 50k")
    ]

    result = model.invoke(messages)
    return(result)