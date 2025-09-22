"""
Test script to verify that app.py works as the main landing page
"""

import os
import sys

def test_app_file():
    """Test that app.py exists and has the right structure"""
    # Check if app.py exists
    if not os.path.exists("app.py"):
        print("❌ app.py file not found")
        return False
    
    # Check if it contains Streamlit imports
    with open("app.py", "r", encoding="utf-8") as f:
        content = f.read()
        
    if "import streamlit as st" not in content:
        print("❌ app.py doesn't contain Streamlit import")
        return False
    
    if "st.set_page_config" not in content:
        print("❌ app.py doesn't configure Streamlit page")
        return False
    
    print("✅ app.py exists and has proper Streamlit structure")
    return True

def test_deploy_script():
    """Test that deploy_streamlit.py points to app.py"""
    with open("deploy_streamlit.py", "r", encoding="utf-8") as f:
        content = f.read()
    
    if '"app.py"' in content:
        print("✅ deploy_streamlit.py correctly points to app.py")
        return True
    else:
        print("❌ deploy_streamlit.py doesn't point to app.py")
        return False

def main():
    """Run all tests"""
    print("Testing app.py as main landing page...")
    print("=" * 50)
    
    tests = [
        test_app_file,
        test_deploy_script
    ]
    
    all_passed = True
    for test in tests:
        if not test():
            all_passed = False
    
    print("=" * 50)
    if all_passed:
        print("🎉 All tests passed! app.py is now the main landing page.")
        print("\nTo run the application, you can:")
        print("1. Execute: python deploy_streamlit.py")
        print("2. Or directly: streamlit run app.py")
    else:
        print("❌ Some tests failed. Please check the issues above.")

if __name__ == "__main__":
    main()