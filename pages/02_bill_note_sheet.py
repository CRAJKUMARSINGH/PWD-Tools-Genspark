import streamlit as st

st.set_page_config(page_title="Bill Note Sheet - PWD Tools", layout="wide")

st.title("📝 Bill Note Sheet Generator")
st.caption("Create standardized bill note sheets for PWD documentation")

st.info("This tool is currently under development. Please use the desktop application for full functionality.")

# Project details
st.subheader("🏗️ Project Information")
col1, col2 = st.columns(2)
with col1:
    project_name = st.text_input("Project Name", "Road Construction Project")
    work_order_no = st.text_input("Work Order Number", "WO/2024/001")
with col2:
    contractor_name = st.text_input("Contractor Name", "ABC Construction Ltd.")
    date = st.date_input("Date")

# Bill details
st.subheader("💰 Bill Details")
bill_amount = st.number_input("Bill Amount (₹)", min_value=0.0, value=100000.0, step=1000.0)
bill_number = st.text_input("Bill Number", "BILL/2024/001")

# Notes section
st.subheader("📋 Notes")
notes = st.text_area("Additional Notes", height=150, 
                    placeholder="Enter any additional notes or remarks for this bill...")

# Generate button
if st.button("Generate Bill Note Sheet"):
    st.success("Bill note sheet generated successfully!")
    st.info("The generated document will be available for download here.")

st.divider()

# Instructions
st.subheader("📋 Instructions")
st.markdown("""
1. Fill in the project and contractor details
2. Enter the bill amount and number
3. Add any relevant notes
4. Click 'Generate Bill Note Sheet' to create the document
""")