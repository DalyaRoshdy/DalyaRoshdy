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


import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Executive Dashboard")

if "df" not in st.session_state:
    st.warning("Please upload a dataset first.")
    st.stop()

df = st.session_state["df"]

# =========================
# KPI SECTION
# =========================

total_appointments = len(df)

attendance_rate = (
    df["showed_up_flag"].mean() * 100
)

no_show_rate = (
    100 - attendance_rate
)

unique_patients = (
    df["patientid"].nunique()
)

unique_physicians = (
    df["physicianid"].nunique()
)

avg_lead_time = (
    df["Average lead time"].mean()
)

st.subheader("Executive KPIs")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Appointments",
    f"{total_appointments:,}"
)

c2.metric(
    "Attendance %",
    f"{attendance_rate:.1f}%"
)

c3.metric(
    "No Show %",
    f"{no_show_rate:.1f}%"
)

c4, c5, c6 = st.columns(3)

c4.metric(
    "Patients",
    f"{unique_patients:,}"
)

c5.metric(
    "Physicians",
    unique_physicians
)

c6.metric(
    "Avg Lead Time",
    f"{avg_lead_time:.1f} Days"
)

st.divider()

# =========================
# APPOINTMENTS BY MONTH
# =========================

st.subheader("Appointments by Month")

monthly = (
    df.groupby("appointment_month")
    .size()
    .reset_index(name="appointments")
)

fig_month = px.bar(
    monthly,
    x="appointment_month",
    y="appointments",
    title="Monthly Appointment Volume"
)

st.plotly_chart(
    fig_month,
    use_container_width=True
)

# =========================
# ATTENDANCE BY WEEKDAY
# =========================

st.subheader("Attendance by Weekday")

weekday = (
    df.groupby("weekday")["showed_up_flag"]
    .mean()
    .reset_index()
)

weekday["showed_up_flag"] *= 100

fig_weekday = px.bar(
    weekday,
    x="weekday",
    y="showed_up_flag",
    title="Attendance Rate by Weekday",
)

st.plotly_chart(
    fig_weekday,
    use_container_width=True
)

# =========================
# ATTENDANCE BY MONTH
# =========================

st.subheader("Attendance by Month")

attendance_month = (
    df.groupby("appointment_month")["showed_up_flag"]
    .mean()
    .reset_index()
)

attendance_month["showed_up_flag"] *= 100

fig_attendance = px.line(
    attendance_month,
    x="appointment_month",
    y="showed_up_flag",
    markers=True,
    title="Attendance Trend"
)

st.plotly_chart(
    fig_attendance,
    use_container_width=True
)

# =========================
# EXECUTIVE INSIGHTS
# =========================

st.subheader("Executive Insights")

if attendance_rate >= 80:
    st.success(
        f"Attendance rate is {attendance_rate:.1f}% and is performing well."
    )
else:
    st.warning(
        f"Attendance rate is {attendance_rate:.1f}% and may require improvement."
    )

if avg_lead_time > 15:
    st.warning(
        "Average lead time is high and may contribute to no-show behavior."
    )
else:
    st.info(
        "Lead time appears within acceptable range."
    )

st.info(
    f"""
Total appointments analyzed: {total_appointments:,}

Unique patients: {unique_patients:,}

Unique physicians: {unique_physicians}
"""
)

