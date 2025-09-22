"""
Deductions Table Tool - Dedicated Deductions Calculator
Separate from other tools
"""

import tkinter as tk
from tkinter import messagebox, ttk
import tempfile
import webbrowser
import os


class DeductionsTableTool:
    def __init__(self):
        """Initialize Deductions Table tool"""
        self.root = tk.Tk()
        self.root.title("Deductions Table Calculator")
        self.root.geometry("700x600")
        self.root.minsize(700, 600)
        
        # Create interface
        self.create_interface()
    
    def create_interface(self):
        """Create interface"""
        # Configure root window background
        self.root.configure(bg="#f0f4f8")
        
        # Header with gradient effect
        header_frame = tk.Frame(self.root, bg="#4ecdc4", height=80)
        header_frame.pack(fill="x", padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        header = tk.Label(
            header_frame,
            text="📊 Deductions Table Calculator",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#4ecdc4"
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
            text="Tax and Deductions Calculator",
            font=("Arial", 16, "bold"),
            fg="#2d3748",
            bg="#ffffff"
        )
        title_label.pack(pady=20)
        
        # Form fields
        fields_frame = tk.Frame(form_container, bg="#ffffff")
        fields_frame.pack(pady=20, padx=20, fill="x")
        
        # Gross Amount
        tk.Label(fields_frame, text="Gross Amount (₹):", font=("Arial", 12), bg="#ffffff").grid(row=0, column=0, sticky="w", pady=5)
        self.gross_entry = tk.Entry(fields_frame, font=("Arial", 12), width=30)
        self.gross_entry.grid(row=0, column=1, pady=5, padx=(10, 0))
        
        # TDS Rate
        tk.Label(fields_frame, text="TDS Rate (%):", font=("Arial", 12), bg="#ffffff").grid(row=1, column=0, sticky="w", pady=5)
        self.tds_rate_entry = tk.Entry(fields_frame, font=("Arial", 12), width=30)
        self.tds_rate_entry.insert(0, "10")  # Default 10%
        self.tds_rate_entry.grid(row=1, column=1, pady=5, padx=(10, 0))
        
        # GST Rate
        tk.Label(fields_frame, text="GST Rate (%):", font=("Arial", 12), bg="#ffffff").grid(row=2, column=0, sticky="w", pady=5)
        self.gst_rate_entry = tk.Entry(fields_frame, font=("Arial", 12), width=30)
        self.gst_rate_entry.insert(0, "18")  # Default 18%
        self.gst_rate_entry.grid(row=2, column=1, pady=5, padx=(10, 0))
        
        # Other Deductions
        tk.Label(fields_frame, text="Other Deductions (₹):", font=("Arial", 12), bg="#ffffff").grid(row=3, column=0, sticky="w", pady=5)
        self.other_entry = tk.Entry(fields_frame, font=("Arial", 12), width=30)
        self.other_entry.insert(0, "0")  # Default 0
        self.other_entry.grid(row=3, column=1, pady=5, padx=(10, 0))
        
        # Buttons frame
        buttons_frame = tk.Frame(form_container, bg="#ffffff")
        buttons_frame.pack(pady=20)
        
        # Calculate button
        calc_btn = tk.Button(
            buttons_frame,
            text="📊 Calculate Deductions",
            command=self.calculate_deductions,
            width=25,
            height=2,
            font=("Arial", 12, "bold"),
            bg="#4ecdc4",
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
        self.gross_label = tk.Label(results_frame, text="", font=("Arial", 12), bg="#ffffff", fg="#2d3748")
        self.gross_label.pack(anchor="w")
        
        self.tds_label = tk.Label(results_frame, text="", font=("Arial", 12), bg="#ffffff", fg="#e53e3e")
        self.tds_label.pack(anchor="w")
        
        self.gst_label = tk.Label(results_frame, text="", font=("Arial", 12), bg="#ffffff", fg="#e53e3e")
        self.gst_label.pack(anchor="w")
        
        self.other_label = tk.Label(results_frame, text="", font=("Arial", 12), bg="#ffffff", fg="#e53e3e")
        self.other_label.pack(anchor="w")
        
        self.total_deductions_label = tk.Label(results_frame, text="", font=("Arial", 12, "bold"), bg="#ffffff", fg="#e53e3e")
        self.total_deductions_label.pack(anchor="w")
        
        self.net_amount_label = tk.Label(results_frame, text="", font=("Arial", 14, "bold"), bg="#ffffff", fg="#2d3748")
        self.net_amount_label.pack(anchor="w", pady=(10, 0))
        
        # Footer
        footer_label = tk.Label(
            main_frame,
            text="Deductions Table Calculator - PWD Tools",
            font=("Arial", 10),
            fg="#718096",
            bg="#f0f4f8"
        )
        footer_label.pack(side="bottom", pady=10)
    
    def calculate_deductions(self):
        """Calculate deductions"""
        try:
            # Get input values
            gross_amount = self.gross_entry.get().strip()
            tds_rate = self.tds_rate_entry.get().strip()
            gst_rate = self.gst_rate_entry.get().strip()
            other_deductions = self.other_entry.get().strip()
            
            # Validate inputs
            if not gross_amount:
                messagebox.showerror("Error", "Please enter gross amount")
                return
            
            # Convert to float
            try:
                gross = float(gross_amount)
                tds_rate_val = float(tds_rate) if tds_rate else 0
                gst_rate_val = float(gst_rate) if gst_rate else 0
                other = float(other_deductions) if other_deductions else 0
                
                if gross <= 0:
                    raise ValueError("Gross amount must be greater than 0")
                    
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numeric values")
                return
            
            # Calculate deductions
            tds_amount = (gross * tds_rate_val) / 100
            gst_amount = (gross * gst_rate_val) / 100
            total_deductions = tds_amount + gst_amount + other
            net_amount = gross - total_deductions
            
            # Display results
            self.gross_label.config(text=f"Gross Amount: ₹ {gross:,.2f}")
            self.tds_label.config(text=f"TDS ({tds_rate_val}%): ₹ {tds_amount:,.2f}")
            self.gst_label.config(text=f"GST ({gst_rate_val}%): ₹ {gst_amount:,.2f}")
            self.other_label.config(text=f"Other Deductions: ₹ {other:,.2f}")
            self.total_deductions_label.config(text=f"Total Deductions: ₹ {total_deductions:,.2f}")
            self.net_amount_label.config(text=f"Net Amount: ₹ {net_amount:,.2f}")
            
            # Show success message
            messagebox.showinfo("Success", f"Deductions Calculated Successfully!\n\nNet Amount: ₹ {net_amount:,.2f}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Calculation error: {str(e)}")
    
    def run(self):
        """Start the application"""
        self.root.mainloop()


def main():
    """Main entry point"""
    try:
        app = DeductionsTableTool()
        app.run()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start Deductions Table Tool: {str(e)}")


if __name__ == "__main__":
    main()
