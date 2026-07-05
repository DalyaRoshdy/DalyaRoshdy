import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Healthcare Intelligence Suite",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Healthcare Intelligence Suite")

st.markdown("""
### Executive Healthcare Analytics Platform

Transform appointment data into actionable operational intelligence.

#### Included Analytics

- Executive KPI Dashboard
- Physician Performance Analytics
- Patient Attendance Analytics
- No-Show Risk Intelligence
- Operational Efficiency Metrics
- Automated Reporting

Upload a dataset to begin.
""")

page = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Executive Dashboard",
        "Physician Analytics",
        "Patient Analytics",
        "No-Show Analytics",
        "Data Quality"
    ]
)

attendance_rate = df["showed_up_flag"].mean() * 100

if attendance_rate < 80:
    st.warning(
        "Attendance rate is below the recommended target of 80%."
    )
else:
    st.success(
        "Attendance rate is meeting target."
    )

top_physicians = physician_stats.sort_values(
    "appointments",
    ascending=False
).head(10)

st.dataframe(top_physicians)

top_physicians = physician_stats.sort_values(
    "appointments",
    ascending=False
).head(10)

st.dataframe(top_physicians)

st.download_button(
    "Download Physician Report",
    physician_stats.to_csv(index=False),
    "physician_report.csv",
    "text/csv"
)

