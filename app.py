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

# pages/05_NoShow_Intelligence.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🚨 No-Show Intelligence")

if "df" not in st.session_state:
    st.warning("Please upload a dataset first.")
    st.stop()

df = st.session_state["df"]

# =========================
# KPI SECTION
# =========================

attendance_rate = df["showed_up_flag"].mean() * 100
no_show_rate = 100 - attendance_rate

c1, c2 = st.columns(2)

c1.metric(
    "Attendance Rate",
    f"{attendance_rate:.1f}%"
)

c2.metric(
    "No Show Rate",
    f"{no_show_rate:.1f}%"
)

st.divider()

# =========================
# SMS EFFECTIVENESS
# =========================

st.subheader("SMS Reminder Effectiveness")

sms = (
    df.groupby("sms_flag")["showed_up_flag"]
      .mean()
      .reset_index()
)

sms["showed_up_flag"] *= 100

fig_sms = px.bar(
    sms,
    x="sms_flag",
    y="showed_up_flag",
    title="Attendance Rate by SMS Reminder"
)

st.plotly_chart(
    fig_sms,
    use_container_width=True
)

# =========================
# LEAD TIME IMPACT
# =========================

st.subheader("Lead Time Impact")

lead = (
    df.groupby("Leadtime group")["showed_up_flag"]
      .mean()
      .reset_index()
)

lead["showed_up_flag"] *= 100

fig_lead = px.bar(
    lead,
    x="Leadtime group",
    y="showed_up_flag",
    title="Attendance by Lead Time Group"
)

st.plotly_chart(
    fig_lead,
    use_container_width=True
)

# =========================
# WEEKDAY IMPACT
# =========================

st.subheader("Weekday Analysis")

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
    title="Attendance by Weekday"
)

st.plotly_chart(
    fig_weekday,
    use_container_width=True
)

# =========================
# RISK SCORE IMPACT
# =========================

st.subheader("Risk Score Analysis")

risk = (
    df.groupby("risk_score")["showed_up_flag"]
      .mean()
      .reset_index()
)

risk["showed_up_flag"] *= 100

fig_risk = px.line(
    risk,
    x="risk_score",
    y="showed_up_flag",
    markers=True,
    title="Attendance by Risk Score"
)

st.plotly_chart(
    fig_risk,
    use_container_width=True
)

# =========================
# AUTOMATED INSIGHTS
# =========================

st.subheader("AI Insights")

best_weekday = (
    weekday.sort_values(
        "showed_up_flag",
        ascending=False
    )
    .iloc[0]["weekday"]
)

worst_weekday = (
    weekday.sort_values(
        "showed_up_flag",
        ascending=True
    )
    .iloc[0]["weekday"]
)

st.success(
    f"Highest attendance occurs on {best_weekday}."
)

st.warning(
    f"Lowest attendance occurs on {worst_weekday}."
)

if risk["showed_up_flag"].iloc[-1] < risk["showed_up_flag"].iloc[0]:
    st.warning(
        "Higher risk scores are associated with lower attendance."
    )

st.info(
    "Review lead-time groups with the lowest attendance for scheduling improvements."
)


# pages/04_Patient_Analytics.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("👥 Patient Analytics")

if "df" not in st.session_state:
    st.warning("Please upload a dataset first.")
    st.stop()

df = st.session_state["df"]

# =========================
# AGE DISTRIBUTION
# =========================

st.subheader("Age Distribution")

fig_age = px.histogram(
    df,
    x="age",
    nbins=20,
    title="Patient Age Distribution"
)

st.plotly_chart(
    fig_age,
    use_container_width=True
)

# =========================
# GENDER ANALYSIS
# =========================

st.subheader("Gender Distribution")

gender = (
    df.groupby("gender")
      .size()
      .reset_index(name="patients")
)

fig_gender = px.pie(
    gender,
    names="gender",
    values="patients",
    title="Gender Distribution"
)

st.plotly_chart(
    fig_gender,
    use_container_width=True
)

# =========================
# TOP NEIGHBORHOODS
# =========================

st.subheader("Top Neighborhoods")

neighborhood = (
    df.groupby("neighbourhood")
      .size()
      .reset_index(name="appointments")
      .sort_values(
          "appointments",
          ascending=False
      )
      .head(15)
)

fig_neigh = px.bar(
    neighborhood,
    x="neighbourhood",
    y="appointments",
    title="Top Neighborhoods"
)

st.plotly_chart(
    fig_neigh,
    use_container_width=True
)

# =========================
# ATTENDANCE BY GENDER
# =========================

st.subheader("Attendance by Gender")

gender_att = (
    df.groupby("gender")["showed_up_flag"]
      .mean()
      .reset_index()
)

gender_att["showed_up_flag"] *= 100

