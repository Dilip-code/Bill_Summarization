# import os
# from dotenv import load_dotenv
# import streamlit as st
# from together import Together

# # Load API key from .env file
# load_dotenv()
# together_api_key = os.getenv("TOGETHER_AI_API_KEY")

# # Initialize Together AI client
# client = Together(api_key=together_api_key)

# # Function to query Together AI with the Meta Llama model
# def query_together_ai(prompt, model="meta-llama/Llama-3.3-70B-Instruct-Turbo", max_tokens=None, temperature=0.7, top_p=0.7, top_k=50, repetition_penalty=1.0):
#     try:
#         # Create a chat completion request
#         response = client.chat.completions.create(
#             model=model,
#             messages=[
#                 {"role": "user", "content": prompt}
#             ],
#             max_tokens=max_tokens,
#             temperature=temperature,
#             top_p=top_p,
#             top_k=top_k,
#             repetition_penalty=repetition_penalty,
#             stop=["<|eot_id|>", "<|eom_id|>"],
#             stream=True
#         )
#         # Collect the streaming response
#         result = ""
#         for token in response:
#             if hasattr(token, 'choices'):
#                 result += token.choices[0].delta.content
#         return result
#     except Exception as e:
#         st.error(f"Error querying Together AI: {e}")
#         return None

# # Function to generate all summaries using Together AI
# def generate_summaries_with_together_ai(combined_text, num_pages):
#     # Define paragraph limits
#     extractive_paragraph_limit = 4 if num_pages >= 4 else num_pages
#     abstractive_paragraph_limit = 2

#     # Define prompts
#     extractive_prompt = f"Generate an extractive summary of the following text with {extractive_paragraph_limit} paragraphs:\n\n{combined_text}"
#     abstractive_prompt = f"Generate an abstractive summary of the following text in {abstractive_paragraph_limit} paragraphs:\n\n{combined_text}"
#     highlights_prompt = f"Generate highlights and analysis of the following text. Provide a maximum of 15-20 bullet points divided under 4 broad headings:\n\n{combined_text}"

#     # Query Together AI
#     extractive_summary = query_together_ai(extractive_prompt)
#     abstractive_summary = query_together_ai(abstractive_prompt)
#     highlights_summary = query_together_ai(highlights_prompt)

#     return extractive_summary, abstractive_summary, highlights_summary

# # Streamlit App
# st.title("Summarization with Together AI")

# uploaded_text = st.text_area("Enter your text here for summarization:")

# if uploaded_text:
#     # For this example, we'll assume 4 pages (you can modify this based on actual PDF processing)
#     num_pages = 4
#     st.write("Generating summaries, please wait...")

#     # Generate summaries
#     extractive_summary, abstractive_summary, highlights_summary = generate_summaries_with_together_ai(uploaded_text, num_pages)

#     # Display results
#     st.subheader("Extractive Summary")
#     st.write(extractive_summary)

#     st.subheader("Abstractive Summary")
#     st.write(abstractive_summary)

#     st.subheader("Highlights and Analysis")
#     st.write(highlights_summary)

# import os
# import requests
# from pdf2image import convert_from_path
# import pytesseract
# from bs4 import BeautifulSoup
# import streamlit as st
# from together import Together
# from dotenv import load_dotenv

# # Load API key from .env
# load_dotenv()
# together_api_key = os.getenv("TOGETHER_AI_API_KEY")

# # Initialize Together AI client
# client = Together(api_key=together_api_key)

# # Ensure Tesseract OCR path is configured
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update path for your system

# # Helper Functions
# def ensure_folder_exists(folder_name):
#     if not os.path.exists(folder_name):
#         os.makedirs(folder_name)

