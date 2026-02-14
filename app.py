import streamlit as st
from agent import run_agent

st.title("TALENTSYNC - AI Resume Analyzer")

resume = st.file_uploader("Upload Resume", type=["pdf"])

if resume is not None:
    with open("uploaded_resume.pdf", "wb") as f:
        f.write(resume.getbuffer())

    if st.button("Analyze Resume"):

        skills, match, ats, missing = run_agent(
            "uploaded_resume.pdf",
            r"C:\Users\Mozhiarasu\OneDrive\Desktop\TALENTSYNC\data\jobs\aws_cloud_engineer.txt"
        )

        st.subheader("Extracted Skills")
        st.write(skills)

        st.subheader("Job Match Percentage")
        st.write(str(match) + " %")

        st.subheader("ATS Score")
        st.write(str(ats) + " %")

        st.subheader("Missing Skills")
        st.write(missing)
