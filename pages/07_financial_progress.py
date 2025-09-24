import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Financial Progress Tracker - PWD Tools", layout="wide")

st.title("📈 Financial Progress Tracker")
st.caption("Track financial progress and liquidity damages")

# Project information
st.subheader("📋 Project Information")

col1, col2 = st.columns(2)

with col1:
    project_name = st.text_input("Project Name", "Road Construction Project")
    work_order_number = st.text_input("Work Order Number", "WO-2024-001")
    contractor_name = st.text_input("Contractor Name", "ABC Construction Ltd.")

with col2:
    contract_value = st.number_input("Total Contract Value (₹)", min_value=0.0, value=5000000.0, step=10000.0)
    project_start_date = st.date_input("Project Start Date", date(2023, 1, 1))
    project_end_date = st.date_input("Planned Completion Date", date(2024, 12, 31))

# Financial progress tracking
st.subheader("📊 Financial Progress")

# Initialize session state for progress entries
if 'progress_entries' not in st.session_state:
    st.session_state.progress_entries = []

# Add progress entry form
with st.form("add_progress_form"):
    st.write("➕ Add Progress Entry")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        entry_date = st.date_input("Date")
    
    with col2:
        work_completed = st.number_input("Work Completed (%)", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    
    with col3:
        amount_certified = st.number_input("Amount Certified (₹)", min_value=0.0, value=0.0, step=1000.0)
    
    with col4:
        amount_paid = st.number_input("Amount Paid (₹)", min_value=0.0, value=0.0, step=1000.0)
    
    add_entry = st.form_submit_button("➕ Add Entry")
    
    if add_entry:
        st.session_state.progress_entries.append({
            "Date": entry_date,
            "Work Completed (%)": work_completed,
            "Amount Certified (₹)": amount_certified,
            "Amount Paid (₹)": amount_paid
        })
        st.success("Progress entry added successfully!")

# Display progress entries
if st.session_state.progress_entries:
    st.subheader("📋 Progress Entries")
    progress_df = pd.DataFrame(st.session_state.progress_entries)
    st.dataframe(progress_df.style.format({
        "Work Completed (%)": "{:.2f}%",
        "Amount Certified (₹)": "₹{:,.2f}",
        "Amount Paid (₹)": "₹{:,.2f}"
    }))
    
    # Calculate totals
    total_certified = progress_df["Amount Certified (₹)"].sum()
    total_paid = progress_df["Amount Paid (₹)"].sum()
    overall_progress = progress_df["Work Completed (%)"].iloc[-1] if not progress_df.empty else 0.0
    
    # Financial summary
    st.subheader("💰 Financial Summary")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Contract Value", f"₹{contract_value:,.2f}")
    
    with col2:
        st.metric("Total Certified", f"₹{total_certified:,.2f}", 
                  delta=f"+₹{total_certified:,.2f}" if total_certified > 0 else None)
    
    with col3:
        st.metric("Total Paid", f"₹{total_paid:,.2f}", 
                  delta=f"+₹{total_paid:,.2f}" if total_paid > 0 else None)
    
    with col4:
        st.metric("Balance Due", f"₹{contract_value - total_paid:,.2f}", 
                  delta=f"-₹{contract_value - total_paid:,.2f}" if contract_value > total_paid else None)
    
    # Progress chart
    st.subheader("📊 Progress Visualization")
    if not progress_df.empty:
        chart_df = progress_df.set_index("Date")[["Work Completed (%)", "Amount Certified (₹)", "Amount Paid (₹)"]]
        st.line_chart(chart_df)
    
    # Progress status
    st.subheader("📋 Progress Status")
    progress_percentage = (total_certified / contract_value) * 100 if contract_value > 0 else 0
    time_elapsed_percentage = 50  # Simplified for this example
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Financial Progress", f"{progress_percentage:.2f}%")
        if progress_percentage >= 90:
            st.success("✅ Project nearly complete")
        elif progress_percentage >= 75:
            st.info("ℹ️ Project significantly progressed")
        else:
            st.warning("⚠️ Project progress below expectations")
    
    with col2:
        st.metric("Time Elapsed", f"{time_elapsed_percentage:.2f}%")
        if progress_percentage > time_elapsed_percentage:
            st.success("✅ Ahead of schedule")
        elif progress_percentage < time_elapsed_percentage:
            st.warning("⚠️ Behind schedule")
        else:
            st.info("ℹ️ On schedule")
    
    # Generate report
    if st.button("📄 Generate Progress Report"):
        st.success("Financial progress report generated successfully!")
        st.info("In a full implementation, this would create a downloadable PDF with the complete progress analysis.")
else:
    st.info("No progress entries added yet. Use the form above to add financial progress data.")

# Clear entries button
if st.session_state.progress_entries and st.button("🗑️ Clear All Entries"):
    st.session_state.progress_entries = []
    st.success("All progress entries cleared!")

# Instructions
st.divider()
st.subheader("📋 Instructions")
st.markdown("""
1. Enter project information in the first section
2. Add financial progress entries using the form
3. Monitor financial progress and payments
4. Analyze the project status with the provided metrics
5. Generate a progress report for documentation
""")