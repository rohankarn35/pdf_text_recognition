# import requests
# import pdfplumber
# import re

# # URL of the PDF
# pdf_url = "https://firebasestorage.googleapis.com/v0/b/medsheet-51999.appspot.com/o/T42M3QqKvBPt9kDXfTUja5FJiYU2%2Freport_231025_123045.pdf?alt=media&token=1d943a2f-51a9-4b31-bfc0-cf6a573423af"

# # Define a function to check if the PDF appears to be a medical report
# def is_medical_report(page_text):
#     # You can define your criteria here for identifying medical reports.
#     # For example, check for keywords that are typically found in medical reports.
#     medical_keywords = []
    
#     for keyword in medical_keywords:
#         if keyword.lower() in page_text.lower():
#             return True

#     return False

# # Function to extract and print all text from a PDF URL if it's a medical report
# def extract_and_print_all_text(pdf_url):
#     # Download the PDF file from the URL
#     response = requests.get(pdf_url)
#     with open("temp.pdf", "wb") as pdf_file:
#         pdf_file.write(response.content)

#     with pdfplumber.open("temp.pdf") as pdf:
#         is_medical = False  # Flag to indicate if it's a medical report
#         for page in pdf.pages:
#             page_text = page.extract_text()
#             if is_medical_report(page_text):
#                 is_medical = True
#                 print(page_text)
        
#         if not is_medical:
#             print("This does not appear to be a medical report. Please upload a medical report.")

# # Call the function to extract and print all text only if it's a medical report
# extract_and_print_all_text(pdf_url)


# import requests
# import pdfplumber

# # URL of the PDF
# pdf_url = "https://pdfobject.com/pdf/sample.pdf"

# # Function to extract and print all text from a PDF URL
# def extract_and_print_all_text(pdf_url):
#     # Download the PDF file from the URL
#     response = requests.get(pdf_url)
#     with open("temp.pdf", "wb") as pdf_file:
#         pdf_file.write(response.content)

#     with pdfplumber.open("temp.pdf") as pdf:
#         for page in pdf.pages:
#             page_text = page.extract_text()
#             print(page_text)

# # Call the function to extract and print all text
# extract_and_print_all_text(pdf_url)


import requests
import pdfplumber
import re

# URL of the PDF
pdf_url = "https://firebasestorage.googleapis.com/v0/b/medsheet-51999.appspot.com/o/T42M3QqKvBPt9kDXfTUja5FJiYU2%2FMed.pdf?alt=media&token=c8686441-91df-426a-b7fb-918267dbf656"

# Define a function to check if the PDF appears to be a medical report
def is_medical_report(page_text):
    # You can define your criteria here for identifying medical reports.
    # For example, check for keywords that are typically found in medical reports.
    medical_keywords = ["patient", "diagnosis", "prescription"]
    
    for keyword in medical_keywords:
        if keyword.lower() in page_text.lower():
            return True

    return False

# Function to extract and print all text from a PDF URL if it's a medical report
def extract_and_print_all_text(pdf_url):
    # Download the PDF file from the URL
    response = requests.get(pdf_url)
    with open("temp.pdf", "wb") as pdf_file:
        pdf_file.write(response.content)

    with pdfplumber.open("temp.pdf") as pdf:
        is_medical = False  # Flag to indicate if it's a medical report
        for page in pdf.pages:
            page_text = page.extract_text()
            if is_medical_report(page_text):
                is_medical = True
                # Print the extracted text using UTF-8 encoding
                print(page_text.encode('utf-8').decode('utf-8'))
                print(page_text)

        if not is_medical:
            print("This does not appear to be a medical report. Please upload a medical report.")


# Call the function to extract and print all text only if it's a medical report
extract_and_print_all_text(pdf_url)


