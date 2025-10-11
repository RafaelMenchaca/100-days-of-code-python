from gtts import gTTS
import PyPDF2
import os
from playsound import playsound


PDF_PATH = "sample.pdf"       
OUTPUT_FILE = "audiobook.mp3" 
LANG = "en"                   


def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        for page_num, page in enumerate(reader.pages, start=1):
            page_text = page.extract_text()
            if page_text:
                text += page_text
                print(f"✅ Extracted page {page_num}")
            else:
                print(f"⚠️ Page {page_num} has no extractable text.")
    return text



def text_to_speech(text, output_file):
    if not text.strip():
        print("❌ No text found in the PDF.")
        return

    print("🎧 Generating audio, please wait...")
    tts = gTTS(text=text, lang=LANG, slow=False)
    tts.save(output_file)
    print(f"✅ Audio saved as {output_file}")


def main():
    if not os.path.exists(PDF_PATH):
        print(f"❌ File not found: {PDF_PATH}")
        return

    text = extract_text_from_pdf(PDF_PATH)
    text_to_speech(text, OUTPUT_FILE)

    play = input("▶ Do you want to play the audio now? (y/n): ").strip().lower()
    if play == "y":
        playsound(OUTPUT_FILE)


if __name__ == "__main__":
    main()
