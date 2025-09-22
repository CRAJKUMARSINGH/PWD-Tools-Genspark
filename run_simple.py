#!/usr/bin/env python3
"""
PWD Tools - SIMPLE LAUNCHER
For Lower Divisional Clerks - NO COMPLEXITY
"""

import sys
import os

def main():
    """Simple launcher"""
    print("PWD Tools - Simple Version")
    print("For Lower Divisional Clerks")
    print("=" * 40)
    
    try:
        from simple_app import SimplePWDTools
        print("Starting simple PWD Tools...")
        app = SimplePWDTools()
        app.run()
    except Exception as e:
        print(f"Error: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
