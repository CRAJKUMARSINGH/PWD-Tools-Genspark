#!/usr/bin/env python3
"""
Hindi Bill Note Tool - FIXED VERSION
For Lower Divisional Clerks - NO COMPLEXITY
Fixes CustomTkinter icon issues
"""

import sys
import os
import warnings

def main():
    """Fixed launcher for Hindi Bill Note"""
    print("Hindi Bill Note Tool - Fixed Version")
    print("For Lower Divisional Clerks")
    print("=" * 40)
    
    # Suppress CustomTkinter warnings
    warnings.filterwarnings("ignore", category=UserWarning)
    
    try:
        # Set environment variable to fix icon issues
        os.environ['CTK_ICON_FIX'] = '1'
        
        from hindi_bill_note import HindiBillNoteTool
        print("Starting Hindi Bill Note Tool...")
        app = HindiBillNoteTool()
        app.run()
    except Exception as e:
        print(f"Error: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
