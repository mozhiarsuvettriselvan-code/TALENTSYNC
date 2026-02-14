def explain_match(resume_skills, jd_skills):

    matched = list(set(resume_skills).intersection(set(jd_skills)))
    missing = list(set(jd_skills) - set(resume_skills))

    explanation = []

    for skill in matched:
        explanation.append(f"✔ {skill} found")

    for skill in missing:
        explanation.append(f"⚠ Missing {skill}")

    return explanation


def recruiter_summary(results, resume_skills, missing_dict):

    best_role = max(results, key=results.get)

    strong = ", ".join(resume_skills[:5])

    summary = f"""
Candidate demonstrates alignment with {best_role} roles.
Has exposure to {strong}.
"""

    if best_role in missing_dict and len(missing_dict[best_role]) > 0:
        gaps = ", ".join(missing_dict[best_role][:3])
        summary += f"May require upskilling in {gaps}."

    summary += f"\nRecommended for entry-level {best_role} positions."

    return summary
