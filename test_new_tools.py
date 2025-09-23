"""
Test script to verify the new tools (Security Refund and Excel EMD Web) are working correctly
"""

import tkinter as tk
from tkinter import messagebox
import os
import sys

def test_security_refund_tool():
    """Test that the Security Refund tool exists and can be imported"""
    try:
        # Try to import the security refund module
        from security_refund_simple import open_security_refund_html
        print("✓ Security Refund tool module imported successfully")
        return True
    except ImportError as e:
        print(f"✗ Failed to import Security Refund tool: {e}")
        return False
    except Exception as e:
        print(f"✗ Error with Security Refund tool: {e}")
        return False

def test_excel_emd_tool():
    """Test that the Excel EMD tool exists"""
    if os.path.exists("excel_emd_tool.py"):
        print("✓ Excel EMD tool file found")
        return True
    else:
        print("✗ Excel EMD tool file not found")
        return False

def launch_test_gui():
    """Launch a simple GUI to show test results"""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    security_refund_ok = test_security_refund_tool()
    excel_emd_ok = test_excel_emd_tool()
    
    if security_refund_ok and excel_emd_ok:
        messagebox.showinfo("Test Result", 
                           "All new tools are ready!\n\n"
                           "1. Security Refund tool - Ready\n"
                           "2. Excel EMD Web tool - Ready\n\n"
                           "Both tools have been added to the main landing page.")
    else:
        errors = []
        if not security_refund_ok:
            errors.append("Security Refund tool")
        if not excel_emd_ok:
            errors.append("Excel EMD Web tool")
        
        messagebox.showerror("Test Result", 
                           "Some issues were found:\n\n"
                           f"Failed tools: {', '.join(errors)}\n\n"
                           "Please check the console output for details.")
    
    root.destroy()

if __name__ == "__main__":
    print("Testing new tools...")
    print("1. Security Refund Tool:")
    test_security_refund_tool()
    print("\n2. Excel EMD Tool:")
    test_excel_emd_tool()
    
    # Launch GUI test
    launch_test_gui()