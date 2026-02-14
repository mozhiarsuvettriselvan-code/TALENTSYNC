from skill_extractor import extract_skills

def calculate_ats(resume_text, job_description):
    resume_skills = set(extract_skills(resume_text.lower()))
    jd_skills = set(extract_skills(job_description.lower()))

    matched = resume_skills.intersection(jd_skills)

    if len(jd_skills) == 0:
        return 0

    score = (len(matched) / len(jd_skills)) * 100

    return round(score, 2)
