"""
Stamp Duty Tool - SIMPLE VERSION
For Lower Divisional Clerks - Only one input needed (Work Order Amount)
Based on original repository implementation
"""

import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class SimpleStampDutyTool:
    def __init__(self):
        """Initialize Simple Stamp Duty tool"""
        self.root = tk.Tk()
        self.root.title("Stamp Duty Calculator")
        self.root.geometry("400x300")
        self.root.minsize(400, 300)
        
        # Create interface
        self.create_interface()
    
    def create_interface(self):
        """Create interface"""
        # Configure root window background
        self.root.configure(bg="#f0f8ff")
        
        # Header with gradient effect
        header_frame = tk.Frame(self.root, bg="#4ecdc4", height=80)
        header_frame.pack(fill="x", padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        header = tk.Label(
            header_frame,
            text="📋 Stamp Duty Calculator",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#4ecdc4"
        )
        header.pack(pady=20)
        
        # Main frame with colored background
        main_frame = tk.Frame(self.root, bg="#f0f8ff")
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Form container with border and shadow effect
        form_container = tk.Frame(main_frame, bg="#ffffff", relief="raised", bd=2)
        form_container.pack(pady=10, padx=10, fill="both", expand=True)
        
        # Title
        title_label = tk.Label(
            form_container,
            text="Work Order Stamp Duty Calculation",
            font=("Arial", 16, "bold"),
            fg="#4ecdc4",
            bg="#ffffff"
        )
        title_label.pack(pady=20)
        
        # Work Order Amount input
        tk.Label(form_container, text="Enter Work Order Amount (₹):", font=("Arial", 12, "bold"), bg="#ffffff", fg="#ff6b6b").pack(pady=10)
        self.work_order_entry = tk.Entry(form_container, width=30, font=("Arial", 12))
        self.work_order_entry.pack(pady=10)
        
        # Calculate button with improved styling
        calc_btn = tk.Button(form_container, text="Calculate Stamp Duty", command=self.calculate_stamp_duty, 
                           width=25, height=2, font=("Arial", 12, "bold"), 
                           bg="#ff6b6b", fg="white", relief="raised", bd=2)
        calc_btn.pack(pady=20)
        
        # Results display
        self.result_label = tk.Label(
            form_container, 
            text="", 
            font=("Arial", 14, "bold"),
            fg="green",
            bg="#ffffff"
        )
        self.result_label.pack(pady=15)
        
        # Footer
        footer_label = tk.Label(
            main_frame,
            text="Stamp Duty Calculator - PWD Tools",
            font=("Arial", 10),
            fg="#718096",
            bg="#f0f8ff"
        )
        footer_label.pack(side="bottom", pady=10)
    
    def calculate_stamp_duty(self):
        """Calculate stamp duty based on work order amount"""
        try:
            # Get input value
            input_value = self.work_order_entry.get().strip()
            print(f"Input value: '{input_value}'")  # Debug
            
            if not input_value:
                messagebox.showerror("Error", "Please enter a work order amount")
                return
                
            work_order_amount = float(input_value)
            print(f"Parsed amount: {work_order_amount}")  # Debug
            
            if work_order_amount <= 0:
                messagebox.showerror("Error", "Work Order Amount must be greater than 0")
                return
            
            # Calculate stamp duty based on original repository logic
            if work_order_amount <= 5000000:
                stamp_duty = 1000
            else:
                stamp_duty = round(work_order_amount * 0.0015)
                if stamp_duty > 2500000:
                    stamp_duty = 2500000
            
            print(f"Calculated stamp duty: {stamp_duty}")  # Debug
            
            # Display result with proper formatting - only the stamp duty amount
            result_text = f"Stamp Duty Amount: ₹ {stamp_duty:,}"
            self.result_label.config(text=result_text)
            print(f"Result displayed: {result_text}")  # Debug
            
        except ValueError as e:
            print(f"ValueError: {e}")  # Debug
            messagebox.showerror("Error", "Please enter a valid work order amount")
        except Exception as e:
            print(f"Exception: {e}")  # Debug
            messagebox.showerror("Error", f"Calculation error: {str(e)}")
    
    def run(self):
        """Start the application"""
        self.root.mainloop()


if __name__ == "__main__":
    app = SimpleStampDutyTool()
    app.run()