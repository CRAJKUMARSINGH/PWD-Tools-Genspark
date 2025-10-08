import streamlit as st

st.set_page_config(page_title="Stamp Duty Calculator - PWD Tools", layout="wide")

st.title("📋 Stamp Duty Calculator")
st.caption("Calculate stamp duty for work orders and agreements")

st.info("This tool is currently under development. Please use the desktop application for full functionality.")

# Agreement details
st.subheader("📄 Agreement Information")
col1, col2 = st.columns(2)
with col1:
    agreement_type = st.selectbox("Agreement Type", 
                                ["Work Order", "Contract Agreement", "Supplementary Agreement", "Other"])
    agreement_value = st.number_input("Agreement Value (₹)", min_value=0.0, value=1000000.0, step=10000.0)
with col2:
    state = st.selectbox("State", ["Rajasthan", "Other State"])
    date = st.date_input("Agreement Date")

# Stamp duty calculation
st.subheader("🧮 Stamp Duty Calculation")
stamp_duty_rates = {
    "Rajasthan": 0.05,  # 5% for Rajasthan
    "Other State": 0.06   # 6% for other states
}

rate = stamp_duty_rates[state]
stamp_duty_amount = agreement_value * (rate / 100)

col1, col2, col3 = st.columns(3)
col1.metric("Agreement Value", f"₹ {agreement_value:,.2f}")
col2.metric("Stamp Duty Rate", f"{rate}%", "🏛️ Rate")
col3.metric("Stamp Duty Amount", f"₹ {stamp_duty_amount:,.2f}", "💰 Due")

# Payment details
st.subheader("💳 Payment Details")
payment_method = st.radio("Payment Method", ["e-Stamp", "Physical Stamp Paper", "Franking"])
if payment_method == "e-Stamp":
    st.info("e-Stamp payment can be made online through authorized agencies")
elif payment_method == "Physical Stamp Paper":
    st.info("Purchase physical stamp paper from authorized vendors")
else:
    st.info("Franking can be done at authorized banks and post offices")

# Generate button
if st.button("Calculate Stamp Duty"):
    st.success("Stamp duty calculated successfully!")
    st.info("Payment instructions and documentation will be provided here.")

st.divider()

# Instructions
st.subheader("📋 Instructions")
st.markdown("""
1. Select the agreement type and enter the agreement value
2. Choose the state where the agreement is executed
3. Review the calculated stamp duty amount
4. Select the preferred payment method
5. Complete the stamp duty payment as per instructions
""")