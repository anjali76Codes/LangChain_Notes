# Prompts

- input instructions or the queries given to a model to guide its output

# Types of prompts

- text based prompts
- multi-modal prompts (image, audio, video)

# Static prompt

- here you take the entire prompt from the user and then we send that to LLM
- but the user has too much control
- and also the prompt may not be proper so the output will not come as desired

# Dynamic prompt

- so we create a prompt template in advance
- and then add the user input parts in the required dynamic inputs

# Main reasons why we use PromptTemplate over f strings

- validation of the input variables
- reusing the prompt templates
- Overall works well with Langchain ecosystem

# Types of messages in Langchain

- this problem is identified, as when we store the messages, and send it in the prompt
  AI should also know which message who has sent
  or else there will be confusions and the responses will be not that proper

- so for that we need to know types of messages

1. System message - sent at the very start, eg: you are a medical doctor answer all the queries in simple manner
2. Human message - sent by the user
3. AI message

# Chat prompt template

- it is used when we are working with conversational messages, and also dynamic data
- we can ues Chat message template there and send dynamic inputs

# Message Placeholder

- it is a special placeholder used inside a chatprompttemplate
- to dynamically insert chat history or a list of messages at runtime
