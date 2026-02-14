from resume_parser import extract_pdf_text, clean_text
from job_processor import load_job_description
from job_matcher import calculate_match

resume = extract_pdf_text(r"C:\Users\Mozhiarasu\OneDrive\Desktop\TALENTSYNC\sample_resume.pdf")
cleaned = clean_text(resume)

jd = load_job_description(r"C:\Users\Mozhiarasu\OneDrive\Desktop\TALENTSYNC\data\jobs\aws_cloud_engineer.txt")

match = calculate_match(cleaned, jd)

print("Job Match Percentage:")
print(match, "%")
