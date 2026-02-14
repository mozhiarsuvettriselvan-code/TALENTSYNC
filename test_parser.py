print("TEST STARTED")

from resume_parser import extract_pdf_text, clean_text

resume = extract_pdf_text(r"C:\Users\Mozhiarasu\OneDrive\Desktop\TALENTSYNC\sample_resume.pdf")

print("RAW TEXT BELOW")
print(resume)

cleaned = clean_text(resume)

print("\nCLEANED TEXT BELOW")
print(cleaned)
