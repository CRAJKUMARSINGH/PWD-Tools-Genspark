#!/usr/bin/env python3
"""
PWD Tools Web - Infrastructure Management Suite
Streamlit-based web application for PWD operations
"""

import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Set page configuration with a beautiful title and icon
st.set_page_config(
    page_title="PWD Tools Web - Infrastructure Management Suite",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for magenta theme
st.markdown("""
<style>
    :root {
        --magenta-primary: #c71585;
        --magenta-secondary: #ff00ff;
        --magenta-accent: #ff69b4;
    }
    
    .main-header {
        background: linear-gradient(135deg, #c71585, #ff00ff);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    .main-header h1 {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        font-weight: 700;
    }
    
    .main-header p {
        font-size: 1.2rem;
        opacity: 0.9;
        margin-bottom: 0;
    }
    
    .tool-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: transform 0.2s, box-shadow 0.2s;
        border-left: 4px solid #c71585;
    }
    
    .tool-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    
    .tool-icon {
        font-size: 2rem;
        margin-bottom: 1rem;
        color: #c71585;
    }
    
    .tool-title {
        font-weight: 600;
        font-size: 1.3rem;
        margin-bottom: 0.5rem;
        color: #333;
    }
    
    .tool-description {
        color: #666;
        margin-bottom: 1rem;
    }
    
    .stButton > button {
        background-color: #c71585 !important;
        color: white !important;
        border: none !important;
        border-radius: 5px !important;
        padding: 0.5rem 1rem !important;
        font-weight: 600 !important;
        transition: background-color 0.2s !important;
    }
    
    .stButton > button:hover {
        background-color: #9b0e66 !important;
    }
    
    .footer {
        text-align: center;
        padding: 2rem 0;
        color: #666;
        font-size: 0.9rem;
        border-top: 1px solid #eee;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Main header with beautiful title
    st.markdown("""
    <div class="main-header">
        <h1>🏗️ PWD Tools Web</h1>
        <p>Infrastructure Management Suite for Public Works Department</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Introduction
    st.markdown("""
    Welcome to **PWD Tools Web** - a comprehensive suite of tools designed specifically for Public Works Department operations. 
    This web application provides all the essential tools you need for financial calculations, document generation, 
    and project management in a streamlined, browser-based interface.
    """)
    
    # Tool grid
    st.subheader("📋 Available Tools")
    
    # Create columns for tool cards
    col1, col2, col3 = st.columns(3)
    
    # Excel se EMD Tool
    with col1:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-icon">📊</div>
            <div class="tool-title">Excel se EMD</div>
            <div class="tool-description">Generate hand receipts from Excel files with automated processing</div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Launch Excel se EMD", key="excel_emd"):
            st.switch_page("pages/01_excel_se_emd.py")
    
    # Bill Note Sheet Tool
    with col2:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-icon">📝</div>
            <div class="tool-title">Bill Note Sheet</div>
            <div class="tool-description">Create standardized bill note sheets for PWD documentation</div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Launch Bill Note Sheet", key="bill_note"):
            st.switch_page("pages/02_bill_note_sheet.py")
    
    # EMD Refund Tool
    with col3:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-icon">💰</div>
            <div class="tool-title">EMD Refund</div>
            <div class="tool-description">Calculate EMD refunds with automatic penalty calculations</div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Launch EMD Refund", key="emd_refund"):
            st.switch_page("pages/03_emd_refund.py")
    
    # Second row of tools
    col4, col5, col6 = st.columns(3)
    
    # Deductions Table Tool
    with col4:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-icon">🧮</div>
            <div class="tool-title">Deductions Table</div>
            <div class="tool-description">Calculate all standard deductions for bill amounts</div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Launch Deductions Table", key="deductions"):
            st.switch_page("pages/04_deductions_table.py")
    
    # Delay Calculator Tool
    with col5:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-icon">⏰</div>
            <div class="tool-title">Delay Calculator</div>
            <div class="tool-description">Calculate project delays and associated penalties</div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Launch Delay Calculator", key="delay"):
            st.switch_page("pages/05_delay_calculator.py")
    
    # Security Refund Tool
    with col6:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-icon">🔒</div>
            <div class="tool-title">Security Refund</div>
            <div class="tool-description">Process security deposit refunds efficiently</div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Launch Security Refund", key="security"):
            st.switch_page("pages/06_security_refund.py")
    
    # Third row of tools
    col7, col8, col9 = st.columns(3)
    
    # Financial Progress Tool
    with col7:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-icon">📈</div>
            <div class="tool-title">Financial Progress</div>
            <div class="tool-description">Track financial progress and liquidity damages</div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Launch Financial Progress", key="financial"):
            st.switch_page("pages/07_financial_progress.py")
    
    # Stamp Duty Tool
    with col8:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-icon"> taxp</div>
            <div class="tool-title">Stamp Duty</div>
            <div class="tool-description">Calculate stamp duty amounts for various documents</div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Launch Stamp Duty", key="stamp"):
            st.switch_page("pages/08_stamp_duty.py")
    
    # Spacer for the last column
    with col9:
        st.markdown("""
        <div style="height: 150px;"></div>
        """, unsafe_allow_html=True)
    
    # Features section
    st.subheader("✨ Key Features")
    col_features1, col_features2, col_features3 = st.columns(3)
    
    with col_features1:
        st.markdown("**📱 Responsive Design**")
        st.markdown("Works seamlessly on desktop, tablet, and mobile devices")
        
        st.markdown("**💾 Data Export**")
        st.markdown("Export results to PDF, Excel, and other formats")
    
    with col_features2:
        st.markdown("**🎨 Magenta Theme**")
        st.markdown("Beautiful UI with consistent magenta color scheme")
        
        st.markdown("**⚡ Fast Processing**")
        st.markdown("Optimized algorithms for quick calculations")
    
    with col_features3:
        st.markdown("**🔒 Secure**")
        st.markdown("All processing happens in your browser - no data uploaded")
        
        st.markdown("**🔄 Regular Updates**")
        st.markdown("Continuously improved with new features")
    
    # Footer
    st.markdown("""
    <div class="footer">
        <p>Prepared for Mrs. Premlata Jain, AAO, PWD Udaipur</p>
        <p>PWD Tools Web - Infrastructure Management Suite | © 2025</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()