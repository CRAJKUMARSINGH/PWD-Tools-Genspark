import streamlit as st

st.set_page_config(page_title="Bill & Deviation Generator - PWD Tools", layout="wide")

st.title("💰 Bill & Deviation Generator")
st.caption("Infrastructure Billing System with deviation tracking")

# Introduction
st.info("ℹ️ This tool is hosted externally. You are being redirected to the dedicated Bill & Deviation Generator application.")

# Redirect notice
st.subheader("🔄 Redirecting to External Application")
st.write("You will be redirected to the specialized Bill & Deviation Generator application which provides advanced features for:")
st.markdown("""
- Infrastructure billing with detailed itemization
- Deviation tracking from original work orders
- Multiple billing formats and templates
- Integration with PWD accounting systems
- Advanced reporting and analytics
""")

# External link
st.link_button("🔗 Open Bill & Deviation Generator", "https://stream-bill-generator-pjzpbb7a9fdxfmpgpg7t4d.streamlit.app/")

# Features overview
st.subheader("✨ Key Features")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **Billing Features:**
    - Itemized billing with descriptions
    - Quantity and rate calculations
    - Automatic total computation
    - Tax and deduction handling
    - Multiple currency support
    """)

with col2:
    st.markdown("""
    **Deviation Tracking:**
    - Original vs actual work comparison
    - Deviation percentage calculation
    - Cost impact analysis
    - Approval workflow integration
    - Change order management
    """)

# Screenshot placeholder
st.subheader("📸 Application Preview")
st.image("https://placehold.co/600x400/2E8B57/FFFFFF?text=Bill+%26+Deviation+Generator", 
         caption="Bill & Deviation Generator Interface", use_column_width=True)

# Instructions
st.divider()
st.subheader("📋 Instructions")
st.markdown("""
1. Click the "Open Bill & Deviation Generator" button above
2. The external application will open in a new tab
3. Log in with your credentials (if required)
4. Create new bills or manage existing ones
5. Track deviations from original work orders
6. Generate reports and documentation
""")

# Support
st.divider()
st.subheader("❓ Need Help?")
st.markdown("""
If you encounter any issues with the Bill & Deviation Generator:
- Check the [User Guide](https://example.com/user-guide) for detailed instructions
- Contact support at support@pwd-tools.example.com
- Refer to the [FAQ](https://example.com/faq) for common questions
""")