#!/usr/bin/env python3
"""
Verification script for GUI components.
"""

import sys
import os

# Add the src directory to the path so we can import bridge_gad modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

print("Verifying GUI components...")

# Check if tkinter is available
try:
    import tkinter as tk
    from tkinter import ttk
    print("✅ Tkinter is available")
except ImportError as e:
    print(f"❌ Tkinter not available: {e}")

# Check if the GUI module can be imported
try:
    import bridge_gad.gui
    print("✅ GUI module can be imported")
except ImportError as e:
    print(f"❌ GUI module cannot be imported: {e}")

# Check if the geometry module can be imported
try:
    import bridge_gad.geometry
    print("✅ Geometry module can be imported")
except ImportError as e:
    print(f"❌ Geometry module cannot be imported: {e}")

# Check if the io_utils module can be imported
try:
    import bridge_gad.io_utils
    print("✅ IO utilities module can be imported")
except ImportError as e:
    print(f"❌ IO utilities module cannot be imported: {e}")

# Check if the config module can be imported
try:
    import bridge_gad.config
    print("✅ Config module can be imported")
except ImportError as e:
    print(f"❌ Config module cannot be imported: {e}")

print("\nVerification complete!")