from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os
import re
import json


class ResumeAnalyzer():
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("GOOGLE_API_KEY")
        llm = GoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=self.api_key)

        prompt_template = PromptTemplate(
            input_variables=["resume_text", "job_description", "required_skills"],
            template=(
                "You are an HR assistant. Evaluate this resume based on the job description.and the required skills."
                "Score the resume on relevance, experience, skills match, and formatting."
                "the output should only be in json format with maximum score as 10. don't give any other explanation.Do not include json word at beggining"
                "Resume: {resume_text}"
                "job description: {job_description}"
                "skills {required_skills}"
            )
        )

        self.chain = LLMChain(llm=llm, prompt=prompt_template)
       
    
    def analyze(self, resume_text, job_description, required_skills) -> dict:
        score = self.chain.run(resume_text=resume_text, job_description=job_description, required_skills=required_skills)
        json_str = re.search(r'\{.*\}', score.replace('\n', ''))
        json_str = json.loads(json_str.group())
        return json_str


# jd = '''We are looking for a senior Software Engineer with experience in Python, Django, and React.js.
# The ideal candidate should have at least 50 years of experience in software development, 
# familiarity with CI/CD pipelines, and a strong understanding of web technologies.'''
# skills = "python, django, react"
# score = chain.run(resume_text=documents[0].page_content, job_description=jd, required_skills=skills)
# json_str = re.search(r'\{.*\}', score.replace('\n', ''))
# json_str = json.loads(json_str.group())
# print(json_str)