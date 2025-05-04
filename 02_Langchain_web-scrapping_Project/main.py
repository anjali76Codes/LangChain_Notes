from langchain_openai import ChatOpenAI  # import 
from dotenv import load_dotenv

load_dotenv()


llm = ChatOpenAI(model="gpt-4o") # model define or add

# invoke 
result = llm.invoke("What is the sqaure root of the 49")


print(result)

