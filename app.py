from fastapi import FastAPI
from pydantic import BaseModel
from scrapper import extract_text_from_url
from qa_model import answer_question

app = FastAPI()
database = {}  # In-memory storage for ingested content

class AskRequest(BaseModel):
    url: str
    question: str

@app.post("/ingest/")
def ingest(url: str):
    try:    
        """Fetches content from a URL and stores it in memory."""
        text = extract_text_from_url(url)
        if not text:  # Handle empty responses
            return {"error": "Failed to extract content from the URL"}
        
        database[url] = text
        print(f"Ingested: {url}")  # Debugging log
        return {"message": "URL ingested successfully", "text": text[:200] + "..."}  # Show preview
    except Exception as e:
        print("Error in /ingest/:", str(e))
        return {"error": "Internal Server Error"}

@app.post("/ask/")
def ask(request: AskRequest):
    """Answers a question using the stored content of the given URL."""
    try:
        url = request.url
        question = request.question

        if url not in database:
            return {"error": "URL not ingested"}
        
        print(f"Answering question: {question} for URL: {url}")  # Debugging log

        # Debug: Print some extracted text before calling the QA model
        print(f"Extracted Text Preview: {database[url][:500]}")
        
        answer = answer_question(database[url], question)

        if not answer:  # Handle empty answers
            answer = "I'm sorry, I couldn't find an answer."

        return {"answer": answer}
    except Exception as e:
        print("Error in /ask/:", str(e))
        return {"error": "Internal Server Error"}





'''from fastapi import FastAPI
from scrapper import extract_text_from_url
from qa_model import answer_question

app = FastAPI()
database = {}  # In-memory storage for ingested content

@app.post("/ingest/")
def ingest(url: str):
    """Fetches content from a URL and stores it in memory."""
    text = extract_text_from_url(url)
    database[url] = text
    return {"message": "URL ingested successfully", "text": text[:200] + "..."}  # Show preview

@app.get("/ask/")
def ask(url: str, question: str):
    """Answers a question using the stored content of the given URL."""
    if url not in database:
        return {"error": "URL not ingested"}
    
    answer = answer_question(database[url], question)
    return {"answer": answer}'''
