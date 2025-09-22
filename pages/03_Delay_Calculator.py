import streamlit as st
from datetime import datetime


st.set_page_config(page_title="Delay Calculator", layout="centered")

st.title("⏰ Project Delay Calculator")
st.caption("Compute start/completion delays and penalties")

with st.form("delay_form"):
	project_name = st.text_input("Project Name")
	contractor_name = st.text_input("Contractor Name")
	col1, col2 = st.columns(2)
	with col1:
		planned_start = st.date_input("Planned Start")
		planned_completion = st.date_input("Planned Completion")
	with col2:
		actual_start = st.date_input("Actual Start", value=None, format="YYYY-MM-DD")
		actual_completion = st.date_input("Actual Completion", value=None, format="YYYY-MM-DD")
	contract_amount = st.number_input("Contract Amount (₹)", min_value=0.0, step=1000.0)
	penalty_rate = st.number_input("Penalty Rate (% per day)", min_value=0.0, value=0.05, step=0.01)
	submitted = st.form_submit_button("🧮 Calculate Delay")

if submitted:
	current_date = datetime.now().date()
	start_delay_days = 0
	if actual_start:
		start_delay_days = max(0, (actual_start - planned_start).days)

	if actual_completion:
		completion_delay_days = max(0, (actual_completion - planned_completion).days)
		project_status = "Completed"
		status_color = "green" if completion_delay_days == 0 else "red"
	else:
		completion_delay_days = max(0, (current_date - planned_completion).days)
		project_status = "Ongoing"
		status_color = "orange" if completion_delay_days > 0 else "green"

	total_delay_days = start_delay_days + completion_delay_days
	penalty_amount = 0.0
	if completion_delay_days > 0:
		daily_penalty = (contract_amount * penalty_rate) / 100.0
		penalty_amount = daily_penalty * completion_delay_days

	planned_duration = (planned_completion - planned_start).days
	if actual_start and actual_completion:
		actual_duration = (actual_completion - actual_start).days
	elif actual_start:
		actual_duration = (current_date - actual_start).days
	else:
		actual_duration = 0

	st.success("Calculation complete")
	colA, colB, colC = st.columns(3)
	with colA:
		st.metric("Start Delay", f"{start_delay_days} days")
	with colB:
		st.metric("Completion Delay", f"{completion_delay_days} days")
	with colC:
		st.metric("Total Delay", f"{total_delay_days} days")
	st.metric("Penalty Amount", f"₹ {penalty_amount:,.2f}")
	st.markdown(f"**Status:** <span style='color:{status_color}'>{project_status}</span>", unsafe_allow_html=True)

	with st.expander("Timeline Details"):
		st.json({
			"project_name": project_name,
			"contractor_name": contractor_name,
			"planned_duration_days": planned_duration,
			"actual_duration_days": actual_duration,
			"delay_days": total_delay_days,
			"penalty_amount": penalty_amount,
		})


