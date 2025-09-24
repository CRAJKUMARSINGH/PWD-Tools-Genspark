import streamlit as st
import pandas as pd
from io import BytesIO
import base64

st.set_page_config(page_title="EMD Refund Calculator - PWD Tools", layout="wide")

st.title("💰 EMD Refund Calculator")
st.caption("Calculate and process Earnest Money Deposit refunds efficiently")

# EMD Refund Calculator Form
st.subheader("📋 EMD Refund Details")

col1, col2 = st.columns(2)

with col1:
    contractor_name = st.text_input("Contractor Name", "ABC Construction Ltd.")
    emd_amount = st.number_input("Original EMD Amount (₹)", min_value=0.0, value=50000.0, step=1000.0)
    work_order_number = st.text_input("Work Order Number", "WO-2024-001")

with col2:
    refund_date = st.date_input("Refund Date")
    tender_number = st.text_input("Tender Number", "TEND-2024-001")
    bank_guarantee = st.text_input("Bank Guarantee Number", "BG-2024-001")

# Deductions
st.subheader("📉 Deductions (if any)")

col1, col2, col3 = st.columns(3)

with col1:
    late_submission = st.number_input("Late Submission Fee (₹)", min_value=0.0, value=0.0, step=100.0)
    
with col2:
    deficiency_in_work = st.number_input("Deficiency in Work (₹)", min_value=0.0, value=0.0, step=100.0)
    
with col3:
    other_deductions = st.number_input("Other Deductions (₹)", min_value=0.0, value=0.0, step=100.0)

# Calculate refund
total_deductions = late_submission + deficiency_in_work + other_deductions
refund_amount = emd_amount - total_deductions

# Display calculation
st.subheader("🧮 Refund Calculation")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Original EMD Amount", f"₹{emd_amount:,.2f}")
    
with col2:
    st.metric("Total Deductions", f"₹{total_deductions:,.2f}", 
              delta=f"-₹{total_deductions:,.2f}" if total_deductions > 0 else None)
    
with col3:
    st.metric("Refund Amount", f"₹{refund_amount:,.2f}", 
              delta=f"+₹{refund_amount:,.2f}" if refund_amount > 0 else None)

# Refund status
if refund_amount <= 0:
    st.error("❌ No refund due. Deductions exceed or equal the EMD amount.")
elif refund_amount < emd_amount * 0.1:
    st.warning("⚠️ Refund amount is less than 10% of original EMD.")
else:
    st.success("✅ Refund can be processed.")

# Generate refund document
st.subheader("🖨️ Generate Refund Documentation")

refund_details = {
    "Contractor Name": contractor_name,
    "Work Order Number": work_order_number,
    "Tender Number": tender_number,
    "Original EMD Amount": emd_amount,
    "Refund Date": refund_date.strftime("%Y-%m-%d") if refund_date else "",
    "Bank Guarantee": bank_guarantee,
    "Late Submission Fee": late_submission,
    "Deficiency in Work": deficiency_in_work,
    "Other Deductions": other_deductions,
    "Total Deductions": total_deductions,
    "Refund Amount": refund_amount
}

if st.button("📄 Generate Refund Receipt"):
    if contractor_name and work_order_number:
        st.success("✅ Refund receipt generated successfully!")
        
        # Create a downloadable Excel file with refund details
        df = pd.DataFrame([refund_details])
        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='EMD_Refund')
        output.seek(0)
        
        # Download button
        b64 = base64.b64encode(output.read()).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="emd_refund_{contractor_name.replace(" ", "_")}.xlsx">📥 Download Refund Details</a>'
        st.markdown(href, unsafe_allow_html=True)
    else:
        st.error("Please fill in the required fields (Contractor Name and Work Order Number)")

# Instructions
st.divider()
st.subheader("📋 Instructions")
st.markdown("""
1. Fill in the EMD refund details in the first section
2. Enter any applicable deductions in the second section
3. Review the calculated refund amount
4. Generate and download the refund documentation
""")