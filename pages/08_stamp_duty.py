import streamlit as st

st.set_page_config(page_title="Stamp Duty Calculator - PWD Tools", layout="wide")

st.title("🎫 Stamp Duty Calculator")
st.caption("Calculate stamp duty with predefined PWD rates")

# Stamp Duty Calculator
st.subheader("📋 Document Details")

col1, col2 = st.columns(2)

with col1:
    document_type = st.selectbox("Document Type", [
        "Work Order",
        "Contract Agreement",
        "Tender Document",
        "Agreement for Services",
        "Lease/Rent Agreement",
        "Mortgage Deed",
        "Affidavit",
        "Power of Attorney"
    ])
    
    document_value = st.number_input("Document Value/Consideration (₹)", min_value=0.0, value=100000.0, step=1000.0)

with col2:
    state = st.selectbox("State", [
        "Rajasthan",
        "Maharashtra",
        "Uttar Pradesh",
        "Madhya Pradesh",
        "Gujarat",
        "Other"
    ])
    
    execution_date = st.date_input("Date of Execution")

# Stamp duty rates (simplified for demonstration)
stamp_duty_rates = {
    "Rajasthan": {
        "Work Order": 0.1,  # 0.1% of document value
        "Contract Agreement": 0.2,  # 0.2% of document value
        "Tender Document": 0.05,  # 0.05% of document value
        "Agreement for Services": 0.15,  # 0.15% of document value
        "Lease/Rent Agreement": 0.25,  # 0.25% of document value
        "Mortgage Deed": 0.3,  # 0.3% of document value
        "Affidavit": 100,  # Fixed amount
        "Power of Attorney": 100  # Fixed amount
    },
    "Maharashtra": {
        "Work Order": 0.15,
        "Contract Agreement": 0.25,
        "Tender Document": 0.075,
        "Agreement for Services": 0.2,
        "Lease/Rent Agreement": 0.3,
        "Mortgage Deed": 0.35,
        "Affidavit": 200,
        "Power of Attorney": 100
    },
    "Uttar Pradesh": {
        "Work Order": 0.12,
        "Contract Agreement": 0.22,
        "Tender Document": 0.06,
        "Agreement for Services": 0.18,
        "Lease/Rent Agreement": 0.28,
        "Mortgage Deed": 0.32,
        "Affidavit": 150,
        "Power of Attorney": 100
    }
}

# Default rates for other states
default_rates = {
    "Work Order": 0.1,
    "Contract Agreement": 0.2,
    "Tender Document": 0.05,
    "Agreement for Services": 0.15,
    "Lease/Rent Agreement": 0.25,
    "Mortgage Deed": 0.3,
    "Affidavit": 100,
    "Power of Attorney": 100
}

# Calculate stamp duty
if state in stamp_duty_rates:
    rate = stamp_duty_rates[state][document_type]
else:
    rate = default_rates[document_type]

if isinstance(rate, float):
    # Percentage-based calculation
    stamp_duty_amount = (rate / 100) * document_value
    rate_display = f"{rate}% of document value"
else:
    # Fixed amount
    stamp_duty_amount = rate
    rate_display = f"Fixed amount: ₹{rate}"

# Display calculation
st.subheader("🧮 Stamp Duty Calculation")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Document Value", f"₹{document_value:,.2f}")
    
with col2:
    st.metric("Applicable Rate", rate_display)
    
with col3:
    st.metric("Stamp Duty Amount", f"₹{stamp_duty_amount:,.2f}")

# Additional charges
st.subheader("💰 Additional Charges")

col1, col2, col3 = st.columns(3)

with col1:
    registration_fee = st.number_input("Registration Fee (₹)", min_value=0.0, value=1000.0, step=100.0)
    
with col2:
    processing_fee = st.number_input("Processing Fee (₹)", min_value=0.0, value=500.0, step=100.0)
    
with col3:
    miscellaneous_charges = st.number_input("Miscellaneous Charges (₹)", min_value=0.0, value=200.0, step=100.0)

# Total charges
total_charges = stamp_duty_amount + registration_fee + processing_fee + miscellaneous_charges

st.subheader("🧮 Total Charges")
col1, col2 = st.columns(2)

with col1:
    st.metric("Stamp Duty", f"₹{stamp_duty_amount:,.2f}")
    st.metric("Registration Fee", f"₹{registration_fee:,.2f}")
    st.metric("Processing Fee", f"₹{processing_fee:,.2f}")
    st.metric("Miscellaneous Charges", f"₹{miscellaneous_charges:,.2f}")
    
with col2:
    st.metric("Total Amount Payable", f"₹{total_charges:,.2f}", 
              delta=f"₹{total_charges:,.2f}")

# Payment status
if total_charges > 0:
    st.success("✅ Stamp duty and charges calculated successfully!")
else:
    st.info("ℹ️ No charges applicable for the selected document.")

# Generate payment receipt
st.subheader("🖨️ Generate Payment Receipt")

if st.button("📄 Generate Stamp Duty Receipt"):
    st.success("Stamp duty receipt generated successfully!")
    st.info("In a full implementation, this would create a downloadable PDF with the payment receipt.")

# Stamp duty rates reference
st.subheader("📋 Stamp Duty Rates Reference")
st.caption("Rates for Rajasthan (sample)")

rates_data = []
for doc_type, rate in stamp_duty_rates["Rajasthan"].items():
    if isinstance(rate, float):
        rate_display = f"{rate}%"
    else:
        rate_display = f"₹{rate}"
    rates_data.append({"Document Type": doc_type, "Rate": rate_display})

st.table(rates_data)

# Instructions
st.divider()
st.subheader("📋 Instructions")
st.markdown("""
1. Select the document type and enter its value
2. Choose the state for applicable rates
3. Review the calculated stamp duty amount
4. Add any additional charges if applicable
5. Generate a payment receipt for documentation
""")