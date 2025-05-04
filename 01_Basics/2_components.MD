# **Components of LangChain (6 Key Components)**

LangChain is a powerful framework designed to simplify the development of applications that utilize language models. Below are its six core components:

---

## 1. **Models**

LangChain provides a unified interface to interact with various AI models, allowing flexibility and modularity in application development.

- **Two main types of models:**
  - **Language Models (LLMs):** Handle tasks like text generation, summarization, and Q&A.
  - **Embedding Models:** Take text as input and return a vector, useful for tasks like semantic search and similarity comparison.

---

## 2. **Prompts**

Prompts are the inputs provided to an LLM, carefully designed to guide the model's behavior.

- **Dynamic Prompts:** Use placeholders so the prompt template can be reused with different inputs.
- **Role-Based Prompts:** Assign roles (e.g., "You are a helpful assistant") to guide tone or context.
- **Few-Shot Prompts:** Include examples of input-output pairs to help the model understand the desired pattern.

---

## 3. **Chains**

Chains allow you to build pipelines by linking multiple components or LLM calls together.

- **Sequential Chains:** Execute steps one after another.
- **Parallel Chains:** Run multiple steps at the same time, useful for generating different parts of a report from various sources.
- **Conditional Chains:** Direct the flow based on logic (e.g., if feedback is good, say “thank you”; if bad, trigger customer support email).

---

## 4. **Indexes**

Indexes connect your application to external knowledge sources, such as:

- PDFs
- Websites
- Databases

This allows your LLM to access and reason over additional context and content not originally part of the model.

---

## 5. **Memory**

LLM API calls are stateless by default. Memory components help retain context across interactions.

- **ConversationBufferMemory:** Stores the entire chat history with each new API call.
- **ConversationBufferWindowMemory:** Stores only the last N interactions (e.g., last 10).
- **Summarizer Memory:** Maintains a running summary of the conversation so far.
- **Custom Memory:** Allows specific preferences or user data to be pre-loaded (e.g., food preferences in a Zomato-like app).

---

## 6. **Agents**

Agents are advanced AI systems that combine the capabilities of LLMs with tools and reasoning.

- Unlike simple chatbots, agents can:
  - **Reason:** Use step-by-step logic (e.g., chain-of-thought reasoning).
  - **Access Tools:** Call APIs, databases, or perform actions beyond text generation.
- Think of agents as chatbots **with superpowers**—able to plan, reason, and interact with external systems.
