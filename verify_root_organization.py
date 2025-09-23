#!/usr/bin/env python3
"""
Verification script for PWD Tools root organization
"""

import os
import sys

def check_files():
    """Check that all required files are in the root directory"""
    
    # Required files and directories
    required_items = [
        "pwd_tools_app.py",
        "run_app.bat",
        "requirements.txt",
        "runtime.txt",
        "components",
        "utils",
        "pages",
        ".streamlit"
    ]
    
    missing_items = []
    
    for item in required_items:
        if not os.path.exists(item):
            missing_items.append(item)
    
    if missing_items:
        print(f"❌ Missing items: {missing_items}")
        return False
    else:
        print("✅ All required items are present")
        return True

def check_components():
    """Check that components directory has required files"""
    required_files = [
        "tool_buttons.py",
        "custom_tool_buttons.py"
    ]
    
    missing_files = []
    
    for file in required_files:
        if not os.path.exists(os.path.join("components", file)):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing component files: {missing_files}")
        return False
    else:
        print("✅ All component files are present")
        return True

def check_utils():
    """Check that utils directory has required files"""
    required_files = [
        "branding.py",
        "excel_handler.py",
        "navigation.py",
        "pdf_generator.py"
    ]
    
    missing_files = []
    
    for file in required_files:
        if not os.path.exists(os.path.join("utils", file)):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing utility files: {missing_files}")
        return False
    else:
        print("✅ All utility files are present")
        return True

def check_streamlit_config():
    """Check that Streamlit config is present"""
    if os.path.exists(".streamlit/config.toml"):
        print("✅ Streamlit configuration is present")
        return True
    else:
        print("❌ Streamlit configuration is missing")
        return False

def main():
    """Run all verification checks"""
    print("Verifying PWD Tools root organization...")
    print("=" * 50)
    
    checks = [
        check_files,
        check_components,
        check_utils,
        check_streamlit_config
    ]
    
    passed = 0
    for check in checks:
        if check():
            passed += 1
        print()
    
    print(f"Verification complete: {passed}/{len(checks)} checks passed")
    
    if passed == len(checks):
        print("🎉 All checks passed! The application is properly organized.")
        print("\nTo run the application, execute: run_app.bat")
        return 0
    else:
        print("❌ Some checks failed. Please review the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())