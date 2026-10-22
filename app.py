import streamlit as st
import sqlite3
import pandas as pd

title = st.title("User Access Logs")
subtitle = st.write("โชว์ข้อมูล logs ของผู้ใช้")

conn = sqlite3.connect("logs.db")
df = pd.read_sql("SELECT * FROM access_logs", conn)

total_requests = len(df)
total_errors = df[df["status"] != 200]
total_size_mb = df["size"].sum()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Requests", total_requests)
col2.metric("Total Errors", len(total_errors))
col3.dataframe(total_errors)
col4.metric("Total Size", total_size_mb)
st.dataframe(df)
