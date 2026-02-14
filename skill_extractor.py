def extract_skills(text):

    text = text.lower()

    skills_db = [

        "python","java","c++","machine learning","deep learning",
        "nlp","data science","tensorflow","pytorch",
        "pandas","numpy","scikit-learn",
        "react","html","css","javascript",
        "aws","ec2","s3","iam","vpc",
        "sql","linux","docker","git",
        "backend","frontend","api",
        "data analysis","statistics"

    ]

    extracted = []

    for skill in skills_db:
        if skill in text:
            extracted.append(skill)

    return extracted

