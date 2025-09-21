"""
EMD Refund Tool - SIMPLIFIED for Lower Divisional Clerks
Only 3 essential inputs: Payee Name, Amount, Work Description
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime
import os
from pathlib import Path
from utils.pdf_generator import PDFGenerator

class EMDRefundTool:
    def __init__(self, db_manager, settings):
        """Initialize simplified EMD Refund tool window"""
        self.db_manager = db_manager
        self.settings = settings
        self.pdf_generator = PDFGenerator(settings)
        
        # Create tool window
        self.window = ctk.CTkToplevel()
        self.setup_window()
        self.create_interface()
    
    def setup_window(self):
        """Configure tool window"""
        self.window.title("EMD Refund - Simple")
        self.window.geometry("600x500")
        self.window.minsize(500, 400)
        
        # Make window modal
        self.window.transient()
        self.window.grab_set()
    
    def create_interface(self):
        """Create the simplified tool interface"""
        # Header
        header_frame = ctk.CTkFrame(self.window, height=60)
        header_frame.pack(fill="x", padx=10, pady=5)
        header_frame.pack_propagate(False)
        
        title_label = ctk.CTkLabel(
            header_frame,
            text="💰 EMD Refund - Simple",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        title_label.pack(pady=15)
        
        # Main content
        main_frame = ctk.CTkFrame(self.window)
        main_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Simple input form - ONLY 3 FIELDS
        self.create_simple_form(main_frame)
        
        # Action buttons
        self.create_action_buttons(main_frame)
        
        # Results section
        self.create_results_section(main_frame)
    
    def create_simple_form(self, parent):
        """Create simple form with only 3 essential inputs"""
        form_frame = ctk.CTkFrame(parent)
        form_frame.pack(fill="x", padx=10, pady=5)
        
        # Form title
        form_title = ctk.CTkLabel(
            form_frame,
            text="Enter EMD Details (Only 3 Fields Required)",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        form_title.pack(pady=(10, 15))
        
        # Input fields - SIMPLIFIED
        fields_frame = ctk.CTkFrame(form_frame)
        fields_frame.pack(fill="x", padx=10, pady=5)
        
        # 1. Payee Name
        ctk.CTkLabel(fields_frame, text="Payee Name:", font=ctk.CTkFont(weight="bold", size=14)).grid(
            row=0, column=0, padx=10, pady=10, sticky="w"
        )
        self.payee_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Enter payee name", font=ctk.CTkFont(size=14))
        self.payee_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        
        # 2. Amount
        ctk.CTkLabel(fields_frame, text="Amount (₹):", font=ctk.CTkFont(weight="bold", size=14)).grid(
            row=1, column=0, padx=10, pady=10, sticky="w"
        )
        self.amount_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Enter amount", font=ctk.CTkFont(size=14))
        self.amount_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        
        # 3. Work Description
        ctk.CTkLabel(fields_frame, text="Work Description:", font=ctk.CTkFont(weight="bold", size=14)).grid(
            row=2, column=0, padx=10, pady=10, sticky="w"
        )
        self.work_entry = ctk.CTkTextbox(fields_frame, width=300, height=80, font=ctk.CTkFont(size=14))
        self.work_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        
        # Configure grid weights
        fields_frame.grid_columnconfigure(1, weight=1)
    
    def create_action_buttons(self, parent):
        """Create simple action buttons"""
        button_frame = ctk.CTkFrame(parent, height=80)
        button_frame.pack(fill="x", padx=10, pady=5)
        button_frame.pack_propagate(False)
        
        # Button container
        btn_container = ctk.CTkFrame(button_frame)
        btn_container.pack(pady=15)
        
        # Calculate button
        calc_btn = ctk.CTkButton(
            btn_container,
            text="🧮 Calculate Refund",
            command=self.calculate_refund,
            width=150,
            height=40,
            font=ctk.CTkFont(size=14, weight="bold")
        )
        calc_btn.pack(side="left", padx=5)
        
        # Generate PDF button
        pdf_btn = ctk.CTkButton(
            btn_container,
            text="📄 Generate PDF",
            command=self.generate_pdf,
            width=150,
            height=40,
            font=ctk.CTkFont(size=14, weight="bold")
        )
        pdf_btn.pack(side="left", padx=5)
        
        # Clear form button
        clear_btn = ctk.CTkButton(
            btn_container,
            text="🗑️ Clear",
            command=self.clear_form,
            width=100,
            height=40,
            fg_color="gray",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        clear_btn.pack(side="left", padx=5)
    
    def create_results_section(self, parent):
        """Create results display section"""
        self.results_frame = ctk.CTkFrame(parent, height=150)
        self.results_frame.pack(fill="x", padx=10, pady=5)
        self.results_frame.pack_propagate(False)
        
        # Results title
        results_title = ctk.CTkLabel(
            self.results_frame,
            text="Refund Calculation",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        results_title.pack(pady=(10, 5))
        
        # Results display
        self.results_text = ctk.CTkTextbox(self.results_frame, height=100, font=ctk.CTkFont(size=12))
        self.results_text.pack(fill="both", expand=True, padx=10, pady=5)
        self.results_text.insert("1.0", "Enter details above and click 'Calculate Refund'")
    
    def calculate_refund(self):
        """Calculate EMD refund - SIMPLIFIED"""
        try:
            # Get only 3 essential inputs
            payee_name = self.payee_entry.get().strip()
            amount_str = self.amount_entry.get().strip()
            work_description = self.work_entry.get("1.0", "end-1c").strip()
            
            # Validate inputs
            if not all([payee_name, amount_str, work_description]):
                messagebox.showerror("Error", "Please fill in all 3 fields.")
                return
            
            try:
                amount = float(amount_str)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid amount.")
                return
            
            # Simple calculation - Full refund (no complex penalty logic)
            refund_amount = amount
            status = "Eligible for Full Refund"
            
            # Store calculation results
            self.calculation_result = {
                'payee_name': payee_name,
                'amount': amount,
                'work_description': work_description,
                'refund_amount': refund_amount,
                'status': status,
                'date_calculated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            # Display results
            self.display_results()
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to calculate refund: {str(e)}")
    
    def display_results(self):
        """Display simple results"""
        if not hasattr(self, 'calculation_result'):
            return
        
        result = self.calculation_result
        
        results_text = f"""EMD REFUND CALCULATION
{'='*30}

