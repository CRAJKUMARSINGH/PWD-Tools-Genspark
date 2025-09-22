"""
Stamp Duty Calculator - Calculate stamp duty for work orders
Desktop implementation for stamp duty calculations
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class StampDutyTool:
    def __init__(self, db_manager, settings, parent=None):
        """Initialize Stamp Duty Calculator tool window"""
        self.db_manager = db_manager
        self.settings = settings
        
        # Create tool window
        if parent is not None:
            self.window = ctk.CTkToplevel(parent)
        else:
            self.window = ctk.CTkToplevel()
        self.setup_window()
        self.create_interface()
        
        # Stamp duty rates (can be configured)
        self.stamp_duty_rates = {
            "Rajasthan": {
                "up_to_1_lakh": 0.5,
                "1_lakh_to_5_lakh": 1.0,
                "5_lakh_to_10_lakh": 1.5,
                "above_10_lakh": 2.0
            }
        }
    
    def setup_window(self):
        """Configure tool window"""
        self.window.title("Stamp Duty Calculator - Calculate work order stamp duty")
        self.window.geometry("700x600")
        self.window.minsize(600, 500)
        
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
            text="📋 Stamp Duty Calculator",
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
        """Create input form for work order details"""
        form_frame = ctk.CTkFrame(parent)
        form_frame.pack(fill="x", padx=10, pady=5)
        
        # Form title
        form_title = ctk.CTkLabel(
            form_frame,
            text="Work Order Details",
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
        
        # Work Description
        ctk.CTkLabel(fields_frame, text="Work Description:", font=ctk.CTkFont(weight="bold")).grid(
            row=1, column=0, padx=10, pady=5, sticky="w"
        )
        self.work_description_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Enter work description")
        self.work_description_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        # Contract Value
        ctk.CTkLabel(fields_frame, text="Contract Value (₹):", font=ctk.CTkFont(weight="bold")).grid(
            row=2, column=0, padx=10, pady=5, sticky="w"
        )
        self.contract_value_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Enter contract value")
        self.contract_value_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        
        # State
        ctk.CTkLabel(fields_frame, text="State:", font=ctk.CTkFont(weight="bold")).grid(
            row=3, column=0, padx=10, pady=5, sticky="w"
        )
        self.state_var = ctk.StringVar(value="Rajasthan")
        state_menu = ctk.CTkOptionMenu(
            fields_frame,
            variable=self.state_var,
            values=["Rajasthan", "Other"],
            width=300,
            command=self.on_state_change
        )
        state_menu.grid(row=3, column=1, padx=10, pady=5, sticky="ew")
        
        # Custom rate (for other states)
        ctk.CTkLabel(fields_frame, text="Custom Rate (%):", font=ctk.CTkFont(weight="bold")).grid(
            row=4, column=0, padx=10, pady=5, sticky="w"
        )
        self.custom_rate_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Enter custom rate if 'Other' state selected")
        self.custom_rate_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")
        self.custom_rate_entry.configure(state="disabled")
        
        # Date
        ctk.CTkLabel(fields_frame, text="Order Date:", font=ctk.CTkFont(weight="bold")).grid(
            row=5, column=0, padx=10, pady=5, sticky="w"
        )
        self.order_date_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="YYYY-MM-DD")
        self.order_date_entry.grid(row=5, column=1, padx=10, pady=5, sticky="ew")
        
        # Calculate button
        calc_btn = ctk.CTkButton(
            fields_frame,
            text="🧮 Calculate Stamp Duty",
            command=self.calculate_stamp_duty,
            width=200,
            height=35
        )
        calc_btn.grid(row=6, column=0, columnspan=2, pady=15)
        
        # Configure grid weights
        fields_frame.grid_columnconfigure(1, weight=1)
    
    def create_results_section(self, parent):
        """Create results display section"""
        self.results_frame = ctk.CTkFrame(parent)
        self.results_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Results title
        results_title = ctk.CTkLabel(
            self.results_frame,
            text="Stamp Duty Calculation Results",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        results_title.pack(pady=(10, 5))
        
        # Results display area
        self.results_display = ctk.CTkFrame(self.results_frame)
        self.results_display.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Initial message
        self.no_calc_label = ctk.CTkLabel(
            self.results_display,
            text="Enter work order details and click 'Calculate Stamp Duty' to see results",
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
            command=self.save_stamp_duty_record,
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
    
    def on_state_change(self, selected_state):
        """Handle state selection change"""
        if selected_state == "Other":
            self.custom_rate_entry.configure(state="normal")
        else:
            self.custom_rate_entry.configure(state="disabled")
            self.custom_rate_entry.delete(0, "end")
    
    def calculate_stamp_duty(self):
        """Calculate stamp duty based on contract value and state"""
        try:
            # Validate inputs
            work_order = self.work_order_entry.get().strip()
            work_description = self.work_description_entry.get().strip()
            contract_value_str = self.contract_value_entry.get().strip()
            state = self.state_var.get()
            order_date_str = self.order_date_entry.get().strip()
            
            if not all([work_order, work_description, contract_value_str, order_date_str]):
                messagebox.showerror("Validation Error", "Please fill in all required fields.")
                return
            
            try:
                contract_value = float(contract_value_str)
            except ValueError:
                messagebox.showerror("Validation Error", "Please enter a valid contract value.")
                return
            
            try:
                order_date = datetime.strptime(order_date_str, "%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Validation Error", "Please enter order date in YYYY-MM-DD format.")
                return
            
            # Calculate stamp duty
            if state == "Rajasthan":
                stamp_duty_rate, rate_description = self.get_rajasthan_rate(contract_value)
            else:
                # Custom rate for other states
                custom_rate_str = self.custom_rate_entry.get().strip()
                if not custom_rate_str:
                    messagebox.showerror("Validation Error", "Please enter custom rate for 'Other' state.")
                    return
                
                try:
                    stamp_duty_rate = float(custom_rate_str)
                    rate_description = f"Custom rate: {stamp_duty_rate}%"
                except ValueError:
                    messagebox.showerror("Validation Error", "Please enter a valid custom rate.")
                    return
            
            # Calculate stamp duty amount
            stamp_duty_amount = (contract_value * stamp_duty_rate) / 100
            
            # Display results
            self.display_stamp_duty_results({
                'work_order': work_order,
                'work_description': work_description,
                'contract_value': contract_value,
                'state': state,
                'order_date': order_date,
                'stamp_duty_rate': stamp_duty_rate,
                'rate_description': rate_description,
                'stamp_duty_amount': stamp_duty_amount
            })
            
            # Store calculation data
            self.current_calculation = {
                'work_order_number': work_order,
                'work_description': work_description,
                'contract_value': contract_value,
                'state': state,
                'stamp_duty_rate': stamp_duty_rate,
                'stamp_duty_amount': stamp_duty_amount,
                'order_date': order_date_str
            }
            
            # Enable save button
            self.save_btn.configure(state="normal")
            
        except Exception as e:
            messagebox.showerror("Calculation Error", f"Failed to calculate stamp duty: {str(e)}")
    
    def get_rajasthan_rate(self, contract_value):
        """Get stamp duty rate for Rajasthan based on contract value"""
        rates = self.stamp_duty_rates["Rajasthan"]
        
        if contract_value <= 100000:  # Up to 1 lakh
            return rates["up_to_1_lakh"], f"Up to ₹1 lakh: {rates['up_to_1_lakh']}%"
        elif contract_value <= 500000:  # 1 lakh to 5 lakh
            return rates["1_lakh_to_5_lakh"], f"₹1 lakh to ₹5 lakh: {rates['1_lakh_to_5_lakh']}%"
        elif contract_value <= 1000000:  # 5 lakh to 10 lakh
            return rates["5_lakh_to_10_lakh"], f"₹5 lakh to ₹10 lakh: {rates['5_lakh_to_10_lakh']}%"
        else:  # Above 10 lakh
            return rates["above_10_lakh"], f"Above ₹10 lakh: {rates['above_10_lakh']}%"
    
    def display_stamp_duty_results(self, data):
        """Display stamp duty calculation results"""
        # Clear previous results
        for widget in self.results_display.winfo_children():
            widget.destroy()
        
        # Work order info
        info_frame = ctk.CTkFrame(self.results_display)
        info_frame.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(info_frame, text="Work Order Information", font=ctk.CTkFont(weight="bold", size=14)).pack(pady=(10, 5))
        
        info_details = [
            ("Work Order Number", data['work_order']),
            ("Work Description", data['work_description']),
            ("Contract Value", f"₹ {data['contract_value']:,.2f}"),
            ("State", data['state']),
            ("Order Date", data['order_date'].strftime('%d/%m/%Y'))
        ]
        
        for label, value in info_details:
            detail_frame = ctk.CTkFrame(info_frame)
            detail_frame.pack(fill="x", padx=10, pady=1)
            
            ctk.CTkLabel(detail_frame, text=f"{label}:", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=10, pady=3)
            ctk.CTkLabel(detail_frame, text=value).pack(side="right", padx=10, pady=3)
        
        # Stamp duty calculation
        calc_frame = ctk.CTkFrame(self.results_display)
        calc_frame.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(calc_frame, text="Stamp Duty Calculation", font=ctk.CTkFont(weight="bold", size=14)).pack(pady=(10, 5))
        
        # Rate applied
        rate_frame = ctk.CTkFrame(calc_frame)
        rate_frame.pack(fill="x", padx=10, pady=2)
        
        ctk.CTkLabel(rate_frame, text="Rate Applied:", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=10, pady=3)
        ctk.CTkLabel(rate_frame, text=data['rate_description']).pack(side="right", padx=10, pady=3)
        
        # Calculation breakdown
        breakdown_frame = ctk.CTkFrame(calc_frame)
        breakdown_frame.pack(fill="x", padx=10, pady=2)
        
        ctk.CTkLabel(breakdown_frame, text="Calculation:", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=10, pady=3)
        calculation_text = f"₹ {data['contract_value']:,.0f} × {data['stamp_duty_rate']}% = ₹ {data['stamp_duty_amount']:,.2f}"
        ctk.CTkLabel(breakdown_frame, text=calculation_text).pack(side="right", padx=10, pady=3)
        
        # Final amount (highlighted)
        amount_frame = ctk.CTkFrame(self.results_display)
        amount_frame.pack(fill="x", padx=10, pady=10)
        
        ctk.CTkLabel(amount_frame, text="Stamp Duty Payable", font=ctk.CTkFont(weight="bold", size=16)).pack(pady=(10, 5))
        
        final_amount_frame = ctk.CTkFrame(amount_frame)
        final_amount_frame.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(final_amount_frame, text="Amount:", font=ctk.CTkFont(weight="bold", size=18)).pack(side="left", padx=10, pady=10)
        ctk.CTkLabel(final_amount_frame, text=f"₹ {data['stamp_duty_amount']:,.2f}", 
                    font=ctk.CTkFont(weight="bold", size=18), text_color="#10B981").pack(side="right", padx=10, pady=10)
        
        # Payment instructions
        instructions_frame = ctk.CTkFrame(self.results_display)
        instructions_frame.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(instructions_frame, text="Payment Instructions", font=ctk.CTkFont(weight="bold", size=14)).pack(pady=(10, 5))
        
        instructions_text = """
