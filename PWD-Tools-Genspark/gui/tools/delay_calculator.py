"""
Delay Calculator Tool - Calculate project delays and timeline analysis
Desktop implementation for delay calculations and penalty assessment
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime, timedelta
import calendar

class DelayCalculatorTool:
    def __init__(self, db_manager, settings, parent=None):
        """Initialize Delay Calculator tool window"""
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
        self.window.title("Delay Calculator - Project timeline analysis")
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
            text="⏰ Project Delay Calculator",
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
        """Create input form for project details"""
        form_frame = ctk.CTkFrame(parent)
        form_frame.pack(fill="x", padx=10, pady=5)
        
        # Form title
        form_title = ctk.CTkLabel(
            form_frame,
            text="Project Timeline Details",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        form_title.pack(pady=(10, 15))
        
        # Input fields
        fields_frame = ctk.CTkFrame(form_frame)
        fields_frame.pack(fill="x", padx=10, pady=5)
        
        # Project Name
        ctk.CTkLabel(fields_frame, text="Project Name:", font=ctk.CTkFont(weight="bold")).grid(
            row=0, column=0, padx=10, pady=5, sticky="w"
        )
        self.project_name_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Enter project name")
        self.project_name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        
        # Contractor Name
        ctk.CTkLabel(fields_frame, text="Contractor Name:", font=ctk.CTkFont(weight="bold")).grid(
            row=1, column=0, padx=10, pady=5, sticky="w"
        )
        self.contractor_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Enter contractor name")
        self.contractor_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        # Planned Start Date
        ctk.CTkLabel(fields_frame, text="Planned Start Date:", font=ctk.CTkFont(weight="bold")).grid(
            row=2, column=0, padx=10, pady=5, sticky="w"
        )
        self.planned_start_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="YYYY-MM-DD")
        self.planned_start_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        
        # Actual Start Date
        ctk.CTkLabel(fields_frame, text="Actual Start Date:", font=ctk.CTkFont(weight="bold")).grid(
            row=3, column=0, padx=10, pady=5, sticky="w"
        )
        self.actual_start_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="YYYY-MM-DD")
        self.actual_start_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")
        
        # Planned Completion Date
        ctk.CTkLabel(fields_frame, text="Planned Completion:", font=ctk.CTkFont(weight="bold")).grid(
            row=4, column=0, padx=10, pady=5, sticky="w"
        )
        self.planned_completion_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="YYYY-MM-DD")
        self.planned_completion_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")
        
        # Actual Completion Date
        ctk.CTkLabel(fields_frame, text="Actual Completion:", font=ctk.CTkFont(weight="bold")).grid(
            row=5, column=0, padx=10, pady=5, sticky="w"
        )
        self.actual_completion_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="YYYY-MM-DD (leave empty if ongoing)")
        self.actual_completion_entry.grid(row=5, column=1, padx=10, pady=5, sticky="ew")
        
        # Contract Amount
        ctk.CTkLabel(fields_frame, text="Contract Amount (₹):", font=ctk.CTkFont(weight="bold")).grid(
            row=6, column=0, padx=10, pady=5, sticky="w"
        )
        self.contract_amount_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Enter contract amount")
        self.contract_amount_entry.grid(row=6, column=1, padx=10, pady=5, sticky="ew")
        
        # Penalty Rate
        ctk.CTkLabel(fields_frame, text="Penalty Rate (% per day):", font=ctk.CTkFont(weight="bold")).grid(
            row=7, column=0, padx=10, pady=5, sticky="w"
        )
        self.penalty_rate_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Default: 0.05% per day")
        self.penalty_rate_entry.insert(0, "0.05")
        self.penalty_rate_entry.grid(row=7, column=1, padx=10, pady=5, sticky="ew")
        
        # Calculate button
        calc_btn = ctk.CTkButton(
            fields_frame,
            text="🧮 Calculate Delay",
            command=self.calculate_delay,
            width=200,
            height=35
        )
        calc_btn.grid(row=8, column=0, columnspan=2, pady=15)
        
        # Configure grid weights
        fields_frame.grid_columnconfigure(1, weight=1)
    
    def create_results_section(self, parent):
        """Create results display section"""
        self.results_frame = ctk.CTkFrame(parent)
        self.results_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Results title
        results_title = ctk.CTkLabel(
            self.results_frame,
            text="Delay Analysis Results",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        results_title.pack(pady=(10, 5))
        
        # Results display area
        self.results_display = ctk.CTkScrollableFrame(self.results_frame, height=200)
        self.results_display.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Initial message
        self.no_calc_label = ctk.CTkLabel(
            self.results_display,
            text="Enter project details above and click 'Calculate Delay' to see analysis",
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
            command=self.save_delay_record,
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
    
    def calculate_delay(self):
        """Calculate project delay and penalties"""
        try:
            # Validate inputs
            project_name = self.project_name_entry.get().strip()
            contractor_name = self.contractor_entry.get().strip()
            planned_start_str = self.planned_start_entry.get().strip()
            actual_start_str = self.actual_start_entry.get().strip()
            planned_completion_str = self.planned_completion_entry.get().strip()
            actual_completion_str = self.actual_completion_entry.get().strip()
            contract_amount_str = self.contract_amount_entry.get().strip()
            penalty_rate_str = self.penalty_rate_entry.get().strip()
            
            if not all([project_name, contractor_name, planned_start_str, planned_completion_str, contract_amount_str]):
                messagebox.showerror("Validation Error", "Please fill in all required fields.")
                return
            
            # Parse dates
            try:
                planned_start = datetime.strptime(planned_start_str, "%Y-%m-%d")
                planned_completion = datetime.strptime(planned_completion_str, "%Y-%m-%d")
                
                actual_start = None
                if actual_start_str:
                    actual_start = datetime.strptime(actual_start_str, "%Y-%m-%d")
                
                actual_completion = None
                if actual_completion_str:
                    actual_completion = datetime.strptime(actual_completion_str, "%Y-%m-%d")
                
            except ValueError:
                messagebox.showerror("Validation Error", "Please enter dates in YYYY-MM-DD format.")
                return
            
            # Parse amounts
            try:
                contract_amount = float(contract_amount_str)
                penalty_rate = float(penalty_rate_str)
            except ValueError:
                messagebox.showerror("Validation Error", "Please enter valid amounts.")
                return
            
            # Calculate delays
            current_date = datetime.now()
            
            # Start delay
            start_delay_days = 0
            if actual_start:
                start_delay_days = max(0, (actual_start - planned_start).days)
            
            # Completion delay
            completion_delay_days = 0
            if actual_completion:
                # Project completed
                completion_delay_days = max(0, (actual_completion - planned_completion).days)
                project_status = "Completed"
                status_color = "#10B981" if completion_delay_days == 0 else "#EF4444"
            else:
                # Project ongoing
                completion_delay_days = max(0, (current_date - planned_completion).days)
                project_status = "Ongoing"
                status_color = "#F59E0B" if completion_delay_days > 0 else "#10B981"
            
            # Total delay
            total_delay_days = start_delay_days + completion_delay_days
            
            # Calculate penalties
            penalty_amount = 0
            if completion_delay_days > 0:
                daily_penalty = (contract_amount * penalty_rate) / 100
                penalty_amount = daily_penalty * completion_delay_days
            
            # Calculate project duration
            planned_duration = (planned_completion - planned_start).days
            if actual_start and actual_completion:
                actual_duration = (actual_completion - actual_start).days
            elif actual_start:
                actual_duration = (current_date - actual_start).days
            else:
                actual_duration = 0
            
            # Display results
            self.display_delay_results({
                'project_name': project_name,
                'contractor_name': contractor_name,
                'planned_start': planned_start,
                'actual_start': actual_start,
                'planned_completion': planned_completion,
                'actual_completion': actual_completion,
                'contract_amount': contract_amount,
                'penalty_rate': penalty_rate,
                'start_delay_days': start_delay_days,
                'completion_delay_days': completion_delay_days,
                'total_delay_days': total_delay_days,
                'penalty_amount': penalty_amount,
                'project_status': project_status,
                'status_color': status_color,
                'planned_duration': planned_duration,
                'actual_duration': actual_duration
            })
            
            # Store calculation data
            self.current_calculation = {
                'project_name': project_name,
                'contractor_name': contractor_name,
                'planned_start_date': planned_start_str,
                'actual_start_date': actual_start_str,
                'planned_completion_date': planned_completion_str,
                'actual_completion_date': actual_completion_str,
                'delay_days': total_delay_days,
                'penalty_amount': penalty_amount,
                'delay_reason': f"Start delay: {start_delay_days} days, Completion delay: {completion_delay_days} days"
            }
            
            # Enable save button
            self.save_btn.configure(state="normal")
            
        except Exception as e:
            messagebox.showerror("Calculation Error", f"Failed to calculate delay: {str(e)}")
    
    def display_delay_results(self, data):
        """Display delay calculation results"""
        # Clear previous results
        for widget in self.results_display.winfo_children():
            widget.destroy()
        
        # Project info
        info_frame = ctk.CTkFrame(self.results_display)
        info_frame.pack(fill="x", padx=5, pady=5)
        
        ctk.CTkLabel(info_frame, text=f"Project: {data['project_name']}", font=ctk.CTkFont(weight="bold", size=14)).pack(anchor="w", padx=10, pady=2)
        ctk.CTkLabel(info_frame, text=f"Contractor: {data['contractor_name']}", font=ctk.CTkFont(size=12)).pack(anchor="w", padx=10, pady=2)
        ctk.CTkLabel(info_frame, text=f"Contract Amount: ₹ {data['contract_amount']:,.2f}", font=ctk.CTkFont(size=12)).pack(anchor="w", padx=10, pady=2)
        
        # Timeline analysis
        timeline_frame = ctk.CTkFrame(self.results_display)
        timeline_frame.pack(fill="x", padx=5, pady=5)
        
        ctk.CTkLabel(timeline_frame, text="Timeline Analysis", font=ctk.CTkFont(weight="bold", size=14)).pack(pady=(10, 5))
        
        # Planned vs Actual dates
        dates_info = [
            ("Planned Start", data['planned_start'].strftime('%d/%m/%Y')),
            ("Actual Start", data['actual_start'].strftime('%d/%m/%Y') if data['actual_start'] else "Not started"),
            ("Planned Completion", data['planned_completion'].strftime('%d/%m/%Y')),
            ("Actual Completion", data['actual_completion'].strftime('%d/%m/%Y') if data['actual_completion'] else "Ongoing"),
            ("Planned Duration", f"{data['planned_duration']} days"),
            ("Actual Duration", f"{data['actual_duration']} days" if data['actual_duration'] > 0 else "N/A")
        ]
        
        for label, value in dates_info:
            date_frame = ctk.CTkFrame(timeline_frame)
            date_frame.pack(fill="x", padx=10, pady=1)
            
            ctk.CTkLabel(date_frame, text=f"{label}:", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=10, pady=3)
            ctk.CTkLabel(date_frame, text=value).pack(side="right", padx=10, pady=3)
        
        # Delay summary
        delay_frame = ctk.CTkFrame(self.results_display)
        delay_frame.pack(fill="x", padx=5, pady=5)
        
        ctk.CTkLabel(delay_frame, text="Delay Summary", font=ctk.CTkFont(weight="bold", size=14)).pack(pady=(10, 5))
        
        # Delay details
        delay_info = [
            ("Start Delay", f"{data['start_delay_days']} days"),
            ("Completion Delay", f"{data['completion_delay_days']} days"),
            ("Total Delay", f"{data['total_delay_days']} days"),
            ("Project Status", data['project_status'])
        ]
        
        for label, value in delay_info:
            delay_detail_frame = ctk.CTkFrame(delay_frame)
            delay_detail_frame.pack(fill="x", padx=10, pady=1)
            
            ctk.CTkLabel(delay_detail_frame, text=f"{label}:", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=10, pady=3)
            
            color = "#EF4444" if "delay" in label.lower() and int(value.split()[0]) > 0 else "#10B981"
            if label == "Project Status":
                color = data['status_color']
            
            ctk.CTkLabel(delay_detail_frame, text=value, text_color=color).pack(side="right", padx=10, pady=3)
        
        # Penalty calculation
        if data['penalty_amount'] > 0:
            penalty_frame = ctk.CTkFrame(self.results_display)
            penalty_frame.pack(fill="x", padx=5, pady=5)
            
            ctk.CTkLabel(penalty_frame, text="Penalty Calculation", font=ctk.CTkFont(weight="bold", size=14)).pack(pady=(10, 5))
            
            penalty_details = ctk.CTkFrame(penalty_frame)
            penalty_details.pack(fill="x", padx=10, pady=5)
            
            ctk.CTkLabel(penalty_details, text=f"Penalty Rate: {data['penalty_rate']}% per day").pack(anchor="w", padx=10, pady=2)
            ctk.CTkLabel(penalty_details, text=f"Delay Days: {data['completion_delay_days']} days").pack(anchor="w", padx=10, pady=2)
            ctk.CTkLabel(penalty_details, text=f"Daily Penalty: ₹ {(data['contract_amount'] * data['penalty_rate']) / 100:,.2f}").pack(anchor="w", padx=10, pady=2)
            
            # Total penalty (highlighted)
            penalty_total_frame = ctk.CTkFrame(penalty_frame)
            penalty_total_frame.pack(fill="x", padx=10, pady=5)
            
            ctk.CTkLabel(penalty_total_frame, text="Total Penalty Amount:", font=ctk.CTkFont(weight="bold", size=16)).pack(side="left", padx=10, pady=8)
            ctk.CTkLabel(penalty_total_frame, text=f"₹ {data['penalty_amount']:,.2f}", font=ctk.CTkFont(weight="bold", size=16), text_color="#EF4444").pack(side="right", padx=10, pady=8)
        else:
            # No penalty
            no_penalty_frame = ctk.CTkFrame(self.results_display)
            no_penalty_frame.pack(fill="x", padx=5, pady=5)
            
            ctk.CTkLabel(no_penalty_frame, text="✅ No Penalty - Project on schedule", font=ctk.CTkFont(weight="bold", size=14), text_color="#10B981").pack(pady=10)
    
    def save_delay_record(self):
        """Save delay record to database"""
        if not hasattr(self, 'current_calculation'):
            messagebox.showerror("Error", "Please calculate delay first.")
            return
        
        try:
            calc = self.current_calculation
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            success = self.db_manager.execute_query('''
                INSERT INTO delay_records (
                    project_name, contractor_name, planned_start_date, actual_start_date,
                    planned_completion_date, actual_completion_date, delay_days, 
                    delay_reason, penalty_amount, date_created
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                calc['project_name'], calc['contractor_name'], calc['planned_start_date'],
                calc['actual_start_date'], calc['planned_completion_date'], calc['actual_completion_date'],
                calc['delay_days'], calc['delay_reason'], calc['penalty_amount'], current_time
            ))
            
            if success:
                messagebox.showinfo("Success", "Delay record saved successfully!")
            else:
                messagebox.showerror("Error", "Failed to save delay record.")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save delay record: {str(e)}")
    
    def clear_form(self):
        """Clear all form fields"""
        self.project_name_entry.delete(0, "end")
        self.contractor_entry.delete(0, "end")
        self.planned_start_entry.delete(0, "end")
        self.actual_start_entry.delete(0, "end")
        self.planned_completion_entry.delete(0, "end")
        self.actual_completion_entry.delete(0, "end")
        self.contract_amount_entry.delete(0, "end")
        self.penalty_rate_entry.delete(0, "end")
        self.penalty_rate_entry.insert(0, "0.05")
        
        # Clear results
        for widget in self.results_display.winfo_children():
            widget.destroy()
        
        self.no_calc_label = ctk.CTkLabel(
            self.results_display,
            text="Enter project details above and click 'Calculate Delay' to see analysis",
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