fig_att = px.bar(
    gender_att,
    x="gender",
    y="showed_up_flag",
    title="Attendance Rate by Gender"
)

st.plotly_chart(
    fig_att,
    use_container_width=True
)


#pages/06_Operational_Analytics.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("⚙️ Operational Analytics")

if "df" not in st.session_state:
    st.warning("Upload dataset first")
    st.stop()

df = st.session_state["df"]

# ==================================
# KPI SECTION
# ==================================

avg_lead_time = df["Average lead time"].mean()

total_physicians = df["physicianid"].nunique()

appointments = len(df)

c1, c2, c3 = st.columns(3)

c1.metric(
    "Appointments",
    f"{appointments:,}"
)

c2.metric(
    "Avg Lead Time",
    f"{avg_lead_time:.1f} Days"
)

c3.metric(
    "Physicians",
    total_physicians
)

st.divider()

# ==================================
# APPOINTMENTS BY WEEKDAY
# ==================================

st.subheader("Workload by Weekday")

weekday_volume = (
    df.groupby("weekday")
      .size()
      .reset_index(name="appointments")
)

fig = px.bar(
    weekday_volume,
    x="weekday",
    y="appointments",
    title="Appointments by Weekday"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==================================
# LEAD TIME DISTRIBUTION
# ==================================

st.subheader("Lead Time Distribution")

fig2 = px.histogram(
    df,
    x="Average lead time",
    nbins=30,
    title="Lead Time Distribution"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ==================================
# MONTHLY WORKLOAD
# ==================================

st.subheader("Monthly Appointment Volume")

monthly = (
    df.groupby("appointment_month")
      .size()
      .reset_index(name="appointments")
)

fig3 = px.line(
    monthly,
    x="appointment_month",
    y="appointments",
    markers=True,
    title="Monthly Volume Trend"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ==================================
# INSIGHTS
# ==================================

st.subheader("Operational Insights")

peak_day = (
    weekday_volume.sort_values(
        "appointments",
        ascending=False
    )
    .iloc[0]["weekday"]
)

st.success(
    f"Highest workload occurs on {peak_day}."
)

if avg_lead_time > 15:
    st.warning(
        "Average lead time is high and may contribute to no-shows."
    )
else:
    st.info(
        "Lead time is within acceptable range."
    )

#pages/07_Data_Quality.py
import streamlit as st
import pandas as pd

st.title("🛡️ Data Quality Center")

if "df" not in st.session_state:
    st.warning("Upload dataset first")
    st.stop()

df = st.session_state["df"]

rows = len(df)
cols = len(df.columns)

missing = df.isnull().sum().sum()

duplicates = df.duplicated().sum()

quality_score = max(
    0,
    100 - (
        (missing / max(rows * cols, 1)) * 100
    )
)

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Rows",
    f"{rows:,}"
)

c2.metric(
    "Columns",
    cols
)

c3.metric(
    "Missing Values",
    f"{missing:,}"
)

c4.metric(
    "Duplicates",
    f"{duplicates:,}"
)

st.divider()

st.subheader("Data Quality Score")

st.progress(int(quality_score))

st.metric(
    "Quality Score",
    f"{quality_score:.1f}/100"
)

st.divider()

st.subheader("Missing Values by Column")

missing_df = (
    df.isnull()
      .sum()
      .reset_index()
)

missing_df.columns = [
    "Column",
    "Missing Values"
]

st.dataframe(
    missing_df.sort_values(
        "Missing Values",
        ascending=False
    )
)

st.subheader("Column Data Types")

dtype_df = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str)
})

st.dataframe(dtype_df)

#pages/08_Reporting_Center.py
import streamlit as st
import pandas as pd

st.title("📄 Reporting Center")

if "df" not in st.session_state:
    st.warning("Upload dataset first")
    st.stop()

df = st.session_state["df"]

st.subheader("Download Reports")

st.download_button(
    label="Download Full Dataset CSV",
    data=df.to_csv(index=False),
    file_name="healthcare_dataset.csv",
    mime="text/csv"
)

physician_report = (
    df.groupby("physicianid")
      .agg(
          appointments=("appointmentid","count"),
          attendance=("showed_up_flag","mean")
      )
      .reset_index()
)

st.download_button(
    label="Download Physician Report",
    data=physician_report.to_csv(index=False),
    file_name="physician_report.csv",
    mime="text/csv"
)

risk_report = (
    df.groupby("risk_score")
      .agg(
          appointments=("appointmentid","count"),
          attendance=("showed_up_flag","mean")
      )
      .reset_index()
)

st.download_button(
    label="Download Risk Report",
    data=risk_report.to_csv(index=False),
    file_name="risk_report.csv",
    mime="text/csv"
)

st.success(
    "Reports ready for export."
)





