import requests
import pdfplumber
import re

# URL of the PDF
pdf_url = ""


# Function to extract and print all text from a PDF URL
def extract_and_print_all_text(pdf_url):
    # Download the PDF file from the URL
    response = requests.get(pdf_url)
    with open("temp.pdf", "wb") as pdf_file:
        pdf_file.write(response.content)

    with pdfplumber.open("temp.pdf") as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            print(page_text)

# Call the function to extract and print all text
extract_and_print_all_text(pdf_url)

