import os
import re
import configparser
from PyPDF2 import PdfReader

CONTENT_FOLDER = "content"
CONFIG_FILE = "config.ini"
PDF_FILE =os.path.join(CONTENT_FOLDER, "Chemistry Questions.pdf")


def ensure_folder_exists(folder_path):
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")
    

def ensure_file_exists(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    

def read_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text_content = ""
    for page in reader.pages:
        text_content += page.extract_text() + "\n"
        return text_content
    

def load_regex_from_config(config_path):
    if not os.path.isfile(config_path):
        raise FileNotFoundError("Configuration File not found")

    config = configparser.ConfigParser()
    config.read(config_path) 

    if "settings" not in config or "regex_pattern" not in config["settings"]:
        raise KeyError("Missing 'regex_pattern' in 'settings' section of the config file.")

    return config["settings"]["regex_pattern"] 



def extract_with_regex(text, regex_pattern):
    pattern = re.compile(regex_pattern)
    matches = pattern.findall(text)
    return matches


def write_to_file(file_path, data):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for item in data:
                file.write(item + "\n")
    except Exception as e:
        raise IOError(f"An error occurred while writing to the file: {e}")
    

def main():
    try:
        ensure_folder_exists(CONTENT_FOLDER)
        ensure_file_exists(PDF_FILE)

        regex_pattern = load_regex_from_config(CONFIG_FILE)

        pdf_text = read_pdf(PDF_FILE)

        extracted_text = extract_with_regex(pdf_text, regex_pattern)

        if not extracted_text.strip():
            print("No matches found with the provided regex pattern.")
            return
        
        subfolder = [f for f in os.listdir(CONTENT_FOLDER)
                     if os.path.isdir(os.path.join(CONTENT_FOLDER, f))]
        
        for folder in subfolder:

            folder_path = os.path.join(CONTENT_FOLDER, folder)
            output_file = os.path.join(folder_path, "extracted_questions.txt")
            write_to_file(output_file, extracted_text)
            print(f"Extracted content written to {output_file}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()


