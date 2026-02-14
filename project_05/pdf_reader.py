import os
from PyPDF2 import PdfReader

def read_pdf(pdf_path):
    if not os.path.isfile(pdf_path):
        raise FileNotFoundError("PDF file not found.")
    
    reader = PdfReader(pdf_path)
    text_content = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            text_content += text + "\n"
    return text_content