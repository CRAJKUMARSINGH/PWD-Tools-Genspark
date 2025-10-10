#!/usr/bin/env python3
"""
Test script to verify GUI functionality.
"""

import sys
import os

# Add the src directory to the path so we can import bridge_gad modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_gui_import():
    """Test importing the GUI module."""
    try:
        from bridge_gad.gui import BridgeGADApp
        print("✅ GUI module imported successfully")
        return True
    except Exception as e:
        print(f"❌ Error importing GUI module: {e}")
        return False

def test_geometry_import():
    """Test importing the geometry module."""
    try:
        from bridge_gad.geometry import summarize
        print("✅ Geometry module imported successfully")
        return True
    except Exception as e:
        print(f"❌ Error importing geometry module: {e}")
        return False

def test_summarize_function():
    """Test the summarize function."""
    try:
        from bridge_gad.geometry import summarize
        results = summarize(20.0, 15.0, 2.1e8, 0.0025)
        print("✅ Summarize function works correctly")
        print(f"   Results: {results}")
        return True
    except Exception as e:
        print(f"❌ Error in summarize function: {e}")
        return False

if __name__ == "__main__":
    print("Testing GUI functionality...")
    
    test_gui_import()
    test_geometry_import()
    test_summarize_function()
    
    print("\nAll tests completed!")