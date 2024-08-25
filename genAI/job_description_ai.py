from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

api_key = os.getenv("AISTUDIO_API_KEY")

model = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)

messages = [
    SystemMessage(content="give a perfect job description for the following in JSON form"),
    HumanMessage(content="senior software devloper role")
]

result = model.invoke(messages)
print(result)