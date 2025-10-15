"""
Streamlit Dashboard for Growth Metrics
-------------------------------------
Run locally: streamlit run dashboard_app.py
"""

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Growth Ops Dashboard", layout="wide")

st.title("📈 Growth Operations Dashboard")
st.markdown("Monitor key growth metrics — revenue, conversion, and churn — over time.")

# Load data
df = pd.read_csv("sample_data/weekly_metrics.csv")

col1, col2, col3 = st.columns(3)
col1.metric("Latest Revenue", f"${df['revenue'].iloc[-1]:,.0f}")
col2.metric("Conversion Rate", f"{df['conversion_rate'].iloc[-1]:.1f}%")
col3.metric("Churn Rate", f"{df['churn'].iloc[-1]:.1f}%")

# Chart
fig = px.line(df, x="week", y=["revenue", "conversion_rate", "churn"],
              markers=True, title="Weekly Growth Trends",
              labels={"value": "Metric Value", "week": "Week"},
              color_discrete_sequence=px.colors.qualitative.Set2)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Insights")
st.write("Revenue and conversion rates show steady improvement, with churn declining slightly — a positive trend for sustainable growth.")

