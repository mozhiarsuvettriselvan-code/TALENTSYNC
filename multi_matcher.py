from resume_parser import extract_pdf_text, clean_text
from skill_extractor import extract_skills
from job_processor import load_job_description
import os

def match_with_multiple_jobs(resume_path):

    # Extract resume
    resume = extract_pdf_text(resume_path)
    cleaned_resume = clean_text(resume)
    resume_skills = extract_skills(cleaned_resume)

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    job_folder = os.path.join(BASE_DIR, "data", "jobs")

    results = {}
    print("\nJOB FOLDER PATH:", job_folder)
    print("FILES FOUND:", os.listdir(job_folder))


    for job_file in os.listdir(job_folder):

        job_path = os.path.join(job_folder, job_file)
        jd = load_job_description(job_path)

        cleaned_jd = clean_text(jd)
        jd_skills = extract_skills(cleaned_jd)

        print("\n====================")
        print("Job File:", job_file)
        print("JD Skills:", jd_skills)
        print("====================")

        if len(jd_skills) == 0:
            match = 0
        else:
            matched = set(resume_skills).intersection(set(jd_skills))
            match = (len(matched) / len(jd_skills)) * 100

        role = job_file.replace(".txt", "").replace("_", " ").title()
        results[role] = match

    return resume_skills, results
