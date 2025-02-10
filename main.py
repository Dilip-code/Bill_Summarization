import streamlit as st
from utils import get_pdf_links, pdf_to_images, extract_html_from_images, html_to_json, summarize_text

st.title("Bill Text Summarization")

# Step 1: Input URL
url = st.text_input("Enter the URL of the webpage containing PDFs:")
if st.button("Find PDF Links"):
    pdf_links = get_pdf_links(url)
    st.write("Found PDF Links:")
    for link in pdf_links:
        st.write(link)

# Step 2: Upload PDF and Extract Text
uploaded_pdf = st.file_uploader("Upload a PDF file:", type=["pdf"])
if uploaded_pdf:
    st.write("Processing PDF...")
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_pdf.read())

    # Convert PDF to images
    images = pdf_to_images("temp.pdf")
    st.write(f"Extracted {len(images)} pages as images.")

    # Extract HTML and Convert to JSON
    html_content = extract_html_from_images(images)
    json_data = html_to_json(html_content)

    # Display JSON Data
    st.subheader("Extracted JSON Data")
    st.json(json_data)

    # Summarize JSON
    if st.button("Summarize"):
        st.write("Generating Summary...")
        summary = summarize_text(json_data)
        st.subheader("Summary")
        st.write(summary)
