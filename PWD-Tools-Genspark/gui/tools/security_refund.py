"""
Security Refund Tool - Process security deposit refund calculations
Desktop implementation for security deposit management
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime, timedelta

class SecurityRefundTool:
    def __init__(self, db_manager, settings, parent=None):
        """Initialize Security Refund tool window"""
        self.db_manager = db_manager
        self.settings = settings
        
        # Create tool window
        if parent is not None:
            self.window = ctk.CTkToplevel(parent)
        else:
            self.window = ctk.CTkToplevel()
        self.setup_window()
        self.create_interface()
    
    def setup_window(self):
        """Configure tool window"""
        self.window.title("Security Refund - Process security deposit refunds")
        self.window.geometry("800x600")
        self.window.minsize(700, 500)
        
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
            text="🔒 Security Deposit Refund Calculator",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        title_label.pack(pady=15)
        
        # Main content
        main_frame = ctk.CTkFrame(self.window)
        main_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Input form
        self.create_input_form(main_frame)
        
        # Results section
        self.create_results_section(main_frame)
        
        # Action buttons
        self.create_action_buttons(main_frame)
    
    def create_input_form(self, parent):
        """Create input form for security deposit details"""
        form_frame = ctk.CTkFrame(parent)
        form_frame.pack(fill="x", padx=10, pady=5)
        
        # Form title
        form_title = ctk.CTkLabel(
            form_frame,
            text="Security Deposit Details",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        form_title.pack(pady=(10, 15))
        
        # Input fields
        fields_frame = ctk.CTkFrame(form_frame)
        fields_frame.pack(fill="x", padx=10, pady=5)
        
        # Work Order Number
        ctk.CTkLabel(fields_frame, text="Work Order Number:", font=ctk.CTkFont(weight="bold")).grid(
            row=0, column=0, padx=10, pady=5, sticky="w"
        )
        self.work_order_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Enter work order number")
        self.work_order_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        
        # Contractor Name
        ctk.CTkLabel(fields_frame, text="Contractor Name:", font=ctk.CTkFont(weight="bold")).grid(
            row=1, column=0, padx=10, pady=5, sticky="w"
        )
        self.contractor_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Enter contractor name")
        self.contractor_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        # Deposit Amount
        ctk.CTkLabel(fields_frame, text="Deposit Amount (₹):", font=ctk.CTkFont(weight="bold")).grid(
            row=2, column=0, padx=10, pady=5, sticky="w"
        )
        self.deposit_amount_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Enter security deposit amount")
        self.deposit_amount_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        
        # Deposit Type
        ctk.CTkLabel(fields_frame, text="Deposit Type:", font=ctk.CTkFont(weight="bold")).grid(
            row=3, column=0, padx=10, pady=5, sticky="w"
        )
        self.deposit_type_var = ctk.StringVar(value="Bank Guarantee")
        deposit_type_menu = ctk.CTkOptionMenu(
            fields_frame,
            variable=self.deposit_type_var,
            values=["Bank Guarantee", "Fixed Deposit", "Cash Deposit", "Insurance Bond"],
            width=300
        )
        deposit_type_menu.grid(row=3, column=1, padx=10, pady=5, sticky="ew")
        
        # Bank Name
        ctk.CTkLabel(fields_frame, text="Bank Name:", font=ctk.CTkFont(weight="bold")).grid(
            row=4, column=0, padx=10, pady=5, sticky="w"
        )
        self.bank_name_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Enter bank name")
        self.bank_name_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")
        
        # Validity Date
        ctk.CTkLabel(fields_frame, text="Validity Date:", font=ctk.CTkFont(weight="bold")).grid(
            row=5, column=0, padx=10, pady=5, sticky="w"
        )
        self.validity_date_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="YYYY-MM-DD")
        self.validity_date_entry.grid(row=5, column=1, padx=10, pady=5, sticky="ew")
        
        # Work Completion Date
        ctk.CTkLabel(fields_frame, text="Work Completion Date:", font=ctk.CTkFont(weight="bold")).grid(
            row=6, column=0, padx=10, pady=5, sticky="w"
        )
        self.completion_date_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="YYYY-MM-DD (leave empty if ongoing)")
        self.completion_date_entry.grid(row=6, column=1, padx=10, pady=5, sticky="ew")
        
        # Calculate button
        calc_btn = ctk.CTkButton(
            fields_frame,
            text="🧮 Calculate Refund",
            command=self.calculate_refund,
            width=200,
            height=35
        )
        calc_btn.grid(row=7, column=0, columnspan=2, pady=15)
        
        # Configure grid weights
        fields_frame.grid_columnconfigure(1, weight=1)
    
    def create_results_section(self, parent):
        """Create results display section"""
        self.results_frame = ctk.CTkFrame(parent)
        self.results_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Results title
        results_title = ctk.CTkLabel(
            self.results_frame,
            text="Refund Eligibility Results",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        results_title.pack(pady=(10, 5))
        
        # Results display area
        self.results_display = ctk.CTkFrame(self.results_frame)
        self.results_display.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Initial message
        self.no_calc_label = ctk.CTkLabel(
            self.results_display,
            text="Enter security deposit details and click 'Calculate Refund' to see eligibility",
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
        
        # Save record button
        self.save_btn = ctk.CTkButton(
            btn_container,
            text="💾 Save Record",
            command=self.save_security_record,
            width=150,
            height=35,
            state="disabled"
        )
        self.save_btn.pack(side="left", padx=5)
        
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
    
    def calculate_refund(self):
        """Calculate security deposit refund eligibility"""
        try:
            # Validate inputs
            work_order = self.work_order_entry.get().strip()
            contractor_name = self.contractor_entry.get().strip()
            deposit_amount_str = self.deposit_amount_entry.get().strip()
            deposit_type = self.deposit_type_var.get()
            bank_name = self.bank_name_entry.get().strip()
            validity_date_str = self.validity_date_entry.get().strip()
            completion_date_str = self.completion_date_entry.get().strip()
            
            if not all([work_order, contractor_name, deposit_amount_str, validity_date_str]):
                messagebox.showerror("Validation Error", "Please fill in all required fields.")
                return
            
            try:
                deposit_amount = float(deposit_amount_str)
            except ValueError:
                messagebox.showerror("Validation Error", "Please enter a valid deposit amount.")
                return
            
            try:
                validity_date = datetime.strptime(validity_date_str, "%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Validation Error", "Please enter validity date in YYYY-MM-DD format.")
                return
            
            completion_date = None
            if completion_date_str:
                try:
                    completion_date = datetime.strptime(completion_date_str, "%Y-%m-%d")
                except ValueError:
                    messagebox.showerror("Validation Error", "Please enter completion date in YYYY-MM-DD format.")
                    return
            
            # Calculate refund eligibility
            current_date = datetime.now()
            
            # Determine work status
            if completion_date:
                work_status = "Completed"
                reference_date = completion_date
                work_completed = True
            else:
                work_status = "Ongoing"
                reference_date = current_date
                work_completed = False
            
            # Calculate days since completion or current status
            days_since_completion = 0
            if work_completed:
                days_since_completion = (current_date - completion_date).days
            
            # Check validity
            validity_status = "Valid" if validity_date >= current_date else "Expired"
            days_to_expiry = (validity_date - current_date).days
            
            # Determine refund eligibility
            refund_eligible = False
            refund_amount = 0
            refund_percentage = 0
            eligibility_reason = ""
            
            if work_completed:
                # Work is completed - check defect liability period
                defect_liability_days = 365  # 1 year standard
                
                if days_since_completion < defect_liability_days:
                    # Still in defect liability period
                    remaining_liability_days = defect_liability_days - days_since_completion
                    refund_eligible = False
                    eligibility_reason = f"Work completed but still in defect liability period. {remaining_liability_days} days remaining."
                else:
                    # Defect liability period over
                    if validity_status == "Valid":
                        refund_eligible = True
                        refund_amount = deposit_amount
                        refund_percentage = 100
                        eligibility_reason = "Work completed and defect liability period over. Full refund eligible."
                    else:
                        # Check how long expired
                        days_expired = abs(days_to_expiry)
                        if days_expired <= 30:
                            refund_eligible = True
                            refund_amount = deposit_amount * 0.95  # 5% penalty
                            refund_percentage = 95
                            eligibility_reason = f"Expired by {days_expired} days. 95% refund with 5% penalty."
                        elif days_expired <= 90:
                            refund_eligible = True
                            refund_amount = deposit_amount * 0.80  # 20% penalty
                            refund_percentage = 80
                            eligibility_reason = f"Expired by {days_expired} days. 80% refund with 20% penalty."
                        else:
                            refund_eligible = False
                            eligibility_reason = f"Expired by {days_expired} days. Too late for refund."
            else:
                # Work is ongoing
                if validity_status == "Valid":
                    refund_eligible = False
                    eligibility_reason = f"Work is ongoing. Refund not eligible until completion and defect liability period."
                else:
                    # Expired during ongoing work
                    days_expired = abs(days_to_expiry)
                    refund_eligible = False
                    eligibility_reason = f"Security expired during ongoing work ({days_expired} days ago). Renewal required."
            
            # Display results
            self.display_refund_results({
                'work_order': work_order,
                'contractor_name': contractor_name,
                'deposit_amount': deposit_amount,
                'deposit_type': deposit_type,
                'bank_name': bank_name,
                'validity_date': validity_date,
                'completion_date': completion_date,
                'work_status': work_status,
                'validity_status': validity_status,
                'days_to_expiry': days_to_expiry,
                'days_since_completion': days_since_completion,
                'refund_eligible': refund_eligible,
                'refund_amount': refund_amount,
                'refund_percentage': refund_percentage,
                'eligibility_reason': eligibility_reason
            })
            
            # Store calculation data
            self.current_calculation = {
                'work_order_number': work_order,
                'contractor_name': contractor_name,
                'deposit_amount': deposit_amount,
                'deposit_type': deposit_type,
                'bank_name': bank_name,
                'validity_date': validity_date_str,
                'refund_status': 'Eligible' if refund_eligible else 'Not Eligible',
                'refund_amount': refund_amount,
                'eligibility_reason': eligibility_reason
            }
            
            # Enable save button
            self.save_btn.configure(state="normal")
            
        except Exception as e:
            messagebox.showerror("Calculation Error", f"Failed to calculate refund: {str(e)}")
    
    def display_refund_results(self, data):
        """Display refund calculation results"""
        # Clear previous results
        for widget in self.results_display.winfo_children():
            widget.destroy()
        
        # Security deposit info
        info_frame = ctk.CTkFrame(self.results_display)
        info_frame.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(info_frame, text="Security Deposit Information", font=ctk.CTkFont(weight="bold", size=14)).pack(pady=(10, 5))
        
        info_details = [
            ("Work Order", data['work_order']),
            ("Contractor", data['contractor_name']),
            ("Deposit Amount", f"₹ {data['deposit_amount']:,.2f}"),
            ("Deposit Type", data['deposit_type']),
            ("Bank Name", data['bank_name']),
            ("Validity Date", data['validity_date'].strftime('%d/%m/%Y')),
            ("Work Status", data['work_status'])
        ]
        
        for label, value in info_details:
            detail_frame = ctk.CTkFrame(info_frame)
            detail_frame.pack(fill="x", padx=10, pady=1)
            
            ctk.CTkLabel(detail_frame, text=f"{label}:", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=10, pady=3)
            ctk.CTkLabel(detail_frame, text=value).pack(side="right", padx=10, pady=3)
        
        # Status analysis
        status_frame = ctk.CTkFrame(self.results_display)
        status_frame.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(status_frame, text="Status Analysis", font=ctk.CTkFont(weight="bold", size=14)).pack(pady=(10, 5))
        
        # Validity status
        validity_color = "#10B981" if data['validity_status'] == "Valid" else "#EF4444"
        validity_frame = ctk.CTkFrame(status_frame)
        validity_frame.pack(fill="x", padx=10, pady=2)
        
        ctk.CTkLabel(validity_frame, text="Validity Status:", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=10, pady=3)
        validity_text = f"{data['validity_status']}"
        if data['days_to_expiry'] >= 0:
            validity_text += f" ({data['days_to_expiry']} days remaining)"
        else:
            validity_text += f" ({abs(data['days_to_expiry'])} days expired)"
        
        ctk.CTkLabel(validity_frame, text=validity_text, text_color=validity_color).pack(side="right", padx=10, pady=3)
        
        # Work completion status
        if data['completion_date']:
            completion_frame = ctk.CTkFrame(status_frame)
            completion_frame.pack(fill="x", padx=10, pady=2)
            
            ctk.CTkLabel(completion_frame, text="Days Since Completion:", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=10, pady=3)
            ctk.CTkLabel(completion_frame, text=f"{data['days_since_completion']} days").pack(side="right", padx=10, pady=3)
        
        # Refund eligibility
        eligibility_frame = ctk.CTkFrame(self.results_display)
        eligibility_frame.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(eligibility_frame, text="Refund Eligibility", font=ctk.CTkFont(weight="bold", size=14)).pack(pady=(10, 5))
        
        # Eligibility status
        eligibility_color = "#10B981" if data['refund_eligible'] else "#EF4444"
        status_text = "ELIGIBLE" if data['refund_eligible'] else "NOT ELIGIBLE"
        
        status_label_frame = ctk.CTkFrame(eligibility_frame)
        status_label_frame.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(status_label_frame, text="Status:", font=ctk.CTkFont(weight="bold", size=16)).pack(side="left", padx=10, pady=8)
        ctk.CTkLabel(status_label_frame, text=status_text, font=ctk.CTkFont(weight="bold", size=16), text_color=eligibility_color).pack(side="right", padx=10, pady=8)
        
        # Refund amount (if eligible)
        if data['refund_eligible']:
            amount_frame = ctk.CTkFrame(eligibility_frame)
            amount_frame.pack(fill="x", padx=10, pady=5)
            
            ctk.CTkLabel(amount_frame, text="Refund Amount:", font=ctk.CTkFont(weight="bold", size=14)).pack(side="left", padx=10, pady=5)
            ctk.CTkLabel(amount_frame, text=f"₹ {data['refund_amount']:,.2f} ({data['refund_percentage']}%)", 
                        font=ctk.CTkFont(weight="bold", size=14), text_color="#10B981").pack(side="right", padx=10, pady=5)
        
        # Reason
        reason_frame = ctk.CTkFrame(eligibility_frame)
        reason_frame.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(reason_frame, text="Reason:", font=ctk.CTkFont(weight="bold")).pack(anchor="w", padx=10, pady=2)
        reason_label = ctk.CTkLabel(reason_frame, text=data['eligibility_reason'], 
                                   font=ctk.CTkFont(size=12), wraplength=600)
        reason_label.pack(anchor="w", padx=10, pady=2)
    
    def save_security_record(self):
        """Save security deposit record to database"""
        if not hasattr(self, 'current_calculation'):
            messagebox.showerror("Error", "Please calculate refund first.")
            return
        
        try:
            calc = self.current_calculation
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            success = self.db_manager.execute_query('''
                INSERT INTO security_deposits (
                    work_order_number, contractor_name, deposit_amount, deposit_type,
                    bank_name, validity_date, refund_status, date_created
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                calc['work_order_number'], calc['contractor_name'], calc['deposit_amount'],
                calc['deposit_type'], calc['bank_name'], calc['validity_date'],
                calc['refund_status'], current_time
            ))
            
            if success:
                messagebox.showinfo("Success", "Security deposit record saved successfully!")
            else:
                messagebox.showerror("Error", "Failed to save security deposit record.")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save security deposit record: {str(e)}")
    
    def clear_form(self):
        """Clear all form fields"""
        self.work_order_entry.delete(0, "end")
        self.contractor_entry.delete(0, "end")
        self.deposit_amount_entry.delete(0, "end")
        self.deposit_type_var.set("Bank Guarantee")
        self.bank_name_entry.delete(0, "end")
        self.validity_date_entry.delete(0, "end")
        self.completion_date_entry.delete(0, "end")
        
        # Clear results
        for widget in self.results_display.winfo_children():
            widget.destroy()
        
        self.no_calc_label = ctk.CTkLabel(
            self.results_display,
            text="Enter security deposit details and click 'Calculate Refund' to see eligibility",
            font=ctk.CTkFont(size=14),
            text_color="#666666"
        )
        self.no_calc_label.pack(pady=40)
        
        # Disable save button
        self.save_btn.configure(state="disabled")
        
        # Clear calculation data
        if hasattr(self, 'current_calculation'):
            delattr(self, 'current_calculation')
    
    def focus(self):
        """Bring window to focus"""
        self.window.lift()
        self.window.focus_force()
