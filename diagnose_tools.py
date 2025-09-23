"""
Diagnostic script to test tool launching
"""

import os
import sys
import subprocess
from tkinter import messagebox
import tkinter as tk

def test_current_directory():
    """Test current working directory"""
    print(f"Current working directory: {os.getcwd()}")
    print(f"Files in directory: {os.listdir('.')}")
    
def test_file_existence():
    """Test if required files exist"""
    files = [
        "hindi_bill_simple.py",
        "stamp_duty_simple.py", 
        "emd_refund_simple.py",
        "delay_calculator_simple.py",
        "financial_analysis_simple.py"
    ]
    
    for file in files:
        exists = os.path.exists(file)
        print(f"{file}: {'FOUND' if exists else 'MISSING'}")
        
def test_subprocess_launch():
    """Test launching a tool with subprocess"""
    try:
        # Test with a simple Python command first
        result = subprocess.run([sys.executable, "--version"], 
                              capture_output=True, text=True, timeout=10)
        print(f"Python version: {result.stdout.strip()}")
        
        # Test launching hindi_bill_simple.py
        if os.path.exists("hindi_bill_simple.py"):
            print("Attempting to launch hindi_bill_simple.py...")
            # Use shell=True to see if it helps
            process = subprocess.Popen([sys.executable, "hindi_bill_simple.py"], 
                                     shell=True)
            print(f"Process started with PID: {process.pid}")
        else:
            print("hindi_bill_simple.py not found")
            
    except Exception as e:
        print(f"Error launching subprocess: {e}")

if __name__ == "__main__":
    print("=== PWD Tools Diagnostic ===")
    test_current_directory()
    print()
    test_file_existence()
    print()
    test_subprocess_launch()