from langchain.llms import google_palm
from langchain.chains import llm as llm_chain
from langchain.prompts import PromptTemplate

# Initialize Google Palm LLM
llm = google_palm(temperature=0)

# Define a prompt template that explicitly asks for JSON output
template = """
You are a helpful AI assistant. Please provide the following information in JSON format:

{query}

Remember to only respond with a valid JSON object.
"""

prompt = PromptTemplate(
    input_variables=["query"],
    template=template,
)

# Create an LLM chain
chain = llm_chain(llm=llm, prompt=prompt)

# Example query
query = "What are the capital cities of France, Germany, and Italy?"

# Run the chain and print the output
response = chain.run(query)
print(response)