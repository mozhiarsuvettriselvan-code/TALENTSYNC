from multi_matcher import match_with_multiple_jobs
from job_processor import load_job_description
from skill_extractor import extract_skills
from resume_parser import extract_pdf_text, clean_text
import os

def explain_match(resume_path):

    resume = extract_pdf_text(resume_path)
    cleaned_resume = clean_text(resume)
    resume_skills = extract_skills(cleaned_resume)

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    job_folder = os.path.join(BASE_DIR, "data", "jobs")

    explanation = {}

    for job_file in os.listdir(job_folder):

        job_path = os.path.join(job_folder, job_file)
        jd = load_job_description(job_path)

        cleaned_jd = clean_text(jd)
        jd_skills = extract_skills(cleaned_jd)

        matched = set(resume_skills).intersection(set(jd_skills))

        role = job_file.replace(".txt", "").replace("_", " ").title()

        explanation[role] = f"Matched Skills: {list(matched)}"

    return explanation
