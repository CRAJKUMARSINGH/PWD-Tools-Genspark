import streamlit as st
import time

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
</style>
""", unsafe_allow_html=True)

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
    # Welcome section
    st.markdown("### 🎯 PWD Tools Hub")
    st.markdown("**Infrastructure Management Tools** - Simple tools for PWD operations")
    
    st.markdown("---")
    
    # Tools grid section
    st.markdown("### 🔧 Available Tools")
    
    # Create the main tool grid (5 columns)
    tools = [
        {
            "name": "📝 Hindi Bill Note",
            "description": "Generate running and final bills in Hindi",
            "icon": "📝",
            "page": "streamlit_landing.py",
            "params": "?tool=hindi_bill"
        },
        {
            "name": "💰 Stamp Duty Calculator",
            "description": "Calculate stamp duty with predefined rates",
            "icon": "💰",
            "page": "streamlit_landing.py",
            "params": "?tool=stamp_duty"
        },
        {
            "name": "💳 EMD Refund",
            "description": "Simple EMD refund with 3 inputs only",
            "icon": "💳",
            "page": "streamlit_landing.py",
            "params": "?tool=emd_refund"
        },
        {
            "name": "⏰ Delay Calculator",
            "description": "Calculate project delays easily",
            "icon": "⏰",
            "page": "streamlit_landing.py",
            "params": "?tool=delay_calculator"
        },
        {
            "name": "📊 Financial Analysis",
            "description": "Simple financial analysis with calendar",
            "icon": "📊",
            "page": "streamlit_landing.py",
            "params": "?tool=financial_analysis"
        },
        {
            "name": "📉 Deductions Table",
            "description": "Calculate TDS, Security, and other deductions",
            "icon": "📉",
            "page": "pages/02_Deductions_Table.py",
            "params": ""
        },
        {
            "name": "📅 Delay Calculator",
            "description": "Calculate project delays and timeline analysis",
            "icon": "📅",
            "page": "pages/03_Delay_Calculator.py",
            "params": ""
        },
        {
            "name": "🎫 Stamp Duty",
            "description": "Calculate stamp duty for work orders",
            "icon": "🎫",
            "page": "pages/04_Stamp_Duty.py",
            "params": ""
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
                        st.switch_page(f"{tool['page']}{tool['params']}")

# Main app execution
if __name__ == "__main__":
    main()
    
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