• Stamp duty must be paid before execution of the work order
• Payment can be made through e-stamping or physical stamps
• Keep the payment receipt for record purposes
• Ensure proper franking of the work order document
        """
        
        instructions_label = ctk.CTkLabel(instructions_frame, text=instructions_text.strip(), 
                                        font=ctk.CTkFont(size=12), justify="left")
        instructions_label.pack(padx=10, pady=5, anchor="w")
    
    def save_stamp_duty_record(self):
        """Save stamp duty record to database"""
        if not hasattr(self, 'current_calculation'):
            messagebox.showerror("Error", "Please calculate stamp duty first.")
            return
        
        try:
            calc = self.current_calculation
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            success = self.db_manager.execute_query('''
                INSERT INTO stamp_duty (
                    work_order_number, work_description, contract_value, state,
                    stamp_duty_rate, stamp_duty_amount, order_date, date_created
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                calc['work_order_number'], calc['work_description'], calc['contract_value'],
                calc['state'], calc['stamp_duty_rate'], calc['stamp_duty_amount'],
                calc['order_date'], current_time
            ))
            
            if success:
                messagebox.showinfo("Success", "Stamp duty record saved successfully!")
            else:
                messagebox.showerror("Error", "Failed to save stamp duty record.")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save stamp duty record: {str(e)}")
    
    def clear_form(self):
        """Clear all form fields"""
        self.work_order_entry.delete(0, "end")
        self.work_description_entry.delete(0, "end")
        self.contract_value_entry.delete(0, "end")
        self.state_var.set("Rajasthan")
        self.custom_rate_entry.delete(0, "end")
        self.custom_rate_entry.configure(state="disabled")
        self.order_date_entry.delete(0, "end")
        
        # Clear results
        for widget in self.results_display.winfo_children():
            widget.destroy()
        
        self.no_calc_label = ctk.CTkLabel(
            self.results_display,
            text="Enter work order details and click 'Calculate Stamp Duty' to see results",
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
