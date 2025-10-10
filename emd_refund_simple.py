"""
EMD Refund Tool - ULTRA SIMPLE VERSION
For Lower Divisional Clerks - Only 3 inputs needed
Payee Name, Amount, Work Description
"""

import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import os
import sqlite3

class SimpleEMDRefundTool:
    def __init__(self):
        """Initialize Ultra Simple EMD Refund tool"""
        self.root = tk.Tk()
        self.root.title("EMD Refund - Ultra Simple")
        
        # Make responsive for different screen sizes
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Adjust window size based on screen size
        if screen_width < 1024:  # Mobile/Tablet
            self.root.geometry(f"{min(screen_width-20, 400)}x{min(screen_height-50, 500)}")
        else:  # Desktop
            self.root.geometry("600x500")
        
        # Make window resizable
        self.root.minsize(400, 500)
        
        # Simple database
        self.init_database()
        
        # Create interface
        self.create_interface()
    
    def init_database(self):
        """Initialize simple database"""
        self.conn = sqlite3.connect('emd_refund.db')
        self.cursor = self.conn.cursor()
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS emd_refund_records (
                id INTEGER PRIMARY KEY,
                payee_name TEXT,
                amount REAL,
                work_description TEXT,
                refund_date TEXT,
                date_created TEXT
            )
        ''')
        self.conn.commit()
    
    def create_interface(self):
        """Create ultra simple interface"""
        # Create scrollable frame for mobile compatibility
        self.main_canvas = tk.Canvas(self.root)
        self.main_scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.main_canvas.yview)
        self.scrollable_frame = tk.Frame(self.main_canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all"))
        )
        
        self.main_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.main_canvas.configure(yscrollcommand=self.main_scrollbar.set)
        
        self.main_canvas.pack(side="left", fill="both", expand=True)
        self.main_scrollbar.pack(side="right", fill="y")
        
        # Header
        header = tk.Label(
            self.scrollable_frame,
            text="EMD Refund - Ultra Simple",
            font=("Arial", 18, "bold"),
            fg="blue"
        )
        header.pack(pady=10)
        
        # Main frame
        main_frame = tk.LabelFrame(self.scrollable_frame, text="EMD Refund Details - Only 3 Fields!", font=("Arial", 12, "bold"))
        main_frame.pack(fill="x", padx=10, pady=5)
        
        # Only 3 inputs as requested
        # 1. Payee Name
        tk.Label(main_frame, text="1. Payee Name:", font=("Arial", 12, "bold"), fg="red").pack(pady=5)
        self.payee_name_entry = tk.Entry(main_frame, width=50, font=("Arial", 12))
        self.payee_name_entry.pack(pady=5)
        
        # 2. Amount
        tk.Label(main_frame, text="2. Amount (₹):", font=("Arial", 12, "bold"), fg="red").pack(pady=5)
        self.amount_entry = tk.Entry(main_frame, width=50, font=("Arial", 12))
        self.amount_entry.pack(pady=5)
        
        # 3. Work Description
        tk.Label(main_frame, text="3. Work Description:", font=("Arial", 12, "bold"), fg="red").pack(pady=5)
        self.work_desc_entry = tk.Entry(main_frame, width=50, font=("Arial", 12))
        self.work_desc_entry.pack(pady=5)
        
        # Generate button
        generate_btn = tk.Button(main_frame, text="Generate EMD Refund Receipt", command=self.generate_receipt, 
                               width=30, height=2, font=("Arial", 12, "bold"), bg="lightgreen")
        generate_btn.pack(pady=15)
        
        # Results section
        self.create_results_section(main_frame)
        
        # Action buttons
        self.create_action_buttons(main_frame)
    
    def create_results_section(self, parent):
        """Create results section"""
        results_frame = tk.LabelFrame(parent, text="EMD Refund Receipt", font=("Arial", 12, "bold"))
        results_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Results display - shrunk vertically by 15%
        text_frame = tk.Frame(results_frame)
        text_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.results_text = tk.Text(text_frame, height=8, font=("Arial", 10), wrap="word")  # Reduced height
        scrollbar = tk.Scrollbar(text_frame, orient="vertical", command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=scrollbar.set)
        
        self.results_text.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        self.results_text.insert("1.0", "Fill the 3 fields above and click 'Generate EMD Refund Receipt'")
    
    def create_action_buttons(self, parent):
        """Create action buttons"""
        button_frame = tk.Frame(parent)
        button_frame.pack(fill="x", padx=5, pady=5)
        
        save_btn = tk.Button(button_frame, text="Save Receipt", command=self.save_receipt, 
                           width=15, height=1, font=("Arial", 9), bg="lightblue")
        save_btn.pack(side="left", padx=5)
        
        clear_btn = tk.Button(button_frame, text="Clear Form", command=self.clear_form, 
                            width=15, height=1, font=("Arial", 9), bg="lightgray")
        clear_btn.pack(side="left", padx=5)
        
        print_btn = tk.Button(button_frame, text="Print Receipt", command=self.print_receipt, 
                            width=15, height=1, font=("Arial", 9), bg="lightcoral")
        print_btn.pack(side="left", padx=5)
    
    def generate_receipt(self):
        """Generate EMD refund receipt"""
        try:
            payee_name = self.payee_name_entry.get().strip()
            amount_str = self.amount_entry.get().strip()
            work_description = self.work_desc_entry.get().strip()
            
            if not all([payee_name, amount_str, work_description]):
                messagebox.showerror("Error", "Please fill all 3 fields: Payee Name, Amount, and Work Description")
                return
            
            try:
                amount = float(amount_str)
                if amount <= 0:
                    messagebox.showerror("Error", "Amount must be greater than 0")
                    return
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid amount")
                return
            
            # Generate receipt
            receipt = f"""
EMD REFUND RECEIPT
==================

Receipt No: EMD-{datetime.now().strftime('%Y%m%d%H%M%S')}
Date: {datetime.now().strftime('%d/%m/%Y')}
Time: {datetime.now().strftime('%H:%M:%S')}

PAYEE DETAILS
=============
Payee Name: {payee_name}
Amount: ₹ {amount:,.2f}
Work Description: {work_description}

REFUND DETAILS
==============
Refund Amount: ₹ {amount:,.2f}
Refund Status: APPROVED
Refund Date: {datetime.now().strftime('%d/%m/%Y')}

AUTHORIZATION
=============
Authorized by: PWD Office
Processed by: Lower Divisional Clerk
Date: {datetime.now().strftime('%d/%m/%Y')}

NOTES
=====
This is an EMD (Earnest Money Deposit) refund receipt.
Amount will be processed within 7 working days.

---
Generated by PWD Tools - Simple Version
For Lower Divisional Clerks
"""
            
            # Display results
            self.results_text.delete("1.0", "end")
            self.results_text.insert("1.0", receipt)
            
            # Store receipt data
            self.current_receipt = {
                'payee_name': payee_name,
                'amount': amount,
                'work_description': work_description
            }
            
        except Exception as e:
            messagebox.showerror("Error", f"Receipt generation error: {str(e)}")
    
    def save_receipt(self):
        """Save receipt record"""
        if not hasattr(self, 'current_receipt'):
            messagebox.showwarning("Warning", "Please generate receipt first")
            return
        
        try:
            receipt = self.current_receipt
            self.cursor.execute('''
                INSERT INTO emd_refund_records (
                    payee_name, amount, work_description, refund_date, date_created
                ) VALUES (?, ?, ?, ?, ?)
            ''', (
                receipt['payee_name'],
                receipt['amount'],
                receipt['work_description'],
                datetime.now().strftime('%d/%m/%Y'),
                datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            ))
            
            self.conn.commit()
            messagebox.showinfo("Success", "Receipt saved successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Save error: {str(e)}")
    
    def clear_form(self):
        """Clear form"""
        self.payee_name_entry.delete(0, "end")
        self.amount_entry.delete(0, "end")
        self.work_desc_entry.delete(0, "end")
        
        self.results_text.delete("1.0", "end")
        self.results_text.insert("1.0", "Fill the 3 fields above and click 'Generate EMD Refund Receipt'")
        
        if hasattr(self, 'current_receipt'):
            delattr(self, 'current_receipt')
    
    def print_receipt(self):
        """Print receipt"""
        try:
            receipt = self.results_text.get("1.0", "end-1c")
            if receipt and receipt != "Fill the 3 fields above and click 'Generate EMD Refund Receipt'":
                print("=" * 50)
                print("EMD REFUND RECEIPT")
                print("=" * 50)
                print(receipt)
                print("=" * 50)
                messagebox.showinfo("Success", "Receipt printed to console!")
            else:
                messagebox.showwarning("Warning", "Please generate receipt first")
        except Exception as e:
            messagebox.showerror("Error", f"Print error: {str(e)}")
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = SimpleEMDRefundTool()
    app.run()
