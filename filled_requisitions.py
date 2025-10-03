import streamlit as st
import pandas as pd
import datetime

# Load CSV directly from GitHub
url_filled_requisitions = "https://raw.githubusercontent.com/Reportingology/RequisitionIQ/refs/heads/main/requisitions/filled_requisitions.csv"
filled_requisitions = pd.read_csv(url_filled_requisitions)

filled_requisitions.head()
