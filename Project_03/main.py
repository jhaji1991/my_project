import os
from PyPDF2 import PdfReader


CONTENT_FOLDER = "content"
PDF_FILE = os.path.join(CONTENT_FOLDER, "Chemistry Questions.pdf")
OUTPUT_FILE = os.path.join(CONTENT_FOLDER, "output.txt")

def ensure_folder_exists(folder_path):
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder '{folder_path}' not found.")
    

def ensure_file_exists(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")
    

def read_pdf(pdf_path):
    page_number = int(input("Press enter the page number you want to read: "))
    reader = PdfReader(pdf_path)
    text_content = ""
    if 0 <= page_number < len(reader.pages):
        text_content = reader.pages[page_number].extract_text()
    else:
        raise ValueError("Page number is out of range.")
    return text_content


def write_to_file(output_path, content):
    """Write content to output.txt file."""
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        raise IOError(f"Error writing to {output_path}: {e}")

def main():
    try:

        ensure_folder_exists(CONTENT_FOLDER)


        ensure_file_exists(PDF_FILE)


        pdf_text = read_pdf(PDF_FILE)

 
        write_to_file(OUTPUT_FILE, pdf_text)

        print(f"Successfully extracted PDF content to {OUTPUT_FILE}")

    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()