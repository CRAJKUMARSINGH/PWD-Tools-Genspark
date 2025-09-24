import streamlit as st
from datetime import date

st.set_page_config(page_title="Security Refund - PWD Tools", layout="wide")

st.title("🔒 Security Deposit Refund Calculator")
st.caption("Process security deposit refunds with proper calculations")

# Security Refund Calculator Form
st.subheader("📋 Security Deposit Details")

col1, col2 = st.columns(2)

with col1:
    contractor_name = st.text_input("Contractor Name", "ABC Construction Ltd.")
    security_deposit_amount = st.number_input("Original Security Deposit Amount (₹)", min_value=0.0, value=100000.0, step=1000.0)
    work_order_number = st.text_input("Work Order Number", "WO-2024-001")

with col2:
    refund_date = st.date_input("Refund Date")
    project_name = st.text_input("Project Name", "Road Construction Project")
    bank_guarantee = st.text_input("Bank Guarantee Number", "BG-2024-001")

# Deductions
st.subheader("📉 Deductions (if any)")

col1, col2, col3 = st.columns(3)

with col1:
    deficiency_in_work = st.number_input("Deficiency in Work (₹)", min_value=0.0, value=0.0, step=100.0)
    
with col2:
    liquidated_damages = st.number_input("Liquidated Damages (₹)", min_value=0.0, value=0.0, step=100.0)
    
with col3:
    other_deductions = st.number_input("Other Deductions (₹)", min_value=0.0, value=0.0, step=100.0)

# Interest calculation
st.subheader("📈 Interest Calculation")

col1, col2 = st.columns(2)

with col1:
    deposit_date = st.date_input("Security Deposit Date", date(2023, 1, 1))
    interest_rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, value=8.0, step=0.1)
    
with col2:
    interest_from_date = st.date_input("Interest Calculation From", date(2023, 1, 1))
    interest_to_date = st.date_input("Interest Calculation To", date(2024, 1, 1))

# Calculate interest period
if interest_to_date and interest_from_date:
    interest_days = (interest_to_date - interest_from_date).days
    interest_amount = (security_deposit_amount * interest_rate / 100) * (interest_days / 365)
else:
    interest_days = 0
    interest_amount = 0.0

# Calculate refund
total_deductions = deficiency_in_work + liquidated_damages + other_deductions
refund_amount = security_deposit_amount + interest_amount - total_deductions

# Display calculation
st.subheader("🧮 Refund Calculation")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Security Deposit", f"₹{security_deposit_amount:,.2f}")
    
with col2:
    st.metric("Interest Earned", f"₹{interest_amount:,.2f}", 
              delta=f"+₹{interest_amount:,.2f}" if interest_amount > 0 else None)
    
with col3:
    st.metric("Total Deductions", f"₹{total_deductions:,.2f}", 
              delta=f"-₹{total_deductions:,.2f}" if total_deductions > 0 else None)
    
with col4:
    st.metric("Refund Amount", f"₹{refund_amount:,.2f}", 
              delta=f"₹{refund_amount:,.2f}" if refund_amount > 0 else None)

# Refund status
if refund_amount <= 0:
    st.error("❌ No refund due. Deductions exceed or equal the security deposit plus interest.")
elif refund_amount < security_deposit_amount * 0.1:
    st.warning("⚠️ Refund amount is less than 10% of original security deposit.")
else:
    st.success("✅ Security deposit refund can be processed.")

# Generate refund document
st.subheader("🖨️ Generate Refund Documentation")

refund_details = {
    "Contractor Name": contractor_name,
    "Work Order Number": work_order_number,
    "Project Name": project_name,
    "Original Security Deposit Amount": security_deposit_amount,
    "Refund Date": refund_date.strftime("%Y-%m-%d") if refund_date else "",
    "Bank Guarantee": bank_guarantee,
    "Deficiency in Work": deficiency_in_work,
    "Liquidated Damages": liquidated_damages,
    "Other Deductions": other_deductions,
    "Interest Period (Days)": interest_days,
    "Interest Rate (%)": interest_rate,
    "Interest Amount": interest_amount,
    "Total Deductions": total_deductions,
    "Refund Amount": refund_amount
}

if st.button("📄 Generate Security Refund Receipt"):
    if contractor_name and work_order_number:
        st.success("✅ Security refund receipt generated successfully!")
        st.info("In a full implementation, this would create a downloadable PDF with the security refund details.")
    else:
        st.error("Please fill in the required fields (Contractor Name and Work Order Number)")

# Instructions
st.divider()
st.subheader("📋 Instructions")
st.markdown("""
1. Fill in the security deposit details in the first section
2. Enter any applicable deductions in the second section
3. Configure interest calculation parameters
4. Review the calculated refund amount
5. Generate and download the refund documentation
""")