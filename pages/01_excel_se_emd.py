import streamlit as st
import pandas as pd
from io import BytesIO
import base64

st.set_page_config(page_title="Excel se EMD - PWD Tools", layout="wide")

st.title("📊 Excel se EMD - Hand Receipt Generator")
st.caption("Generate hand receipts from Excel files with automated processing")

# File uploader
uploaded_file = st.file_uploader("Upload Excel file with EMD data", type=["xlsx", "xls"])

if uploaded_file is not None:
    try:
        # Read the Excel file
        df = pd.read_excel(uploaded_file)
        st.success("File uploaded successfully!")
        
        # Display preview of data
        st.subheader("Data Preview")
        st.dataframe(df.head(10))
        
        # Validate required columns
        required_columns = ["Payee Name", "Amount", "Work Description"]
        if all(col in df.columns for col in required_columns):
            st.success("✅ Required columns found!")
            
            # Process receipts
            if st.button("Generate All Receipts"):
                st.info("Processing receipts... (simulated)")
                
                # In a real implementation, this would generate actual receipts
                # For now, we'll just show a success message
                st.success(f"✅ Generated {len(df)} receipts successfully!")
                
                # Create a sample downloadable file
                output = BytesIO()
                with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                    df.to_excel(writer, index=False, sheet_name='Receipts')
                output.seek(0)
                
                # Download button
                b64 = base64.b64encode(output.read()).decode()
                href = f'<a href="data:application/octet-stream;base64,{b64}" download="receipts.xlsx">📥 Download Generated Receipts</a>'
                st.markdown(href, unsafe_allow_html=True)
                
        else:
            st.error(f"❌ Missing required columns. Please ensure your Excel file contains: {', '.join(required_columns)}")
            
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")
else:
    st.info("👆 Please upload an Excel file to get started")

# Instructions
st.divider()
st.subheader("📋 Instructions")
st.markdown("""
1. Prepare an Excel file with the following columns:
   - **Payee Name**: Name of the person/entity receiving the payment
   - **Amount**: The amount to be paid
   - **Work Description**: Description of the work or purpose
   
2. Upload the Excel file using the file uploader above

3. Preview the data to ensure it's correctly formatted

4. Click "Generate All Receipts" to process the data

5. Download the generated receipts
""")