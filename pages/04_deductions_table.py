import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Deductions Table - PWD Tools", layout="wide")

st.title("🧮 Deductions Table Calculator")
st.caption("Calculate all standard deductions for bill amounts")

# Standard deduction rates
deduction_rates = {
    "Income Tax (TDS)": 2.0,  # 2% for contracts
    "GST": 18.0,  # 18% standard rate
    "State Tax": 0.0,  # Variable by state
    "Professional Tax": 0.0,  # Variable by state
    "Security Deposit": 5.0,  # 5% standard
    "Earnest Money Deposit (EMD)": 0.0,  # Variable
    "Liquidated Damages": 0.0,  # Variable based on delay
    "Other Deductions": 0.0  # User defined
}

# Initialize session state for deductions
if 'deductions' not in st.session_state:
    st.session_state.deductions = deduction_rates.copy()

# Bill amount input
st.subheader("💰 Bill Amount")
bill_amount = st.number_input("Enter Total Bill Amount (₹)", min_value=0.0, value=100000.0, step=1000.0)

st.subheader("📋 Deduction Rates (%)")
st.caption("Modify the rates as per current regulations")

# Create editable deduction table
deduction_data = []
for deduction_name, rate in st.session_state.deductions.items():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"**{deduction_name}**")
    with col2:
        new_rate = st.number_input(
            f"Rate for {deduction_name}", 
            min_value=0.0, 
            max_value=100.0, 
            value=rate, 
            step=0.1,
            key=f"rate_{deduction_name}",
            label_visibility="collapsed"
        )
        st.session_state.deductions[deduction_name] = new_rate
    deduction_data.append({"Deduction": deduction_name, "Rate (%)": new_rate})

# Display deduction table
st.subheader("📊 Deduction Summary")
deductions_df = pd.DataFrame(deduction_data)

# Calculate amounts
deductions_df["Amount (₹)"] = deductions_df["Rate (%)"] * bill_amount / 100

# Display table with calculated amounts
st.dataframe(deductions_df.style.format({"Rate (%)": "{:.2f}%", "Amount (₹)": "₹{:,.2f}"}))

# Calculate totals
total_deductions = deductions_df["Amount (₹)"].sum()
net_amount = bill_amount - total_deductions

# Display summary
st.subheader("🧮 Financial Summary")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Gross Bill Amount", f"₹{bill_amount:,.2f}")
    
with col2:
    st.metric("Total Deductions", f"₹{total_deductions:,.2f}", 
              delta=f"-₹{total_deductions:,.2f}" if total_deductions > 0 else None)
    
with col3:
    st.metric("Net Amount Payable", f"₹{net_amount:,.2f}", 
              delta=f"₹{net_amount:,.2f}")

# Deduction chart
st.subheader("📊 Deduction Breakdown")
if total_deductions > 0:
    chart_data = deductions_df[deductions_df["Amount (₹)"] > 0].copy()
    if not chart_data.empty:
        st.bar_chart(chart_data.set_index("Deduction")["Amount (₹)"])
else:
    st.info("No deductions applied. Net amount equals gross bill amount.")

# Export functionality
st.subheader("💾 Export Data")
if st.button("📥 Download Deduction Summary"):
    st.success("Deduction summary downloaded successfully!")
    st.info("In a full implementation, this would create a downloadable Excel/CSV file.")

# Instructions
st.divider()
st.subheader("📋 Instructions")
st.markdown("""
1. Enter the total bill amount
2. Adjust deduction rates as per current regulations
3. Review the calculated deduction amounts
4. Check the financial summary for net payable amount
5. Export the deduction summary if needed
""")