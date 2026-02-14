from resume_parser import extract_pdf_text, clean_text
from job_processor import load_job_description
from ats_score import calculate_ats

resume = extract_pdf_text(r"C:\Users\Mozhiarasu\OneDrive\Desktop\TALENTSYNC\sample_resume.pdf")
cleaned = clean_text(resume)

jd = load_job_description(r"C:\Users\Mozhiarasu\OneDrive\Desktop\TALENTSYNC\data\jobs\aws_cloud_engineer.txt")

score = calculate_ats(cleaned, jd)

print("ATS Score:")
print(score, "%")
