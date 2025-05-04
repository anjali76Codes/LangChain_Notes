import streamlit as st
from utils import process_url

st.set_page_config(page_title="Equity News QA", layout="centered")
st.title("📰 Equity News Q&A Tool")

# Sidebar
st.sidebar.header("Instructions")
st.sidebar.write("""
1. Paste a news article URL about a company or market.
2. Ask any question about the article.
3. The AI will extract and answer using that content.
""")

# User inputs
url = st.text_input("Enter the URL of the news article")

qa_chain = None
error_message = ""

if url:
    with st.spinner("Processing the article..."):
        qa_chain, error_message = process_url(url)
    if error_message:
        st.error(error_message)
    else:
        st.success("Article processed! Ask your question below.")

# Question input
if qa_chain:
    question = st.text_input("Ask a question about the article")

    if question:
        with st.spinner("Thinking..."):
            answer = qa_chain.run(question)
        st.markdown("**Answer:**")
        st.write(answer)
