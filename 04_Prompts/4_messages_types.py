from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Prepare the conversation messages
messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about LangChain"),
]

# Invoke the model with the messages
result = model.invoke(messages)

# Add the AI's response to the conversation
messages.append(AIMessage(content=result.content))

# Print the conversation
print(messages)
