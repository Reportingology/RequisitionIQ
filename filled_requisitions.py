import streamlit as st
import pandas as pd
import datetime

# Load CSV directly from GitHub
url_filled_requisitions = "https://raw.githubusercontent.com/Reportingology/RequisitionIQ/refs/heads/main/requisitions/filled_requisitions.csv"
filled_requisitions = pd.read_csv(url_filled_requisitions)

def print_filled_requisitions(df):
    """Display the filled requisitions DataFrame in Streamlit."""
    import streamlit as st
    st.write(df)
