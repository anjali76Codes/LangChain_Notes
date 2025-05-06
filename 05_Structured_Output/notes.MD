## **Unstructured Output**

- When we give a text prompt to a Large Language Model (LLM), it typically returns a response in plain text.
- This plain text is considered **unstructured output**, meaning it lacks a predefined format or schema.
- Parsing unstructured text for downstream tasks often requires additional processing or pattern matching.

---

## **Structured Output**

- In structured output, LLMs return data in a **well-defined format**, such as JSON.
- This makes the output easier to **parse, store, and integrate** into applications or systems.

---

## **Use Cases for Structured Output**

1. **Data Extraction**

   - Example: Extracting information from resumes or documents and storing it in a database.

2. **API Development**

   - Example: Summarizing Amazon product reviews by extracting pros, cons, and sentiment, then formatting it into a JSON schema.

3. **Autonomous Agents**

   - Agents often require structured data to make decisions or perform tasks accurately.

---

## **Ways to Get Structured Output from LLMs**

- **LLMs may or may not natively support structured output.**
- **LangChain** provides tools to achieve structured outputs from both types of LLMs:

### 1. **LLMs That Can Generate Structured Output Directly**

- Use LangChain's `with_structured_output()` function.
- Example output formats: JSON, key-value dictionaries.

### 2. **LLMs That Cannot Generate Structured Output Directly**

- Use **Output Parsers** (classes in LangChain) to parse and structure the output after it's generated.

---

## **Techniques for Structuring Output**

### 1. **Type Dict (Python Typing)**

- Define a dictionary with specific keys and value types.
- Used for **type hints** and documentation, not runtime validation.
- Can include annotations like `Optional`, `Literal` for clarity.

### 2. **Pydantic**

- A Python library for data **validation** and **parsing**.
- Ensures data is correctly typed and structured.
- Key Features:

  - **Optional Fields** using `Optional[]`
  - **Type Coercion**: Automatically converts strings to integers, etc.
  - **Built-in Validators** (e.g., for email formats)
  - **`Field()` Function** for setting:

    - Default values
    - Constraints
    - Descriptions
    - Regex validation

  - Objects can be easily converted to dictionaries or JSON.

### 3. **JSON Schema**

- A **language-agnostic** format for describing the structure of JSON data.
- Useful in multi-language projects or API definitions.

---

## **LangChain Notes**

- The `with_structured_output()` function has a `method` parameter:

  - `json` — for LLMs like **Gemini** and **Claude** that support direct JSON mode.
  - `function_calling` — when using agents or tools that require calling functions based on output.
