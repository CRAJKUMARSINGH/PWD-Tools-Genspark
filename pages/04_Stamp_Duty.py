import streamlit as st


st.set_page_config(page_title="Stamp Duty", layout="centered")

st.title("📋 Stamp Duty Calculator")
st.caption("Compute stamp duty for work orders")

with st.form("stamp_form"):
	work_order_number = st.text_input("Work Order Number")
	contractor_name = st.text_input("Contractor Name")
	work_description = st.text_area("Work Description")
	contract_value = st.number_input("Contract Value (₹)", min_value=0.0, step=1000.0)
	stamp_duty_rate = st.number_input("Stamp Duty Rate (%)", min_value=0.0, value=0.1, step=0.05)
	submitted = st.form_submit_button("🧮 Calculate Stamp Duty")

if submitted:
	stamp_duty_amount = (contract_value * stamp_duty_rate) / 100.0
	st.success("Calculation complete")
	st.metric("Stamp Duty Amount", f"₹ {stamp_duty_amount:,.2f}")
	with st.expander("Details"):
		st.json({
			"work_order_number": work_order_number,
			"contractor_name": contractor_name,
			"work_description": work_description,
			"contract_value": contract_value,
			"stamp_duty_rate": stamp_duty_rate,
			"stamp_duty_amount": stamp_duty_amount,
		})


