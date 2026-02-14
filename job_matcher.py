from skill_extractor import extract_skills

def calculate_match_percentage(resume_text, job_description):

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_description)

    if len(jd_skills) == 0:
        return 0

    matched = set(resume_skills).intersection(set(jd_skills))

    match_percent = (len(matched) / len(jd_skills)) * 100

    return match_percent
