import streamlit as st
import pandas as pd

st.set_page_config(page_title="Deductions Table - PWD Tools", layout="wide")

st.title("📊 Deductions Calculator")
st.caption("Calculate standard deductions for PWD bill amounts")

st.info("This tool is currently under development. Please use the desktop application for full functionality.")

# Bill amount
st.subheader("💰 Bill Amount")
bill_amount = st.number_input("Total Bill Amount (₹)", min_value=0.0, value=100000.0, step=1000.0)

# Deductions calculator
st.subheader("🧮 Standard Deductions")
deductions = {
    "Income Tax (2%)": bill_amount * 0.02,
    "VAT (5%)": bill_amount * 0.05,
    "Service Tax (10%)": bill_amount * 0.10,
    "Retention Money (10%)": bill_amount * 0.10,
    "Security Deposit (5%)": bill_amount * 0.05,
    "Other Deductions": 0.0
}

# Display deductions table
deductions_df = pd.DataFrame({
    "Deduction Type": list(deductions.keys()),
    "Amount (₹)": list(deductions.values())
})

st.dataframe(deductions_df, use_container_width=True)

# Total deductions
total_deductions = sum(deductions.values())
net_amount = bill_amount - total_deductions

col1, col2, col3 = st.columns(3)
col1.metric("Total Bill Amount", f"₹ {bill_amount:,.2f}")
col2.metric("Total Deductions", f"₹ {total_deductions:,.2f}")
col3.metric("Net Amount", f"₹ {net_amount:,.2f}", f"-₹ {total_deductions:,.2f}")

# Calculate button
if st.button("Calculate Deductions"):
    st.success("Deductions calculated successfully!")
    st.info("Detailed breakdown will be shown here.")

st.divider()

# Instructions
st.subheader("📋 Instructions")
st.markdown("""
1. Enter the total bill amount
2. Review the standard deductions calculated
3. Adjust any custom deduction values if needed
4. View the net amount after all deductions
""")