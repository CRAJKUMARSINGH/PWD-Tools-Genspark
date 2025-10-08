import streamlit as st

st.set_page_config(page_title="Security Refund - PWD Tools", layout="wide")

st.title("🔒 Security Deposit Refund")
st.caption("Calculate and process security deposit refunds")

st.info("This tool is currently under development. Please use the desktop application for full functionality.")

# Security deposit details
st.subheader("💰 Security Deposit Information")
col1, col2 = st.columns(2)
with col1:
    deposit_id = st.text_input("Deposit ID", "SEC-DEP-2024-001")
    contractor_name = st.text_input("Contractor Name", "ABC Construction Ltd.")
    deposit_amount = st.number_input("Deposit Amount (₹)", min_value=0.0, value=100000.0, step=1000.0)
with col2:
    work_order_no = st.text_input("Work Order Number", "WO/2024/001")
    deposit_date = st.date_input("Deposit Date")
    refund_date = st.date_input("Refund Date")

# Refund calculation
st.subheader("🧮 Refund Calculation")
interest_rate = st.slider("Interest Rate (%)", 0.0, 15.0, 8.0, 0.1)
years_deposited = (refund_date - deposit_date).days / 365.25 if refund_date > deposit_date else 0
interest_amount = deposit_amount * (interest_rate / 100) * years_deposited
total_refund = deposit_amount + interest_amount

col1, col2, col3 = st.columns(3)
col1.metric("Principal Amount", f"₹ {deposit_amount:,.2f}")
col2.metric("Interest Amount", f"₹ {interest_amount:,.2f}")
col3.metric("Total Refund", f"₹ {total_refund:,.2f}")

# Refund details
st.subheader("📝 Refund Details")
bank_details = st.text_area("Bank Details for Refund", 
                          "State Bank of India\nBranch: Main Branch, Udaipur\nAccount: 1234567890\nIFSC: SBIN0001234")

# Generate button
if st.button("Process Security Refund"):
    st.success("Security refund processed successfully!")
    st.info("Refund documentation will be available for download here.")

st.divider()

# Instructions
st.subheader("📋 Instructions")
st.markdown("""
1. Enter the security deposit details including contractor name and amount
2. Provide the work order number and deposit date
3. Set the refund date and adjust interest rate if needed
4. Review the calculated refund amount with interest
5. Enter bank details for the refund transfer
6. Click 'Process Security Refund' to generate documentation
""")