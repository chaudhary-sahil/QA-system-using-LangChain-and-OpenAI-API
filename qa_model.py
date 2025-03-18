from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.docstore.document import Document
import os
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API key securely
openai_api_key = os.getenv("OPENAI_API_KEY")

# Ensure the API key is set
if not openai_api_key:
    raise ValueError("Missing OpenAI API key. Set it in the .env file.")

print("API Key Loaded Successfully!")  # Confirmation message

# Initialize OpenAI LLM (Pass the API key explicitly)
# llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=openai_api_key)


# Initialize OpenAI Chat Model (Updated)
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=openai_api_key)

# Load QA chain
qa_chain = load_qa_chain(llm, chain_type="stuff")

def answer_question(text, question):
    """Answers a question based on the given text."""
    document = Document(page_content=text)
    time.sleep(2)
    return qa_chain.invoke({"input_documents": [document], "question": question})["output_text"]

# Example Usage (Optional - Can be removed in production)
if __name__ == "__main__":
    sample_text = "The capital of France is Paris."
    sample_question = "What is the capital of France?"
    print("Answer:", answer_question(sample_text, sample_question))
