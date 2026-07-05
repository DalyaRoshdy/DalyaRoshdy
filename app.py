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

    import pandas as pd

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("Dataset loaded successfully")

    st.subheader("Dataset Information")

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", len(df))
    col2.metric("Columns", len(df.columns))
    col3.metric("Missing Values", df.isnull().sum().sum())

    st.subheader("Columns")

    st.write(df.columns.tolist())

    st.subheader("Numeric KPIs")

    numeric_cols = df.select_dtypes(include="number").columns

    for col in numeric_cols:

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            f"{col} Mean",
            round(df[col].mean(), 2)
        )

        c2.metric(
            f"{col} Sum",
            round(df[col].sum(), 2)
        )

        c3.metric(
            f"{col} Max",
            round(df[col].max(), 2)
        )

        c4.metric(
            f"{col} Min",
            round(df[col].min(), 2)
        )


    import plotly.express as px

    st.subheader("Visual Analytics")

    selected_column = st.selectbox(
        "Select Numeric Column",
        numeric_cols
    )

    fig = px.histogram(
        df,
        x=selected_column,
        title=f"Distribution of {selected_column}"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

