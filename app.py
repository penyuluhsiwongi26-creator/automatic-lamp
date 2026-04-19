import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Pertanian", layout="wide")

st.title("🌾 Dashboard Indikator Pertanian")

uploaded_file = st.file_uploader("Upload file Excel", type=["xlsx"])

if uploaded_file:
    xls = pd.ExcelFile(uploaded_file)
    sheets = xls.sheet_names

    selected_sheet = st.sidebar.selectbox("Pilih Indikator", sheets)

    df = pd.read_excel(uploaded_file, sheet_name=selected_sheet)

    st.subheader(f"Data: {selected_sheet}")
    st.dataframe(df, use_container_width=True)

    numeric_cols = df.select_dtypes(include=['int64','float64']).columns

    if len(numeric_cols) > 0:
        col = st.selectbox("Pilih kolom grafik", numeric_cols)
        st.line_chart(df[col])

        col1, col2, col3 = st.columns(3)
        col1.metric("Total", df[col].sum())
        col2.metric("Rata-rata", df[col].mean())
        col3.metric("Max", df[col].max())

else:
    st.info("Upload file Excel untuk mulai")