import streamlit as st
import requests
from bs4 import BeautifulSoup
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from io import BytesIO
from PyPDF2 import PdfReader

def fetch_url_content(url):
    """Fetch content from the URL."""
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        content_type = response.headers.get("Content-Type", "")
        return response.content, content_type
    except requests.exceptions.RequestException as e:
        return None, f"Error fetching URL: {e}"

def extract_text_from_html(html_content):
    """Extract main text from HTML using BeautifulSoup."""
    soup = BeautifulSoup(html_content, "html.parser")
    # Look for tags likely containing the main content
    for tag in ["article", "main", "div"]:
        main_content = soup.find(tag)
        if main_content:
            return main_content.get_text(separator=" ", strip=True)
    # Fallback: Extract all text if no main tags found
    return soup.get_text(separator=" ", strip=True)

def extract_text_from_pdf(pdf_content):
    """Extract text from PDF content."""
    try:
        pdf_reader = PdfReader(BytesIO(pdf_content))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text.strip()
    except Exception as e:
        return f"Error extracting text from PDF: {e}"

def summarize_text(text, num_sentences=5):
    """Summarize text using sumy LSA summarizer."""
    try:
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, num_sentences)
        return " ".join(str(sentence) for sentence in summary)
    except Exception as e:
        return f"Error summarizing text: {e}"

# Streamlit UI
st.title("Webpage and PDF Summarizer")

# Input URL
url = st.text_input("Enter a URL:")

if url:
    with st.spinner("Fetching content..."):
        content, content_type = fetch_url_content(url)
    
    if content and "Error" not in content_type:
        if "pdf" in content_type.lower():  
            with st.spinner("Extracting text from PDF..."):
                extracted_text = extract_text_from_pdf(content)
        else:  
            with st.spinner("Extracting text from HTML..."):
                extracted_text = extract_text_from_html(content.decode("utf-8", errors="ignore"))
        
        if extracted_text:
            with st.spinner("Summarizing..."):
                summary = summarize_text(extracted_text, num_sentences=5)
            
            st.subheader("Summary:")
            st.write(summary)
        else:
            st.error("Failed to extract text from the content.")
    else:
        st.error(content_type or "Failed to fetch content.")
