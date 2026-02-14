from multi_matcher import match_with_multiple_jobs

skills, results = match_with_multiple_jobs("ml_resume.pdf")

print("\nExtracted Skills:")
print(skills)

print("\nJob Role Matching:\n")

for role, match in results.items():
    print(role, "→", round(match, 2), "%")
