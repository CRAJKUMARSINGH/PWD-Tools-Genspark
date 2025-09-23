import streamlit as st
import time

def apply_custom_css():
    """Apply custom CSS styling with crane branding and green gradient theme"""
    st.markdown("""
    <style>
    /* Main app styling */
    .main > div {
        padding-top: 0rem;
    }
    
    /* Header styling with enhanced green gradient */
    .header-container {
        background: linear-gradient(135deg, #1a5d38 0%, #2E8B57 50%, #3CB371 100%);
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 25px;
        color: white;
        text-align: center;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        border: 1px solid #1a5d38;
    }
    
    /* Enhanced tool button styling - closer to repo design */
    .tool-button {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border: 2px solid #2E8B57;
        border-radius: 15px;
        padding: 25px 15px;
        margin: 15px 5px;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    .tool-button:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        border-color: #228B22;
        background: linear-gradient(135deg, #f0f8f5 0%, #e8f5e8 100%);
    }
    
    /* Metric styling */
    .metric-container {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #2E8B57;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
    }
    
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background-color: #f0f8f5;
    }
    
    /* Success animation */
    .celebration {
        animation: bounce 1s ease-in-out infinite alternate;
    }
    
    @keyframes bounce {
        0% { transform: translateY(0px); }
        100% { transform: translateY(-10px); }
    }
    
    /* Credits styling with enhanced design */
    .credits {
        background: linear-gradient(135deg, #1a5d38 0%, #2E8B57 100%);
        color: white;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin-top: 30px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        border: 1px solid #1a5d38;
    }
    
    /* Button styling - closer to repo design */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #2E8B57 0%, #3CB371 100%);
        color: white;
        border-radius: 12px;
        border: none;
        padding: 12px 20px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 8px rgba(46, 139, 87, 0.3);
        margin-top: 10px;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #228B22 0%, #2E8B57 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(46, 139, 87, 0.4);
    }
    
    /* Page link styling */
    a[href*="pages/"] {
        display: block;
        text-decoration: none;
        color: #2E8B57;
        font-weight: 600;
        margin-top: 15px;
        padding: 12px 20px;
        border-radius: 12px;
        background-color: rgba(46, 139, 87, 0.1);
        transition: all 0.2s ease;
        text-align: center;
    }
    
    a[href*="pages/"]:hover {
        background-color: rgba(46, 139, 87, 0.2);
        transform: translateY(-2px);
    }
    
    /* External link styling */
    a[href^="http"] {
        display: block;
        text-decoration: none;
        color: white;
        font-weight: 600;
        margin-top: 15px;
        padding: 12px 20px;
        border-radius: 12px;
        background: linear-gradient(135deg, #2E8B57 0%, #3CB371 100%);
        transition: all 0.2s ease;
        text-align: center;
        box-shadow: 0 4px 8px rgba(46, 139, 87, 0.3);
    }
    
    a[href^="http"]:hover {
        background: linear-gradient(135deg, #228B22 0%, #2E8B57 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(46, 139, 87, 0.4);
    }
    
    /* Breadcrumb styling */
    .breadcrumb {
        background-color: #f0f8f5;
        padding: 12px 20px;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

def show_header():
    """Display the main header with crane logo and branding"""
    st.markdown("""
    <div class="header-container">
        <h1>🏗️ PWD Tools Hub</h1>
        <h3>Infrastructure Management Suite</h3>
        <p style="font-size: 1.1rem; opacity: 0.95; max-width: 800px; margin: 15px auto 0;">
            Empowering Public Works Department with digital tools for efficient infrastructure management
        </p>
    </div>
    """, unsafe_allow_html=True)

def show_credits():
    """Display credits and attribution"""
    st.markdown("""
    <div class="credits">
        <h4>🏆 Initiative Credit</h4>
        <p style="font-size: 1.2rem;"><strong>Mrs. Premlata Jain</strong></p>
        <p style="font-size: 1rem;">Additional Administrative Officer<br>
        Public Works Department (PWD), Udaipur</p>
        <p style="font-style: italic; font-size: 1.1rem; margin-top: 15px;">🎯 "Empowering Infrastructure Excellence Through Digital Innovation"</p>
        <div style="margin-top: 20px; font-size: 0.9rem; opacity: 0.9;">
            <p>Version 2.0 | Last Updated: September 2025</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_balloons():
    """Display celebration balloons animation"""
    st.balloons()
    time.sleep(1)

def get_tool_colors():
    """Return color schemes for different tool categories"""
    return {
        "financial": {"bg": "#E8F5E8", "border": "#2E8B57", "icon": "💰"},
        "processing": {"bg": "#F0F8FF", "border": "#4169E1", "icon": "📋"},
        "operations": {"bg": "#FFF8DC", "border": "#FF8C00", "icon": "🏗️"},
        "monitoring": {"bg": "#F5F5DC", "border": "#8B4513", "icon": "📊"},
        "external": {"bg": "#FFE4E1", "border": "#DC143C", "icon": "🔗"}
    }