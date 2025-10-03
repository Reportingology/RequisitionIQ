import streamlit as st
import pandas as pd

st.title("RequisitionIQ Input Form")

with st.form("req_form"):
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        recruiter = st.selectbox("Recruiter", sorted(df["recruiter"].dropna().unique()))

    with col2:
        job_group = st.selectbox("Job Group", sorted(df["job_group"].dropna().unique()))

    with col3:
        job_family = st.selectbox("Job Family", sorted(df["job_family"].dropna().unique()))

    with col4:
        country = st.selectbox("Country", sorted(df["country"].dropna().unique()))

    with col5:
        job_level = st.selectbox("Job Level", sorted(df["job_level"].dropna().unique()))

    submitted = st.form_submit_button("Submit")

if submitted:
    st.write("### Selected Filters")
    st.write(f"👤 Recruiter: {recruiter}")
    st.write(f"📂 Job Group: {job_group}")
    st.write(f"🏷️ Job Family: {job_family}")
    st.write(f"🌍 Country: {country}")
    st.write(f"📊 Job Level: {job_level}")
