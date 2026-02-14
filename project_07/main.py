import sys
import pdfplumber
import os


PDF_PATH = os.path.join("content", "Chemistry Questions.pdf")

def load_questions_from_pdf(chapter_name: str):
    if not chapter_name.strip():
        print("Error: Chapter name cannot be empty. ")
        return
    
    questions = []
    with pdfplumber.open(PDF_PATH) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text and chapter_name.lower() in text.lower():
                
               for line in text.split("\n"):
                   if "?" in line:
                          questions.append(line.strip())

    if not questions:
        print(f"No questions found for chapter: {chapter_name}")
        return


    print(f"Questions for chapter '{chapter_name}':")
    for idx, question in enumerate(questions, start=1):
        print(f"{idx}. {question}")                      



def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <chapter_name>")
        return
    
    chapter_name = sys.argv[1]
    load_questions_from_pdf(chapter_name)


if __name__ == "__main__":
    main()    
