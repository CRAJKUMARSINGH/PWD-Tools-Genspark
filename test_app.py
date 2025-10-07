import tkinter as tk
from tkinter import messagebox
import sys
import os

def test_tkinter():
    try:
        print("Creating root window...")
        root = tk.Tk()
        root.title("Test Window")
        root.geometry("300x200")
        
        label = tk.Label(root, text="Tkinter is working!")
        label.pack(pady=20)
        
        def close_app():
            print("Closing application...")
            root.destroy()
        
        button = tk.Button(root, text="Close", command=close_app)
        button.pack(pady=10)
        
        print("Starting mainloop...")
        root.mainloop()
        print("Application closed.")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("Python version:", sys.version)
    print("Current directory:", os.getcwd())
    test_tkinter()