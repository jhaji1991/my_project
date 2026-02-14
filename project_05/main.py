import os
from pdf_reader import read_pdf
from extractor import load_regex, extract_questions
from database import create_table, insert_question

CONTENT_FOLDER = "content"
PDF_FILE = os.path.join(CONTENT_FOLDER, "Chemistry Questions.pdf")
CONFIG_FILE = "config.ini"

def main():
    try:

        pdf_text = read_pdf(PDF_FILE)



        regex_pattern = load_regex(CONFIG_FILE)



        questions = extract_questions(pdf_text, regex_pattern)

        if not questions:
            print("⚠️ No questions found with given regex.")
            return

        create_table()

        subject = "Chemistry"
        chapter = "Chapter 1"

        for q in questions:
            parts = q.split("\n")
            question_text = parts[0]
            answer_options = "\n".join(parts[1:]) if len(parts) > 1 else ""
            insert_question(subject, question_text, answer_options, chapter)

        print("All questions stored in MySQL.")

    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()