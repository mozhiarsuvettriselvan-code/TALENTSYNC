import streamlit as st
from multi_matcher import match_with_multiple_jobs
from recommender_multi import recommend_skills_for_all
from explain_engine import explain_match, recruiter_summary
from skill_extractor import extract_skills
from job_processor import load_job_description
from resume_parser import clean_text
import os
import matplotlib.pyplot as plt

st.set_page_config(page_title="TALENTSYNC", layout="wide")

# DARK MNC STYLE UI
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}
h1, h2, h3 {
    color: #00ADB5;
}
.stButton>button {
    background-color: #00ADB5;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 TALENTSYNC - AI Hiring Intelligence Platform")

uploaded_file = st.file_uploader("Upload Your Resume", type=["pdf"])

if uploaded_file is not None:

    with open("uploaded_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Resume Uploaded Successfully!")

    resume_skills, results = match_with_multiple_jobs("uploaded_resume.pdf")
    recommendations = recommend_skills_for_all("uploaded_resume.pdf")

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    job_folder = os.path.join(BASE_DIR, "data", "jobs")

    missing_dict = {}
    explain_dict = {}

    for job_file in os.listdir(job_folder):

        job_path = os.path.join(job_folder, job_file)
        jd = load_job_description(job_path)

        cleaned_jd = clean_text(jd)
        jd_skills = extract_skills(cleaned_jd)

        role = job_file.replace(".txt", "").replace("_", " ").title()

        matched = set(resume_skills).intersection(set(jd_skills))
        missing = list(set(jd_skills) - set(resume_skills))

        missing_dict[role] = missing
        explain_dict[role] = explain_match(resume_skills, jd_skills)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🧠 Extracted Skills")
        st.write(resume_skills)

    with col2:
        st.subheader("🎯 Best Matched Role")
        best_role = max(results, key=results.get)
        st.success(f"{best_role} ({round(results[best_role],2)}%)")

    st.markdown("## 📊 Job Role Match Percentage")

    roles = list(results.keys())
    scores = list(results.values())

    fig, ax = plt.subplots()
    ax.barh(roles, scores)
    ax.set_xlabel("Match %")
    st.pyplot(fig)

    st.markdown("## 📉 Missing Skills Per Role")

    for role, skills in recommendations.items():
        if len(skills) == 0:
            st.success(f"{role} → You are Job Ready!")
        else:
            st.warning(f"{role} → Learn: {skills}")

    st.markdown("## 🔍 Match Explanation")

    for role, explanation in explain_dict.items():

        st.markdown(f"### {role}")

        for line in explanation:
            st.write(line)

    st.markdown("## 📋 Recruiter Insight Summary")

    summary = recruiter_summary(results, resume_skills, missing_dict)
    st.info(summary)
