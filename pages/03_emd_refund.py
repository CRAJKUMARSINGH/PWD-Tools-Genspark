import streamlit as st

st.set_page_config(page_title="EMD Refund - PWD Tools", layout="wide")

st.title("💰 EMD Refund Generator")
st.caption("Create EMD refund documentation and receipts")

st.info("This tool is currently under development. Please use the desktop application for full functionality.")

# Refund details
st.subheader("📋 Refund Information")
col1, col2 = st.columns(2)
with col1:
    refund_id = st.text_input("Refund ID", "EMD-REF-2024-001")
    contractor_name = st.text_input("Contractor Name", "ABC Construction Ltd.")
    refund_amount = st.number_input("Refund Amount (₹)", min_value=0.0, value=50000.0, step=1000.0)
with col2:
    work_order_no = st.text_input("Work Order Number", "WO/2024/001")
    refund_date = st.date_input("Refund Date")
    bank_details = st.text_area("Bank Details", "State Bank of India\nAccount: 1234567890\nIFSC: SBIN0001234")

# Refund reason
st.subheader("📝 Refund Reason")
refund_reason = st.text_area("Reason for Refund", 
                           "Work completed as per terms and conditions. Security deposit being refunded.",
                           height=100)

# Generate button
if st.button("Generate EMD Refund Document"):
    st.success("EMD refund document generated successfully!")
    st.info("The generated document will be available for download here.")

st.divider()

# Instructions
st.subheader("📋 Instructions")
st.markdown("""
1. Enter the refund details including contractor name and amount
2. Provide the work order number and refund date
3. Enter bank details for the refund transfer
4. Specify the reason for the refund
5. Click 'Generate EMD Refund Document' to create the paperwork
""")