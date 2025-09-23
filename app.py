import streamlit as st
import webbrowser
from utils.branding import apply_custom_css, show_header, show_credits, get_tool_colors

# Configure page
st.set_page_config(
    page_title="PWD Tools Hub",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom styling
apply_custom_css()

# Show header
show_header()

# Main content
st.markdown("""
<div style="text-align: center; margin-bottom: 30px;">
    <h2>Comprehensive PWD Tools Suite</h2>
    <p style="font-size: 1.2rem; color: #666; max-width: 800px; margin: 0 auto;">
        A complete digital solution for Public Works Department operations with both desktop and web capabilities
    </p>
</div>
""", unsafe_allow_html=True)

# Create tool grid
st.markdown("### 🛠️ Available Tools")

# Define tools with their properties
tools = [
    {
        "name": "Excel se EMD",
        "description": "Generate hand receipts from Excel files with automated processing",
        "icon": "📊",
        "color": "#8B5CF6",  # Purple
        "url": "https://marudharhr.onrender.com/",
        "type": "external"
    },
    {
        "name": "Bill Note Sheet",
        "description": "Create running and final bills with standardized PWD formats",
        "icon": "📋",
        "color": "#10B981",  # Green
        "url": "https://raj-bill-generator-v01.streamlit.app/",
        "type": "external"
    },
    {
        "name": "EMD Refund",
        "description": "Calculate and process Earnest Money Deposit refunds efficiently",
        "icon": "💰",
        "color": "#F59E0B",  # Orange
        "url": None,
        "type": "internal"
    },
    {
        "name": "Deductions Table",
        "description": "Calculate TDS, Security, and other financial deductions",
        "icon": "🧮",
        "color": "#EF4444",  # Red
        "url": None,
        "type": "internal"
    },
    {
        "name": "Delay Calculator",
        "description": "Calculate project delays and associated penalties",
        "icon": "⏱️",
        "color": "#6366F1",  # Indigo
        "url": None,
        "type": "internal"
    },
    {
        "name": "Financial Progress",
        "description": "Track financial progress and liquidity damages",
        "icon": "📈",
        "color": "#10B981",  # Green
        "url": None,
        "type": "internal"
    },
    {
        "name": "Security Refund",
        "description": "Process security deposit refunds with proper calculations",
        "icon": "🔒",
        "color": "#8B5CF6",  # Purple
        "url": None,
        "type": "internal"
    },
    {
        "name": "Stamp Duty",
        "description": "Calculate stamp duty with predefined PWD rates",
        "icon": "🎫",
        "color": "#F59E0B",  # Orange
        "url": None,
        "type": "internal"
    },
    {
        "name": "Bill & Deviation",
        "description": "Infrastructure billing with deviation tracking",
        "icon": "📐",
        "color": "#EF4444",  # Red
        "url": "https://raj-bill-generator-v01.streamlit.app/",
        "type": "external"
    },
    {
        "name": "Tender Processing",
        "description": "Streamline tender processing workflows",
        "icon": "📄",
        "color": "#6366F1",  # Indigo
        "url": None,
        "type": "internal"
    }
]

# Display tools in a grid
cols = st.columns(2)
for i, tool in enumerate(tools):
    with cols[i % 2]:
        tool_color = tool["color"]
        st.markdown(f"""
        <div class="tool-button" style="border-left: 5px solid {tool_color};">
            <h3 style="color: {tool_color}; margin-bottom: 15px;">{tool["icon"]} {tool["name"]}</h3>
            <p style="color: #555; margin-bottom: 20px;">{tool["description"]}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if tool["type"] == "external" and tool["url"]:
            if st.button(f"Launch {tool['name']}", key=f"btn_{tool['name']}", use_container_width=True):
                webbrowser.open(tool["url"])
        elif tool["type"] == "internal":
            st.info(f"{tool['name']} tool is available in the desktop version")

# Show credits
show_credits()

# Additional information
st.markdown("""
<div style="background-color: #f0f8f5; padding: 20px; border-radius: 10px; margin-top: 30px;">
    <h3>🖥️ Desktop vs Web Version</h3>
    <p><strong>Desktop Version:</strong> Full-featured offline application with all tools installed locally</p>
    <p><strong>Web Version:</strong> Select tools accessible online with cloud integration</p>
    <p>For the complete experience, download the desktop application.</p>
</div>
""", unsafe_allow_html=True)