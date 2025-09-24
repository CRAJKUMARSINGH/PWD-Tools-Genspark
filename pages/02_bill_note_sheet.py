import streamlit as st
import pandas as pd

st.set_page_config(page_title="Bill Note Sheet - PWD Tools", layout="wide")

st.title("📝 Bill Note Sheet Generator")
st.caption("Create running and final bills with standardized PWD formats")

# Bill information
st.subheader("📋 Bill Information")
col1, col2 = st.columns(2)

with col1:
    bill_type = st.selectbox("Bill Type", ["Running Bill", "Final Bill"])
    bill_number = st.text_input("Bill Number", "BILL-001")
    work_order = st.text_input("Work Order Number", "WO-2024-001")

with col2:
    bill_date = st.date_input("Bill Date")
    agency_name = st.text_input("Agency Name", "Public Works Department")
    work_description = st.text_area("Work Description", "Construction of Road Infrastructure")

# Items table
st.subheader("🧮 Bill Items")
if 'items' not in st.session_state:
    st.session_state.items = []

# Add item form
with st.form("add_item_form"):
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        item_description = st.text_input("Item Description")
    
    with col2:
        quantity = st.number_input("Quantity", min_value=0.0, step=0.1)
    
    with col3:
        rate = st.number_input("Rate per Unit", min_value=0.0, step=0.1)
    
    with col4:
        unit = st.text_input("Unit", "Nos")
    
    add_item = st.form_submit_button("➕ Add Item")
    
    if add_item:
        if item_description and quantity > 0 and rate > 0:
            item_total = quantity * rate
            st.session_state.items.append({
                "Description": item_description,
                "Quantity": quantity,
                "Unit": unit,
                "Rate": rate,
                "Total": item_total
            })
            st.success("Item added successfully!")
        else:
            st.error("Please fill all fields with valid values")

# Display items
if st.session_state.items:
    st.subheader("📋 Added Items")
    items_df = pd.DataFrame(st.session_state.items)
    st.dataframe(items_df)
    
    # Calculate totals
    total_amount = items_df["Total"].sum()
    
    st.subheader("💰 Bill Summary")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Items", len(st.session_state.items))
    
    with col2:
        st.metric("Total Amount", f"₹{total_amount:,.2f}")
    
    with col3:
        st.metric("Bill Type", bill_type)
    
    # Generate bill button
    if st.button("🖨️ Generate Bill Document"):
        st.success("Bill document generated successfully!")
        st.info("In a full implementation, this would create a downloadable PDF with the PWD bill format.")
else:
    st.info("No items added yet. Use the form above to add bill items.")

# Clear items button
if st.session_state.items and st.button("🗑️ Clear All Items"):
    st.session_state.items = []
    st.success("All items cleared!")
    
# Instructions
st.divider()
st.subheader("📋 Instructions")
st.markdown("""
1. Fill in the bill information in the top section
2. Add items using the form (description, quantity, rate, unit)
3. Review the added items in the table
4. Generate the bill document when ready
""")