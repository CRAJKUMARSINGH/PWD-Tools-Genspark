import streamlit as st
from datetime import datetime, date
import pandas as pd

st.set_page_config(page_title="Delay Calculator - PWD Tools", layout="wide")

st.title("⏱️ Project Delay Calculator")
st.caption("Calculate project delays and associated penalties")

# Project information
st.subheader("📋 Project Information")

col1, col2 = st.columns(2)

with col1:
    project_name = st.text_input("Project Name", "Road Construction Project")
    work_order_number = st.text_input("Work Order Number", "WO-2024-001")
    contractor_name = st.text_input("Contractor Name", "ABC Construction Ltd.")

with col2:
    original_completion_date = st.date_input("Original Completion Date", date(2024, 6, 30))
    actual_completion_date = st.date_input("Actual Completion Date", date(2024, 8, 15))
    contract_value = st.number_input("Contract Value (₹)", min_value=0.0, value=5000000.0, step=10000.0)

# Delay calculation
if actual_completion_date and original_completion_date:
    delay_days = (actual_completion_date - original_completion_date).days
else:
    delay_days = 0

# Penalty rates
st.subheader("⚙️ Penalty Configuration")

col1, col2 = st.columns(2)

with col1:
    ld_rate_type = st.radio("LD Rate Type", ["Fixed Amount per Day", "Percentage of Contract Value"])
    
with col2:
    if ld_rate_type == "Fixed Amount per Day":
        ld_rate = st.number_input("LD Rate per Day (₹)", min_value=0.0, value=1000.0, step=100.0)
    else:
        ld_rate = st.number_input("LD Rate (% of contract value per day)", min_value=0.0, value=0.01, step=0.001)

# Calculate penalties
if delay_days > 0:
    if ld_rate_type == "Fixed Amount per Day":
        total_penalty = delay_days * ld_rate
        penalty_rate_display = f"₹{ld_rate:,.2f} per day"
    else:
        daily_penalty = (ld_rate / 100) * contract_value
        total_penalty = delay_days * daily_penalty
        penalty_rate_display = f"{ld_rate}% of contract value per day (₹{daily_penalty:,.2f})"
else:
    total_penalty = 0.0
    penalty_rate_display = "N/A"

# Display results
st.subheader("📊 Delay Analysis")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Delay Duration", f"{delay_days} days" if delay_days > 0 else "No delay", 
              delta=f"+{delay_days} days" if delay_days > 0 else None)
    
with col2:
    st.metric("Penalty Rate", penalty_rate_display)
    
with col3:
    st.metric("Total Penalty", f"₹{total_penalty:,.2f}", 
              delta=f"+₹{total_penalty:,.2f}" if total_penalty > 0 else None)

# Penalty breakdown
penalty_df = None
if delay_days > 0:
    st.subheader("📅 Penalty Breakdown")
    
    # Create a timeline of penalties
    penalty_data = []
    running_total = 0.0
    
    for day in range(1, delay_days + 1):
        if ld_rate_type == "Fixed Amount per Day":
            daily_amount = ld_rate
        else:
            daily_amount = (ld_rate / 100) * contract_value
        running_total += daily_amount
        penalty_data.append({
            "Day": day,
            "Date": original_completion_date + pd.Timedelta(days=day),
            "Daily Penalty": daily_amount,
            "Cumulative Penalty": running_total
        })
    
    penalty_df = pd.DataFrame(penalty_data)
    st.dataframe(penalty_df.style.format({
        "Daily Penalty": "₹{:,.2f}",
        "Cumulative Penalty": "₹{:,.2f}"
    }))

# Penalty chart
if delay_days > 0 and penalty_df is not None:
    st.subheader("📊 Penalty Progression")
    chart_df = penalty_df.set_index("Day")[["Daily Penalty", "Cumulative Penalty"]]
    st.line_chart(chart_df)

# Generate report
st.subheader("🖨️ Generate Delay Report")

if st.button("📄 Generate Delay Analysis Report"):
    st.success("Delay analysis report generated successfully!")
    st.info("In a full implementation, this would create a downloadable PDF with the complete delay analysis.")

# Instructions
st.divider()
st.subheader("📋 Instructions")
st.markdown("""
1. Enter project information including dates and contract value
2. Configure penalty rates based on contract terms
3. Review the calculated delay duration and penalties
4. Analyze the penalty breakdown if needed
5. Generate a delay analysis report for documentation
""")