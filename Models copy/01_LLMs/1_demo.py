from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Step1 - create object of the llm model
llm = OpenAI(model="gpt-3.5-turbo-instruct")

# Step2 - use the invoke function and get the result from the model
result = llm.invoke("What is the capital of India?")

print(result)
