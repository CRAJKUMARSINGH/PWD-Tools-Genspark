"""
EMD Refund Tool - ULTRA SIMPLE VERSION
For Lower Divisional Clerks - Only 3 inputs needed
Payee Name, Amount, Work Description
"""

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os
import sqlite3
import subprocess
import sys
import webbrowser

# Try to import ReportLab for PDF generation, fallback if not available
try:
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
    from reportlab.lib.units import mm
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False
    print("ReportLab not available. PDF printing will be disabled.")

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
            self.root.geometry(f"{min(screen_width-20, 450)}x{min(screen_height-50, 550)}")
        else:  # Desktop
            self.root.geometry("650x550")
        
        # Make window resizable
        self.root.minsize(450, 550)
        
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
        # Configure root window background
        self.root.configure(bg="#f8fafc")
        
        # Header with enhanced styling
        header_frame = tk.Frame(self.root, bg="#f59e0b", height=100)
        header_frame.pack(fill="x", padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        header = tk.Label(
            header_frame,
            text="💰 EMD Refund Tool",
            font=("Arial", 28, "bold"),
            fg="white",
            bg="#f59e0b"
        )
        header.pack(pady=25)
        
        # Subtitle
        subtitle = tk.Label(
            self.root,
            text="Earnest Money Deposit Refund Calculator",
            font=("Arial", 14),
            fg="#64748b",
            bg="#f8fafc"
        )
        subtitle.pack(pady=15)
        
        # Main frame with enhanced styling
        main_frame = tk.Frame(self.root, bg="#f8fafc")
        main_frame.pack(pady=25, padx=30, fill="both", expand=True)
        
        # Form container with enhanced border and shadow effect
        form_container = tk.Frame(main_frame, bg="#ffffff", relief="raised", bd=3)
        form_container.pack(pady=15, padx=15, fill="both", expand=True)
        
        # Title
        title_label = tk.Label(
            form_container,
            text="EMD Refund Details - Only 3 Fields!",
            font=("Arial", 18, "bold"),
            fg="#f59e0b",
            bg="#ffffff"
        )
        title_label.pack(pady=25)
        
        # Only 3 inputs as requested
        # 1. Payee Name
        tk.Label(form_container, text="1. Payee Name:", font=("Arial", 14, "bold"), bg="#ffffff", fg="#ef4444").pack(pady=8)
        self.payee_name_entry = tk.Entry(form_container, width=50, font=("Arial", 13), relief="solid", bd=1)
        self.payee_name_entry.pack(pady=8)
        
        # 2. Amount
        tk.Label(form_container, text="2. Amount (₹):", font=("Arial", 14, "bold"), bg="#ffffff", fg="#ef4444").pack(pady=8)
        self.amount_entry = tk.Entry(form_container, width=50, font=("Arial", 13), relief="solid", bd=1)
        self.amount_entry.pack(pady=8)
        
        # 3. Work Description
        tk.Label(form_container, text="3. Work Description:", font=("Arial", 14, "bold"), bg="#ffffff", fg="#ef4444").pack(pady=8)
        self.work_desc_entry = tk.Entry(form_container, width=50, font=("Arial", 13), relief="solid", bd=1)
        self.work_desc_entry.pack(pady=8)
        
        # Generate button with enhanced styling
        generate_btn = tk.Button(form_container, text="Generate EMD Refund Receipt", command=self.generate_receipt, 
                               width=32, height=2, font=("Arial", 13, "bold"), 
                               bg="#10b981", fg="white", relief="flat", bd=0, cursor="hand2")
        generate_btn.pack(pady=20)
        
        # Add hover effect
        self.add_hover_effect(generate_btn, "#10b981")
        
        # Results section
        self.create_results_section(main_frame)
        
        # Action buttons
        self.create_action_buttons(main_frame)
        
        # Footer
        footer_label = tk.Label(
            main_frame,
            text="EMD Refund Calculator - PWD Tools",
            font=("Arial", 11, "bold"),
            fg="#94a3b8",
            bg="#f8fafc"
        )
        footer_label.pack(side="bottom", pady=15)
    
    def add_hover_effect(self, button, original_color):
        """Add hover effect to button"""
        def on_enter(e):
            # Lighten color on hover
            light_color = self.lighten_color(original_color)
            button.config(bg=light_color)
        
        def on_leave(e):
            button.config(bg=original_color)
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
    
    def lighten_color(self, color):
        """Lighten a hex color"""
        color_map = {
            "#10b981": "#34d399",   # Green
            "#f59e0b": "#fbbf24",   # Amber
            "#ef4444": "#f87171"    # Red
        }
        return color_map.get(color, color)
    
    def create_results_section(self, parent):
        """Create results section"""
        results_frame = tk.LabelFrame(parent, text="EMD Refund Receipt", font=("Arial", 14, "bold"), fg="#475569")
        results_frame.pack(fill="both", expand=True, padx=10, pady=15)
        
        # Results display - enhanced styling
        text_frame = tk.Frame(results_frame)
        text_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.results_text = tk.Text(text_frame, height=10, font=("Arial", 11), wrap="word", relief="solid", bd=1)
        scrollbar = tk.Scrollbar(text_frame, orient="vertical", command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=scrollbar.set)
        
        self.results_text.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        self.results_text.insert("1.0", "Fill the 3 fields above and click 'Generate EMD Refund Receipt'")
    
    def create_action_buttons(self, parent):
        """Create action buttons"""
        button_frame = tk.Frame(parent, bg="#f8fafc")
        button_frame.pack(fill="x", padx=10, pady=15)
        
        save_btn = tk.Button(button_frame, text="💾 Save Receipt", command=self.save_receipt, 
                           width=16, height=2, font=("Arial", 11, "bold"), bg="#6366f1", fg="white", relief="flat", bd=0, cursor="hand2")
        save_btn.pack(side="left", padx=8)
        self.add_hover_effect(save_btn, "#6366f1")
        
        clear_btn = tk.Button(button_frame, text="🔄 Clear Form", command=self.clear_form, 
                            width=16, height=2, font=("Arial", 11, "bold"), bg="#f59e0b", fg="white", relief="flat", bd=0, cursor="hand2")
        clear_btn.pack(side="left", padx=8)
        self.add_hover_effect(clear_btn, "#f59e0b")
        
        print_btn = tk.Button(button_frame, text="🖨️ Print Receipt", command=self.print_receipt, 
                            width=16, height=2, font=("Arial", 11, "bold"), bg="#8b5cf6", fg="white", relief="flat", bd=0, cursor="hand2")
        print_btn.pack(side="left", padx=8)
        self.add_hover_effect(print_btn, "#8b5cf6")
    
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
    
    def number_to_words(self, num):
        """Convert number to words (Indian numbering system)"""
        if num == 0:
            return "Zero"
        
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        def convert_hundreds(n):
            result = ""
            if n >= 100:
                result += ones[n // 100] + " Hundred "
                n %= 100
            if n >= 20:
                result += tens[n // 10] + " "
                if n % 10:
                    result += ones[n % 10] + " "
            elif n >= 10:
                result += teens[n - 10] + " "
            elif n > 0:
                result += ones[n] + " "
            return result.strip()
        
        # Convert to integer and then process
        num = int(num)
        if num == 0:
            return "Zero"
        
        result = ""
        # Handle crores
        if num >= 10000000:
            crores = num // 10000000
            result += convert_hundreds(crores) + " Crore "
            num %= 10000000
        
        # Handle lakhs
        if num >= 100000:
            lakhs = num // 100000
            result += convert_hundreds(lakhs) + " Lakh "
            num %= 100000
        
        # Handle thousands
        if num >= 1000:
            thousands = num // 1000
            result += convert_hundreds(thousands) + " Thousand "
            num %= 1000
        
        # Handle hundreds and below
        if num > 0:
            result += convert_hundreds(num)
        
        return result.strip()
    
    def print_receipt(self):
        """Print receipt - using PDF generation and saving to downloads folder"""
        if not hasattr(self, 'current_receipt'):
            messagebox.showwarning("Warning", "Please generate receipt first")
            return
        
        # Use PDF generation if available, otherwise fallback to HTML
        if PDF_AVAILABLE:
            self._print_receipt_pdf_to_downloads()
        else:
            self._print_receipt_html()
    
    def _print_receipt_pdf_to_downloads(self):
        """Generate PDF and save to downloads folder"""
        try:
            # Import ReportLab components locally to avoid issues if not available
            from reportlab.lib.pagesizes import A4
            from reportlab.pdfgen import canvas
            from reportlab.lib.units import mm
            
            # Get current receipt data
            receipt = self.current_receipt
            payee_name = receipt['payee_name']
            amount = receipt['amount']
            work_description = receipt['work_description']
            
            # Convert amount to words
            amount_words = self.number_to_words(amount)
            
            # Get downloads folder path
            import pathlib
            downloads_path = pathlib.Path.home() / "Downloads"
            
            # Make sure the downloads directory exists
            downloads_path.mkdir(parents=True, exist_ok=True)
            
            # Create PDF filename with full path
            filename = f"EMD_Refund_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            full_path = downloads_path / filename
            
            # Print debug information
            print(f"Generating PDF for: {payee_name}")
            print(f"Amount: {amount}")
            print(f"Work: {work_description}")
            print(f"Downloads path: {downloads_path}")
            print(f"Full PDF path: {full_path}")
            
            # Create PDF
            c = canvas.Canvas(str(full_path), pagesize=A4)
            width, height = A4
            
            # Set margins (10mm on each side)
            left_margin = 10*mm
            right_margin = 10*mm
            top_margin = 10*mm
            bottom_margin = 10*mm
            
            # Draw border (2px solid #ccc)
            c.setStrokeColorRGB(0.8, 0.8, 0.8)  # Light gray color (#ccc)
            c.setLineWidth(2)
            c.rect(left_margin, bottom_margin, width - left_margin - right_margin, height - top_margin - bottom_margin)
            
            # Header section
            c.setFont("Helvetica-Bold", 16)
            c.drawCentredString(width/2, height - 50*mm, f"Payable to: - {payee_name} ( Electric Contractor)")
            c.setFont("Helvetica-Bold", 14)
            c.drawCentredString(width/2, height - 60*mm, "HAND RECEIPT (RPWA 28)")
            c.setFont("Helvetica", 10)
            c.drawCentredString(width/2, height - 65*mm, "(Referred to in PWF&A Rules 418,424,436 & 438)")
            c.drawCentredString(width/2, height - 70*mm, "Division - PWD Electric Division, Udaipur")
            
            # Details section
            c.setFont("Helvetica", 10)
            y_position = height - 80*mm
            
            # Line 1
            c.drawString(30*mm, y_position, "(1)Cash Book Voucher No.                Date")
            y_position -= 10*mm
            
            # Line 2
            c.drawString(30*mm, y_position, "(2)Cheque No. and Date")
            y_position -= 10*mm
            
            # Line 3
            c.drawString(30*mm, y_position, f"(3) Pay for ECS Rs.{amount}/- (Rupees {amount_words} Only)")
            y_position -= 10*mm
            
            # Line 4
            c.drawString(30*mm, y_position, "(4) Paid by me")
            y_position -= 10*mm
            
            # Line 5
            c.drawString(30*mm, y_position, f"(5) Received from The Executive Engineer PWD Electric Division, Udaipur the sum of Rs. {amount}/- (Rupees {amount_words} Only)")
            y_position -= 10*mm
            
            # Line 6
            c.drawString(30*mm, y_position, f" Name of work for which payment is made: {work_description}")
            y_position -= 10*mm
            
            # Line 7
            c.drawString(30*mm, y_position, " Chargeable to Head:- 8443 [EMD-Refund] ")
            y_position -= 15*mm
            
            # Signature area table
            # Table headers
            c.setFont("Helvetica", 10)
            c.drawString(30*mm, y_position, "Witness")
            c.drawString(90*mm, y_position, "Stamp")
            c.drawString(150*mm, y_position, "Signature of payee")
            y_position -= 10*mm
            
            # Table content
            c.drawString(30*mm, y_position, "Cash Book No.                Page No.")
            y_position -= 20*mm
            
            # Offices table
            # Table headers
            c.drawString(30*mm, y_position, "For use in the Divisional Office")
            c.drawString(120*mm, y_position, "For use in the Accountant General's office")
            y_position -= 10*mm
            
            # Second row
            c.drawString(30*mm, y_position, "Checked")
            c.drawString(120*mm, y_position, "Audited/Reviewed")
            y_position -= 10*mm
            
            # Third row
            c.drawString(30*mm, y_position, "Accounts Clerk")
            c.drawString(120*mm, y_position, "DA          Auditor          Supdt.          G.O.")
            y_position -= 30*mm
            
            # Bottom left box with blue border (no circular seal)
            c.setStrokeColorRGB(0, 0, 1)  # Blue color
            c.setLineWidth(2)
            c.rect(40*mm, 40*mm, 120*mm, 55*mm)  # Position and size matching the HTML
            
            # Text in bottom left box (blue color)
            c.setFillColorRGB(0, 0, 1)  # Blue color
            c.setFont("Helvetica", 10)
            y_position = 90*mm  # Starting position for text in the box
            c.drawString(45*mm, y_position, "")
            y_position -= 5*mm
            c.drawString(45*mm, y_position, "")
            y_position -= 5*mm
            c.drawString(45*mm, y_position, "")
            y_position -= 10*mm
            c.drawString(45*mm, y_position, f" Passed for Rs. {amount}")
            y_position -= 5*mm
            c.drawString(45*mm, y_position, f" In Words Rupees: {amount_words} Only")
            y_position -= 5*mm
            c.drawString(45*mm, y_position, " Chargeable to Head:- 8443 [EMD-Refund]")
            y_position -= 10*mm
            
            # Seal text in bottom left box
            c.drawString(45*mm, y_position, "Ar.                    D.A.                    E.E.")
            
            # Reset colors to default
            c.setFillColorRGB(0, 0, 0)  # Black color
            c.setStrokeColorRGB(0, 0, 0)  # Black color
            c.setLineWidth(1)
            
            # Save the PDF
            c.save()
            
            messagebox.showinfo("Success", f"Receipt saved to Downloads folder as {filename}")
            
        except Exception as e:
            messagebox.showerror("Error", f"PDF generation error: {str(e)}")
            import traceback
            traceback.print_exc()
    
    def _print_receipt_html(self):
        """Print receipt by opening HTML template with parameters"""
        try:
            # Get current receipt data
            receipt = self.current_receipt
            payee_name = receipt['payee_name']
            amount = receipt['amount']
            work_description = receipt['work_description']
            
            # URL encode the parameters
            import urllib.parse
            encoded_payee = urllib.parse.quote(payee_name)
            encoded_amount = urllib.parse.quote(str(amount))
            encoded_work = urllib.parse.quote(work_description)
            
            # Create URL with parameters
            html_file = os.path.abspath("emd-refund.html")
            url = f"file://{html_file}?payee={encoded_payee}&amount={encoded_amount}&work={encoded_work}"
            
            # Open in browser
            webbrowser.open(url)
            
            messagebox.showinfo("Success", "Receipt opened in browser for printing!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Print error: {str(e)}")
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = SimpleEMDRefundTool()
    app.run()