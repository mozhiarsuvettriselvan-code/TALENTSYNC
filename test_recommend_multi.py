from multi_matcher import match_with_multiple_jobs
from skill_recommender import recommend_skills_for_jobs

skills, results = match_with_multiple_jobs("ml_resume.pdf")

recommend = recommend_skills_for_jobs(skills)

print("\nSkill Recommendations:\n")

for role, miss in recommend.items():
    print(role, "→ Learn:", miss)
