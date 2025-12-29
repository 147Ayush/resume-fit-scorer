import streamlit as st

from nlp.text_cleaner import clean_text
from nlp.skill_extractor import extract_skills
from ml.similarity import calculate_similarity
from ml.scoring import skill_match_score, final_resume_score
from assets.skill_plot import plot_skill_gap

# -------------------------------------------------
st.set_page_config(page_title="Resume Fit Scorer", layout="wide")

SKILL_DB = [
    "python", "machine learning", "deep learning", "nlp",
    "data analysis", "sql", "tensorflow", "pytorch",
    "streamlit", "scikit-learn", "pandas", "numpy",
    "git", "docker", "aws"
]

st.title("📄 Resume Fit Sccorer")
st.markdown("**ML + NLP based Resume–Job Description Matching System**")

col1, col2 = st.columns(2)

with col1:
    resume_text = st.text_area("📄 Paste Resume Text", height=300)

with col2:
    jd_text = st.text_area("🧾 Paste Job Description", height=300)

if st.button("🔍 Analyze Fit"):
    if not resume_text.strip() or not jd_text.strip():
        st.error("Please paste both Resume and Job Description.")
    else:
        # --- Clean text for similarity ---
        clean_resume = clean_text(resume_text)
        clean_jd = clean_text(jd_text)

        # --- Skill extraction (raw text) ---
        resume_skills = extract_skills(resume_text, SKILL_DB)
        jd_skills = extract_skills(jd_text, SKILL_DB)

        matched_skills = resume_skills & jd_skills
        missing_skills = jd_skills - resume_skills

        # --- Scores ---
        text_score = calculate_similarity(clean_resume, clean_jd)
        skill_score = skill_match_score(resume_skills, jd_skills)
        final_score = final_resume_score(skill_score, text_score)

        # --- Display ---
        st.subheader("📊 Results")
        st.metric("Resume Match Score", f"{final_score} %")

        st.caption(
            f"Skill Match: {skill_score}% | Text Similarity: {text_score}%"
        )

        col3, col4 = st.columns(2)

        with col3:
            st.success("✅ Matched Skills")
            st.write(", ".join(sorted(matched_skills)) if matched_skills else "None")

        with col4:
            st.warning("❌ Missing Skills")
            st.write(", ".join(sorted(missing_skills)) if missing_skills else "No missing skills 🎉")

        fig = plot_skill_gap(len(matched_skills), len(missing_skills))
        st.pyplot(fig)
