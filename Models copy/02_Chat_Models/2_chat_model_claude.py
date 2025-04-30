from langchain_anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

model = Anthropic(model="claude-3.5-sonnet-20241022")

result = model.invoke("What is the capital of India?")
print(result.content)
