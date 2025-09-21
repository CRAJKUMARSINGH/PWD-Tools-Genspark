#!/usr/bin/env python3
"""
Hindi Bill Note Tool - SIMPLE LAUNCHER
For Lower Divisional Clerks - NO COMPLEXITY
"""

import sys
import os

def main():
    """Simple launcher for Hindi Bill Note"""
    print("Hindi Bill Note Tool - Simple Version")
    print("For Lower Divisional Clerks")
    print("=" * 40)
    
    try:
        from hindi_bill_note import HindiBillNoteTool
        print("Starting Hindi Bill Note Tool...")
        app = HindiBillNoteTool()
        app.run()
    except Exception as e:
        print(f"Error: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
