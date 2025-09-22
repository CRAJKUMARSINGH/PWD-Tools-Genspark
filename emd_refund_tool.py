"""
EMD Refund Tool - Dedicated EMD Refund Calculator
Separate from other tools
"""

import tkinter as tk
from tkinter import messagebox, ttk
import tempfile
import webbrowser
import os


class EMDRefundTool:
    def __init__(self):
        """Initialize EMD Refund tool"""
        self.root = tk.Tk()
        self.root.title("EMD Refund Calculator")
        self.root.geometry("600x500")
        self.root.minsize(600, 500)
        
        # Create interface
        self.create_interface()
    
    def create_interface(self):
        """Create interface"""
        # Configure root window background
        self.root.configure(bg="#f0f4f8")
        
        # Header with gradient effect
        header_frame = tk.Frame(self.root, bg="#f093fb", height=80)
        header_frame.pack(fill="x", padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        header = tk.Label(
            header_frame,
            text="💰 EMD Refund Calculator",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#f093fb"
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
            text="Earnest Money Deposit Refund Calculator",
            font=("Arial", 16, "bold"),
            fg="#2d3748",
            bg="#ffffff"
        )
        title_label.pack(pady=20)
        
        # Form fields
        fields_frame = tk.Frame(form_container, bg="#ffffff")
        fields_frame.pack(pady=20, padx=20, fill="x")
        
        # Tender Number
        tk.Label(fields_frame, text="Tender Number:", font=("Arial", 12), bg="#ffffff").grid(row=0, column=0, sticky="w", pady=5)
        self.tender_entry = tk.Entry(fields_frame, font=("Arial", 12), width=30)
        self.tender_entry.grid(row=0, column=1, pady=5, padx=(10, 0))
        
        # Contractor Name
        tk.Label(fields_frame, text="Contractor Name:", font=("Arial", 12), bg="#ffffff").grid(row=1, column=0, sticky="w", pady=5)
        self.contractor_entry = tk.Entry(fields_frame, font=("Arial", 12), width=30)
        self.contractor_entry.grid(row=1, column=1, pady=5, padx=(10, 0))
        
        # EMD Amount
        tk.Label(fields_frame, text="EMD Amount (₹):", font=("Arial", 12), bg="#ffffff").grid(row=2, column=0, sticky="w", pady=5)
        self.emd_entry = tk.Entry(fields_frame, font=("Arial", 12), width=30)
        self.emd_entry.grid(row=2, column=1, pady=5, padx=(10, 0))
        
        # Tender Date
        tk.Label(fields_frame, text="Tender Date (DD/MM/YYYY):", font=("Arial", 12), bg="#ffffff").grid(row=3, column=0, sticky="w", pady=5)
        self.tender_date_entry = tk.Entry(fields_frame, font=("Arial", 12), width=30)
        self.tender_date_entry.grid(row=3, column=1, pady=5, padx=(10, 0))
        
        # Validity Date
        tk.Label(fields_frame, text="Validity Date (DD/MM/YYYY):", font=("Arial", 12), bg="#ffffff").grid(row=4, column=0, sticky="w", pady=5)
        self.validity_date_entry = tk.Entry(fields_frame, font=("Arial", 12), width=30)
        self.validity_date_entry.grid(row=4, column=1, pady=5, padx=(10, 0))
        
        # Buttons frame
        buttons_frame = tk.Frame(form_container, bg="#ffffff")
        buttons_frame.pack(pady=20)
        
        # Calculate button
        calc_btn = tk.Button(
            buttons_frame,
            text="💰 Calculate EMD Refund",
            command=self.calculate_emd_refund,
            width=25,
            height=2,
            font=("Arial", 12, "bold"),
            bg="#f093fb",
            fg="white",
            relief="raised",
            bd=2,
            cursor="hand2"
        )
        calc_btn.pack(pady=10)
        
        # Result label
        self.result_label = tk.Label(
            form_container,
            text="",
            font=("Arial", 14, "bold"),
            fg="#2d3748",
            bg="#ffffff"
        )
        self.result_label.pack(pady=10)
        
        # Footer
        footer_label = tk.Label(
            main_frame,
            text="EMD Refund Calculator - PWD Tools",
            font=("Arial", 10),
            fg="#718096",
            bg="#f0f4f8"
        )
        footer_label.pack(side="bottom", pady=10)
    
    def calculate_emd_refund(self):
        """Calculate EMD refund"""
        try:
            # Get input values
            tender_no = self.tender_entry.get().strip()
            contractor = self.contractor_entry.get().strip()
            emd_amount = self.emd_entry.get().strip()
            tender_date = self.tender_date_entry.get().strip()
            validity_date = self.validity_date_entry.get().strip()
            
            # Validate inputs
            if not all([tender_no, contractor, emd_amount, tender_date, validity_date]):
                messagebox.showerror("Error", "Please fill in all fields")
                return
            
            # Convert EMD amount to float
            try:
                emd_value = float(emd_amount)
                if emd_value <= 0:
                    raise ValueError("EMD amount must be greater than 0")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid EMD amount")
                return
            
            # Calculate refund (simplified logic)
            # In real implementation, this would check tender status, completion, etc.
            refund_amount = emd_value  # Full refund for demonstration
            
            # Display result
            result_text = f"EMD Refund Amount: ₹ {refund_amount:,.2f}"
            self.result_label.config(text=result_text)
            
            # Show success message
            messagebox.showinfo("Success", f"EMD Refund Calculated Successfully!\n\n{result_text}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Calculation error: {str(e)}")
    
    def run(self):
        """Start the application"""
        self.root.mainloop()


def main():
    """Main entry point"""
    try:
        app = EMDRefundTool()
        app.run()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start EMD Refund Tool: {str(e)}")


if __name__ == "__main__":
    main()