# def convert_pdf_to_images(pdf_path, output_folder):
#     try:
#         # Update the Poppler path for your system
#         poppler_path = r"C:\Release-24.08.0-0\poppler-24.08.0\Library\bin"  # For Windows
#         pages = convert_from_path(pdf_path, poppler_path=poppler_path)
#         image_paths = []
#         for i, page in enumerate(pages):
#             image_path = os.path.join(output_folder, f"{os.path.basename(pdf_path)}_page_{i + 1}.jpg")
#             page.save(image_path, "JPEG")
#             image_paths.append(image_path)
#         return image_paths, len(pages)  # Return image paths and the number of pages
#     except Exception as e:
#         st.error(f"Failed to convert PDF to images: {e}")
#         return [], 0

# def extract_text_from_image(image_path):
#     try:
#         text = pytesseract.image_to_string(image_path, config='--psm 6')  # Page segmentation mode
#         return text
#     except Exception as e:
#         st.error(f"Failed to extract text from image: {e}")
#         return ""

# def query_together_ai(prompt, model="meta-llama/Llama-3.3-70B-Instruct-Turbo", max_tokens=None, temperature=0.7, top_p=0.7, top_k=50, repetition_penalty=1.0):
#     try:
#         response = client.chat.completions.create(
#             model=model,
#             messages=[
#                 {"role": "user", "content": prompt}
#             ],
#             max_tokens=max_tokens,
#             temperature=temperature,
#             top_p=top_p,
#             top_k=top_k,
#             repetition_penalty=repetition_penalty,
#             stop=["<|eot_id|>", "<|eom_id|>"],
#             stream=True
#         )
#         # Collect streaming response
#         result = ""
#         for token in response:
#             if hasattr(token, 'choices'):
#                 result += token.choices[0].delta.content
#         return result
#     except Exception as e:
#         st.error(f"Error querying Together AI: {e}")
#         return None

# def generate_summaries_with_together_ai(combined_text, num_pages):
#     extractive_paragraph_limit = 4 if num_pages >= 4 else num_pages
#     abstractive_paragraph_limit = 2

#     extractive_prompt = f"Generate an extractive summary of the following text with {extractive_paragraph_limit} paragraphs:\n\n{combined_text}"
#     abstractive_prompt = f"Generate an abstractive summary of the following text in {abstractive_paragraph_limit} paragraphs:\n\n{combined_text}"
#     highlights_prompt = f"Generate highlights and analysis of the following text. Provide a maximum of 15-20 bullet points divided under 4 broad headings:\n\n{combined_text}"

#     extractive_summary = query_together_ai(extractive_prompt)
#     abstractive_summary = query_together_ai(abstractive_prompt)
#     highlights_summary = query_together_ai(highlights_prompt)

#     return extractive_summary, abstractive_summary, highlights_summary

# # Streamlit Application
# st.title("Document Summarization with Together AI")

# prompt = (
#     "You are an assistant for document summarization. Extract relevant information from text "
#     "and generate summaries in extractive, abstractive, and highlights format."
# )

# option = st.radio("Choose an option:", ("Upload a PDF", "Input a website link"))

# if option == "Upload a PDF":
#     uploaded_pdf = st.file_uploader("Upload a PDF file", type=["pdf"])
#     if uploaded_pdf is not None:
#         uploads_folder = "uploads"
#         ensure_folder_exists(uploads_folder)
#         images_folder = "images"
#         ensure_folder_exists(images_folder)

#         file_path = os.path.join(uploads_folder, uploaded_pdf.name)
#         with open(file_path, "wb") as f:
#             f.write(uploaded_pdf.read())

#         # Convert PDF to images and extract text
#         image_paths, num_pages = convert_pdf_to_images(file_path, images_folder)
#         if image_paths:
#             all_text = ""
#             for image_path in image_paths:
#                 extracted_text = extract_text_from_image(image_path)
#                 all_text += extracted_text

#             # Generate summaries
#             if all_text:
#                 st.write("Generating summaries, please wait...")
#                 extractive_summary, abstractive_summary, highlights_summary = generate_summaries_with_together_ai(all_text, num_pages)

