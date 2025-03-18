import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"  # Change if deployed

st.title("Web Content Q&A Tool")

# Ingest URL
url = st.text_input("Enter URL:")
if st.button("Ingest Content"):
    response = requests.post(
        f"{API_URL}/ingest/",
        params={"url": url})
    st.write(response.json())

# Ask a question
question = st.text_input("Ask a question about the content:")
if st.button("Get Answer"):
    response = requests.post(
        f"{API_URL}/ask/", 
        json={"url": url, 
        "question": question}
)

    print("API Response:", response.text)  # Debugging line
    st.write(response.json().get("answer", "No answer available"))
