import streamlit as st
from datetime import datetime, date

st.set_page_config(page_title="Delay Calculator - PWD Tools", layout="wide")

st.title("⏰ Project Delay Calculator")
st.caption("Calculate project delays and timeline analysis")

st.info("This tool is currently under development. Please use the desktop application for full functionality.")

# Project timeline
st.subheader("📅 Project Timeline")
col1, col2, col3 = st.columns(3)
with col1:
    start_date = st.date_input("Planned Start Date", date(2024, 1, 1))
with col2:
    end_date = st.date_input("Planned End Date", date(2024, 12, 31))
with col3:
    current_date = st.date_input("Current Date", date.today())

# Calculate delays
planned_duration = (end_date - start_date).days
elapsed_days = (current_date - start_date).days
remaining_days = (end_date - current_date).days if current_date < end_date else 0
delay_days = max(0, elapsed_days - planned_duration)

# Display timeline info
col1, col2, col3, col4 = st.columns(4)
col1.metric("Planned Duration", f"{planned_duration} days")
col2.metric("Elapsed Days", f"{elapsed_days} days")
col3.metric("Remaining Days", f"{remaining_days} days")
col4.metric("Delay", f"{delay_days} days", f"{'🔴' if delay_days > 0 else '🟢'}")

# Progress visualization
st.subheader("📊 Progress Visualization")
progress_percentage = min(100, (elapsed_days / planned_duration) * 100) if planned_duration > 0 else 0

st.progress(progress_percentage / 100)
st.markdown(f"Project is **{progress_percentage:.1f}%** complete")

# Delay analysis
if delay_days > 0:
    st.warning(f"⚠️ Project is delayed by {delay_days} days")
    st.info("Consider adjusting project timeline or allocating additional resources")

# Calculate button
if st.button("Analyze Project Timeline"):
    st.success("Timeline analysis completed!")
    st.info("Detailed delay analysis will be shown here.")

st.divider()

# Instructions
st.subheader("📋 Instructions")
st.markdown("""
1. Enter the planned start and end dates for the project
2. Set the current date to analyze progress
3. Review the calculated timeline metrics
4. Check for any delays and their impact
""")