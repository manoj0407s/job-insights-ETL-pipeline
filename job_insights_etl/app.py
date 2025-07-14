import streamlit as st
import pandas as pd
import mysql.connector
from db_config import MYSQL_CONFIG

@st.cache_data(ttl=1800)
def fetch_data():
    conn = mysql.connector.connect(**MYSQL_CONFIG)
    df = pd.read_sql("SELECT * FROM jobs", conn)
    conn.close()
    return df

# Load data
st.set_page_config(page_title="Job Insights Dashboard", layout="wide")
st.title("💼 Job Insights Dashboard")

df = fetch_data()

# Normalize strings to avoid mismatches
df['title'] = df['title'].str.strip()
df['location'] = df['location'].str.strip()

# Sidebar filters
st.sidebar.title("Filters")
title_sel = st.sidebar.multiselect("Job Title", sorted(df['title'].unique()))
loc_sel = st.sidebar.multiselect("Location", sorted(df['location'].unique()))

# Apply filters
filtered_df = df.copy()
if title_sel:
    filtered_df = filtered_df[filtered_df['title'].isin(title_sel)]
if loc_sel:
    filtered_df = filtered_df[filtered_df['location'].isin(loc_sel)]

# Display warning if no data
if filtered_df.empty:
    st.warning("⚠️ No matching jobs found. Try removing some filters.")
else:
    st.metric("Total Jobs Found", len(filtered_df))

    st.subheader("📊 Jobs by Title")
    st.bar_chart(filtered_df['title'].value_counts())

    st.subheader("📈 Jobs Over Time")
    timeline = filtered_df.groupby('date_posted').size()
    st.line_chart(timeline)

    st.subheader("🧾 Preview of Filtered Jobs")
    st.dataframe(filtered_df)
