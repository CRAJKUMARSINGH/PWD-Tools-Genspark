"""
EMD Refund Tool - A4 Portrait Format
For Lower Divisional Clerks - Standard RPWA 28 Format
Based on original repository HTML format
"""

import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from datetime import datetime
import os
import sqlite3
import webbrowser
import tempfile

class SimpleEMDRefundA4Tool:
    def __init__(self):
        """Initialize EMD Refund A4 tool"""
        self.root = tk.Tk()
        self.root.title("EMD Refund - A4 Format (RPWA 28)")
        
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
        self.conn = sqlite3.connect('emd_refund_a4.db')
        self.cursor = self.conn.cursor()
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS emd_refund_a4_records (
                id INTEGER PRIMARY KEY,
                payee_name TEXT,
                amount REAL,
                work_description TEXT,
                receipt_number TEXT,
                refund_date TEXT,
                date_created TEXT
            )
        ''')
        self.conn.commit()
    
    def create_interface(self):
        """Create interface"""
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
            text="EMD Refund - A4 Format (RPWA 28)",
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
        generate_btn = tk.Button(main_frame, text="Generate A4 EMD Refund Receipt", command=self.generate_a4_receipt, 
                               width=35, height=2, font=("Arial", 12, "bold"), bg="lightgreen")
        generate_btn.pack(pady=15)
        
        # Results section
        self.create_results_section(main_frame)
        
        # Action buttons
        self.create_action_buttons(main_frame)
    
    def create_results_section(self, parent):
        """Create results section"""
        results_frame = tk.LabelFrame(parent, text="A4 EMD Refund Receipt Preview", font=("Arial", 12, "bold"))
        results_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Results display - shrunk vertically by 15%
        text_frame = tk.Frame(results_frame)
        text_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.results_text = tk.Text(text_frame, height=8, font=("Arial", 9), wrap="word")  # Reduced height
        scrollbar = tk.Scrollbar(text_frame, orient="vertical", command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=scrollbar.set)
        
        self.results_text.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        self.results_text.insert("1.0", "Fill the 3 fields above and click 'Generate A4 EMD Refund Receipt'")
    
    def create_action_buttons(self, parent):
        """Create action buttons"""
        button_frame = tk.Frame(parent)
        button_frame.pack(fill="x", padx=5, pady=5)
        
        save_btn = tk.Button(button_frame, text="Save Receipt", command=self.save_receipt, 
                           width=15, height=1, font=("Arial", 9), bg="lightblue")
        save_btn.pack(side="left", padx=5)
        
        html_btn = tk.Button(button_frame, text="Open in Browser", command=self.open_in_browser, 
                           width=18, height=1, font=("Arial", 9), bg="orange")
        html_btn.pack(side="left", padx=5)
        
        clear_btn = tk.Button(button_frame, text="Clear Form", command=self.clear_form, 
                            width=15, height=1, font=("Arial", 9), bg="lightgray")
        clear_btn.pack(side="left", padx=5)
    
    def convert_number_to_words(self, num):
        """Convert number to words"""
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        
        if num == 0:
            return "Zero"
        
        def convert_hundreds(n):
            result = ""
            if n >= 100:
                result += ones[n // 100] + " Hundred "
                n %= 100
            if n >= 20:
                result += tens[n // 10] + " "
                n %= 10
            elif n >= 10:
                result += teens[n - 10] + " "
                return result
            if n > 0:
                result += ones[n] + " "
            return result
        
        if num < 0:
            return "Negative " + convert_number_to_words(-num)
        
        result = ""
        if num >= 10000000:  # Crores
            result += convert_hundreds(num // 10000000) + "Crore "
            num %= 10000000
        if num >= 100000:  # Lakhs
            result += convert_hundreds(num // 100000) + "Lakh "
            num %= 100000
        if num >= 1000:  # Thousands
            result += convert_hundreds(num // 1000) + "Thousand "
            num %= 1000
        if num > 0:
            result += convert_hundreds(num)
        
        return result.strip()
    
    def generate_a4_receipt(self):
        """Generate A4 EMD refund receipt in standard RPWA 28 format"""
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
            
            # Convert amount to words
            amount_words = self.convert_number_to_words(int(amount))
            
            # Generate receipt number
            receipt_number = f"EMD-{datetime.now().strftime('%Y%m%d%H%M%S')}"
            
            # Generate A4 HTML receipt
            html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=210mm, height: 297mm">
    <title>Hand Receipt (RPWA 28)</title>
    <style>
        body { 
            font-family: 'Times New Roman', serif; 
            margin: 0; 
            padding: 0;
            background: white;
        }
        @page {{
            size: A4 portrait;
            margin: 10mm;
        }}
        .container {{
            width: 210mm;
            min-height: 297mm;
            margin: 0;
            padding: 20mm;
            box-sizing: border-box;
            position: relative;
            border: 2px solid #000;
            background: white;
        }}
        .header {{
            text-align: center;
            margin-bottom: 20px;
            color: #000;
        }}
        .header h2 {{
            margin: 5px 0;
            font-size: 18px;
            font-weight: bold;
        }}
        .header p {{
            margin: 3px 0;
            font-size: 14px;
        }}
        .details {{
            margin-bottom: 15px;
            line-height: 1.6;
        }}
        .details p {{
            margin: 8px 0;
            font-size: 14px;
        }}
        .amount-words {{
            font-style: italic;
            font-weight: bold;
        }}
        .signature-area {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 30px;
            margin-bottom: 20px;
        }}
        .signature-area td, .signature-area th {{
            border: 1px solid #000;
            padding: 8px;
            text-align: left;
            font-size: 12px;
        }}
        .offices {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        .offices td, .offices th {{
            border: 1px solid #000;
            padding: 8px;
            text-align: left;
            font-size: 12px;
        }}
        .input-field {{
            border-bottom: 1px dotted #000;
            padding: 2px;
            min-width: 200px;
            display: inline-block;
        }}
        .bottom-left-box {{
            position: absolute;
            bottom: 20mm;
            left: 20mm;
            border: 2px solid #000;
            padding: 10px;
            width: 120mm;
            text-align: left;
            height: 40mm;
            font-size: 12px;
        }}
        .bottom-left-box p {{
            margin: 2px 0;
        }}
        .seal-area {{
            position: absolute;
            bottom: 20mm;
            right: 20mm;
            width: 50mm;
            height: 30mm;
            border: 1px solid #000;
            text-align: center;
            padding: 5px;
        }}
        .seal-area p {{
            margin: 5px 0;
            font-size: 10px;
        }}
        @media print {{
            .container {{
                border: 2px solid #000;
                width: 210mm;
                min-height: 297mm;
                margin: 0;
                padding: 20mm;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h2>Payable to: - {payee_name} (Electric Contractor)</h2>
            <h2>HAND RECEIPT (RPWA 28)</h2>
            <p>(Referred to in PWF&A Rules 418,424,436 & 438)</p>
            <p>Division - PWD Electric Division, Udaipur</p>
        </div>
        <div class="details">
            <p>(1) Cash Book Voucher No. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Date &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
            <p>(2) Cheque No. and Date &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
            <p>(3) Pay for ECS Rs.{amount:,.0f}/- (Rupees <span class="amount-words">{amount_words} Only</span>)</p>
            <p>(4) Paid by me</p>
            <p>(5) Received from The Executive Engineer PWD Electric Division, Udaipur the sum of Rs. {amount:,.0f}/- (Rupees <span class="amount-words">{amount_words} Only</span>)</p>
            <p>Name of work for which payment is made: <span class="input-field">{work_description}</span></p>
            <p>Chargeable to Head:- 8443 [EMD-Refund]</p>
            <table class="signature-area">
                <tr>
                    <td>Witness</td>
                    <td>Stamp</td>
                    <td>Signature of payee</td>
                </tr>
                <tr>
                    <td>Cash Book No. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Page No. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
                    <td></td>
                    <td></td>
                </tr>
            </table>
            <table class="offices">
                <tr>
                    <td>For use in the Divisional Office</td>
                    <td>For use in the Accountant General's office</td>
                </tr>
                <tr>
                    <td>Checked</td>
                    <td>Audited/Reviewed</td>
                </tr>
                <tr>
                    <td>Accounts Clerk</td>
                    <td>DA &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Auditor &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Supdt. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; G.O.</td>
                </tr>
            </table>
        </div>
        <div class="seal-area">
            <p>SEAL</p>
            <p></p>
            <p></p>
            <p></p>
        </div>
        <div class="bottom-left-box">
            <p></p>
            <p></p>
            <p></p>
            <p>Passed for Rs. {amount:,.0f}</p>
            <p>In Words Rupees: {amount_words} Only</p>
            <p>Chargeable to Head:- 8443 [EMD-Refund]</p>
            <div style="margin-top: 10px;">
                <p>Ar.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;D.A.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;E.E.</p>
            </div>
        </div>
    </div>
</body>
</html>
"""
            
            # Display preview
            preview_text = f"""
A4 EMD REFUND RECEIPT PREVIEW
=============================

Receipt No: {receipt_number}
Date: {datetime.now().strftime('%d/%m/%Y')}

PAYEE DETAILS
=============
Payee Name: {payee_name}
Amount: ₹ {amount:,.2f}
Amount in Words: {amount_words} Only
Work Description: {work_description}

FORMAT
=======
- Standard RPWA 28 Format
- A4 Portrait Layout
- Professional Government Format
- Ready for Printing

Click 'Open in Browser' to view full A4 format
"""
            
            # Display results
            self.results_text.delete("1.0", "end")
            self.results_text.insert("1.0", preview_text)
            
            # Store receipt data
            self.current_receipt = {
                'payee_name': payee_name,
                'amount': amount,
                'work_description': work_description,
                'receipt_number': receipt_number,
                'html_content': html_content
            }
            
        except Exception as e:
            messagebox.showerror("Error", f"Receipt generation error: {str(e)}")
    
    def open_in_browser(self):
        """Open A4 receipt in browser"""
        if not hasattr(self, 'current_receipt'):
            messagebox.showwarning("Warning", "Please generate receipt first")
            return
        
        try:
            # Create temporary HTML file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8') as f:
                f.write(self.current_receipt['html_content'])
                temp_file = f.name
            
            # Open in browser
            webbrowser.open(f'file://{temp_file}')
            messagebox.showinfo("Success", "A4 EMD Refund Receipt opened in browser!\nYou can print it directly from the browser.")
            
        except Exception as e:
            messagebox.showerror("Error", f"Could not open browser: {str(e)}")
    
    def save_receipt(self):
        """Save receipt record"""
        if not hasattr(self, 'current_receipt'):
            messagebox.showwarning("Warning", "Please generate receipt first")
            return
        
        try:
            receipt = self.current_receipt
            self.cursor.execute('''
                INSERT INTO emd_refund_a4_records (
                    payee_name, amount, work_description, receipt_number, refund_date, date_created
                ) VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                receipt['payee_name'],
                receipt['amount'],
                receipt['work_description'],
                receipt['receipt_number'],
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
        self.results_text.insert("1.0", "Fill the 3 fields above and click 'Generate A4 EMD Refund Receipt'")
        
        if hasattr(self, 'current_receipt'):
            delattr(self, 'current_receipt')
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = SimpleEMDRefundA4Tool()
    app.run()
