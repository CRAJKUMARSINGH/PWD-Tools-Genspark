#!/usr/bin/env python3
"""
Minimal test to verify GUI components can be imported.
"""

import sys
import os

# Add the src directory to the path so we can import bridge_gad modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

print("Testing GUI component imports...")

# Test importing tkinter components
try:
    import tkinter as tk
    from tkinter import ttk, messagebox, filedialog
    print("✅ Tkinter components imported successfully")
except ImportError as e:
    print(f"❌ Error importing tkinter components: {e}")
    sys.exit(1)

# Test importing bridge_gad modules
try:
    from bridge_gad.geometry import summarize
    from bridge_gad.io_utils import save_results_to_excel
    from bridge_gad.config import DEFAULT_E, DEFAULT_I
    print("✅ Bridge_GAD modules imported successfully")
except ImportError as e:
    print(f"❌ Error importing Bridge_GAD modules: {e}")
    sys.exit(1)

# Test the summarize function
try:
    results = summarize(20.0, 15.0, DEFAULT_E, DEFAULT_I)
    print("✅ Summarize function works correctly")
    print(f"   Sample results: {list(results.items())[:2]}...")  # Show first 2 items
except Exception as e:
    print(f"❌ Error in summarize function: {e}")
    sys.exit(1)

print("\n✅ All GUI components verified successfully!")
print("The GUI application should work correctly.")