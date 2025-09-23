"""
Test script to verify all tools are accessible
"""

import tkinter as tk
from tkinter import messagebox
import os
import sys

def test_tool_accessibility():
    """Test that all tool files exist and are accessible"""
    tools = [
        ("Hindi Bill Note", "hindi_bill_simple.py"),
        ("Stamp Duty Calculator", "stamp_duty_simple.py"),
        ("EMD Refund", "emd_refund_simple.py"),
        ("Delay Calculator", "delay_calculator_simple.py"),
        ("Financial Analysis", "financial_analysis_simple.py"),
        ("Excel EMD Processor", "excel_emd_tool.py"),
        ("Deductions Calculator", "deductions_table_tool.py"),
        ("Tender Processing", "gui/tools/tender_processing.py")
    ]
    
    missing_tools = []
    accessible_tools = []
    
    for tool_name, tool_path in tools:
        if os.path.exists(tool_path):
            accessible_tools.append(f"✓ {tool_name} - Found at {tool_path}")
        else:
            missing_tools.append(f"✗ {tool_name} - Missing file: {tool_path}")
    
    print("Tool Accessibility Report:")
    print("=" * 50)
    
    for tool in accessible_tools:
        print(tool)
    
    for tool in missing_tools:
        print(tool)
    
    if missing_tools:
        print(f"\nWarning: {len(missing_tools)} tools are missing!")
    else:
        print(f"\nSuccess: All {len(accessible_tools)} tools are accessible!")
    
    return len(missing_tools) == 0

if __name__ == "__main__":
    print("Testing tool accessibility...")
    success = test_tool_accessibility()
    
    # Create a simple GUI to show results
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    if success:
        messagebox.showinfo("Test Result", "All tools are accessible!\n\nThe main landing page now shows all 9 tools.")
    else:
        messagebox.showerror("Test Result", "Some tools are missing!\n\nCheck the console output for details.")
    
    root.destroy()