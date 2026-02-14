import streamlit as st
from multi_matcher import match_with_multiple_jobs
from recommender_multi import recommend_skills_for_all
from explainable_engine import explain_match
from recruiter_summary import generate_summary
import matplotlib.pyplot as plt

# ===== LOAD CSS =====
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styles.css")

st.title("TALENTSYNC Resume Intelligence Dashboard")

uploaded = st.file_uploader("Upload Resume", type=["pdf"])

if uploaded:

    with open("uploaded_resume.pdf", "wb") as f:
        f.write(uploaded.read())

    skills, results = match_with_multiple_jobs("uploaded_resume.pdf")
    rec = recommend_skills_for_all("uploaded_resume.pdf")
    explanation = explain_match("uploaded_resume.pdf")
    summary = generate_summary("uploaded_resume.pdf")

    col1, col2 = st.columns([1,1])

    with col1:

        st.markdown('<div class="skills-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Extracted Skills</div>', unsafe_allow_html=True)

        st.markdown('<div class="skills-container">', unsafe_allow_html=True)
        for s in skills:
            st.markdown(f'<div class="skill-pill">{s}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Recruiter Summary</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="summary-box">{summary}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Role Match Graph</div>', unsafe_allow_html=True)

        fig, ax = plt.subplots(figsize=(4,3))
        ax.barh(list(results.keys()), list(results.values()))
        st.pyplot(fig)

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### Role Based Insights")

    for role, score in results.items():

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader(role)
        st.write(f"Match Score: {round(score,2)}%")

        st.markdown(f'<div class="progress-bar" style="width:{score}%"></div>', unsafe_allow_html=True)

        if len(rec[role]) == 0:
            st.write("You are Job Ready!")
        else:
            st.write("Learn:", rec[role])

        st.write(explanation[role])

        st.markdown('</div>', unsafe_allow_html=True)

