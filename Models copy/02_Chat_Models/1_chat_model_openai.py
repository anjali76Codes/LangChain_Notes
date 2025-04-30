from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# normal call
model = ChatOpenAI(model="gpt-4")

# call with different parameters
# temperature is the creativity parameter
# max_completion_tokens is how many words response I want
model = ChatOpenAI(model="gpt-4", temperature=0.5, max_completion_tokens=10)

result = model.invoke("What is the capital of India")
print(result)  # gives us complete information
print(result.content)  # gives just the string answer that we want
