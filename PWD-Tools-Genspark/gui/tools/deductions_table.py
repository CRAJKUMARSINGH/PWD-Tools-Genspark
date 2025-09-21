"""
Deductions Table Tool - Desktop implementation
Calculate all standard deductions for bill amounts
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime
import os
from pathlib import Path
from utils.pdf_generator import PDFGenerator

class DeductionsTableTool:
    def __init__(self, db_manager, settings, parent=None):
        """Initialize Deductions Table tool window"""
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
        self.window.title("Deductions Table - PWD Tools")
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
            text="📊 Deductions Table Calculator",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        title_label.pack(pady=15)
        
        # Main content
        main_frame = ctk.CTkFrame(self.window)
        main_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Input form
        self.create_input_form(main_frame)
        
        # Action buttons
        self.create_action_buttons(main_frame)
        
        # Results section
        self.create_results_section(main_frame)
        
        # Recent calculations section
        self.create_recent_calculations_section(main_frame)
    
    def create_input_form(self, parent):
        """Create input form for deductions calculation"""
        form_frame = ctk.CTkFrame(parent)
        form_frame.pack(fill="x", padx=10, pady=5)
        
        # Form title
        form_title = ctk.CTkLabel(
            form_frame,
            text="Bill Details & Deduction Rates",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        form_title.pack(pady=(10, 15))
        
        # Input fields
        fields_frame = ctk.CTkFrame(form_frame)
        fields_frame.pack(fill="x", padx=10, pady=5)
        
        # Bill Number
        ctk.CTkLabel(fields_frame, text="Bill Number:", font=ctk.CTkFont(weight="bold")).grid(
            row=0, column=0, padx=10, pady=5, sticky="w"
        )
        self.bill_number_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Enter bill number")
        self.bill_number_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        
        # Contractor Name
        ctk.CTkLabel(fields_frame, text="Contractor Name:", font=ctk.CTkFont(weight="bold")).grid(
            row=1, column=0, padx=10, pady=5, sticky="w"
        )
        self.contractor_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Enter contractor name")
        self.contractor_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        # Gross Amount
        ctk.CTkLabel(fields_frame, text="Gross Amount (₹):", font=ctk.CTkFont(weight="bold")).grid(
            row=2, column=0, padx=10, pady=5, sticky="w"
        )
        self.gross_amount_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Enter gross bill amount")
        self.gross_amount_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        
        # TDS Rate
        ctk.CTkLabel(fields_frame, text="TDS Rate (%):", font=ctk.CTkFont(weight="bold")).grid(
            row=3, column=0, padx=10, pady=5, sticky="w"
        )
        self.tds_rate_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Default: 2%")
        self.tds_rate_entry.insert(0, "2.0")  # Default value
        self.tds_rate_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")
        
        # Security Deduction Rate
        ctk.CTkLabel(fields_frame, text="Security Deduction (%):", font=ctk.CTkFont(weight="bold")).grid(
            row=4, column=0, padx=10, pady=5, sticky="w"
        )
        self.security_rate_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Default: 5%")
        self.security_rate_entry.insert(0, "5.0")  # Default value
        self.security_rate_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")
        
        # Other Deductions
        ctk.CTkLabel(fields_frame, text="Other Deductions (₹):", font=ctk.CTkFont(weight="bold")).grid(
            row=5, column=0, padx=10, pady=5, sticky="w"
        )
        self.other_deductions_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Enter other deductions (optional)")
        self.other_deductions_entry.insert(0, "0")  # Default value
        self.other_deductions_entry.grid(row=5, column=1, padx=10, pady=5, sticky="ew")
        
        # Work Description
        ctk.CTkLabel(fields_frame, text="Work Description:", font=ctk.CTkFont(weight="bold")).grid(
            row=6, column=0, padx=10, pady=5, sticky="w"
        )
        self.work_desc_entry = ctk.CTkTextbox(fields_frame, width=300, height=60)
        self.work_desc_entry.grid(row=6, column=1, padx=10, pady=5, sticky="ew")
        
        # Configure grid weights
        fields_frame.grid_columnconfigure(1, weight=1)
    
    def create_action_buttons(self, parent):
        """Create action buttons"""
        button_frame = ctk.CTkFrame(parent, height=80)
        button_frame.pack(fill="x", padx=10, pady=5)
        button_frame.pack_propagate(False)
        
        # Button container
        btn_container = ctk.CTkFrame(button_frame)
        btn_container.pack(pady=15)
        
        # Calculate button
        calc_btn = ctk.CTkButton(
            btn_container,
            text="🧮 Calculate Deductions",
            command=self.calculate_deductions,
            width=150,
            height=35
        )
        calc_btn.pack(side="left", padx=5)
        
        # Save button
        save_btn = ctk.CTkButton(
            btn_container,
            text="💾 Save Calculation",
            command=self.save_calculation,
            width=150,
            height=35
        )
        save_btn.pack(side="left", padx=5)
        
        # Generate PDF button
        pdf_btn = ctk.CTkButton(
            btn_container,
            text="📄 Generate PDF",
            command=self.generate_pdf,
            width=150,
            height=35
        )
        pdf_btn.pack(side="left", padx=5)
        
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
    
    def create_results_section(self, parent):
        """Create results display section"""
        self.results_frame = ctk.CTkFrame(parent, height=250)
        self.results_frame.pack(fill="x", padx=10, pady=5)
        self.results_frame.pack_propagate(False)
        
        # Results title
        results_title = ctk.CTkLabel(
            self.results_frame,
            text="Deductions Calculation Results",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        results_title.pack(pady=(10, 5))
        
        # Results display
        self.results_text = ctk.CTkTextbox(self.results_frame, height=200)
        self.results_text.pack(fill="both", expand=True, padx=10, pady=5)
        self.results_text.insert("1.0", "No calculations performed yet.")
    
    def create_recent_calculations_section(self, parent):
        """Create recent calculations section"""
        recent_frame = ctk.CTkFrame(parent)
        recent_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Section title
        recent_title = ctk.CTkLabel(
            recent_frame,
            text="Recent Deduction Calculations",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        recent_title.pack(pady=(10, 5))
        
        # Calculations list
        self.calculations_listbox = ctk.CTkScrollableFrame(recent_frame, height=150)
        self.calculations_listbox.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Load recent calculations
        self.load_recent_calculations()
    
    def calculate_deductions(self):
        """Calculate all deductions for the bill"""
        try:
            # Validate inputs
            bill_number = self.bill_number_entry.get().strip()
            contractor_name = self.contractor_entry.get().strip()
            gross_amount_str = self.gross_amount_entry.get().strip()
            tds_rate_str = self.tds_rate_entry.get().strip()
            security_rate_str = self.security_rate_entry.get().strip()
            other_deductions_str = self.other_deductions_entry.get().strip()
            work_description = self.work_desc_entry.get("1.0", "end-1c").strip()
            
            if not all([bill_number, contractor_name, gross_amount_str]):
                messagebox.showerror("Validation Error", "Please fill in all required fields.")
                return
            
            try:
                gross_amount = float(gross_amount_str)
                tds_rate = float(tds_rate_str) if tds_rate_str else 2.0
                security_rate = float(security_rate_str) if security_rate_str else 5.0
                other_deductions = float(other_deductions_str) if other_deductions_str else 0.0
            except ValueError as e:
                messagebox.showerror("Validation Error", f"Invalid input format: {str(e)}")
                return
            
            # Calculate deductions
            tds_amount = (gross_amount * tds_rate) / 100
            security_deduction = (gross_amount * security_rate) / 100
            total_deductions = tds_amount + security_deduction + other_deductions
            net_amount = gross_amount - total_deductions
            
            # Store calculation results
            self.calculation_result = {
                'bill_number': bill_number,
                'contractor_name': contractor_name,
                'gross_amount': gross_amount,
                'tds_rate': tds_rate,
                'tds_amount': tds_amount,
                'security_rate': security_rate,
                'security_deduction': security_deduction,
                'other_deductions': other_deductions,
                'total_deductions': total_deductions,
                'net_amount': net_amount,
                'work_description': work_description,
                'date_calculated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            # Display results
            self.display_results()
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to calculate deductions: {str(e)}")
    
    def display_results(self):
        """Display deduction calculation results"""
        if not hasattr(self, 'calculation_result'):
            return
        
        result = self.calculation_result
        
        results_text = f"""DEDUCTIONS CALCULATION RESULTS
{'='*50}

