import pdfplumber

def extract_questions(pdf_file):
    chapters = {}
    current_chapter = None

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue

            for line in text.split("\n"):
                # Detect chapter headers
                if line.strip().startswith("Chapter"):
                    current_chapter = line.strip()
                    chapters[current_chapter] = []
                elif current_chapter:
                    # Treat every line after chapter as a question
                    chapters[current_chapter].append(line.strip())
    return chapters

def main():
    # ✅ Take chapter name input from user
    chapter_name = input("Enter chapter name: ").strip()

    # Error handling: empty input
    if not chapter_name:
        print("❌ Error: Chapter name cannot be empty.")
        return

    chapters = extract_questions("Chemistry Question.pdf")

    # Find matching chapter
    questions = None
    for ch, qs in chapters.items():
        if chapter_name.lower() in ch.lower():
            questions = qs
            break

    if not questions:
        print(f"⚠️ No questions found for chapter: {chapter_name}")
        return

    print(f"📖 Questions from {chapter_name}:")
    for idx, q in enumerate(questions, start=1):
        print(f"{idx}. {q}")

if __name__ == "__main__":
    main()