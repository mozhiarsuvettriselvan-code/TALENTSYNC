import spacy

nlp = spacy.load("en_core_web_sm")

# Predefined Skill List
skills_list = [
    "python", "java", "c++", "machine learning", "deep learning",
    "aws", "html", "css", "javascript", "react", "nodejs",
    "sql", "mongodb", "data science", "nlp", "tensorflow",
    "pandas", "numpy", "scikit-learn"
]

def extract_skills(text):
    doc = nlp(text.lower())
    extracted_skills = set()

    for skill in skills_list:
        if skill in text.lower():
            extracted_skills.add(skill)

    return list(extracted_skills)
