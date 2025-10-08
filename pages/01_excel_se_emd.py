import streamlit as st

st.set_page_config(page_title="Excel se EMD - PWD Tools", layout="wide")

st.title("📊 Excel se EMD - Hand Receipt Generator")
st.caption("Generate EMD hand receipts from Excel files")

st.info("This tool is currently under development. Please use the desktop application for full functionality.")

# File uploader
uploaded_file = st.file_uploader("Upload Excel file with EMD data", type=["xlsx", "xls"])

if uploaded_file is not None:
    st.success("File uploaded successfully! Processing will be implemented here.")
    
    # Preview button
    if st.button("Preview Sample Receipt"):
        st.info("Sample receipt preview will appear here.")

st.divider()

# Instructions
st.subheader("📋 Instructions")
st.markdown("""
1. Prepare an Excel file with the following columns:
   - Payee Name
   - Amount
   - Work Description
2. Upload the file using the uploader above
3. Preview the generated receipts
4. Download the final receipts
""")

# Sample data
st.subheader("📝 Sample Data Format")
st.markdown("""
| Payee Name | Amount | Work Description |
|------------|--------|------------------|
| ABC Company | 50000 | Road Construction |
| XYZ Contractor | 75000 | Building Renovation |
""")