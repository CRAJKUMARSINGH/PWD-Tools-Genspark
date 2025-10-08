import streamlit as st
import pandas as pd

st.set_page_config(page_title="Financial Progress - PWD Tools", layout="wide")

st.title("📈 Financial Progress Tracker")
st.caption("Track financial progress and Liquidated Damages (LDs)")

st.info("This tool is currently under development. Please use the desktop application for full functionality.")

# Project financials
st.subheader("💰 Project Financial Overview")
col1, col2, col3 = st.columns(3)
with col1:
    total_budget = st.number_input("Total Project Budget (₹)", min_value=0.0, value=10000000.0, step=100000.0)
with col2:
    expenditure_to_date = st.number_input("Expenditure to Date (₹)", min_value=0.0, value=6500000.0, step=100000.0)
with col3:
    bills_certified = st.number_input("Bills Certified (₹)", min_value=0.0, value=6200000.0, step=100000.0)

# Progress calculation
progress_percentage = (expenditure_to_date / total_budget) * 100 if total_budget > 0 else 0
budget_utilization = (expenditure_to_date / total_budget) * 100 if total_budget > 0 else 0

col1, col2 = st.columns(2)
col1.metric("Financial Progress", f"{progress_percentage:.1f}%", "↗️ Progress")
col2.metric("Budget Utilization", f"{budget_utilization:.1f}%", "📊 Utilization")

# LD (Liquidated Damages) calculation
st.subheader("⚖️ Liquidated Damages (LDs)")
delay_days = st.number_input("Delay Days", min_value=0, value=0, step=1)
ld_rate = st.number_input("LD Rate per Day (₹)", min_value=0.0, value=1000.0, step=100.0)
total_ld = delay_days * ld_rate

st.metric("Total LD Amount", f"₹ {total_ld:,.2f}", "⚠️ Penalty")

# Financial data table
st.subheader("📊 Financial Data")
financial_data = pd.DataFrame({
    "Month": ["Jan 2024", "Feb 2024", "Mar 2024", "Apr 2024", "May 2024", "Jun 2024"],
    "Planned Progress (%)": [8.3, 16.7, 25.0, 33.3, 41.7, 50.0],
    "Actual Progress (%)": [7.5, 15.2, 23.1, 31.8, 39.5, 48.2],
    "Bills Raised (₹ Lakh)": [8.3, 16.7, 25.0, 33.3, 41.7, 50.0],
    "Payments Made (₹ Lakh)": [8.1, 16.2, 24.1, 32.5, 40.2, 48.8]
})

st.dataframe(financial_data, use_container_width=True)

# Generate report button
if st.button("Generate Financial Progress Report"):
    st.success("Financial progress report generated successfully!")
    st.info("The detailed report will be available for download here.")

st.divider()

# Instructions
st.subheader("📋 Instructions")
st.markdown("""
1. Enter the total project budget and current expenditure
2. Review the financial progress percentage
3. Calculate any LD amounts based on project delays
4. Analyze the monthly financial data
5. Generate a comprehensive financial progress report
""")