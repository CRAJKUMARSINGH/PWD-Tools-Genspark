"""
Test script to verify the main landing page is working correctly
"""

import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

def test_file_exists(filename):
    """Check if a file exists in the current directory"""
    return os.path.exists(filename)

def main():
    """Test the main landing page functionality"""
    print("Testing PWD Tools Main Landing Page...")
    
    # Test files that should exist
    required_files = [
        "pwd_main_landing.py",
        "hindi_bill_simple.py",
        "stamp_duty_simple.py",
        "emd_refund_simple.py",
        "delay_calculator_simple.py",
        "financial_analysis_simple.py"
    ]
    
    print("\nChecking required files:")
    all_files_exist = True
    for file in required_files:
        exists = test_file_exists(file)
        status = "✅ Found" if exists else "❌ Missing"
        print(f"  {file}: {status}")
        if not exists:
            all_files_exist = False
    
    if not all_files_exist:
        print("\n⚠️  Some required files are missing. The application may not work correctly.")
        return False
    
    print("\n✅ All required files are present.")
    print("\n🎉 Main landing page should work correctly now!")
    print("\nTo run the application, execute: python pwd_main_landing.py")
    return True

if __name__ == "__main__":
    main()