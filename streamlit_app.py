import streamlit as st
import datetime

from filled_requisitions import print_filled_requisitions

st.title("RequisitionIQ")
st.write(
    "At the center of a stalled requisition is a conversation that never happened. "
    "ReqIQ starts it—before it's too late."
)

st.subheader("Requisition Input Form")

with st.form("req_form"):
    # 6 columns for left-to-right layout
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        st.markdown("**Requisition Number**")
        st.text_input("", value="R01854", disabled=True, key="req_id")

    with col2:
        st.markdown("**Days to First Screen**")
        date_first_screen = st.number_input("", min_value=0, step=1, key="days_to_first_screen")

    with col3:
        st.markdown("**Total Applicants**")
        total_applicants = st.number_input("", min_value=0, step=1, key="total_applicants")

    with col4:
        st.markdown("**Reviewed in X Days**")
        reviewed_in_x_days = st.number_input("", min_value=0, step=1, key="reviewed")

    with col5:
        st.markdown("**Total Interviews**")
        total_interviews = st.number_input("", min_value=0, step=1, key="interviews")

    with col6:
        st.markdown("**Time to Fill (days)**")
        time_to_fill = st.number_input("", min_value=0, step=1, key="time_to_fill")

    submitted = st.form_submit_button("Submit")

if submitted:
    st.write("### Results")
    st.write(f"📅 Date of First Screen: {date_first_screen}")
    st.write(f"👥 Total Applicants: {total_applicants}")
    st.write(f"📑 Reviewed in X Days: {reviewed_in_x_days}")
    st.write(f"🎤 Total Interviews: {total_interviews}")
    st.write(f"⏳ Time to Fill: {time_to_fill} days")

print_filled_requisitions(df_filled_requisitions)
