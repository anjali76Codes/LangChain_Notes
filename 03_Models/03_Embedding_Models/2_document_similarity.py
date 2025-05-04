from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)

documents = [
    "Yash Chavan is the best person in the college",
    "Anjali Gupta is the second best person in the college",
    "Vivek Bargude is the topper of our college",
    "Jayvin Parmar is a good student but does not come to the college",
]

query = "tell me about Anjali Gupta"

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)

index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

print(query)
print(documents[index])
print("Similarity Score is : ", score)

"""
1. `enumerate(scores)`: Pairs each score with its index.  
2. `list(enumerate(scores))`: Converts the pairs into a list.  
3. `sorted(..., key=lambda x: x[1])`: Sorts the list by score values.  
4. `[-1]`: Picks the last item in the sorted list (highest score).  
5. `index, score = ...`: Extracts the index and score of the highest value.  

This finds the highest score and its index.
"""
