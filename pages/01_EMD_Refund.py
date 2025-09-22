import streamlit as st
from datetime import datetime


st.set_page_config(page_title="EMD Refund", layout="centered")

st.title("💰 EMD Refund Calculator & Generator")
st.caption("Calculate eligibility, penalties, and refund amount")

with st.form("emd_form"):
	tender_number = st.text_input("Tender Number", placeholder="e.g., TN-2025-001")
	contractor_name = st.text_input("Contractor Name")
	emd_amount = st.number_input("EMD Amount (₹)", min_value=0.0, step=100.0)
	col1, col2, col3 = st.columns(3)
	with col1:
		bank_name = st.text_input("Bank Name", placeholder="e.g., SBI")
	with col2:
		guarantee_number = st.text_input("Guarantee Number", placeholder="if applicable")
	with col3:
		validity_date = st.date_input("Validity Date")
	submitted = st.form_submit_button("🧮 Calculate Refund")

if submitted:
	current_date = datetime.now().date()
	days_difference = (current_date - validity_date).days
	if validity_date >= current_date:
		refund_amount = emd_amount
		status = "Eligible for Full Refund"
		status_color = "green"
		penalty = 0.0
	elif days_difference <= 30:
		penalty = emd_amount * 0.10
		refund_amount = emd_amount - penalty
		status = f"Eligible for Refund with 10% penalty ({days_difference} days late)"
		status_color = "orange"
	elif days_difference <= 90:
		penalty = emd_amount * 0.50
		refund_amount = emd_amount - penalty
		status = f"Eligible for 50% Refund ({days_difference} days late)"
		status_color = "red"
	else:
		penalty = emd_amount
		refund_amount = 0.0
		status = f"Not eligible for refund ({days_difference} days expired)"
		status_color = "red"

	st.success("Calculation complete")
	st.metric("Original EMD", f"₹ {emd_amount:,.2f}")
	colA, colB, colC = st.columns(3)
	with colA:
		st.metric("Penalty", f"₹ {penalty:,.2f}")
	with colB:
		st.metric("Refund Amount", f"₹ {refund_amount:,.2f}")
	with colC:
		st.markdown(f"**Status:** <span style='color:{status_color}'>{status}</span>", unsafe_allow_html=True)

	# Simple record preview
	with st.expander("Preview Details"):
		st.json({
			"tender_number": tender_number,
			"contractor_name": contractor_name,
			"emd_amount": emd_amount,
			"bank_name": bank_name,
			"guarantee_number": guarantee_number,
			"validity_date": str(validity_date),
			"refund_amount": refund_amount,
			"status": status,
			"penalty": penalty,
			"days_difference": days_difference,
		})


