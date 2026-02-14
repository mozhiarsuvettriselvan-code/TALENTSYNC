from skill_extractor import extract_skills

def recommend_skills(resume_text, job_description):
    resume_skills = set(extract_skills(resume_text.lower()))
    jd_skills = set(extract_skills(job_description.lower()))

    missing = jd_skills - resume_skills

    return list(missing)
