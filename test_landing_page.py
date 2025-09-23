"""
Test script for the enhanced PWD Main Landing Page
"""

import os
import sys
import tkinter as tk
from tkinter import messagebox

def test_file_existence():
    """Test if all required tool files exist"""
    required_files = [
        "hindi_bill_simple.py",
        "stamp_duty_simple.py", 
        "emd_refund_simple.py",
        "delay_calculator_simple.py",
        "financial_analysis_simple.py"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"Missing files: {missing_files}")
        return False
    else:
        print("All required files found")
        return True

def test_import_landing_page():
    """Test if we can import the landing page"""
    try:
        # Add current directory to path
        sys.path.insert(0, '.')
        
        # Try to import the landing page
        import pwd_main_landing
        print("Successfully imported pwd_main_landing")
        return True
    except Exception as e:
        print(f"Failed to import pwd_main_landing: {e}")
        return False

if __name__ == "__main__":
    print("Testing PWD Main Landing Page...")
    
    # Change to the correct directory
    os.chdir(r"c:\Users\Rajkumar\PWD-Tools-Genspark")
    
    # Test file existence
    files_ok = test_file_existence()
    
    # Test import
    import_ok = test_import_landing_page()
    
    if files_ok and import_ok:
        print("All tests passed!")
    else:
        print("Some tests failed!")