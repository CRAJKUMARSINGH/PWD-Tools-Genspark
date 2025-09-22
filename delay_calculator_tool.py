"""
Delay Calculator Tool - Dedicated Delay Calculator
Separate from other tools
"""

import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime, timedelta
import tempfile
import webbrowser
import os


class DelayCalculatorTool:
    def __init__(self):
        """Initialize Delay Calculator tool"""
        self.root = tk.Tk()
        self.root.title("Delay Calculator")
        self.root.geometry("600x500")
        self.root.minsize(600, 500)
        
        # Create interface
        self.create_interface()
    
    def create_interface(self):
        """Create interface"""
        # Configure root window background
        self.root.configure(bg="#f0f4f8")
        
        # Header with gradient effect
        header_frame = tk.Frame(self.root, bg="#45b7d1", height=80)
        header_frame.pack(fill="x", padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        header = tk.Label(
            header_frame,
            text="⏰ Delay Calculator",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#45b7d1"
        )
        header.pack(pady=20)
        
        # Main frame
        main_frame = tk.Frame(self.root, bg="#f0f4f8")
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Form container
        form_container = tk.Frame(main_frame, bg="#ffffff", relief="raised", bd=2)
        form_container.pack(pady=10, padx=10, fill="both", expand=True)
        
        # Title
        title_label = tk.Label(
            form_container,
            text="Project Delay Analysis Calculator",
            font=("Arial", 16, "bold"),
            fg="#2d3748",
            bg="#ffffff"
        )
        title_label.pack(pady=20)
        
        # Form fields
        fields_frame = tk.Frame(form_container, bg="#ffffff")
        fields_frame.pack(pady=20, padx=20, fill="x")
        
        # Work Name
        tk.Label(fields_frame, text="Work Name:", font=("Arial", 12), bg="#ffffff").grid(row=0, column=0, sticky="w", pady=5)
        self.work_entry = tk.Entry(fields_frame, font=("Arial", 12), width=30)
        self.work_entry.grid(row=0, column=1, pady=5, padx=(10, 0))
        
        # Start Date
        tk.Label(fields_frame, text="Start Date (DD/MM/YYYY):", font=("Arial", 12), bg="#ffffff").grid(row=1, column=0, sticky="w", pady=5)
        self.start_date_entry = tk.Entry(fields_frame, font=("Arial", 12), width=30)
        self.start_date_entry.grid(row=1, column=1, pady=5, padx=(10, 0))
        
        # Completion Date
        tk.Label(fields_frame, text="Completion Date (DD/MM/YYYY):", font=("Arial", 12), bg="#ffffff").grid(row=2, column=0, sticky="w", pady=5)
        self.completion_date_entry = tk.Entry(fields_frame, font=("Arial", 12), width=30)
        self.completion_date_entry.grid(row=2, column=1, pady=5, padx=(10, 0))
        
        # Contract Period (Days)
        tk.Label(fields_frame, text="Contract Period (Days):", font=("Arial", 12), bg="#ffffff").grid(row=3, column=0, sticky="w", pady=5)
        self.contract_period_entry = tk.Entry(fields_frame, font=("Arial", 12), width=30)
        self.contract_period_entry.grid(row=3, column=1, pady=5, padx=(10, 0))
        
        # Buttons frame
        buttons_frame = tk.Frame(form_container, bg="#ffffff")
        buttons_frame.pack(pady=20)
        
        # Calculate button
        calc_btn = tk.Button(
            buttons_frame,
            text="⏰ Calculate Delay",
            command=self.calculate_delay,
            width=25,
            height=2,
            font=("Arial", 12, "bold"),
            bg="#45b7d1",
            fg="white",
            relief="raised",
            bd=2,
            cursor="hand2"
        )
        calc_btn.pack(pady=10)
        
        # Results frame
        results_frame = tk.Frame(form_container, bg="#ffffff")
        results_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Results labels
        self.work_label = tk.Label(results_frame, text="", font=("Arial", 12), bg="#ffffff", fg="#2d3748")
        self.work_label.pack(anchor="w")
        
        self.start_label = tk.Label(results_frame, text="", font=("Arial", 12), bg="#ffffff", fg="#2d3748")
        self.start_label.pack(anchor="w")
        
        self.completion_label = tk.Label(results_frame, text="", font=("Arial", 12), bg="#ffffff", fg="#2d3748")
        self.completion_label.pack(anchor="w")
        
        self.contract_label = tk.Label(results_frame, text="", font=("Arial", 12), bg="#ffffff", fg="#2d3748")
        self.contract_label.pack(anchor="w")
        
        self.actual_label = tk.Label(results_frame, text="", font=("Arial", 12), bg="#ffffff", fg="#2d3748")
        self.actual_label.pack(anchor="w")
        
        self.delay_label = tk.Label(results_frame, text="", font=("Arial", 14, "bold"), bg="#ffffff", fg="#e53e3e")
        self.delay_label.pack(anchor="w", pady=(10, 0))
        
        # Footer
        footer_label = tk.Label(
            main_frame,
            text="Delay Calculator - PWD Tools",
            font=("Arial", 10),
            fg="#718096",
            bg="#f0f4f8"
        )
        footer_label.pack(side="bottom", pady=10)
    
    def parse_date(self, date_str):
        """Parse date string in DD/MM/YYYY format"""
        try:
            return datetime.strptime(date_str, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD/MM/YYYY")
    
    def calculate_delay(self):
        """Calculate project delay"""
        try:
            # Get input values
            work_name = self.work_entry.get().strip()
            start_date_str = self.start_date_entry.get().strip()
            completion_date_str = self.completion_date_entry.get().strip()
            contract_period_str = self.contract_period_entry.get().strip()
            
            # Validate inputs
            if not all([work_name, start_date_str, completion_date_str, contract_period_str]):
                messagebox.showerror("Error", "Please fill in all fields")
                return
            
            # Parse dates
            start_date = self.parse_date(start_date_str)
            completion_date = self.parse_date(completion_date_str)
            
            # Parse contract period
            try:
                contract_period = int(contract_period_str)
                if contract_period <= 0:
                    raise ValueError("Contract period must be greater than 0")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid contract period")
                return
            
            # Calculate actual period
            actual_period = (completion_date - start_date).days
            
            # Calculate delay
            delay_days = actual_period - contract_period
            
            # Display results
            self.work_label.config(text=f"Work Name: {work_name}")
            self.start_label.config(text=f"Start Date: {start_date.strftime('%d/%m/%Y')}")
            self.completion_label.config(text=f"Completion Date: {completion_date.strftime('%d/%m/%Y')}")
            self.contract_label.config(text=f"Contract Period: {contract_period} days")
            self.actual_label.config(text=f"Actual Period: {actual_period} days")
            
            if delay_days > 0:
                self.delay_label.config(text=f"Delay: {delay_days} days", fg="#e53e3e")
                delay_status = f"Project is delayed by {delay_days} days"
            elif delay_days < 0:
                self.delay_label.config(text=f"Early Completion: {abs(delay_days)} days", fg="#38a169")
                delay_status = f"Project completed {abs(delay_days)} days early"
            else:
                self.delay_label.config(text="No Delay", fg="#38a169")
                delay_status = "Project completed on time"
            
            # Show success message
            messagebox.showinfo("Delay Analysis", f"Delay Analysis Complete!\n\n{delay_status}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Calculation error: {str(e)}")
    
    def run(self):
        """Start the application"""
        self.root.mainloop()


def main():
    """Main entry point"""
    try:
        app = DelayCalculatorTool()
        app.run()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start Delay Calculator Tool: {str(e)}")


if __name__ == "__main__":
    main()
