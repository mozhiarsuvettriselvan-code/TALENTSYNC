from multi_matcher import match_with_multiple_jobs

def generate_summary(resume_path):

    skills, results = match_with_multiple_jobs(resume_path)

    best_role = max(results,key=results.get)

    summary = f"""
Candidate shows strong technical alignment towards the role of {best_role}.
Demonstrates practical exposure in skills such as {skills}.
Profile indicates readiness for deployment in real-world AI/Development environments.
Further upskilling in domain-specific tools may enhance placement probability.
    """

    return summary
