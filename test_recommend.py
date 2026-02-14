from resume_parser import extract_pdf_text, clean_text
from job_processor import load_job_description
from recommender import recommend_skills

resume = extract_pdf_text(r"C:\Users\Mozhiarasu\OneDrive\Desktop\TALENTSYNC\sample_resume.pdf")
cleaned = clean_text(resume)

jd = load_job_description(r"C:\Users\Mozhiarasu\OneDrive\Desktop\TALENTSYNC\data\jobs\aws_cloud_engineer.txt")

missing = recommend_skills(cleaned, jd)

print("Missing Skills:")
print(missing)