Bill Number: {result['bill_number']}
Contractor: {result['contractor_name']}
Work Description: {result['work_description']}

BILL AMOUNTS:
Gross Amount: ₹{result['gross_amount']:,.2f}

DEDUCTIONS BREAKDOWN:
TDS ({result['tds_rate']}%): ₹{result['tds_amount']:,.2f}
Security Deduction ({result['security_rate']}%): ₹{result['security_deduction']:,.2f}
Other Deductions: ₹{result['other_deductions']:,.2f}
─────────────────────────────────────────
Total Deductions: ₹{result['total_deductions']:,.2f}

NET AMOUNT PAYABLE: ₹{result['net_amount']:,.2f}

Calculated on: {result['date_calculated']}"""
        
        self.results_text.delete("1.0", "end")
        self.results_text.insert("1.0", results_text)
    
    def save_calculation(self):
        """Save deduction calculation to database"""
        if not hasattr(self, 'calculation_result'):
            messagebox.showwarning("No Data", "Please calculate deductions first.")
            return
        
        try:
            result = self.calculation_result
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            success = self.db_manager.execute_query('''
                INSERT INTO deductions (
                    bill_number, contractor_name, gross_amount, tds_amount,
                    security_deduction, other_deductions, net_amount, date_created
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                result['bill_number'],
                result['contractor_name'],
                result['gross_amount'],
                result['tds_amount'],
                result['security_deduction'],
                result['other_deductions'],
                result['net_amount'],
                current_time
            ))
            
            if success:
                messagebox.showinfo("Success", "Deduction calculation saved successfully!")
                self.load_recent_calculations()  # Refresh the list
            else:
                messagebox.showerror("Error", "Failed to save calculation.")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save calculation: {str(e)}")
    
    def generate_pdf(self):
        """Generate PDF for deduction calculation"""
        if not hasattr(self, 'calculation_result'):
            messagebox.showwarning("No Data", "Please calculate deductions first.")
            return
        
        try:
            # Choose save location
            file_path = filedialog.asksaveasfilename(
                title="Save Deductions Table PDF",
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf")],
                initialname=f"Deductions_Table_{self.calculation_result['bill_number']}_{datetime.now().strftime('%Y%m%d')}.pdf"
            )
            
            if file_path:
                # Generate PDF
                if self.pdf_generator.generate_deductions_table_pdf(file_path, self.calculation_result):
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
        self.bill_number_entry.delete(0, "end")
        self.contractor_entry.delete(0, "end")
        self.gross_amount_entry.delete(0, "end")
        self.tds_rate_entry.delete(0, "end")
        self.tds_rate_entry.insert(0, "2.0")  # Reset to default
        self.security_rate_entry.delete(0, "end")
        self.security_rate_entry.insert(0, "5.0")  # Reset to default
        self.other_deductions_entry.delete(0, "end")
        self.other_deductions_entry.insert(0, "0")  # Reset to default
        self.work_desc_entry.delete("1.0", "end")
        
        # Clear results
        self.results_text.delete("1.0", "end")
        self.results_text.insert("1.0", "No calculations performed yet.")
        
        # Clear calculation result
        if hasattr(self, 'calculation_result'):
            delattr(self, 'calculation_result')
    
    def load_recent_calculations(self):
        """Load and display recent deduction calculations"""
        try:
            # Clear existing items
            for widget in self.calculations_listbox.winfo_children():
                widget.destroy()
            
            # Fetch recent calculations
            calculations = self.db_manager.fetch_all('''
                SELECT bill_number, contractor_name, gross_amount, net_amount, 
                       total_deductions, date_created
                FROM deductions 
                ORDER BY date_created DESC 
                LIMIT 10
            ''')
            
            if calculations:
                for calc in calculations:
                    calc_frame = ctk.CTkFrame(self.calculations_listbox)
                    calc_frame.pack(fill="x", padx=5, pady=2)
                    
                    # Calculation info
                    info_text = f"Bill: {calc[0]} | Contractor: {calc[1]} | Gross: ₹{calc[2]:,.2f} | Net: ₹{calc[4]:,.2f}"
                    info_label = ctk.CTkLabel(
                        calc_frame,
                        text=info_text,
                        font=ctk.CTkFont(size=11)
                    )
                    info_label.pack(side="left", padx=10, pady=5)
                    
                    # Load button
                    load_btn = ctk.CTkButton(
                        calc_frame,
                        text="Load",
                        command=lambda c=calc: self.load_calculation_data(c),
                        width=60,
                        height=25
                    )
                    load_btn.pack(side="right", padx=10, pady=5)
            else:
                no_calcs_label = ctk.CTkLabel(
                    self.calculations_listbox,
                    text="No deduction calculations found. Create your first calculation above.",
                    font=ctk.CTkFont(size=12),
                    text_color="#666666"
                )
                no_calcs_label.pack(pady=20)
                
        except Exception as e:
            print(f"Error loading recent calculations: {e}")
    
    def load_calculation_data(self, calc_tuple):
        """Load calculation data into form"""
        try:
            # Get full calculation data
            calc_data = self.db_manager.fetch_one('''
                SELECT bill_number, contractor_name, gross_amount, tds_amount,
                       security_deduction, other_deductions, work_description
                FROM deductions 
                WHERE bill_number = ?
            ''', (calc_tuple[0],))
            
            if calc_data:
                # Clear form first
                self.clear_form()
                
                # Load data
                self.bill_number_entry.insert(0, calc_data[0])
                self.contractor_entry.insert(0, calc_data[1])
                self.gross_amount_entry.insert(0, str(calc_data[2]))
                
                # Calculate rates from amounts
                if calc_data[2] > 0:  # gross_amount > 0
                    tds_rate = (calc_data[3] / calc_data[2]) * 100
                    security_rate = (calc_data[4] / calc_data[2]) * 100
                    
                    self.tds_rate_entry.delete(0, "end")
                    self.tds_rate_entry.insert(0, f"{tds_rate:.2f}")
                    
                    self.security_rate_entry.delete(0, "end")
                    self.security_rate_entry.insert(0, f"{security_rate:.2f}")
                
                self.other_deductions_entry.delete(0, "end")
                self.other_deductions_entry.insert(0, str(calc_data[5]))
                
                if calc_data[6]:  # work_description
                    self.work_desc_entry.insert("1.0", calc_data[6])
                    
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load calculation data: {str(e)}")
    
    def focus(self):
        """Bring window to focus"""
        self.window.lift()
        self.window.focus_force()