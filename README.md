# QA-system-using-LangChain-and-OpenAI-API
## Overview

This project is a Question-Answering (QA) system built using **LangChain** and **OpenAI API**. It allows users to ingest documents, extract relevant information, and answer queries efficiently.

## Features

- **Document Ingestion**: Load data from various sources, including URLs and local files.
- **Text Processing**: Extracts meaningful content from documents.
- **Question Answering**: Answers user queries based on ingested data.
- **FastAPI Integration**: Provides a REST API to interact with the QA system.
- **Security**: Implements API key authentication.

## Technologies Used
- Python
- FastAPI
- Streamlit
- LangChain
- OpenAI API

## Installation

Clone the repository:

```sh
git clone https://github.com/chaudhary-sahil/QA-system-using-LangChain-and-OpenAI-API.git
cd QA-system-using-LangChain-and-OpenAI-API
```

Create and activate a virtual environment:

```sh
python3 -m venv venv
source venv/bin/activate  
```

Install dependencies:

```sh
pip install -r requirements.txt
```

## Configuration

Set up environment variables in a `.env` file:

```sh
OPENAI_API_KEY=your_openai_api_key
```

## Running the Application

Start the FastAPI server:

```sh
uvicorn main:app --reload
```
The API will be available at: http://127.0.0.1:8000

Start the frontend server:

```sh
streamlit run frontend.py
```


## API Endpoints

1. **Ingest a Document:**
   **EndPoint** : Post /ingest/
   - **Query Param** : url=<document_url>
   - **Example:**
  ```sh
  curl -X POST "http://127.0.0.1:8000/ingest/?url=<document_url>
  ```
2. **Ask a Question:**
   **EndPoint**: Post /ask/
   - **Request Body:**
  ```sh
  {
      "question": "Your question goes here"
  }
  ```
  - **Example:**
  ```sh
  curl -X POST "http://127.0.0.1:8000/ask/" -H "Content-Type: application/json" -d '{"question": "your question here"}'
  ```

## Contributors

- Sahil (@chaudhary-sahil)

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
