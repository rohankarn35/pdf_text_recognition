from flask import Flask, request, jsonify
import requests
import pdfplumber
import re

app = Flask(__name__)

def is_medical_report(page_text):
    medical_keywords = ["patient", "diagnosis", "prescription"]
    
    for keyword in medical_keywords:
        if keyword.lower() in page_text.lower():
            return True

    return False


@app.route('/extract_pdf_text', methods=['POST'])
def extract_pdf_text():
    pdf_url = request.json.get('pdf_url')
    
    if not pdf_url:
        return jsonify({"error": "Missing 'pdf_url' parameter"}), 400

   
    response = requests.head(pdf_url)
    content_type = response.headers.get('Content-Type')
    
    if not content_type or not content_type.lower().startswith('application/pdf'):
        return jsonify({"is_pdf": False, "message": "The provided URL is not for a PDF file."})

    # Download the PDF
    response = requests.get(pdf_url)

    if response.status_code != 200:
        return jsonify({"error": "Failed to download the PDF"}), 400

    with open("temp.pdf", "wb") as pdf_file:
        pdf_file.write(response.content)

    with pdfplumber.open("temp.pdf") as pdf:
        is_medical = False  
        extracted_text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if is_medical_report(page_text):
                is_medical = True
                extracted_text += page_text

        response_data = {
            "extracted_text": extracted_text,
            "is_medical_report": is_medical,
            "is_pdf": True
        }

        if not is_medical:
            response_data["message"] = "This does not appear to be a medical report."

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
