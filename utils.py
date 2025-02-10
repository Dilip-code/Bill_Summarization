import requests
from bs4 import BeautifulSoup
from pdf2image import convert_from_path
import pytesseract
from pytesseract import Output
import json

# 1. Scrape the website for PDF links
def get_pdf_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    pdf_links = []

    # Find links with 'Relevant link' span class
    for span in soup.find_all('span', class_='Relevant link'):
        link = span.find('a', href=True)
        if link and link['href'].endswith('.pdf'):
            pdf_links.append(link['href'])

    return pdf_links

# 2. Convert PDF to images
from pdf2image import convert_from_path

def pdf_to_images(pdf_path):
    images = convert_from_path(pdf_path)
    for i, img in enumerate(images):
        img.save(f"page_{i+1}.png", "PNG")  # Save each page as an image
    return images


# 3. Extract text and convert to hierarchical HTML
def extract_html_from_images(images):
    html_content = ""
    for img in images:
        text = pytesseract.image_to_string(img, lang='eng', config='--psm 6')
        lines = text.split('\n')
        for line in lines:
            if line.strip().startswith("SECTION"):
                html_content += f"<h1>{line.strip()}</h1>"
            else:
                html_content += f"<p>{line.strip()}</p>"
    return html_content

# 4. Convert HTML to JSON
def html_to_json(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    json_data = {}
    current_section = None

    for tag in soup.find_all():
        if tag.name == 'h1':
            current_section = tag.text.strip()
            json_data[current_section] = []
        elif tag.name == 'p' and current_section:
            json_data[current_section].append(tag.text.strip())

    return json.dumps(json_data, indent=4)


import openai

openai.api_key = "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"

def summarize_text(json_data):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Summarize the following data: {json_data}"}
        ]
    )
    return response['choices'][0]['message']['content']



