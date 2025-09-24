import streamlit as st

st.set_page_config(page_title="Tender Processing - PWD Tools", layout="wide")

st.title("📋 Tender Processing System")
st.caption("Comprehensive tender management system")

# Introduction
st.info("ℹ️ This tool is hosted externally. You are being redirected to the dedicated Tender Processing application.")

# Redirect notice
st.subheader("🔄 Redirecting to External Application")
st.write("You will be redirected to the specialized Tender Processing application which provides advanced features for:")
st.markdown("""
- Complete tender lifecycle management
- Vendor registration and qualification
- Bid submission and evaluation
- Contract management
- Reporting and analytics
""")

# External link
st.link_button("🔗 Open Tender Processing System", "https://priyankatenderfinal-unlhs2yudbpg2ipxgdggws.streamlit.app/")

# Features overview
st.subheader("✨ Key Features")
features = st.tabs(["📋 Tender Management", "👥 Vendor Management", "📊 Evaluation", "📜 Contracts", "📈 Reporting"])

with features[0]:
    st.markdown("""
    **Tender Management:**
    - Create and publish tenders
    - Set submission deadlines
    - Manage tender documents
    - Track tender status
    - Automated notifications
    """)

with features[1]:
    st.markdown("""
    **Vendor Management:**
    - Vendor registration portal
    - Qualification verification
    - Performance tracking
    - Blacklist management
    - Vendor database
    """)

with features[2]:
    st.markdown("""
    **Bid Evaluation:**
    - Technical evaluation forms
    - Financial bid analysis
    - Comparative charts
    - Evaluation committee workflow
    - Transparency features
    """)

with features[3]:
    st.markdown("""
    **Contract Management:**
    - Contract generation
    - Amendment tracking
    - Milestone management
    - Payment scheduling
    - Performance monitoring
    """)

with features[4]:
    st.markdown("""
    **Reporting & Analytics:**
    - Tender performance reports
    - Vendor performance dashboards
    - Financial analytics
    - Compliance reporting
    - Custom report builder
    """)

# Screenshot placeholder
st.subheader("📸 Application Preview")
st.image("https://placehold.co/600x400/2E8B57/FFFFFF?text=Tender+Processing+System", 
         caption="Tender Processing System Interface", use_column_width=True)

# Instructions
st.divider()
st.subheader("📋 Instructions")
st.markdown("""
1. Click the "Open Tender Processing System" button above
2. The external application will open in a new tab
3. Log in with your credentials (if required)
4. Navigate to the desired module (Tenders, Vendors, etc.)
5. Follow the workflow for your specific task
6. Generate reports as needed
""")

# Support
st.divider()
st.subheader("❓ Need Help?")
st.markdown("""
If you encounter any issues with the Tender Processing System:
- Check the [User Manual](https://example.com/user-manual) for detailed instructions
- Contact support at tender-support@pwd-tools.example.com
- Refer to the [Training Materials](https://example.com/training) for video tutorials
""")