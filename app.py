
import streamlit as st
from main import recommend_courses

st.title("Course Recommendation Engine")
profile = st.text_area("Enter your learning profile:")
completed = st.text_input("Enter completed course IDs (comma-separated):")

if st.button("Recommend"):
    completed_ids = [x.strip() for x in completed.split(',') if x.strip()]
    recommendations = recommend_courses(profile, completed_ids)
    st.write("### Top 5 Recommended Courses:")
    for course_id, score in recommendations:
        st.write(f"{course_id} (Similarity Score: {score:.4f})")
