import streamlit as st
import time
import subprocess
import sys
import os

# Page configuration
st.set_page_config(
    page_title="PWD Tools Hub | Infrastructure Management Suite",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
/* Main app styling */
.main > div {
    padding-top: 0rem;
}

/* Header styling with green gradient */
.header-container {
    background: linear-gradient(135deg, #2E8B57 0%, #90EE90 100%);
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 20px;
    color: white;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

/* Tool button styling */
.tool-card {
    background: linear-gradient(135deg, #f0f8f5 0%, #e8f5e8 100%);
    border: 2px solid #2E8B57;
    border-radius: 15px;
    padding: 20px;
    margin: 10px;
    text-align: center;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    min-height: 150px;
}

.tool-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    border-color: #228B22;
}

/* Metric styling */
.metric-container {
    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    padding: 15px;
    border-radius: 10px;
    border-left: 4px solid #2E8B57;
}

/* Credits styling */
.credits {
    background: linear-gradient(135deg, #2E8B57 0%, #3CB371 100%);
    color: white;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    margin-top: 20px;
}

/* Button styling */
.stButton > button {
    width: 100%;
    background-color: #2E8B57;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
    font-weight: bold;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    background-color: #228B22;
    transform: translateY(-1px);
}

/* Stats card styling */
.stats-card {
    background: linear-gradient(135deg, #4ECDC4 0%, #44A08D 100%);
    padding: 1rem;
    border-radius: 10px;
    color: white;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state for navigation
if 'current_tool' not in st.session_state:
    st.session_state.current_tool = None

# Show header with branding
st.markdown("""
<div class="header-container">
    <h1>🏗️ PWD Tools Hub</h1>
    <h3>Infrastructure Management Suite</h3>
    <p>Simple tools for PWD operations - Designed for Lower Divisional Clerks</p>
</div>
""", unsafe_allow_html=True)

# Main content area
def main():
    # Check if we're in tool mode or dashboard mode
    if st.session_state.current_tool:
        # Show specific tool based on session state
        show_tool(st.session_state.current_tool)
        return
    
    # Welcome section
    st.markdown("### 🎯 PWD Tools Hub")
    st.markdown("**Infrastructure Management Tools** - Simple tools for PWD operations")
    
    st.markdown("---")
    
    # Stats cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="stats-card">
            <h3>8</h3>
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
    
    # Tools grid section
    st.markdown("### 🔧 Available Tools")
    
    # Create the main tool grid (4 columns)
    tools = [
        {
            "name": "📝 Hindi Bill Note",
            "description": "Generate running and final bills in Hindi",
            "icon": "📝",
            "key": "hindi_bill"
        },
        {
            "name": "💰 Stamp Duty Calculator",
            "description": "Calculate stamp duty with predefined rates",
            "icon": "💰",
            "key": "stamp_duty"
        },
        {
            "name": "💳 EMD Refund",
            "description": "Simple EMD refund with 3 inputs only",
            "icon": "💳",
            "key": "emd_refund"
        },
        {
            "name": "⏰ Delay Calculator",
            "description": "Calculate project delays easily",
            "icon": "⏰",
            "key": "delay_calculator"
        },
        {
            "name": "📊 Financial Analysis",
            "description": "Simple financial analysis with calendar",
            "icon": "📊",
            "key": "financial_analysis"
        },
        {
            "name": "📉 Deductions Table",
            "description": "Calculate TDS, Security, and other deductions",
            "icon": "📉",
            "page": "pages/02_Deductions_Table.py"
        },
        {
            "name": "📅 Delay Calculator Pro",
            "description": "Calculate project delays and timeline analysis",
            "icon": "📅",
            "page": "pages/03_Delay_Calculator.py"
        },
        {
            "name": "🎫 Stamp Duty Pro",
            "description": "Calculate stamp duty for work orders",
            "icon": "🎫",
            "page": "pages/04_Stamp_Duty.py"
        }
    ]
    
    # Display tools in a grid
    num_columns = 4
    for i in range(0, len(tools), num_columns):
        cols = st.columns(num_columns)
        for j in range(num_columns):
            if i + j < len(tools):
                tool = tools[i + j]
                with cols[j]:
                    st.markdown(f"""
                    <div class="tool-card">
                        <div style="font-size: 2.5rem; margin-bottom: 8px;">{tool['icon']}</div>
                        <div style="font-size: 1.2rem; font-weight: bold; color: #2E8B57;">
                            {tool['name']}
                        </div>
                        <div style="font-size: 0.9rem; margin-top: 10px; color: #666;">
                            {tool['description']}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Navigation button
                    if st.button(f"Open {tool['name']}", key=f"btn_{i+j}"):
                        if 'key' in tool:
                            # For tools that should be handled by this app
                            st.session_state.current_tool = tool['key']
                            st.experimental_rerun()
                        else:
                            # For tools that have their own page files
                            st.switch_page(tool['page'])
    
    # Show credits at bottom
    st.markdown("---")
    st.markdown("""
    <div class="credits">
        <h4>🏆 Initiative Credit</h4>
        <p><strong>Mrs. Premlata Jain</strong><br>
        Additional Administrative Officer<br>
        Public Works Department (PWD), Udaipur</p>
        <p>🎯 <em>"Empowering Infrastructure Excellence Through Digital Innovation"</em></p>
    </div>
    """, unsafe_allow_html=True)

def show_tool(tool_key):
    """Show specific tool based on key"""
    # Add a back button
    if st.sidebar.button("🏠 Back to Dashboard"):
        st.session_state.current_tool = None
        st.experimental_rerun()
    
    st.sidebar.markdown("---")
    
    if tool_key == "hindi_bill":
        show_hindi_bill_tool()
    elif tool_key == "stamp_duty":
        show_stamp_duty_tool()
    elif tool_key == "emd_refund":
        show_emd_refund_tool()
    elif tool_key == "delay_calculator":
        show_delay_calculator_tool()
    elif tool_key == "financial_analysis":
        show_financial_analysis_tool()

def show_hindi_bill_tool():
    """Show Hindi Bill Note tool"""
    st.markdown("## 📝 Hindi Bill Note Generator")
    st.markdown("Generate running and final bills in Hindi")
    
    # This would contain the actual tool implementation
    st.info("Hindi Bill Note tool implementation would go here")
    st.write("This tool would generate running and final bills in Hindi based on work order details.")

def show_stamp_duty_tool():
    """Show Stamp Duty Calculator tool"""
    st.markdown("## 💰 Stamp Duty Calculator")
    st.markdown("Calculate stamp duty with predefined rates")
    
    # This would contain the actual tool implementation
    st.info("Stamp Duty Calculator tool implementation would go here")
    st.write("This tool would calculate stamp duty based on work order amounts.")

def show_emd_refund_tool():
    """Show EMD Refund tool"""
    st.markdown("## 💳 EMD Refund")
    st.markdown("Simple EMD refund with 3 inputs only")
    
    # This would contain the actual tool implementation
    st.info("EMD Refund tool implementation would go here")
    st.write("This tool would process EMD refunds with minimal inputs.")

def show_delay_calculator_tool():
    """Show Delay Calculator tool"""
    st.markdown("## ⏰ Delay Calculator")
    st.markdown("Calculate project delays easily")
    
    # This would contain the actual tool implementation
    st.info("Delay Calculator tool implementation would go here")
    st.write("This tool would calculate project delays based on planned vs actual dates.")

def show_financial_analysis_tool():
    """Show Financial Analysis tool"""
    st.markdown("## 📊 Financial Analysis")
    st.markdown("Simple financial analysis with calendar")
    
    # This would contain the actual tool implementation
    st.info("Financial Analysis tool implementation would go here")
    st.write("This tool would perform financial analysis of projects.")

# Main app execution
if __name__ == "__main__":
    main()