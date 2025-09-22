# pwd_tools_desktop.py - Main Desktop Application
# Converted from Streamlit web app to standalone desktop application

import customtkinter as ctk
import sqlite3
import pandas as pd
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import os
import json
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import openpyxl
import numpy as np
from io import BytesIO
import zipfile
import re

class PWDToolsApp:
    def __init__(self):
        # Initialize main window
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
        self.root = ctk.CTk()
        self.root.title("PWD Tools Hub")
        self.root.geometry("1400x900")
        self.root.resizable(True, True)
        
        # Initialize database
        self.init_database()
        
        # Create main interface
        self.create_main_interface()
        
    def init_database(self):
        """Initialize SQLite database for local storage"""
        self.conn = sqlite3.connect('pwd_tools.db')
        self.cursor = self.conn.cursor()
        
        # Create tables for different tools
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS bills (
                id INTEGER PRIMARY KEY,
                bill_number TEXT,
                contractor_name TEXT,
                work_description TEXT,
                bill_amount REAL,
                date_created TEXT,
                status TEXT
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS emd_records (
                id INTEGER PRIMARY KEY,
                tender_number TEXT,
                contractor_name TEXT,
                emd_amount REAL,
                bank_name TEXT,
                guarantee_number TEXT,
                validity_date TEXT,
                refund_status TEXT
            )
        ''')
        
        self.conn.commit()
        
    def create_main_interface(self):
        """Create the main application interface"""
        # Header Frame
        header_frame = ctk.CTkFrame(self.root, height=100)
        header_frame.pack(fill="x", padx=10, pady=5)
        
        title_label = ctk.CTkLabel(
            header_frame,
            text="PWD Tools Hub",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        title_label.pack(pady=10)
        
        # Main Content Frame
        content_frame = ctk.CTkFrame(self.root)
        content_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Tools Grid
        self.create_tools_grid(content_frame)
        
    def create_tools_grid(self, parent):
        """Create grid of tool buttons"""
        tools = [
            ("Excel se EMD", self.open_excel_emd_refund, "#8B5CF6"),
            ("Bill Note Sheet", self.open_bill_note_sheet, "#8B5CF6"),
            ("Bill Deviation", self.open_bill_deviation, "#8B5CF6"),
            ("Tender Processing", self.open_tender_processing, "#8B5CF6"),
            ("Deductions Table", self.open_deductions_table, "#8B5CF6"),
            ("Delay Calculator", self.open_delay_calculator, "#8B5CF6"),
            ("EMD Refund", self.open_emd_refund, "#8B5CF6"),
            ("Financial Progress", self.open_financial_progress, "#8B5CF6"),
            ("Security Refund", self.open_security_refund, "#8B5CF6"),
            ("Stamp Duty", self.open_stamp_duty, "#8B5CF6"),
            ("Hand Receipt", self.open_hand_receipt, "#8B5CF6"),
            ("Excel to EMD Web", self.open_excel_emd_web, "#8B5CF6")
        ]
        
        # Create buttons in grid layout
        row, col = 0, 0
        for tool_name, command, color in tools:
            btn = ctk.CTkButton(
                parent,
                text=tool_name,
                command=command,
                width=250,
                height=70,
                font=ctk.CTkFont(size=14, weight="bold"),
                fg_color=color,
                hover_color="#7C3AED"
            )
            btn.grid(row=row, column=col, padx=15, pady=15, sticky="ew")
            
            col += 1
            if col > 2:  # 3 columns per row
                col = 0
                row += 1
        
        # Configure grid weights
        for i in range(3):
            parent.grid_columnconfigure(i, weight=1)

    def create_tool_window(self, title, content_function):
        """Create a new window for a specific tool"""
        tool_window = ctk.CTkToplevel(self.root)
        tool_window.title(f"{title} - PWD Tools")
        tool_window.geometry("1000x700")
        tool_window.resizable(True, True)
        
        # Create scrollable frame
        scrollable_frame = ctk.CTkScrollableFrame(tool_window)
        scrollable_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Add content
        content_function(scrollable_frame)
        
        # Center the window
        tool_window.update_idletasks()
        x = (tool_window.winfo_screenwidth() // 2) - (tool_window.winfo_width() // 2)
        y = (tool_window.winfo_screenheight() // 2) - (tool_window.winfo_height() // 2)
        tool_window.geometry(f"+{x}+{y}")

    # Tool Implementation Methods
    def open_excel_emd_refund(self):
        self.create_tool_window("Excel se EMD", self.excel_emd_refund_content)
    
    def open_bill_note_sheet(self):
        self.create_tool_window("Bill Note Sheet", self.bill_note_sheet_content)
    
    def open_bill_deviation(self):
        self.create_tool_window("Bill Deviation", self.bill_deviation_content)
    
    def open_tender_processing(self):
        self.create_tool_window("Tender Processing", self.tender_processing_content)
    
    def open_deductions_table(self):
        self.create_tool_window("Deductions Table", self.deductions_table_content)
    
    def open_delay_calculator(self):
        self.create_tool_window("Delay Calculator", self.delay_calculator_content)
    
    def open_emd_refund(self):
        self.create_tool_window("EMD Refund", self.emd_refund_content)
    
    def open_financial_progress(self):
        self.create_tool_window("Financial Progress", self.financial_progress_content)
    
    def open_security_refund(self):
        self.create_tool_window("Security Refund", self.security_refund_content)
    
    def open_stamp_duty(self):
        self.create_tool_window("Stamp Duty", self.stamp_duty_content)
    
    def open_hand_receipt(self):
        self.create_tool_window("Hand Receipt Generator", self.hand_receipt_content)
    
    def open_excel_emd_web(self):
        self.create_tool_window("Excel to EMD Web", self.excel_emd_web_content)

    # Individual Tool Content Methods
    def excel_emd_refund_content(self, parent):
        """Excel se EMD tool implementation"""
        # Title
        title_label = ctk.CTkLabel(parent, text="Excel se EMD", 
                                  font=ctk.CTkFont(size=20, weight="bold"))
        title_label.pack(pady=10)
        
        # File upload frame
        upload_frame = ctk.CTkFrame(parent)
        upload_frame.pack(fill="x", padx=10, pady=10)
        
        ctk.CTkLabel(upload_frame, text="Upload Excel File:", 
                    font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)
        
        self.file_path_var = tk.StringVar()
        file_entry = ctk.CTkEntry(upload_frame, textvariable=self.file_path_var, width=400)
        file_entry.pack(pady=5)
        
        browse_btn = ctk.CTkButton(upload_frame, text="Browse", command=self.browse_excel_file)
        browse_btn.pack(pady=5)
        
        # Process button
        process_btn = ctk.CTkButton(parent, text="Process Excel File", 
                                   command=self.process_excel_emd, 
                                   font=ctk.CTkFont(size=16, weight="bold"))
        process_btn.pack(pady=20)
        
        # Results frame
        self.results_frame = ctk.CTkFrame(parent)
        self.results_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def bill_note_sheet_content(self, parent):
        """Bill Note Sheet tool implementation"""
        # Title
        title_label = ctk.CTkLabel(parent, text="Bill Note Sheet", 
                                  font=ctk.CTkFont(size=20, weight="bold"))
        title_label.pack(pady=10)
        
        # Input Frame
        input_frame = ctk.CTkFrame(parent)
        input_frame.pack(fill="x", padx=10, pady=10)
        
        # Bill Details
        ctk.CTkLabel(input_frame, text="Bill Number:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.bill_number_entry = ctk.CTkEntry(input_frame, width=200)
        self.bill_number_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ctk.CTkLabel(input_frame, text="Contractor Name:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.contractor_entry = ctk.CTkEntry(input_frame, width=200)
        self.contractor_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ctk.CTkLabel(input_frame, text="Work Description:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.work_desc_entry = ctk.CTkEntry(input_frame, width=400)
        self.work_desc_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)
        
        ctk.CTkLabel(input_frame, text="Bill Amount (₹):").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.bill_amount_entry = ctk.CTkEntry(input_frame, width=200)
        self.bill_amount_entry.grid(row=3, column=1, padx=5, pady=5)
        
        # Buttons
        btn_frame = ctk.CTkFrame(parent)
        btn_frame.pack(fill="x", padx=10, pady=10)
        
        save_btn = ctk.CTkButton(btn_frame, text="Save Bill", command=self.save_bill_note)
        save_btn.pack(side="left", padx=5)
        
        generate_btn = ctk.CTkButton(btn_frame, text="Generate PDF", command=self.generate_bill_pdf)
        generate_btn.pack(side="left", padx=5)

    def delay_calculator_content(self, parent):
        """Delay Calculator tool implementation"""
        # Title
        title_label = ctk.CTkLabel(parent, text="Delay Calculator", 
                                  font=ctk.CTkFont(size=20, weight="bold"))
        title_label.pack(pady=10)
        
        # Input Frame
        input_frame = ctk.CTkFrame(parent)
        input_frame.pack(fill="x", padx=10, pady=10)
        
        # Work Details
        ctk.CTkLabel(input_frame, text="Work Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.work_name_entry = ctk.CTkEntry(input_frame, width=300)
        self.work_name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ctk.CTkLabel(input_frame, text="Start Date:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.start_date_entry = ctk.CTkEntry(input_frame, width=200, placeholder_text="YYYY-MM-DD")
        self.start_date_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ctk.CTkLabel(input_frame, text="Completion Date:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.completion_date_entry = ctk.CTkEntry(input_frame, width=200, placeholder_text="YYYY-MM-DD")
        self.completion_date_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Calculate button
        calc_btn = ctk.CTkButton(input_frame, text="Calculate Delay", 
                                command=self.calculate_delay)
        calc_btn.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Results frame
        self.delay_results_frame = ctk.CTkFrame(parent)
        self.delay_results_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def emd_refund_content(self, parent):
        """EMD Refund calculator implementation"""
        # Title
        title_label = ctk.CTkLabel(parent, text="EMD Refund Calculator", 
                                  font=ctk.CTkFont(size=20, weight="bold"))
        title_label.pack(pady=10)
        
        # Input fields for EMD details
        fields_frame = ctk.CTkFrame(parent)
        fields_frame.pack(fill="x", padx=10, pady=10)
        
        # Tender Number
        ctk.CTkLabel(fields_frame, text="Tender Number:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.tender_number_entry = ctk.CTkEntry(fields_frame, width=200)
        self.tender_number_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # EMD Amount
        ctk.CTkLabel(fields_frame, text="EMD Amount (₹):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.emd_amount_entry = ctk.CTkEntry(fields_frame, width=200)
        self.emd_amount_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Bank Guarantee Details
        ctk.CTkLabel(fields_frame, text="Bank Name:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.bank_name_entry = ctk.CTkEntry(fields_frame, width=200)
        self.bank_name_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Validity Date
        ctk.CTkLabel(fields_frame, text="Validity Date:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.validity_date_entry = ctk.CTkEntry(fields_frame, width=200, placeholder_text="YYYY-MM-DD")
        self.validity_date_entry.grid(row=3, column=1, padx=5, pady=5)
        
        # Calculate button
        calc_btn = ctk.CTkButton(fields_frame, text="Calculate Refund", 
                                command=self.calculate_emd_refund)
        calc_btn.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Results frame
        self.emd_results_frame = ctk.CTkFrame(parent)
        self.emd_results_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Placeholder methods for other tools
    def bill_deviation_content(self, parent):
        ctk.CTkLabel(parent, text="Bill Deviation Tool - Coming Soon", 
                    font=ctk.CTkFont(size=20, weight="bold")).pack(pady=50)
    
    def tender_processing_content(self, parent):
        ctk.CTkLabel(parent, text="Tender Processing Tool - Coming Soon", 
                    font=ctk.CTkFont(size=20, weight="bold")).pack(pady=50)
    
    def deductions_table_content(self, parent):
        ctk.CTkLabel(parent, text="Deductions Table Tool - Coming Soon", 
                    font=ctk.CTkFont(size=20, weight="bold")).pack(pady=50)
    
    def financial_progress_content(self, parent):
        ctk.CTkLabel(parent, text="Financial Progress Tool - Coming Soon", 
                    font=ctk.CTkFont(size=20, weight="bold")).pack(pady=50)
    
    def security_refund_content(self, parent):
        ctk.CTkLabel(parent, text="Security Refund Tool - Coming Soon", 
                    font=ctk.CTkFont(size=20, weight="bold")).pack(pady=50)
    
    def stamp_duty_content(self, parent):
        ctk.CTkLabel(parent, text="Stamp Duty Tool - Coming Soon", 
                    font=ctk.CTkFont(size=20, weight="bold")).pack(pady=50)
    
    def hand_receipt_content(self, parent):
        ctk.CTkLabel(parent, text="Hand Receipt Generator - Coming Soon", 
                    font=ctk.CTkFont(size=20, weight="bold")).pack(pady=50)
    
    def excel_emd_web_content(self, parent):
        ctk.CTkLabel(parent, text="Excel to EMD Web Tool - Coming Soon", 
                    font=ctk.CTkFont(size=20, weight="bold")).pack(pady=50)

    # Helper methods
    def browse_excel_file(self):
        """Browse for Excel file"""
        filename = filedialog.askopenfilename(
            title="Select Excel File",
            filetypes=[("Excel files", "*.xlsx *.xls"), ("All files", "*.*")]
        )
        if filename:
            self.file_path_var.set(filename)

    def process_excel_emd(self):
        """Process Excel file for EMD refund"""
        file_path = self.file_path_var.get()
        if not file_path:
            messagebox.showerror("Error", "Please select an Excel file first")
            return
        
        try:
            # Read Excel file
            df = pd.read_excel(file_path)
            
            # Clear previous results
            for widget in self.results_frame.winfo_children():
                widget.destroy()
            
            # Display results
            ctk.CTkLabel(self.results_frame, text="Excel File Processed Successfully!", 
                        font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)
            
            # Show data preview
            preview_text = f"File: {os.path.basename(file_path)}\n"
            preview_text += f"Rows: {len(df)}\n"
            preview_text += f"Columns: {len(df.columns)}\n\n"
            preview_text += "First 5 rows:\n"
            preview_text += df.head().to_string()
            
            text_widget = ctk.CTkTextbox(self.results_frame, width=800, height=400)
            text_widget.pack(pady=10)
            text_widget.insert("1.0", preview_text)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process Excel file: {str(e)}")

    def save_bill_note(self):
        """Save bill note to database"""
        try:
            bill_data = (
                self.bill_number_entry.get(),
                self.contractor_entry.get(),
                self.work_desc_entry.get(),
                float(self.bill_amount_entry.get()),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Active"
            )
            
            self.cursor.execute('''
                INSERT INTO bills (bill_number, contractor_name, work_description, 
                                 bill_amount, date_created, status)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', bill_data)
            
            self.conn.commit()
            messagebox.showinfo("Success", "Bill note saved successfully!")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid bill amount")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save bill: {str(e)}")

    def generate_bill_pdf(self):
        """Generate PDF for bill note"""
        try:
            filename = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf")]
            )
            if filename:
                # Create PDF
                c = canvas.Canvas(filename, pagesize=A4)
                c.drawString(100, 750, "BILL NOTE SHEET")
                c.drawString(100, 720, f"Bill Number: {self.bill_number_entry.get()}")
                c.drawString(100, 690, f"Contractor: {self.contractor_entry.get()}")
                c.drawString(100, 660, f"Work: {self.work_desc_entry.get()}")
                c.drawString(100, 630, f"Amount: ₹{self.bill_amount_entry.get()}")
                c.save()
                messagebox.showinfo("Success", f"PDF generated: {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate PDF: {str(e)}")

    def calculate_delay(self):
        """Calculate delay between start and completion dates"""
        try:
            start_date = datetime.strptime(self.start_date_entry.get(), "%Y-%m-%d")
            completion_date = datetime.strptime(self.completion_date_entry.get(), "%Y-%m-%d")
            
            delay_days = (completion_date - start_date).days
            
            # Clear previous results
            for widget in self.delay_results_frame.winfo_children():
                widget.destroy()
            
            # Display results
            ctk.CTkLabel(self.delay_results_frame, text="Delay Calculation Results", 
                        font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)
            
            result_text = f"Work Name: {self.work_name_entry.get()}\n"
            result_text += f"Start Date: {start_date.strftime('%Y-%m-%d')}\n"
            result_text += f"Completion Date: {completion_date.strftime('%Y-%m-%d')}\n"
            result_text += f"Total Days: {delay_days}\n"
            
            if delay_days > 0:
                result_text += f"Status: Delayed by {delay_days} days"
            else:
                result_text += "Status: Completed on time"
            
            text_widget = ctk.CTkTextbox(self.delay_results_frame, width=400, height=200)
            text_widget.pack(pady=10)
            text_widget.insert("1.0", result_text)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid dates in YYYY-MM-DD format")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to calculate delay: {str(e)}")

    def calculate_emd_refund(self):
        """Calculate EMD refund based on tender conditions"""
        try:
            emd_amount = float(self.emd_amount_entry.get())
            validity_date = datetime.strptime(self.validity_date_entry.get(), "%Y-%m-%d")
            current_date = datetime.now()
            
            # Clear previous results
            for widget in self.emd_results_frame.winfo_children():
                widget.destroy()
            
            # Calculate refund eligibility
            if validity_date > current_date:
                refund_amount = emd_amount
                status = "Eligible for Full Refund"
                color = "green"
            else:
                days_expired = (current_date - validity_date).days
                if days_expired <= 30:
                    refund_amount = emd_amount * 0.9  # 10% penalty
                    status = f"Eligible for Refund with 10% penalty ({days_expired} days late)"
                    color = "orange"
                else:
                    refund_amount = 0
                    status = f"Not eligible for refund ({days_expired} days expired)"
                    color = "red"
            
            # Display results
            result_label = ctk.CTkLabel(self.emd_results_frame, 
                                      text=f"Refund Status: {status}",
                                      font=ctk.CTkFont(size=14, weight="bold"))
            result_label.pack(pady=10)
            
            amount_label = ctk.CTkLabel(self.emd_results_frame,
                                      text=f"Refund Amount: ₹{refund_amount:,.2f}",
                                      font=ctk.CTkFont(size=16, weight="bold"))
            amount_label.pack(pady=5)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid amount and date")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to calculate refund: {str(e)}")

    def run(self):
        """Start the application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = PWDToolsApp()
    app.run()
