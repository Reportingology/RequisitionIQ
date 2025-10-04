import pandas as pd
import datetime

# Load CSV directly from GitHub
url_filled_requisitions = "https://raw.githubusercontent.com/Reportingology/RequisitionIQ/refs/heads/main/requisitions/filled_requisitions.csv"
filled_requisitions = pd.read_csv(url_filled_requisitions)

def print_filled_requisitions():
    """Display the filled requisitions DataFrame in Streamlit."""
    st.write(filled_requisitions)

def get_filled_requisitions():
    """Display the filled requisitions DataFrame in Streamlit."""
    return
    filled_requisitions
