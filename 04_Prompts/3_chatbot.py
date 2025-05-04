from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# implementing the messages logic here
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

chat_history = [SystemMessage(content="You are a helpful AI assistant")]

while True:
    user_input = input("Me: ")

    if user_input == "exit":
        break

    # send the entire message history to the prompt
    # chat_history.append(user_input)

    chat_history.append(HumanMessage(content=user_input))

    # result = model.invoke(user_input)
    result = model.invoke(chat_history)

    print("AI: ", result.content)
    # chat_history.append(result.content)

    chat_history.append(AIMessage(content=result.content))


print(chat_history)
