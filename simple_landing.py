"""
Simple PWD Tools Landing Page - Minimal version for testing
"""

import tkinter as tk
from tkinter import messagebox
import webbrowser
import os
import sys
import subprocess

class SimplePWDLanding:
    def __init__(self):
        """Initialize simple landing page"""
        self.root = tk.Tk()
        self.root.title("PWD Tools - Simple Test")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f8ff")
        
        # Create simple interface
        self.create_interface()
    
    def create_interface(self):
        """Create simple interface"""
        # Header
        header = tk.Label(
            self.root,
            text="PWD Tools - Simple Test",
            font=("Arial", 16, "bold"),
            bg="#2E8B57",
            fg="white"
        )
        header.pack(fill="x", pady=10)
        
        # Welcome message
        welcome = tk.Label(
            self.root,
            text="Click buttons below to test tools",
            font=("Arial", 12),
            bg="#f0f8ff"
        )
        welcome.pack(pady=10)
        
        # Tool buttons
        btn_frame = tk.Frame(self.root, bg="#f0f8ff")
        btn_frame.pack(pady=20)
        
        # Hindi Bill Note button
        hindi_btn = tk.Button(
            btn_frame,
            text="Hindi Bill Note",
            command=self.open_hindi_bill,
            width=20,
            height=2,
            bg="#FF6B6B",
            fg="white"
        )
        hindi_btn.pack(pady=5)
        
        # Stamp Duty button
        stamp_btn = tk.Button(
            btn_frame,
            text="Stamp Duty Calculator",
            command=self.open_stamp_duty,
            width=20,
            height=2,
            bg="#4ECDC4",
            fg="white"
        )
        stamp_btn.pack(pady=5)
        
        # EMD Refund button
        emd_btn = tk.Button(
            btn_frame,
            text="EMD Refund",
            command=self.open_emd_refund,
            width=20,
            height=2,
            bg="#45B7D1",
            fg="white"
        )
        emd_btn.pack(pady=5)
        
        # Status label
        self.status_label = tk.Label(
            self.root,
            text="Ready",
            font=("Arial", 10),
            bg="#f0f8ff"
        )
        self.status_label.pack(side="bottom", pady=10)
    
    def update_status(self, message):
        """Update status message"""
        self.status_label.config(text=message)
    
    def open_hindi_bill(self):
        """Open Hindi Bill Note tool"""
        try:
            if os.path.exists("hindi_bill_simple.py"):
                subprocess.Popen([sys.executable, "hindi_bill_simple.py"])
                self.update_status("Hindi Bill Note opened")
            else:
                messagebox.showerror("Error", "hindi_bill_simple.py not found")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Hindi Bill Note: {e}")
    
    def open_stamp_duty(self):
        """Open Stamp Duty tool"""
        try:
            if os.path.exists("stamp_duty_simple.py"):
                subprocess.Popen([sys.executable, "stamp_duty_simple.py"])
                self.update_status("Stamp Duty Calculator opened")
            else:
                messagebox.showerror("Error", "stamp_duty_simple.py not found")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Stamp Duty Calculator: {e}")
    
    def open_emd_refund(self):
        """Open EMD Refund tool"""
        try:
            if os.path.exists("emd_refund_simple.py"):
                subprocess.Popen([sys.executable, "emd_refund_simple.py"])
                self.update_status("EMD Refund opened")
            else:
                messagebox.showerror("Error", "emd_refund_simple.py not found")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open EMD Refund: {e}")
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = SimplePWDLanding()
    app.run()