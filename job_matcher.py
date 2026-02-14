from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_match(resume_text, job_description):
    text = [resume_text, job_description]

    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(text)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    return round(similarity[0][0] * 100, 2)
