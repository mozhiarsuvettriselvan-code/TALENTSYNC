from resume_parser import extract_pdf_text, clean_text
from skill_extractor import extract_skills
from job_processor import load_job_description
from job_matcher import calculate_match
from ats_score import calculate_ats
from recommender import recommend_skills

def run_agent(resume_path, jd_path):

    resume = extract_pdf_text(resume_path)
    cleaned = clean_text(resume)

    jd = load_job_description(jd_path)

    skills = extract_skills(cleaned)
    match = calculate_match(cleaned, jd)
    ats = calculate_ats(cleaned, jd)
    missing = recommend_skills(cleaned, jd)

    return skills, match, ats, missing
