import streamlit as st
import pandas as pd
import sqlite3
import os
from datetime import datetime
import base64

# Set page config
st.set_page_config(
    page_title="PWD Tools - Dashboard",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #2E8B57 0%, #3CB371 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
    }
    .tool-card {
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        background-color: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: transform 0.2s;
    }
    .tool-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    .tool-icon {
        font-size: 2rem;
        margin-bottom: 1rem;
    }
    .footer {
        text-align: center;
        padding: 1rem;
        background-color: #2E8B57;
        color: white;
        border-radius: 5px;
        margin-top: 2rem;
    }
    .stats-card {
        background: linear-gradient(135deg, #4ECDC4 0%, #44A08D 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for tools
if 'current_tool' not in st.session_state:
    st.session_state.current_tool = None

# Database initialization
def init_database():
    conn = sqlite3.connect('pwd_tools_streamlit.db')
    cursor = conn.cursor()
    
    # Create tables for each tool
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hindi_bills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bill_type TEXT,
            work_order_amount REAL,
            upto_date_amount REAL,
            extra_items TEXT,
            extra_amount REAL,
            start_date TEXT,
            completion_date TEXT,
            actual_completion TEXT,
            repair_work TEXT,
            excess_quantity TEXT,
            delay_comment TEXT,
            generated_note TEXT,
            date_created TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stamp_duty_calculations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            work_order_amount REAL,
            stamp_duty_amount REAL,
            date_created TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS emd_refund_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            payee_name TEXT,
            amount REAL,
            work_description TEXT,
            refund_date TEXT,
            date_created TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS delay_calculations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_name TEXT,
            planned_start_date TEXT,
            actual_start_date TEXT,
            planned_completion_date TEXT,
            actual_completion_date TEXT,
            delay_days INTEGER,
            delay_reason TEXT,
            penalty_amount REAL,
            date_created TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS financial_analysis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_name TEXT,
            budget_amount REAL,
            spent_amount REAL,
            remaining_amount REAL,
            completion_percentage REAL,
            start_date TEXT,
            end_date TEXT,
            analysis_date TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

# Initialize database
init_database()

# Main header
st.markdown("""
<div class="main-header">
    <h1>🏗️ PWD Tools Dashboard</h1>
    <p style="font-size: 1.2rem;">Infrastructure Management Suite for Lower Divisional Clerks</p>
</div>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🧭 Navigation")
if st.sidebar.button("🏠 Home Dashboard"):
    st.session_state.current_tool = None

st.sidebar.markdown("---")
st.sidebar.subheader("🛠️ Available Tools")

# Tool buttons in sidebar
tools = [
    {"name": "📝 Hindi Bill Note", "icon": "📝", "key": "hindi_bill"},
    {"name": "💰 Stamp Duty Calculator", "icon": "💰", "key": "stamp_duty"},
    {"name": "💳 EMD Refund", "icon": "💳", "key": "emd_refund"},
    {"name": "⏰ Delay Calculator", "icon": "⏰", "key": "delay_calculator"},
    {"name": "📊 Financial Analysis", "icon": "📊", "key": "financial_analysis"},
]

for tool in tools:
    if st.sidebar.button(f"{tool['icon']} {tool['name']}"):
        st.session_state.current_tool = tool['key']

st.sidebar.markdown("---")
st.sidebar.info("All tools work offline and are optimized for ease of use.")

# Main content area
if st.session_state.current_tool is None:
    # Dashboard view
    st.markdown("## 🎉 Welcome to PWD Tools - Simple & Efficient!")
    st.markdown("Select a tool from the sidebar to get started.")
    
    # Stats cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="stats-card">
            <h3>6</h3>
            <p>Available Tools</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stats-card">
            <h3>100%</h3>
            <p>Offline Functionality</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stats-card">
            <h3>0</h3>
            <p>Web Dependencies</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Tool cards
    st.markdown("## 🛠️ Available Tools")
    
    for i in range(0, len(tools), 2):
        cols = st.columns(2)
        for j in range(2):
            if i + j < len(tools):
                tool = tools[i + j]
                with cols[j]:
                    st.markdown(f"""
                    <div class="tool-card">
                        <div class="tool-icon">{tool['icon']}</div>
                        <h3>{tool['name']}</h3>
                        <p>Simple and efficient tool for PWD operations</p>
                    </div>
                    """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div class="footer">
        <p>Version 1.0.0 | Prepared for Mrs. Premlata Jain, AAO, PWD Udaipur</p>
        <p>Simple, Efficient, and User-Friendly</p>
    </div>
    """, unsafe_allow_html=True)

else:
    # Tool specific views
    if st.session_state.current_tool == "hindi_bill":
        st.markdown("## 📝 Hindi Bill Note Generator")
        st.markdown("Generate running and final bills in Hindi")
        
        # Form for Hindi Bill Note
        bill_type = st.radio("बिल का प्रकार", ["रनिंग बिल", "फाइनल बिल"])
        
        work_order_amount = st.number_input("वर्क ऑर्डर राशि (₹)", min_value=0.0, step=1000.0)
        upto_date_amount = st.number_input("अब तक की बिल राशि (₹)", min_value=0.0, step=1000.0)
        extra_items = st.radio("Extra Items शामिल:", ["नहीं", "हाँ"])
        extra_amount = st.number_input("Extra Items राशि (₹):", min_value=0.0, step=1000.0, value=0.0)
        
        if bill_type == "फाइनल बिल":
            start_date = st.date_input("प्रारंभ तिथि")
            schedule_completion = st.date_input("निर्धारित समापन तिथि")
            actual_completion = st.date_input("वास्तविक समापन तिथि")
            repair_work = st.radio("मरम्मत कार्य:", ["नहीं", "हाँ"])
            excess_quantity = st.radio("अधिक मात्रा (Excess Quantity):", ["नहीं", "हाँ"])
            delay_comment = st.radio("बिल देर से जमा (>6 माह):", ["नहीं", "हाँ"])
        
        if st.button("नोट शीट जनरेट करें"):
            # Calculate percentage
            percentage_work_done = (upto_date_amount / work_order_amount) * 100 if work_order_amount > 0 else 0
            
            # Generate note
            note = ""
            serial_number = 1
            
            if bill_type == "रनिंग बिल":
                note += f"{serial_number}. इस Stage में कार्य {percentage_work_done:.2f}% संपादित हुआ है।\n"
                serial_number += 1
                note += f"{serial_number}. कार्य प्रगति पर है।\n"
                serial_number += 1
                
                if extra_items == "हाँ":
                    extra_percentage = (extra_amount / work_order_amount) * 100 if work_order_amount > 0 else 0
                    if extra_percentage > 5:
                        note += f"{serial_number}. ₹{extra_amount:.2f} की Extra Items कार्यान्वित किए गए हैं, जो वर्क ऑर्डर राशि का {extra_percentage:.2f}% है, जो 5% से अधिक है। जिसकी स्वीकृति Superintending Engineer, Electric Circle Udaipur कार्यालय के क्षेत्राधिकार में है।\n"
                    elif extra_percentage == 5:
                        note += f"{serial_number}. ₹{extra_amount:.2f} की Extra Items कार्यान्वित किए गए हैं, जो वर्क ऑर्डर राशि का {extra_percentage:.2f}% है, जो 5% के बराबर है। जिसकी स्वीकृति इस कार्यालय के क्षेत्राधिकार में है।\n"
                    else:
                        note += f"{serial_number}. ₹{extra_amount:.2f} की Extra Items कार्यान्वित किए गए हैं, जो वर्क ऑर्डर राशि का {extra_percentage:.2f}% है, जो 5% से कम है। जिसकी स्वीकृति इस कार्यालय के क्षेत्राधिकार में है।\n"
                    serial_number += 1
                
                note += f"{serial_number}. उपरोक्त विवरण के सन्दर्भ में समुचित निर्णय हेतु प्रस्तुत है।"
            
            else:  # Final bill
                note += f"{serial_number}. कार्य {percentage_work_done:.2f}% पूर्ण हुआ है।\n"
                serial_number += 1
                
                # Work completion percentage logic
                if percentage_work_done < 90:
                    note += f"{serial_number}. कार्य का वांछित Deviation Statement भी स्वीकृति हेतु प्राप्त हुआ है, जिसकी स्वीकृति इसी कार्यालय के क्षेत्राधिकार में निहित है।\n"
                    serial_number += 1
                elif percentage_work_done > 90 and percentage_work_done <= 100:
                    note += f"{serial_number}. कार्य पूर्णता का प्रतिशत ({percentage_work_done:.2f}%) 90% से अधिक किंतु 100% तक है।\n"
                    serial_number += 1
                elif percentage_work_done == 100:
                    note += f"{serial_number}. कार्य ({percentage_work_done:.2f}%) पूर्ण हुआ है।\n"
                    serial_number += 1
                elif percentage_work_done > 100 and percentage_work_done <= 105:
                    note += f"{serial_number}. कार्य का वांछित Deviation Statement भी स्वीकृति हेतु प्राप्त हुआ है, Overall Excess कार्य की मात्रा 5% से कम/बराबर है, जिसकी स्वीकृति इसी कार्यालय के क्षेत्राधिकार में निहित है।\n"
                    serial_number += 1
                elif percentage_work_done > 105:
                    note += f"{serial_number}. कार्य का वांछित Deviation Statement भी स्वीकृति हेतु प्राप्त हुआ है, Overall Excess कार्य की मात्रा 5% से अधिक है, जिसकी स्वीकृति Superintending Engineer, PWD Electric Circle, Udaipur के क्षेत्राधिकार में निहित है।\n"
                    serial_number += 1
                
                # Delay calculation
                if start_date and schedule_completion and actual_completion:
                    delay_days = (actual_completion - schedule_completion).days
                    if actual_completion > schedule_completion:
                        note += f"{serial_number}. कार्य में {delay_days} दिन की देरी हुई है।\n"
                        serial_number += 1
                        
                        schedule_duration = (schedule_completion - start_date).days
                        if delay_days > (schedule_duration / 2 + 1):
                            note += f"{serial_number}. Time Extension केस Superintending Engineer, Electric Circle, Udaipur कार्यालय द्वारा अनुमोदित किया जाना है।\n"
                        else:
                            note += f"{serial_number}. Time Extension केस इस कार्यालय द्वारा अनुमोदित किया जाना है।\n"
                        serial_number += 1
                    else:
                        note += f"{serial_number}. कार्य समय पर संपादित हुआ है।\n"
                        serial_number += 1
                
                # Extra items
                if extra_items == "हाँ":
                    extra_percentage = (extra_amount / work_order_amount) * 100 if work_order_amount > 0 else 0
                    if extra_percentage > 5:
                        note += f"{serial_number}. ₹{extra_amount:.2f} की Extra Items कार्यान्वित किए गए हैं, जो वर्क ऑर्डर राशि का {extra_percentage:.2f}% है, जो 5% से अधिक है। जिसकी स्वीकृति Superintending Engineer, Electric Circle, Udaipur कार्यालय के क्षेत्राधिकार में है।\n"
                    elif extra_percentage == 5:
                        note += f"{serial_number}. ₹{extra_amount:.2f} की Extra Items कार्यान्वित किए गए हैं, जो वर्क ऑर्डर राशि का {extra_percentage:.2f}% है, अथवा (5% के बराबर है)। जिसकी स्वीकृति इस कार्यालय के क्षेत्राधिकार में है।\n"
                    else:
                        note += f"{serial_number}. ₹{extra_amount:.2f} की Extra Items कार्यान्वित किए गए हैं, जो वर्क ऑर्डर राशि का {extra_percentage:.2f}% है, जो 5% से कम है। जिसकी स्वीकृति इस कार्यालय के क्षेत्राधिकार में है।\n"
                    serial_number += 1
                
                # Excess quantity
                if excess_quantity == "हाँ":
                    note += f"{serial_number}. Work Order के कुछ आइटम में अतिरिक्त मात्रा (Excess Quantity) संपादित की गई है। इसके लिए Deviation Statement भी स्वीकृति हेतु प्राप्त हुआ है।\n"
                    serial_number += 1
                
                # Quality control
                note += f"{serial_number}. गुणवत्ता नियंत्रण (Q.C.) परीक्षण रिपोर्ट (Test Reports) संलग्न हैं।\n"
                serial_number += 1
                
                # Hand over statement
                if repair_work == "नहीं":
                    note += f"{serial_number}. हस्तांतरण विवरण Hand Over Statement संलग्न है।\n"
                    serial_number += 1
                
                # Delay comment
                if delay_comment == "हाँ":
                    note += f"{serial_number}. कार्य समाप्ति के करीब 6 महीने बाद फाइनल बिल इस कार्यालय में प्रस्तुत किया गया है। इस अप्रत्याशित देरी के लिए सहायक अभियंता से स्पष्टीकरण मांगा जाए, ऐसी प्रस्तावना है।\n"
                    serial_number += 1
                
                note += f"{serial_number}. उचित निर्णय के लिए उपर्युक्त विवरण संलग्न है।"
            
            st.text_area("Generated Note", note, height=300)
            
            # Save to database
            conn = sqlite3.connect('pwd_tools_streamlit.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO hindi_bills (
                    bill_type, work_order_amount, upto_date_amount, extra_items, extra_amount,
                    start_date, completion_date, actual_completion, repair_work, excess_quantity,
                    delay_comment, generated_note, date_created
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                bill_type,
                work_order_amount,
                upto_date_amount,
                extra_items,
                extra_amount,
                str(start_date) if bill_type == "फाइनल बिल" else "",
                str(schedule_completion) if bill_type == "फाइनल बिल" else "",
                str(actual_completion) if bill_type == "फाइनल बिल" else "",
                repair_work if bill_type == "फाइनल बिल" else "",
                excess_quantity if bill_type == "फाइनल बिल" else "",
                delay_comment if bill_type == "फाइनल बिल" else "",
                note,
                datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            ))
            conn.commit()
            conn.close()
            
            st.success("Note generated and saved successfully!")
    
    elif st.session_state.current_tool == "stamp_duty":
        st.markdown("## 💰 Stamp Duty Calculator")
        st.markdown("Calculate stamp duty with predefined rates")
        
        work_order_amount = st.number_input("Enter Work Order Amount (₹):", min_value=0.0, step=1000.0)
        
        if st.button("Calculate Stamp Duty"):
            if work_order_amount <= 0:
                st.error("Work Order Amount must be greater than 0")
            else:
                # Calculate stamp duty based on original repository logic
                if work_order_amount <= 5000000:
                    stamp_duty = 1000
                else:
                    stamp_duty = round(work_order_amount * 0.0015)
                    if stamp_duty > 2500000:
                        stamp_duty = 2500000
                
                st.markdown(f"## 📋 Stamp Duty Amount: ₹ {stamp_duty:,}")
                
                # Save to database
                conn = sqlite3.connect('pwd_tools_streamlit.db')
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO stamp_duty_calculations (
                        work_order_amount, stamp_duty_amount, date_created
                    ) VALUES (?, ?, ?)
                ''', (
                    work_order_amount,
                    stamp_duty,
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                ))
                conn.commit()
                conn.close()
                
                st.success("Calculation completed and saved!")
    
    elif st.session_state.current_tool == "emd_refund":
        st.markdown("## 💳 EMD Refund")
        st.markdown("Simple EMD refund with 3 inputs only")
        
        payee_name = st.text_input("1. Payee Name:")
        amount = st.number_input("2. Amount (₹):", min_value=0.0, step=1000.0)
        work_description = st.text_input("3. Work Description:")
        
        if st.button("Generate EMD Refund Receipt"):
            if not all([payee_name, amount > 0, work_description]):
                st.error("Please fill all 3 fields: Payee Name, Amount, and Work Description")
            else:
                # Generate receipt
                receipt = f"""
EMD REFUND RECEIPT
==================

Receipt No: EMD-{datetime.now().strftime('%Y%m%d%H%M%S')}
Date: {datetime.now().strftime('%d/%m/%Y')}
Time: {datetime.now().strftime('%H:%M:%S')}

PAYEE DETAILS
=============
Payee Name: {payee_name}
Amount: ₹ {amount:,.2f}
Work Description: {work_description}

REFUND DETAILS
==============
Refund Amount: ₹ {amount:,.2f}
Refund Status: APPROVED
Refund Date: {datetime.now().strftime('%d/%m/%Y')}

AUTHORIZATION
=============
Authorized by: PWD Office
Processed by: Lower Divisional Clerk
Date: {datetime.now().strftime('%d/%m/%Y')}

NOTES
=====
This is an EMD (Earnest Money Deposit) refund receipt.
Amount will be processed within 7 working days.

---
Generated by PWD Tools - Simple Version
For Lower Divisional Clerks
"""
                
                st.text_area("EMD Refund Receipt", receipt, height=400)
                
                # Save to database
                conn = sqlite3.connect('pwd_tools_streamlit.db')
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO emd_refund_records (
                        payee_name, amount, work_description, refund_date, date_created
                    ) VALUES (?, ?, ?, ?, ?)
                ''', (
                    payee_name,
                    amount,
                    work_description,
                    datetime.now().strftime('%d/%m/%Y'),
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                ))
                conn.commit()
                conn.close()
                
                st.success("Receipt generated and saved successfully!")
    
    elif st.session_state.current_tool == "delay_calculator":
        st.markdown("## ⏰ Delay Calculator")
        st.markdown("Calculate project delays easily")
        
        project_name = st.text_input("Project Name:")
        planned_start = st.date_input("Planned Start Date:")
        actual_start = st.date_input("Actual Start Date:")
        planned_completion = st.date_input("Planned Completion Date:")
        actual_completion = st.date_input("Actual Completion Date:")
        delay_reason = st.text_area("Delay Reason (Optional):")
        
        if st.button("Calculate Delay"):
            if not project_name:
                st.error("Please enter project name")
            elif not all([planned_start, actual_start, planned_completion, actual_completion]):
                st.error("Please fill all date fields")
            else:
                # Calculate delays
                start_delay = (actual_start - planned_start).days
                completion_delay = (actual_completion - planned_completion).days
                total_delay = completion_delay
                
                # Calculate project duration
                planned_duration = (planned_completion - planned_start).days
                actual_duration = (actual_completion - actual_start).days
                
                # Generate analysis
                analysis = f"""
DELAY CALCULATION REPORT
========================

Project Name: {project_name}
Analysis Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}

SCHEDULE ANALYSIS
=================
Planned Start: {planned_start.strftime('%d/%m/%Y')}
Actual Start: {actual_start.strftime('%d/%m/%Y')}
Start Delay: {start_delay} days

Planned Completion: {planned_completion.strftime('%d/%m/%Y')}
Actual Completion: {actual_completion.strftime('%d/%m/%Y')}
Completion Delay: {completion_delay} days

PROJECT DURATION
================
Planned Duration: {planned_duration} days
Actual Duration: {actual_duration} days
Duration Difference: {actual_duration - planned_duration} days

DELAY SUMMARY
=============
Total Delay: {total_delay} days
Delay Status: {'DELAYED' if total_delay > 0 else 'ON TIME' if total_delay == 0 else 'EARLY'}

DELAY ANALYSIS
==============
"""
                
                if total_delay > 0:
                    analysis += f"⚠️  PROJECT DELAYED by {total_delay} days\n"
                    if total_delay > 30:
                        analysis += "🔴  MAJOR DELAY - Requires immediate attention\n"
                    elif total_delay > 15:
                        analysis += "🟡  MODERATE DELAY - Monitor closely\n"
                    else:
                        analysis += "🟢  MINOR DELAY - Within acceptable limits\n"
                elif total_delay == 0:
                    analysis += "✅  PROJECT COMPLETED ON TIME\n"
                else:
                    analysis += f"🎉  PROJECT COMPLETED EARLY by {abs(total_delay)} days\n"
                
                if delay_reason:
                    analysis += f"\nDelay Reason: {delay_reason}\n"
                
                # Penalty calculation (simple)
                if total_delay > 0:
                    penalty_rate = 0.1  # 0.1% per day
                    analysis += f"\nPENALTY CALCULATION\n"
                    analysis += f"===================\n"
                    analysis += f"Delay Days: {total_delay}\n"
                    analysis += f"Penalty Rate: {penalty_rate}% per day\n"
                    analysis += f"Note: Actual penalty calculation depends on contract terms\n"
                
                analysis += f"\nRECOMMENDATIONS\n"
                analysis += f"===============\n"
                if total_delay > 0:
                    analysis += f"• Review project timeline and resource allocation\n"
                    analysis += f"• Implement corrective measures for future projects\n"
                    analysis += f"• Document delay reasons for future reference\n"
                else:
                    analysis += f"• Maintain current project management practices\n"
                    analysis += f"• Use this project as a benchmark for future planning\n"
                
                st.text_area("Delay Calculation Results", analysis, height=500)
                
                # Save to database
                conn = sqlite3.connect('pwd_tools_streamlit.db')
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO delay_calculations (
                        project_name, planned_start_date, actual_start_date, 
                        planned_completion_date, actual_completion_date, 
                        delay_days, delay_reason, penalty_amount, date_created
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    project_name,
                    planned_start.strftime('%d/%m/%Y'),
                    actual_start.strftime('%d/%m/%Y'),
                    planned_completion.strftime('%d/%m/%Y'),
                    actual_completion.strftime('%d/%m/%Y'),
                    total_delay,
                    delay_reason,
                    0.0,  # Simple penalty calculation
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                ))
                conn.commit()
                conn.close()
                
                st.success("Calculation completed and saved!")
    
    elif st.session_state.current_tool == "financial_analysis":
        st.markdown("## 📊 Financial Analysis")
        st.markdown("Simple financial analysis with calendar")
        
        project_name = st.text_input("Project Name:")
        budget_amount = st.number_input("Budget Amount (₹):", min_value=0.0, step=1000.0)
        spent_amount = st.number_input("Spent Amount (₹):", min_value=0.0, step=1000.0)
        start_date = st.date_input("Project Start Date:")
        end_date = st.date_input("Project End Date:")
        
        if st.button("Analyze Financial Status"):
            if not project_name:
                st.error("Please enter project name")
            elif budget_amount <= 0 or spent_amount < 0:
                st.error("Please enter valid amounts")
            else:
                # Calculate financial metrics
                remaining_amount = budget_amount - spent_amount
                completion_percentage = (spent_amount / budget_amount) * 100 if budget_amount > 0 else 0
                budget_utilization = completion_percentage
                
                # Calculate project duration
                duration_days = (end_date - start_date).days if start_date and end_date else 0
                
                # Generate analysis
                analysis = f"""
FINANCIAL ANALYSIS REPORT
========================

Project Name: {project_name}
Analysis Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}

BUDGET ANALYSIS
===============
Budget Amount: ₹ {budget_amount:,.2f}
Spent Amount: ₹ {spent_amount:,.2f}
Remaining Amount: ₹ {remaining_amount:,.2f}

PERFORMANCE METRICS
===================
Budget Utilization: {budget_utilization:.2f}%
Completion Status: {'Over Budget' if spent_amount > budget_amount else 'Within Budget'}

PROJECT TIMELINE
================
Start Date: {start_date.strftime('%d/%m/%Y') if start_date else 'Not specified'}
End Date: {end_date.strftime('%d/%m/%Y') if end_date else 'Not specified'}
Duration: {duration_days} days

FINANCIAL STATUS
================
"""
                
                if spent_amount > budget_amount:
                    analysis += f"⚠️  OVER BUDGET by ₹ {abs(remaining_amount):,.2f}\n"
                    analysis += "Recommendation: Review expenses and seek additional funding\n"
                elif budget_utilization > 90:
                    analysis += f"⚠️  HIGH BUDGET UTILIZATION ({budget_utilization:.2f}%)\n"
                    analysis += "Recommendation: Monitor expenses closely\n"
                elif budget_utilization > 75:
                    analysis += f"✅  MODERATE BUDGET UTILIZATION ({budget_utilization:.2f}%)\n"
                    analysis += "Recommendation: Continue current spending pattern\n"
                else:
                    analysis += f"✅  LOW BUDGET UTILIZATION ({budget_utilization:.2f}%)\n"
                    analysis += "Recommendation: Consider accelerating project activities\n"
                
                if remaining_amount > 0:
                    analysis += f"\nRemaining Budget: ₹ {remaining_amount:,.2f} available for completion\n"
                else:
                    analysis += f"\nBudget Exceeded: ₹ {abs(remaining_amount):,.2f} over budget\n"
                
                st.text_area("Financial Analysis Results", analysis, height=500)
                
                # Save to database
                conn = sqlite3.connect('pwd_tools_streamlit.db')
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO financial_analysis (
                        project_name, budget_amount, spent_amount, remaining_amount,
                        completion_percentage, start_date, end_date, analysis_date
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    project_name,
                    budget_amount,
                    spent_amount,
                    remaining_amount,
                    budget_utilization,
                    start_date.strftime('%d/%m/%Y') if start_date else "",
                    end_date.strftime('%d/%m/%Y') if end_date else "",
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                ))
                conn.commit()
                conn.close()
                
                st.success("Analysis completed and saved!")