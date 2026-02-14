from resume_parser import extract_pdf_text, clean_text
from skill_extractor import extract_skills

resume = extract_pdf_text(r"C:\Users\Mozhiarasu\OneDrive\Desktop\TALENTSYNC\sample_resume.pdf")
cleaned = clean_text(resume)

skills = extract_skills(cleaned)

print("Extracted Skills:")
print(skills)
