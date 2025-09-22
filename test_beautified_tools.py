"""
Test script for beautified PWD tools
"""

import tkinter as tk
from tkinter import messagebox
import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_delay_calculator():
    """Test the beautified delay calculator tool"""
    try:
        from delay_calculator_simple import SimpleDelayCalculatorTool
        print("✓ Beautified Delay Calculator imported successfully")
        
        # Create a simple test instance
        tool = SimpleDelayCalculatorTool()
        print("✓ Beautified Delay Calculator instantiated successfully")
        
        # Close the window immediately to avoid blocking
        tool.root.destroy()
        print("✓ Beautified Delay Calculator test completed")
        return True
    except Exception as e:
        print(f"✗ Beautified Delay Calculator test failed: {e}")
        return False

def test_stamp_duty():
    """Test the beautified stamp duty tool"""
    try:
        from stamp_duty_simple import SimpleStampDutyTool
        print("✓ Beautified Stamp Duty imported successfully")
        
        # Create a simple test instance
        tool = SimpleStampDutyTool()
        print("✓ Beautified Stamp Duty instantiated successfully")
        
        # Close the window immediately to avoid blocking
        tool.root.destroy()
        print("✓ Beautified Stamp Duty test completed")
        return True
    except Exception as e:
        print(f"✗ Beautified Stamp Duty test failed: {e}")
        return False

def test_emd_refund():
    """Test the beautified EMD refund tool"""
    try:
        from emd_refund_simple import SimpleEMDRefundTool
        print("✓ Beautified EMD Refund imported successfully")
        
        # Create a simple test instance
        tool = SimpleEMDRefundTool()
        print("✓ Beautified EMD Refund instantiated successfully")
        
        # Close the window immediately to avoid blocking
        tool.root.destroy()
        print("✓ Beautified EMD Refund test completed")
        return True
    except Exception as e:
        print(f"✗ Beautified EMD Refund test failed: {e}")
        return False

def test_deductions_table():
    """Test the deductions table tool (already beautified)"""
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
    print("Testing Beautified PWD Tools...")
    print("=" * 40)
    
    results = []
    results.append(test_delay_calculator())
    results.append(test_stamp_duty())
    results.append(test_emd_refund())
    results.append(test_deductions_table())
    
    print("=" * 40)
    if all(results):
        print("✓ All beautified tools tests passed!")
        return 0
    else:
        print("✗ Some beautified tools tests failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main())