"""
Test script to verify that streamlit_app.py works as the main landing page
"""

import os
import sys

def test_streamlit_app_file():
    """Test that streamlit_app.py exists and has the right structure"""
    # Check if streamlit_app.py exists
    if not os.path.exists("streamlit_app.py"):
        print("❌ streamlit_app.py file not found")
        return False
    
    # Check if it contains Streamlit imports
    with open("streamlit_app.py", "r", encoding="utf-8") as f:
        content = f.read()
        
    if "import streamlit as st" not in content:
        print("❌ streamlit_app.py doesn't contain Streamlit import")
        return False
    
    if "st.set_page_config" not in content:
        print("❌ streamlit_app.py doesn't configure Streamlit page")
        return False
    
    print("✅ streamlit_app.py exists and has proper Streamlit structure")
    return True

def test_deploy_script():
    """Test that deploy_streamlit.py points to streamlit_app.py"""
    with open("deploy_streamlit.py", "r", encoding="utf-8") as f:
        content = f.read()
    
    if '"streamlit_app.py"' in content:
        print("✅ deploy_streamlit.py correctly points to streamlit_app.py")
        return True
    else:
        print("❌ deploy_streamlit.py doesn't point to streamlit_app.py")
        return False

def main():
    """Run all tests"""
    print("Testing streamlit_app.py as main landing page...")
    print("=" * 50)
    
    tests = [
        test_streamlit_app_file,
        test_deploy_script
    ]
    
    all_passed = True
    for test in tests:
        if not test():
            all_passed = False
    
    print("=" * 50)
    if all_passed:
        print("🎉 All tests passed! streamlit_app.py is now the main landing page.")
        print("\nTo run the application, you can:")
        print("1. Execute: python deploy_streamlit.py")
        print("2. Or directly: streamlit run streamlit_app.py")
    else:
        print("❌ Some tests failed. Please check the issues above.")

if __name__ == "__main__":
    main()