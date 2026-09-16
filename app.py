import streamlit as st
from pypdf import PdfReader
import re

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

# ---------------- TITLE ----------------
st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and get a quick AI-based analysis.")

# ---------------- SKILLS DATABASE ----------------
skills_database = [
    "python",
    "java",
    "c++",
    "sql",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data science",
    "data analysis",
    "html",
    "css",
    "javascript",
    "react",
    "git",
    "github",
    "excel",
    "power bi",
    "tensorflow",
    "pytorch",
    "opencv",
    "nlp",
    "communication",
    "teamwork"
]

# ---------------- JOB ROLES ----------------
job_roles = {
    "Data Scientist": [
        "python",
        "sql",
        "machine learning",
        "data science",
        "statistics"
    ],
    "AI/ML Engineer": [
        "python",
        "machine learning",
        "deep learning",
        "tensorflow",
        "pytorch",
        "artificial intelligence"
    ],
    "Web Developer": [
        "html",
        "css",
        "javascript",
        "react",
        "git"
    ],
    "Data Analyst": [
        "python",
        "sql",
        "excel",
        "power bi",
        "data analysis"
    ]
}

# ---------------- PDF TEXT EXTRACTION ----------------
def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text

# ---------------- SKILL EXTRACTION ----------------
def find_skills(resume_text):
    resume_text = resume_text.lower()
    found_skills = []

    for skill in skills_database:
        if skill in resume_text:
            found_skills.append(skill)

    return found_skills

# ---------------- SCORE CALCULATION ----------------
def calculate_score(resume_text, found_skills):
    score = 0

    if len(resume_text) > 200:
        score += 20

    if "education" in resume_text:
        score += 15

    if "experience" in resume_text:
        score += 15

    if "projects" in resume_text:
        score += 15

    if "skills" in resume_text:
        score += 10

    if "contact" in resume_text or "email" in resume_text:
        score += 10

    score += min(len(found_skills) * 2, 15)

    return min(score, 100)

# ---------------- SUGGESTIONS ----------------
def generate_suggestions(resume_text, found_skills):
    suggestions = []

    if len(resume_text) < 200:
        suggestions.append("Add more details to your resume.")

    if "education" not in resume_text:
        suggestions.append("Add an Education section.")

    if "projects" not in resume_text:
        suggestions.append("Add academic or personal projects.")

    if "experience" not in resume_text:
        suggestions.append("Add internship, training, or experience details.")

    if len(found_skills) < 5:
        suggestions.append("Mention more relevant technical skills.")

    if not suggestions:
        suggestions.append("Your resume has a good basic structure. Keep improving it!")

    return suggestions

# ---------------- USER INTERFACE ----------------
uploaded_file = st.file_uploader(
    "Upload your resume (PDF only)",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("Resume uploaded successfully! ✅")

    if st.button("🔍 Analyze Resume"):

        with st.spinner("Analyzing your resume..."):

            resume_text = extract_text_from_pdf(uploaded_file)
            found_skills = find_skills(resume_text)
            score = calculate_score(resume_text, found_skills)
            suggestions = generate_suggestions(resume_text, found_skills)

        st.subheader("📊 Resume Analysis")

        st.metric("Resume Score", f"{score}/100")

        st.subheader("🛠️ Skills Detected")

        if found_skills:
            st.write(", ".join(found_skills))
        else:
            st.warning("No predefined skills detected.")

        st.subheader("💡 Suggestions")

        for suggestion in suggestions:
            st.write("• " + suggestion)

        st.subheader("💼 Job Role Matching")

        selected_role = st.selectbox(
            "Select a job role",
            list(job_roles.keys())
        )

        required_skills = job_roles[selected_role]
        matched_skills = [
            skill for skill in required_skills
            if skill in found_skills
        ]

        missing_skills = [
            skill for skill in required_skills
            if skill not in found_skills
        ]

        st.write("**Matched Skills:**", ", ".join(matched_skills) if matched_skills else "None")
        st.write("**Missing Skills:**", ", ".join(missing_skills) if missing_skills else "None")

        if required_skills:
            match_percentage = int(
                len(matched_skills) / len(required_skills) * 100
            )
            st.progress(match_percentage / 100)
            st.write(f"Job Match: {match_percentage}%")

        with st.expander("📃 View Extracted Resume Text"):
            st.text(resume_text)
