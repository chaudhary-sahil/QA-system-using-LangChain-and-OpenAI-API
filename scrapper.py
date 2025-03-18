import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    """Extracts and returns visible text from the given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract only meaningful text (paragraphs)
        text = ' '.join([p.get_text() for p in soup.find_all('p')])
        return text if text else "No readable content found."

    except requests.exceptions.RequestException as e:
        return f"Error fetching URL: {e}"
