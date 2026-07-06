import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Healthcare Intelligence Suite",
    page_icon="🏥",
    layout="wide"
)

st.sidebar.title("🏥 Healthcare Intelligence Suite")

uploaded_file = st.sidebar.file_uploader(
    "Upload Healthcare Dataset",
    type=["xlsx", "csv"]
)

if uploaded_file:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.session_state["df"] = df

    st.success("Dataset loaded successfully")

else:

    st.title("🏥 Healthcare Intelligence Suite")

    st.markdown("""
    ## Executive Healthcare Analytics Platform

    Upload a healthcare dataset to begin.

    Features:

    - Executive Dashboard
    - Physician Analytics
    - Patient Analytics
    - No-Show Intelligence
    - Operational Analytics
    - Data Quality Center
    - Reporting Center
    """)

    st.stop()



