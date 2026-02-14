from skill_extractor import extract_skills
from job_processor import load_job_description
from resume_parser import clean_text
import os

def recommend_skills_for_jobs(resume_skills):

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    job_folder = os.path.join(BASE_DIR, "data", "jobs")

    recommendations = {}

    for job_file in os.listdir(job_folder):

        job_path = os.path.join(job_folder, job_file)
        jd = load_job_description(job_path)

        cleaned_jd = clean_text(jd)
        jd_skills = extract_skills(cleaned_jd)

        missing = list(set(jd_skills) - set(resume_skills))

        role = job_file.replace(".txt", "").replace("_", " ").title()
        recommendations[role] = missing

    return recommendations
