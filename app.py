import streamlit as st

st.set_page_config(
    page_title="Healthcare Analytics Platform",
    layout="wide"
)

st.title("🏥 Healthcare Analytics Platform")

uploaded_file = st.file_uploader(
    "Upload Dataset",
    type=["xlsx", "csv"]
)

if uploaded_file:
    st.write("File uploaded successfully!")
