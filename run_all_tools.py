#!/usr/bin/env python3
"""
PWD Tools - All Tools Launcher
For Lower Divisional Clerks - Simple and Efficient
"""

import sys
import os
import subprocess

def main():
    """Main launcher for all PWD tools"""
    print("PWD Tools - All Tools Launcher")
    print("For Lower Divisional Clerks")
    print("=" * 50)
    
    while True:
        print("\nAvailable Tools:")
        print("1. Hindi Bill Note (with calendar)")
        print("2. Stamp Duty Calculator (predefined rates)")
        print("3. EMD Refund (only 3 inputs)")
        print("4. Financial Analysis (with calendar)")
        print("5. Delay Calculator (with calendar)")
        print("6. Main Dashboard (colorful landing page)")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == "1":
            print("Opening Hindi Bill Note Tool...")
            try:
                subprocess.run([sys.executable, "hindi_bill_simple.py"])
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == "2":
            print("Opening Stamp Duty Calculator...")
            try:
                subprocess.run([sys.executable, "stamp_duty_simple.py"])
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == "3":
            print("Opening EMD Refund Tool...")
            try:
                subprocess.run([sys.executable, "emd_refund_simple.py"])
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == "4":
            print("Opening Financial Analysis Tool...")
            try:
                subprocess.run([sys.executable, "financial_analysis_simple.py"])
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == "5":
            print("Opening Delay Calculator Tool...")
            try:
                subprocess.run([sys.executable, "delay_calculator_simple.py"])
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == "6":
            print("Opening Main Dashboard...")
            try:
                subprocess.run([sys.executable, "pwd_main_landing.py"])
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == "7":
            print("Thank you for using PWD Tools!")
            break
        
        else:
            print("Invalid choice. Please enter 1-7.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
