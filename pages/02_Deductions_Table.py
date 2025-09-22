import streamlit as st


st.set_page_config(page_title="Deductions Table", layout="centered")

st.title("📊 Deductions Table Calculator")
st.caption("Calculate TDS, Security, and other deductions")

with st.form("deductions_form"):
	bill_number = st.text_input("Bill Number")
	contractor_name = st.text_input("Contractor Name")
	gross_amount = st.number_input("Gross Amount (₹)", min_value=0.0, step=100.0)
	col1, col2, col3 = st.columns(3)
	with col1:
		tds_rate = st.number_input("TDS Rate (%)", min_value=0.0, value=2.0, step=0.1)
	with col2:
		security_rate = st.number_input("Security Deduction (%)", min_value=0.0, value=5.0, step=0.1)
	with col3:
		other_deductions = st.number_input("Other Deductions (₹)", min_value=0.0, value=0.0, step=50.0)
	work_description = st.text_area("Work Description", placeholder="Brief description")
	submitted = st.form_submit_button("🧮 Calculate Deductions")

if submitted:
	tds_amount = (gross_amount * tds_rate) / 100.0
	security_deduction = (gross_amount * security_rate) / 100.0
	total_deductions = tds_amount + security_deduction + other_deductions
	net_amount = gross_amount - total_deductions

	st.success("Calculation complete")
	colA, colB, colC = st.columns(3)
	with colA:
		st.metric("TDS", f"₹ {tds_amount:,.2f}")
	with colB:
		st.metric("Security Deduction", f"₹ {security_deduction:,.2f}")
	with colC:
		st.metric("Total Deductions", f"₹ {total_deductions:,.2f}")
	st.metric("Net Amount Payable", f"₹ {net_amount:,.2f}")

	with st.expander("Calculation Details"):
		st.json({
			"bill_number": bill_number,
			"contractor_name": contractor_name,
			"gross_amount": gross_amount,
			"tds_rate": tds_rate,
			"tds_amount": tds_amount,
			"security_rate": security_rate,
			"security_deduction": security_deduction,
			"other_deductions": other_deductions,
			"total_deductions": total_deductions,
			"net_amount": net_amount,
			"work_description": work_description,
		})


