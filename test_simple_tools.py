"""
Test script for simple PWD tools
"""

import tkinter as tk
from tkinter import messagebox
import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_delay_calculator():
    """Test the delay calculator tool"""
    try:
        from delay_calculator_simple import SimpleDelayCalculatorTool
        print("✓ Delay Calculator imported successfully")
        
        # Create a simple test instance
        tool = SimpleDelayCalculatorTool()
        print("✓ Delay Calculator instantiated successfully")
        
        # Close the window immediately to avoid blocking
        tool.root.destroy()
        print("✓ Delay Calculator test completed")
        return True
    except Exception as e:
        print(f"✗ Delay Calculator test failed: {e}")
        return False

def test_deductions_table():
    """Test the deductions table tool"""
    try:
        from deductions_table_tool import DeductionsTableTool
        print("✓ Deductions Table imported successfully")
        
        # Create a simple test instance
        tool = DeductionsTableTool()
        print("✓ Deductions Table instantiated successfully")
        
        # Close the window immediately to avoid blocking
        tool.root.destroy()
        print("✓ Deductions Table test completed")
        return True
    except Exception as e:
        print(f"✗ Deductions Table test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("Testing Simple PWD Tools...")
    print("=" * 40)
    
    results = []
    results.append(test_delay_calculator())
    results.append(test_deductions_table())
    
    print("=" * 40)
    if all(results):
        print("✓ All tests passed!")
        return 0
    else:
        print("✗ Some tests failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main())