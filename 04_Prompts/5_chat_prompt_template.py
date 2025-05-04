from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

chat_template = ChatPromptTemplate(
    # changing the message functions as they do not work
    [
        # SystemMessage(content="You are a helpful {domain} expert"),
        ("system", "You are a helpful {domain} expert"),
        # HumanMessage(content="Explain in simple words what is {topic}"),
        ("human", "Explain in simple words what is {topic}"),
    ]
)

prompt = chat_template.invoke({"domain": "Cricket Expert", "topic": "Dusra"})
print(prompt)
