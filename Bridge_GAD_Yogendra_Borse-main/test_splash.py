#!/usr/bin/env python3
"""Test script to verify splash screen functionality."""

import tkinter as tk
from src.bridge_gad.gui import show_splash

def test_splash():
    """Test the splash screen functionality."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Show splash screen for 3 seconds
    show_splash(root, 3.0)
    
    # Close after 4 seconds
    root.after(4000, root.destroy)
    
    root.mainloop()

if __name__ == "__main__":
    test_splash()