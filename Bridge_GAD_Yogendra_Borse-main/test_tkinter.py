#!/usr/bin/env python3
"""
Simple test to verify tkinter is working.
"""

try:
    import tkinter as tk
    from tkinter import ttk
    
    print("✅ Tkinter is available")
    
    # Create a simple window to verify GUI functionality
    root = tk.Tk()
    root.title("Tkinter Test")
    root.geometry("300x200")
    
    label = ttk.Label(root, text="Tkinter is working!")
    label.pack(pady=20)
    
    button = ttk.Button(root, text="Close", command=root.destroy)
    button.pack(pady=10)
    
    print("✅ Tkinter window created successfully")
    print("If you see a window, tkinter is working correctly.")
    
    # Don't start the mainloop to avoid blocking the script
    root.update()
    root.destroy()
    
except ImportError as e:
    print(f"❌ Tkinter not available: {e}")
except Exception as e:
    print(f"❌ Error with tkinter: {e}")

print("\nTest completed!")