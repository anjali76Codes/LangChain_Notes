from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

def process_url(url):
    try:
        loader = WebBaseLoader(url)
        docs = loader.load()
    except Exception as e:
        return None, f"Failed to load URL: {e}"

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    try:
        # ✅ Correct embedding model
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vectorstore = FAISS.from_documents(chunks, embeddings)

        retriever = vectorstore.as_retriever()

        # ✅ Updated LLM model
        llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-pro", temperature=0.3)

        qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=False)
    except Exception as e:
        return None, f"Error during processing: {e}"

    return qa_chain, None
