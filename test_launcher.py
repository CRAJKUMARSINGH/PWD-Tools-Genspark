"""
Test script for PWD Simple Tools Launcher
"""

import tkinter as tk
from tkinter import messagebox
import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_launcher():
    """Test the PWD Simple Tools Launcher"""
    try:
        from pwd_simple_tools_launcher import PWDSimpleToolsLauncher
        print("✓ PWD Simple Tools Launcher imported successfully")
        
        # Create a simple test instance
        launcher = PWDSimpleToolsLauncher()
        print("✓ PWD Simple Tools Launcher instantiated successfully")
        
        # Close the window immediately to avoid blocking
        launcher.root.destroy()
        print("✓ PWD Simple Tools Launcher test completed")
        return True
    except Exception as e:
        print(f"✗ PWD Simple Tools Launcher test failed: {e}")
        return False

def main():
    """Run launcher test"""
    print("Testing PWD Simple Tools Launcher...")
    print("=" * 40)
    
    result = test_launcher()
    
    print("=" * 40)
    if result:
        print("✓ Launcher test passed!")
        return 0
    else:
        print("✗ Launcher test failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main())