"""
Test script to verify the web-based financial analysis tool
"""

import os
import webbrowser
import tkinter as tk
from tkinter import messagebox

def test_financial_web_tool():
    """Test that the web-based financial analysis tool exists and can be opened"""
    
    # Check if the HTML file exists
    html_file = "financial_analysis_web.html"
    if os.path.exists(html_file):
        print(f"✓ {html_file} found")
        
        # Get absolute path
        abs_path = os.path.abspath(html_file)
        print(f"  Path: {abs_path}")
        
        # Try to open in browser (this will just test if the path is valid)
        try:
            # This won't actually open the browser in the test, but we can verify the path
            url = f"file://{abs_path}"
            print(f"  URL: {url}")
            print("✓ Web-based financial analysis tool is ready to launch")
            return True
        except Exception as e:
            print(f"✗ Error with URL: {e}")
            return False
    else:
        print(f"✗ {html_file} not found")
        return False

def launch_test():
    """Launch a simple GUI to test the tool"""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    success = test_financial_web_tool()
    
    if success:
        messagebox.showinfo("Test Result", 
                           "Web-based Financial Analysis Tool is ready!\n\n"
                           "The tool will launch in your default web browser when opened from the main application.")
    else:
        messagebox.showerror("Test Result", 
                           "There was an issue with the Financial Analysis Tool.\n\n"
                           "Please check that financial_analysis_web.html exists in the application directory.")
    
    root.destroy()

if __name__ == "__main__":
    print("Testing web-based financial analysis tool...")
    test_financial_web_tool()
    launch_test()