import spacy
from pdfminer.high_level import extract_text
import docx

# Load NLP Model
nlp = spacy.load("en_core_web_sm")

# Extract text from PDF
def extract_pdf_text(file_path):
    try:
        text = extract_text(file_path)
        print("PDF TEXT LENGTH:", len(text))
        return text
    except Exception as e:
        print("Error reading PDF:", e)
        return ""


# Extract text from DOCX
def extract_docx_text(file_path):
    doc = docx.Document(file_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text
    return text

# Clean Resume Text using NLP
def clean_text(text):
    doc = nlp(text)
    clean = []
    for token in doc:
        if not token.is_stop and not token.is_punct:
            clean.append(token.lemma_)
    return " ".join(clean)