#                 # Display summaries
#                 st.subheader("Extractive Summary")
#                 st.write(extractive_summary)

#                 st.subheader("Abstractive Summary")
#                 st.write(abstractive_summary)

#                 st.subheader("Highlights and Analysis")
#                 st.write(highlights_summary)

# elif option == "Input a website link":
#     website_url = st.text_input("Enter the website URL:")
#     if website_url:
#         response = requests.get(website_url)
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.text, "html.parser")
#             # Extract text content
#             all_text = soup.get_text(separator="\n")
#             num_pages = 4  # Assume 4 pages for URL-based content

#             # Generate summaries
#             if all_text:
#                 st.write("Generating summaries, please wait...")
#                 extractive_summary, abstractive_summary, highlights_summary = generate_summaries_with_together_ai(all_text, num_pages)

#                 # Display summaries
#                 st.subheader("Extractive Summary")
#                 st.write(extractive_summary)

#                 st.subheader("Abstractive Summary")
#                 st.write(abstractive_summary)

#                 st.subheader("Highlights and Analysis")
#                 st.write(highlights_summary)
#         else:
#             st.error("Failed to retrieve content from the URL. Please check the link.")

import os
import requests
import pandas as pd
from pdf2image import convert_from_path
import pytesseract
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from together import Together
import streamlit as st

load_dotenv()
together_api_key = os.getenv("TOGETHER_AI_API_KEY")
client = Together(api_key=together_api_key)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  

