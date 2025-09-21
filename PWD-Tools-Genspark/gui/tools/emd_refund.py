"""
EMD Refund Tool - Generate EMD refund receipts and documentation
Desktop implementation for EMD refund processing
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime, timedelta
import os
from pathlib import Path
from utils.pdf_generator import PDFGenerator

class EMDRefundTool:
    def __init__(self, db_manager, settings, parent=None):
        """Initialize EMD Refund tool window"""
        self.db_manager = db_manager
        self.settings = settings
        self.pdf_generator = PDFGenerator(settings)
        
        # Create tool window
        if parent is not None:
            self.window = ctk.CTkToplevel(parent)
        else:
            self.window = ctk.CTkToplevel()
        self.setup_window()
        self.create_interface()
    
    def setup_window(self):
        """Configure tool window"""
        self.window.title("EMD Refund - Generate EMD refund receipts and documentation")
        self.window.geometry("900x700")
        self.window.minsize(800, 600)
        
        # Disable icon to prevent errors
        try:
            self.window.iconbitmap("")
        except:
            pass
        
        # Make window modal
        self.window.transient()
        self.window.grab_set()
    
    def focus(self):
        """Bring window to focus"""
        self.window.lift()
        self.window.focus_force()
    
    def create_interface(self):
        """Create the tool interface"""
        # Header
        header_frame = ctk.CTkFrame(self.window, height=60)
        header_frame.pack(fill="x", padx=10, pady=5)
        header_frame.pack_propagate(False)
        
        title_label = ctk.CTkLabel(
            header_frame,
            text="💰 EMD Refund Calculator & Generator",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        title_label.pack(pady=15)
        
        # Main content
        main_frame = ctk.CTkFrame(self.window)
        main_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Input form
        self.create_input_form(main_frame)
        
        # Calculation results
        self.create_results_section(main_frame)
        
        # Action buttons
        self.create_action_buttons(main_frame)
        
        # Recent EMD records
        self.create_recent_records_section(main_frame)
    
    def create_input_form(self, parent):
        """Create input form for EMD details"""
        form_frame = ctk.CTkFrame(parent)
        form_frame.pack(fill="x", padx=10, pady=5)
        
        # Form title
        form_title = ctk.CTkLabel(
            form_frame,
            text="EMD Details",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        form_title.pack(pady=(10, 15))
        
        # Input fields
        fields_frame = ctk.CTkFrame(form_frame)
        fields_frame.pack(fill="x", padx=10, pady=5)
        
        # Tender Number
        ctk.CTkLabel(fields_frame, text="Tender Number:", font=ctk.CTkFont(weight="bold")).grid(
            row=0, column=0, padx=10, pady=5, sticky="w"
        )
        self.tender_number_entry = ctk.CTkEntry(fields_frame, width=250, placeholder_text="Enter tender number")
        self.tender_number_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        
        # Contractor Name
        ctk.CTkLabel(fields_frame, text="Contractor Name:", font=ctk.CTkFont(weight="bold")).grid(
            row=1, column=0, padx=10, pady=5, sticky="w"
        )
        self.contractor_entry = ctk.CTkEntry(fields_frame, width=250, placeholder_text="Enter contractor name")
        self.contractor_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        # EMD Amount
        ctk.CTkLabel(fields_frame, text="EMD Amount (₹):", font=ctk.CTkFont(weight="bold")).grid(
            row=2, column=0, padx=10, pady=5, sticky="w"
        )
        self.emd_amount_entry = ctk.CTkEntry(fields_frame, width=250, placeholder_text="Enter EMD amount")
        self.emd_amount_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        
        # Bank Name
        ctk.CTkLabel(fields_frame, text="Bank Name:", font=ctk.CTkFont(weight="bold")).grid(
            row=0, column=2, padx=10, pady=5, sticky="w"
        )
        self.bank_name_entry = ctk.CTkEntry(fields_frame, width=250, placeholder_text="Enter bank name")
        self.bank_name_entry.grid(row=0, column=3, padx=10, pady=5, sticky="ew")
        
        # Guarantee Number
        ctk.CTkLabel(fields_frame, text="Guarantee Number:", font=ctk.CTkFont(weight="bold")).grid(
            row=1, column=2, padx=10, pady=5, sticky="w"
        )
        self.guarantee_number_entry = ctk.CTkEntry(fields_frame, width=250, placeholder_text="Enter guarantee number")
        self.guarantee_number_entry.grid(row=1, column=3, padx=10, pady=5, sticky="ew")
        
        # Validity Date
        ctk.CTkLabel(fields_frame, text="Validity Date:", font=ctk.CTkFont(weight="bold")).grid(
            row=2, column=2, padx=10, pady=5, sticky="w"
        )
        self.validity_date_entry = ctk.CTkEntry(fields_frame, width=250, placeholder_text="YYYY-MM-DD")
        self.validity_date_entry.grid(row=2, column=3, padx=10, pady=5, sticky="ew")
        
        # Calculate button
        calc_btn = ctk.CTkButton(
            fields_frame,
            text="🧮 Calculate Refund",
            command=self.calculate_refund,
            width=200,
            height=35
        )
        calc_btn.grid(row=3, column=1, columnspan=2, pady=15)
        
        # Configure grid weights
        fields_frame.grid_columnconfigure(1, weight=1)
        fields_frame.grid_columnconfigure(3, weight=1)
    
    def create_results_section(self, parent):
        """Create results display section"""
        self.results_frame = ctk.CTkFrame(parent, height=150)
        self.results_frame.pack(fill="x", padx=10, pady=5)
        self.results_frame.pack_propagate(False)
        
        # Results title
        results_title = ctk.CTkLabel(
            self.results_frame,
            text="Refund Calculation Results",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        results_title.pack(pady=(10, 5))
        
        # Results display area
        self.results_display = ctk.CTkFrame(self.results_frame)
        self.results_display.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Initial message
        self.no_calc_label = ctk.CTkLabel(
            self.results_display,
            text="Enter EMD details above and click 'Calculate Refund' to see results",
            font=ctk.CTkFont(size=14),
            text_color="#666666"
        )
        self.no_calc_label.pack(pady=40)
    
    def create_action_buttons(self, parent):
        """Create action buttons"""
        button_frame = ctk.CTkFrame(parent, height=80)
        button_frame.pack(fill="x", padx=10, pady=5)
        button_frame.pack_propagate(False)
        
        # Button container
        btn_container = ctk.CTkFrame(button_frame)
        btn_container.pack(pady=15)
        
        # Save EMD button
        self.save_btn = ctk.CTkButton(
            btn_container,
            text="💾 Save EMD Record",
            command=self.save_emd_record,
            width=150,
            height=35,
            state="disabled"
        )
        self.save_btn.pack(side="left", padx=5)
        
        # Generate PDF button
        self.pdf_btn = ctk.CTkButton(
            btn_container,
            text="📄 Generate PDF",
            command=self.generate_pdf,
            width=150,
            height=35,
            state="disabled"
        )
        self.pdf_btn.pack(side="left", padx=5)
        
        # Clear form button
        clear_btn = ctk.CTkButton(
            btn_container,
            text="🗑️ Clear Form",
            command=self.clear_form,
            width=150,
            height=35,
            fg_color="gray"
        )
        clear_btn.pack(side="left", padx=5)
    
    def create_recent_records_section(self, parent):
        """Create recent EMD records section"""
        recent_frame = ctk.CTkFrame(parent)
        recent_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Section title
        recent_title = ctk.CTkLabel(
            recent_frame,
            text="Recent EMD Records",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        recent_title.pack(pady=(10, 5))
        
        # Records list
        self.records_listbox = ctk.CTkScrollableFrame(recent_frame, height=120)
        self.records_listbox.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Load recent records
        self.load_recent_records()
    
    def calculate_refund(self):
        """Calculate EMD refund based on validity and rules"""
        try:
            # Validate inputs
            tender_number = self.tender_number_entry.get().strip()
            contractor_name = self.contractor_entry.get().strip()
            emd_amount_str = self.emd_amount_entry.get().strip()
            validity_date_str = self.validity_date_entry.get().strip()
            
            if not all([tender_number, contractor_name, emd_amount_str, validity_date_str]):
                messagebox.showerror("Validation Error", "Please fill in all required fields.")
                return
            
            try:
                emd_amount = float(emd_amount_str)
            except ValueError:
                messagebox.showerror("Validation Error", "Please enter a valid EMD amount.")
                return
            
            try:
                validity_date = datetime.strptime(validity_date_str, "%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Validation Error", "Please enter validity date in YYYY-MM-DD format.")
                return
            
            # Calculate refund
            current_date = datetime.now()
            days_difference = (current_date - validity_date).days
            
            # Determine refund eligibility and amount
            if validity_date >= current_date:
                # Valid EMD - full refund
                refund_amount = emd_amount
                refund_status = "Eligible for Full Refund"
                status_color = "#10B981"  # Green
                penalty = 0
            elif days_difference <= 30:
                # Expired but within 30 days - 90% refund
                penalty = emd_amount * 0.10
                refund_amount = emd_amount - penalty
                refund_status = f"Eligible for Refund with 10% penalty ({days_difference} days late)"
                status_color = "#F59E0B"  # Orange
            elif days_difference <= 90:
                # Expired 31-90 days - 50% refund
                penalty = emd_amount * 0.50
                refund_amount = emd_amount - penalty
                refund_status = f"Eligible for 50% Refund ({days_difference} days late)"
                status_color = "#EF4444"  # Red
            else:
                # Expired more than 90 days - no refund
                penalty = emd_amount
                refund_amount = 0
                refund_status = f"Not eligible for refund ({days_difference} days expired)"
                status_color = "#DC2626"  # Dark red
            
            # Display results
            self.display_calculation_results(
                emd_amount, refund_amount, penalty, refund_status, status_color, days_difference
            )
            
            # Store calculation data
            self.current_calculation = {
                'tender_number': tender_number,
                'contractor_name': contractor_name,
                'emd_amount': emd_amount,
                'bank_name': self.bank_name_entry.get().strip(),
                'guarantee_number': self.guarantee_number_entry.get().strip(),
                'validity_date': validity_date_str,
                'refund_amount': refund_amount,
                'refund_status': refund_status,
                'penalty': penalty,
                'days_difference': days_difference
            }
            
            # Enable action buttons
            self.save_btn.configure(state="normal")
            self.pdf_btn.configure(state="normal")
            
        except Exception as e:
            messagebox.showerror("Calculation Error", f"Failed to calculate refund: {str(e)}")
    
    def display_calculation_results(self, emd_amount, refund_amount, penalty, status, color, days_diff):
        """Display calculation results"""
        # Clear previous results
        for widget in self.results_display.winfo_children():
            widget.destroy()
        
        # Results grid
        results_grid = ctk.CTkFrame(self.results_display)
        results_grid.pack(fill="both", expand=True, padx=10, pady=10)
        
        # EMD Amount
        ctk.CTkLabel(results_grid, text="Original EMD Amount:", font=ctk.CTkFont(weight="bold")).grid(
            row=0, column=0, padx=10, pady=5, sticky="w"
        )
        ctk.CTkLabel(results_grid, text=f"₹ {emd_amount:,.2f}", font=ctk.CTkFont(size=14)).grid(
            row=0, column=1, padx=10, pady=5, sticky="w"
        )
        
        # Penalty
        if penalty > 0:
            ctk.CTkLabel(results_grid, text="Penalty Amount:", font=ctk.CTkFont(weight="bold")).grid(
                row=1, column=0, padx=10, pady=5, sticky="w"
            )
            ctk.CTkLabel(results_grid, text=f"₹ {penalty:,.2f}", font=ctk.CTkFont(size=14), text_color="#EF4444").grid(
                row=1, column=1, padx=10, pady=5, sticky="w"
            )
        
        # Refund Amount
        ctk.CTkLabel(results_grid, text="Refund Amount:", font=ctk.CTkFont(weight="bold", size=16)).grid(
            row=2, column=0, padx=10, pady=10, sticky="w"
        )
        ctk.CTkLabel(results_grid, text=f"₹ {refund_amount:,.2f}", 
                    font=ctk.CTkFont(size=18, weight="bold"), text_color=color).grid(
            row=2, column=1, padx=10, pady=10, sticky="w"
        )
        
        # Status
        ctk.CTkLabel(results_grid, text="Status:", font=ctk.CTkFont(weight="bold")).grid(
            row=3, column=0, padx=10, pady=5, sticky="w"
        )
        status_label = ctk.CTkLabel(results_grid, text=status, font=ctk.CTkFont(size=12), text_color=color)
        status_label.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        
        # Configure grid
        results_grid.grid_columnconfigure(1, weight=1)
    
    def save_emd_record(self):
        """Save EMD record to database"""
        if not hasattr(self, 'current_calculation'):
            messagebox.showerror("Error", "Please calculate refund first.")
            return
        
        try:
            calc = self.current_calculation
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            success = self.db_manager.execute_query('''
                INSERT INTO emd_records (
                    tender_number, contractor_name, emd_amount, bank_name,
                    guarantee_number, validity_date, refund_status, refund_amount, date_created
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                calc['tender_number'], calc['contractor_name'], calc['emd_amount'],
                calc['bank_name'], calc['guarantee_number'], calc['validity_date'],
                calc['refund_status'], calc['refund_amount'], current_time
            ))
            
            if success:
                messagebox.showinfo("Success", "EMD record saved successfully!")
                self.load_recent_records()  # Refresh the list
            else:
                messagebox.showerror("Error", "Failed to save EMD record.")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save EMD record: {str(e)}")
    
    def generate_pdf(self):
        """Generate PDF for EMD refund"""
        if not hasattr(self, 'current_calculation'):
            messagebox.showerror("Error", "Please calculate refund first.")
            return
        
        try:
            calc = self.current_calculation
            
            # Choose save location
            file_path = filedialog.asksaveasfilename(
                title="Save EMD Refund PDF",
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf")],
                initialname=f"EMD_Refund_{calc['tender_number']}_{datetime.now().strftime('%Y%m%d')}.pdf"
            )
            
            if file_path:
                # Generate PDF
                if self.pdf_generator.create_emd_refund_pdf(calc, file_path):
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
        self.tender_number_entry.delete(0, "end")
        self.contractor_entry.delete(0, "end")
        self.emd_amount_entry.delete(0, "end")
        self.bank_name_entry.delete(0, "end")
        self.guarantee_number_entry.delete(0, "end")
        self.validity_date_entry.delete(0, "end")
        
        # Clear results
        for widget in self.results_display.winfo_children():
            widget.destroy()
        
        self.no_calc_label = ctk.CTkLabel(
            self.results_display,
            text="Enter EMD details above and click 'Calculate Refund' to see results",
            font=ctk.CTkFont(size=14),
            text_color="#666666"
        )
        self.no_calc_label.pack(pady=40)
        
        # Disable action buttons
        self.save_btn.configure(state="disabled")
        self.pdf_btn.configure(state="disabled")
        
        # Clear calculation data
        if hasattr(self, 'current_calculation'):
            delattr(self, 'current_calculation')
    
    def load_recent_records(self):
        """Load and display recent EMD records"""
        try:
            # Clear existing items
            for widget in self.records_listbox.winfo_children():
                widget.destroy()
            
            # Fetch recent records
            records = self.db_manager.fetch_all('''
                SELECT tender_number, contractor_name, emd_amount, refund_amount, refund_status, date_created
                FROM emd_records 
                ORDER BY date_created DESC 
                LIMIT 10
            ''')
            
            if records:
                for record in records:
                    record_frame = ctk.CTkFrame(self.records_listbox)
                    record_frame.pack(fill="x", padx=5, pady=2)
                    
                    # Record info
                    info_text = f"Tender: {record[0]} | Contractor: {record[1]} | EMD: ₹{record[2]:,.2f} | Refund: ₹{record[3]:,.2f}"
                    info_label = ctk.CTkLabel(
                        record_frame,
                        text=info_text,
                        font=ctk.CTkFont(size=11)
                    )
                    info_label.pack(side="left", padx=10, pady=5)
                    
                    # Status
                    status_color = "#10B981" if "Full Refund" in record[4] else "#F59E0B" if "penalty" in record[4] else "#EF4444"
                    status_label = ctk.CTkLabel(
                        record_frame,
                        text=record[4][:30] + "..." if len(record[4]) > 30 else record[4],
                        font=ctk.CTkFont(size=10),
                        text_color=status_color
                    )
                    status_label.pack(side="right", padx=10, pady=5)
            else:
                no_records_label = ctk.CTkLabel(
                    self.records_listbox,
                    text="No EMD records found. Calculate and save your first EMD refund above.",
                    font=ctk.CTkFont(size=12),
                    text_color="#666666"
                )
                no_records_label.pack(pady=20)
                
        except Exception as e:
            print(f"Error loading recent records: {e}")
    
    def focus(self):
        """Bring window to focus"""
        self.window.lift()
        self.window.focus_force()
