# Unstructured Output

- when we give a text prompt to LLM then we get the response in the text
- and text is unstructured output

# Structured Output

- here the LLMs return output in a well defined data format, eg: JSON
- this makes the program output easier to parse

# Use cases

- Data Extraction - if we want to store the LLM response in the database so there you need a structured output
- API Building - Amazon product reviews, extract the key information and structure the pros, corns and sentiment and store it
- Agents

# Ways to get structured Output

- LLMs can or cannot generate structured output
- but using langchain we can get structured output from both of the LLM types
- Can generate structured output - function with_structured_output
- Cannot generate structured output - Output parsers (classes)

# With structured Output

1. Type Dict
   define dictionary in python where you specify what keys and values should exist
   it does not validate data at runtime (it just helps with type hints and tells us)
   Annotation - adding a line so that LLM understands what we have to extract (along with the keys)
   Optional
   Literal

2. Pydantic
   Data validation and data parsing library in python
   It ensures that the data that you work with is correct, structured and type safe
   Optional Fields
   Type coercing - if we pass a string instead of a integer then it will implicitely do the type conversion
   in build validation - eg: regarding the emails
   field function - default values, constraints, description, regex
   the pydantic object can also be converted to python dictionary or a json format

3. JSON Schema
   It is used when your entire project is not made in a single language

# Note

when we are using with_structured_output() function, it has a method parameter - we can set it to - json mode (gemini and cluade)
function calling (when using agent that calls tools)