Payee: {result['payee_name']}
Amount: ₹{result['amount']:,.2f}
Work: {result['work_description']}

REFUND AMOUNT: ₹{result['refund_amount']:,.2f}
STATUS: {result['status']}

Date: {result['date_calculated']}"""
        
        self.results_text.delete("1.0", "end")
        self.results_text.insert("1.0", results_text)
    
    def generate_pdf(self):
        """Generate simple PDF"""
        if not hasattr(self, 'calculation_result'):
            messagebox.showwarning("No Data", "Please calculate refund first.")
            return
        
        try:
            # Choose save location
            file_path = filedialog.asksaveasfilename(
                title="Save EMD Refund PDF",
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf")],
                initialname=f"EMD_Refund_{self.calculation_result['payee_name'].replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.pdf"
            )
            
            if file_path:
                # Generate simple PDF
                if self.pdf_generator.generate_simple_emd_pdf(file_path, self.calculation_result):
                    messagebox.showinfo("Success", f"PDF generated successfully!\nSaved to: {file_path}")
                    
                    # Ask if user wants to open the file
                    if messagebox.askyesno("Open File", "Would you like to open the generated PDF?"):
                        os.startfile(file_path)
                else:
                    messagebox.showerror("Error", "Failed to generate PDF.")
                    
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate PDF: {str(e)}")
    
    def clear_form(self):
        """Clear all form fields"""
        self.payee_entry.delete(0, "end")
        self.amount_entry.delete(0, "end")
        self.work_entry.delete("1.0", "end")
        
        # Clear results
        self.results_text.delete("1.0", "end")
        self.results_text.insert("1.0", "Enter details above and click 'Calculate Refund'")
        
        # Clear calculation result
        if hasattr(self, 'calculation_result'):
            delattr(self, 'calculation_result')
    
    def focus(self):
        """Bring window to focus"""
        self.window.lift()
        self.window.focus_force()
