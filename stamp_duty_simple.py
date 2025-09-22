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
        # Header
        header = tk.Label(
            self.root,
            text="Stamp Duty Calculator",
            font=("Arial", 18, "bold"),
            fg="blue"
        )
        header.pack(pady=20)
        
        # Main frame
        main_frame = tk.Frame(self.root)
        main_frame.pack(pady=20)
        
        # Work Order Amount input
        tk.Label(main_frame, text="Enter Work Order Amount (₹):", font=("Arial", 12, "bold")).pack(pady=10)
        self.work_order_entry = tk.Entry(main_frame, width=30, font=("Arial", 12))
        self.work_order_entry.pack(pady=10)
        
        # Calculate button
        calc_btn = tk.Button(main_frame, text="Calculate", command=self.calculate_stamp_duty, 
                           width=20, height=2, font=("Arial", 12, "bold"), bg="lightblue")
        calc_btn.pack(pady=20)
        
        # Results display
        self.result_label = tk.Label(
            main_frame, 
            text="", 
            font=("Arial", 14, "bold"),
            fg="green"
        )
        self.result_label.pack(pady=10)
    
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