def ensure_folder_exists(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def download_pdf_from_url(url, output_folder):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        content_type = response.headers.get("Content-Type")
        
        if "application/pdf" not in content_type:
            return None
        
        pdf_name = url.split("/")[-1] or "downloaded_pdf.pdf"
        pdf_path = os.path.join(output_folder, pdf_name)
        with open(pdf_path, "wb") as pdf_file:
            for chunk in response.iter_content(chunk_size=8192):
                pdf_file.write(chunk)
        
        return pdf_path
    except Exception as e:
        return None

def convert_pdf_to_images(pdf_path, output_folder):
    try:
        poppler_path = r"C:\\Release-24.08.0-0\\poppler-24.08.0\\Library\\bin"  
        pages = convert_from_path(pdf_path, poppler_path=poppler_path)
        image_paths = []
        for i, page in enumerate(pages):
            image_path = os.path.join(output_folder, f"{os.path.basename(pdf_path)}_page_{i + 1}.jpg")
            page.save(image_path, "JPEG")
            image_paths.append(image_path)
        return image_paths, len(pages)
    except Exception as e:
        return [], 0

def extract_text_from_image(image_path):
    try:
        return pytesseract.image_to_string(image_path, config='--psm 6')
    except Exception as e:
        return ""

def extract_text_from_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.get_text(separator=" ")
    except Exception as e:
        return ""

def query_together_ai(prompt):
    try:
        response = client.chat.completions.create(
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
            messages=[{"role": "user", "content": prompt}],
            stream=True
        )
        result = ""
        for token in response:
            if hasattr(token, 'choices'):
                result += token.choices[0].delta.content
        return result
    except Exception as e:
        return None

def generate_summaries_with_together_ai(combined_text, num_pages):
    extractive_prompt = f"Generate an extractive summary with {min(num_pages, 4)} paragraphs:\n\n{combined_text}"
    abstractive_prompt = f"Generate an abstractive summary in 2 paragraphs:\n\n{combined_text}"
    highlights_prompt = f"Generate highlights in 15-20 bullet points under 4 headings:\n\n{combined_text}"
    
    return (
        query_together_ai(extractive_prompt),
        query_together_ai(abstractive_prompt),
        query_together_ai(highlights_prompt),
    )

st.title("PDF and Webpage Summarization with Together AI")

option = st.radio("Choose an option:", ("Upload a PDF", "Input a website link", "Upload an Excel file"))

if option == "Upload a PDF":
    uploaded_pdf = st.file_uploader("Upload a PDF file", type=["pdf"])
    if uploaded_pdf:
        uploads_folder = "uploads"
        ensure_folder_exists(uploads_folder)
        images_folder = "images"
        ensure_folder_exists(images_folder)
        
        pdf_path = os.path.join(uploads_folder, uploaded_pdf.name)
        with open(pdf_path, "wb") as f:
            f.write(uploaded_pdf.read())
        
        image_paths, num_pages = convert_pdf_to_images(pdf_path, images_folder)
        if image_paths:
            all_text = "".join([extract_text_from_image(img) for img in image_paths])
            summaries = generate_summaries_with_together_ai(all_text, num_pages)
            st.subheader("Extractive Summary")
            st.write(summaries[0])
            st.subheader("Abstractive Summary")
            st.write(summaries[1])
            st.subheader("Highlights and Analysis")
            st.write(summaries[2])

elif option == "Input a website link":
    url = st.text_input("Enter the URL:")
    if url:
        if url.lower().endswith(".pdf"):  # PDF Link
            downloads_folder = "downloads"
            ensure_folder_exists(downloads_folder)
            images_folder = "images"
            ensure_folder_exists(images_folder)

            pdf_path = download_pdf_from_url(url, downloads_folder)
            if pdf_path:
                image_paths, num_pages = convert_pdf_to_images(pdf_path, images_folder)
                if image_paths:
                    all_text = "".join([extract_text_from_image(img) for img in image_paths])
                    summaries = generate_summaries_with_together_ai(all_text, num_pages)
                    st.subheader("Extractive Summary")
                    st.write(summaries[0])
                    st.subheader("Abstractive Summary")
                    st.write(summaries[1])
                    st.subheader("Highlights and Analysis")
                    st.write(summaries[2])
                else:
                    st.error("Could not extract text from the PDF.")
            else:
                st.error("Failed to download the PDF.")
        else:  # Webpage Link
            webpage_text = extract_text_from_webpage(url)
            if webpage_text.strip():
                summaries = generate_summaries_with_together_ai(webpage_text, 3)
                st.subheader("Extractive Summary")
                st.write(summaries[0])
                st.subheader("Abstractive Summary")
                st.write(summaries[1])
                st.subheader("Highlights and Analysis")
                st.write(summaries[2])
            else:
                st.error("Failed to extract text from the webpage.")

elif option == "Upload an Excel file":
    uploaded_excel = st.file_uploader("Upload an Excel file", type=["xlsx"])
    if uploaded_excel:
        df = pd.read_excel(uploaded_excel)
        if "BillTextURL" in df.columns:
            for url in df["BillTextURL"].dropna():
                if url.lower().endswith(".pdf"):  # PDF URL
                    pdf_path = download_pdf_from_url(url, "downloads")
                    if pdf_path:
                        image_paths, num_pages = convert_pdf_to_images(pdf_path, "images")
                        if image_paths:
                            all_text = "".join([extract_text_from_image(img) for img in image_paths])
                            summaries = generate_summaries_with_together_ai(all_text, num_pages)
                            st.subheader(f"Summaries for {url}")
                            st.write("**Extractive Summary:**", summaries[0])
                            st.write("**Abstractive Summary:**", summaries[1])
                            st.write("**Highlights and Analysis:**", summaries[2])
                else:  # Webpage URL
                    webpage_text = extract_text_from_webpage(url)
                    if webpage_text:
                        summaries = generate_summaries_with_together_ai(webpage_text, 3)
                        st.subheader(f"Summaries for {url}")
                        st.write("**Extractive Summary:**", summaries[0])
                        st.write("**Abstractive Summary:**", summaries[1])
                        st.write("**Highlights and Analysis:**", summaries[2])
        else:
            st.error("The uploaded file does not contain a 'BillTextURL' column.")
