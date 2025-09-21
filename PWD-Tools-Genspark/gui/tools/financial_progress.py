"""
Financial Progress Tracker - Track project financial progress and liquidity damages
Desktop implementation for financial progress monitoring
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime, timedelta
import json

class FinancialProgressTool:
    def __init__(self, db_manager, settings, parent=None):
        """Initialize Financial Progress Tracker tool window"""
        self.db_manager = db_manager
        self.settings = settings
        
        # Create tool window
        if parent is not None:
            self.window = ctk.CTkToplevel(parent)
        else:
            self.window = ctk.CTkToplevel()
        self.setup_window()
        self.create_interface()
        
        # Initialize data
        self.progress_records = []
    
    def setup_window(self):
        """Configure tool window"""
        self.window.title("Financial Progress Tracker - Monitor project financial progress")
        self.window.geometry("1000x700")
        self.window.minsize(900, 600)
        
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
            text="📊 Financial Progress Tracker",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        title_label.pack(pady=15)
        
        # Main content
        main_frame = ctk.CTkFrame(self.window)
        main_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Project Setup Tab
        self.create_project_tab()
        
        # Progress Entry Tab
        self.create_progress_tab()
        
        # Analysis Tab
        self.create_analysis_tab()
    
    def create_project_tab(self):
        """Create project setup tab"""
        project_frame = ctk.CTkFrame(self.notebook)
        self.notebook.add(project_frame, text="Project Setup")
        
        # Project details form
        form_frame = ctk.CTkFrame(project_frame)
        form_frame.pack(fill="x", padx=10, pady=10)
        
        ctk.CTkLabel(form_frame, text="Project Information", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(10, 15))
        
        # Input fields
        fields_frame = ctk.CTkFrame(form_frame)
        fields_frame.pack(fill="x", padx=10, pady=5)
        
        # Project Name
        ctk.CTkLabel(fields_frame, text="Project Name:", font=ctk.CTkFont(weight="bold")).grid(
            row=0, column=0, padx=10, pady=5, sticky="w"
        )
        self.project_name_entry = ctk.CTkEntry(fields_frame, width=400, placeholder_text="Enter project name")
        self.project_name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        
        # Contract Value
        ctk.CTkLabel(fields_frame, text="Contract Value (₹):", font=ctk.CTkFont(weight="bold")).grid(
            row=1, column=0, padx=10, pady=5, sticky="w"
        )
        self.contract_value_entry = ctk.CTkEntry(fields_frame, width=400, placeholder_text="Enter total contract value")
        self.contract_value_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        # Start Date
        ctk.CTkLabel(fields_frame, text="Start Date:", font=ctk.CTkFont(weight="bold")).grid(
            row=2, column=0, padx=10, pady=5, sticky="w"
        )
        self.start_date_entry = ctk.CTkEntry(fields_frame, width=400, placeholder_text="YYYY-MM-DD")
        self.start_date_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        
        # Completion Date
        ctk.CTkLabel(fields_frame, text="Scheduled Completion:", font=ctk.CTkFont(weight="bold")).grid(
            row=3, column=0, padx=10, pady=5, sticky="w"
        )
        self.completion_date_entry = ctk.CTkEntry(fields_frame, width=400, placeholder_text="YYYY-MM-DD")
        self.completion_date_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")
        
        # Contractor Name
        ctk.CTkLabel(fields_frame, text="Contractor:", font=ctk.CTkFont(weight="bold")).grid(
            row=4, column=0, padx=10, pady=5, sticky="w"
        )
        self.contractor_name_entry = ctk.CTkEntry(fields_frame, width=400, placeholder_text="Enter contractor name")
        self.contractor_name_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")
        
        # Liquidity Damages Rate
        ctk.CTkLabel(fields_frame, text="Liquidity Damages (% per week):", font=ctk.CTkFont(weight="bold")).grid(
            row=5, column=0, padx=10, pady=5, sticky="w"
        )
        self.ld_rate_entry = ctk.CTkEntry(fields_frame, width=400, placeholder_text="Enter LD rate (e.g., 0.5 for 0.5%)")
        self.ld_rate_entry.grid(row=5, column=1, padx=10, pady=5, sticky="ew")
        
        # Save project button
        save_project_btn = ctk.CTkButton(
            fields_frame,
            text="💾 Save Project",
            command=self.save_project,
            width=200,
            height=35
        )
        save_project_btn.grid(row=6, column=0, columnspan=2, pady=15)
        
        # Configure grid weights
        fields_frame.grid_columnconfigure(1, weight=1)
    
    def create_progress_tab(self):
        """Create progress entry tab"""
        progress_frame = ctk.CTkFrame(self.notebook)
        self.notebook.add(progress_frame, text="Progress Entry")
        
        # Progress entry form
        entry_frame = ctk.CTkFrame(progress_frame)
        entry_frame.pack(fill="x", padx=10, pady=10)
        
        ctk.CTkLabel(entry_frame, text="Add Progress Record", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(10, 15))
        
        # Input fields
        fields_frame = ctk.CTkFrame(entry_frame)
        fields_frame.pack(fill="x", padx=10, pady=5)
        
        # Date
        ctk.CTkLabel(fields_frame, text="Date:", font=ctk.CTkFont(weight="bold")).grid(
            row=0, column=0, padx=10, pady=5, sticky="w"
        )
        self.progress_date_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="YYYY-MM-DD")
        self.progress_date_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        
        # Physical Progress %
        ctk.CTkLabel(fields_frame, text="Physical Progress (%):", font=ctk.CTkFont(weight="bold")).grid(
            row=1, column=0, padx=10, pady=5, sticky="w"
        )
        self.physical_progress_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Enter physical progress percentage")
        self.physical_progress_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        # Financial Progress (Amount)
        ctk.CTkLabel(fields_frame, text="Amount Paid (₹):", font=ctk.CTkFont(weight="bold")).grid(
            row=2, column=0, padx=10, pady=5, sticky="w"
        )
        self.amount_paid_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Enter cumulative amount paid")
        self.amount_paid_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        
        # Remarks
        ctk.CTkLabel(fields_frame, text="Remarks:", font=ctk.CTkFont(weight="bold")).grid(
            row=3, column=0, padx=10, pady=5, sticky="w"
        )
        self.remarks_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Optional remarks")
        self.remarks_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")
        
        # Add progress button
        add_progress_btn = ctk.CTkButton(
            fields_frame,
            text="➕ Add Progress Record",
            command=self.add_progress_record,
            width=200,
            height=35
        )
        add_progress_btn.grid(row=4, column=0, columnspan=2, pady=15)
        
        # Configure grid weights
        fields_frame.grid_columnconfigure(1, weight=1)
        
        # Progress records display
        records_frame = ctk.CTkFrame(progress_frame)
        records_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        ctk.CTkLabel(records_frame, text="Progress Records", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(10, 5))
        
        # Create treeview for progress records
        self.progress_tree = ttk.Treeview(records_frame, columns=('Date', 'Physical %', 'Amount Paid', 'Financial %', 'Remarks'), show='headings')
        
        # Define headings
        self.progress_tree.heading('Date', text='Date')
        self.progress_tree.heading('Physical %', text='Physical %')
        self.progress_tree.heading('Amount Paid', text='Amount Paid (₹)')
        self.progress_tree.heading('Financial %', text='Financial %')
        self.progress_tree.heading('Remarks', text='Remarks')
        
        # Configure column widths
        self.progress_tree.column('Date', width=100)
        self.progress_tree.column('Physical %', width=80)
        self.progress_tree.column('Amount Paid', width=120)
        self.progress_tree.column('Financial %', width=80)
        self.progress_tree.column('Remarks', width=200)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(records_frame, orient="vertical", command=self.progress_tree.yview)
        self.progress_tree.configure(yscrollcommand=scrollbar.set)
        
        # Pack treeview and scrollbar
        self.progress_tree.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        scrollbar.pack(side="right", fill="y", pady=10)
    
    def create_analysis_tab(self):
        """Create analysis and reporting tab"""
        analysis_frame = ctk.CTkFrame(self.notebook)
        self.notebook.add(analysis_frame, text="Analysis & Reports")
        
        # Analysis controls
        controls_frame = ctk.CTkFrame(analysis_frame)
        controls_frame.pack(fill="x", padx=10, pady=10)
        
        ctk.CTkLabel(controls_frame, text="Project Analysis", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(10, 15))
        
        # Analysis buttons
        btn_frame = ctk.CTkFrame(controls_frame)
        btn_frame.pack(pady=10)
        
        analyze_btn = ctk.CTkButton(
            btn_frame,
            text="🔍 Analyze Progress",
            command=self.analyze_progress,
            width=150,
            height=35
        )
        analyze_btn.pack(side="left", padx=5)
        
        generate_report_btn = ctk.CTkButton(
            btn_frame,
            text="📄 Generate Report",
            command=self.generate_report,
            width=150,
            height=35
        )
        generate_report_btn.pack(side="left", padx=5)
        
        # Analysis results display
        self.analysis_frame = ctk.CTkFrame(analysis_frame)
        self.analysis_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Initial message
        self.no_analysis_label = ctk.CTkLabel(
            self.analysis_frame,
            text="Set up project details and add progress records, then click 'Analyze Progress'",
            font=ctk.CTkFont(size=14),
            text_color="#666666"
        )
        self.no_analysis_label.pack(pady=40)
    
    def save_project(self):
        """Save project information"""
        try:
            # Validate inputs
            project_name = self.project_name_entry.get().strip()
            contract_value_str = self.contract_value_entry.get().strip()
            start_date_str = self.start_date_entry.get().strip()
            completion_date_str = self.completion_date_entry.get().strip()
            contractor_name = self.contractor_name_entry.get().strip()
            ld_rate_str = self.ld_rate_entry.get().strip()
            
            if not all([project_name, contract_value_str, start_date_str, completion_date_str, contractor_name, ld_rate_str]):
                messagebox.showerror("Validation Error", "Please fill in all project fields.")
                return
            
            try:
                contract_value = float(contract_value_str)
                ld_rate = float(ld_rate_str)
            except ValueError:
                messagebox.showerror("Validation Error", "Please enter valid numeric values for contract value and LD rate.")
                return
            
            try:
                start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
                completion_date = datetime.strptime(completion_date_str, "%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Validation Error", "Please enter dates in YYYY-MM-DD format.")
                return
            
            if completion_date <= start_date:
                messagebox.showerror("Validation Error", "Completion date must be after start date.")
                return
            
            # Save to database
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            success = self.db_manager.execute_query('''
                INSERT INTO financial_progress (
                    project_name, contract_value, start_date, completion_date,
                    contractor_name, ld_rate, date_created
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                project_name, contract_value, start_date_str, completion_date_str,
                contractor_name, ld_rate, current_time
            ))
            
            if success:
                messagebox.showinfo("Success", "Project information saved successfully!")
                
                # Store project data for current session
                self.current_project = {
                    'name': project_name,
                    'contract_value': contract_value,
                    'start_date': start_date,
                    'completion_date': completion_date,
                    'contractor': contractor_name,
                    'ld_rate': ld_rate
                }
            else:
                messagebox.showerror("Error", "Failed to save project information.")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save project: {str(e)}")
    
    def add_progress_record(self):
        """Add progress record"""
        try:
            if not hasattr(self, 'current_project'):
                messagebox.showerror("Error", "Please save project information first.")
                return
            
            # Validate inputs
            progress_date_str = self.progress_date_entry.get().strip()
            physical_progress_str = self.physical_progress_entry.get().strip()
            amount_paid_str = self.amount_paid_entry.get().strip()
            remarks = self.remarks_entry.get().strip()
            
            if not all([progress_date_str, physical_progress_str, amount_paid_str]):
                messagebox.showerror("Validation Error", "Please fill in date, physical progress, and amount paid.")
                return
            
            try:
                progress_date = datetime.strptime(progress_date_str, "%Y-%m-%d")
                physical_progress = float(physical_progress_str)
                amount_paid = float(amount_paid_str)
            except ValueError:
                messagebox.showerror("Validation Error", "Please enter valid values for date, physical progress, and amount paid.")
                return
            
            if not (0 <= physical_progress <= 100):
                messagebox.showerror("Validation Error", "Physical progress must be between 0 and 100%.")
                return
            
            # Calculate financial progress percentage
            financial_progress = (amount_paid / self.current_project['contract_value']) * 100
            
            # Add to records list
            record = {
                'date': progress_date,
                'physical_progress': physical_progress,
                'amount_paid': amount_paid,
                'financial_progress': financial_progress,
                'remarks': remarks
            }
            
            self.progress_records.append(record)
            
            # Update treeview
            self.progress_tree.insert('', 'end', values=(
                progress_date.strftime('%Y-%m-%d'),
                f"{physical_progress:.1f}%",
                f"₹ {amount_paid:,.0f}",
                f"{financial_progress:.1f}%",
                remarks
            ))
            
            # Clear form
            self.progress_date_entry.delete(0, "end")
            self.physical_progress_entry.delete(0, "end")
            self.amount_paid_entry.delete(0, "end")
            self.remarks_entry.delete(0, "end")
            
            messagebox.showinfo("Success", "Progress record added successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add progress record: {str(e)}")
    
    def analyze_progress(self):
        """Analyze project progress and calculate delays/penalties"""
        try:
            if not hasattr(self, 'current_project') or not self.progress_records:
                messagebox.showerror("Error", "Please set up project and add progress records first.")
                return
            
            # Clear previous analysis
            for widget in self.analysis_frame.winfo_children():
                widget.destroy()
            
            # Get latest progress
            latest_record = max(self.progress_records, key=lambda x: x['date'])
            current_date = datetime.now()
            
            # Calculate project timeline
            project_duration = (self.current_project['completion_date'] - self.current_project['start_date']).days
            elapsed_days = (current_date - self.current_project['start_date']).days
            scheduled_progress = min(100, (elapsed_days / project_duration) * 100)
            
            # Calculate delays and penalties
            physical_delay = scheduled_progress - latest_record['physical_progress']
            financial_delay = scheduled_progress - latest_record['financial_progress']
            
            # Calculate liquidity damages
            if physical_delay > 0:
                delay_weeks = max(0, (current_date - self.current_project['completion_date']).days / 7)
                if delay_weeks > 0:
                    ld_amount = (self.current_project['contract_value'] * self.current_project['ld_rate'] / 100) * delay_weeks
                else:
                    ld_amount = 0
            else:
                delay_weeks = 0
                ld_amount = 0
            
            # Display analysis results
            self.display_analysis_results({
                'project': self.current_project,
                'latest_record': latest_record,
                'current_date': current_date,
                'project_duration': project_duration,
                'elapsed_days': elapsed_days,
                'scheduled_progress': scheduled_progress,
                'physical_delay': physical_delay,
                'financial_delay': financial_delay,
                'delay_weeks': delay_weeks,
                'ld_amount': ld_amount
            })
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to analyze progress: {str(e)}")
    
    def display_analysis_results(self, data):
        """Display analysis results"""
        # Project status overview
        status_frame = ctk.CTkFrame(self.analysis_frame)
        status_frame.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(status_frame, text="Project Status Overview", font=ctk.CTkFont(weight="bold", size=16)).pack(pady=(10, 5))
        
        # Status details
        status_details = [
            ("Project Name", data['project']['name']),
            ("Contract Value", f"₹ {data['project']['contract_value']:,.0f}"),
            ("Project Duration", f"{data['project_duration']} days"),
            ("Days Elapsed", f"{data['elapsed_days']} days"),
            ("Scheduled Progress", f"{data['scheduled_progress']:.1f}%")
        ]
        
        for label, value in status_details:
            detail_frame = ctk.CTkFrame(status_frame)
            detail_frame.pack(fill="x", padx=10, pady=1)
            
            ctk.CTkLabel(detail_frame, text=f"{label}:", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=10, pady=3)
            ctk.CTkLabel(detail_frame, text=value).pack(side="right", padx=10, pady=3)
        
        # Current progress
        progress_frame = ctk.CTkFrame(self.analysis_frame)
        progress_frame.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(progress_frame, text="Current Progress Status", font=ctk.CTkFont(weight="bold", size=16)).pack(pady=(10, 5))
        
        # Progress bars
        physical_frame = ctk.CTkFrame(progress_frame)
        physical_frame.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(physical_frame, text="Physical Progress:", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=10, pady=5)
        physical_progress_bar = ctk.CTkProgressBar(physical_frame, width=300)
        physical_progress_bar.set(data['latest_record']['physical_progress'] / 100)
        physical_progress_bar.pack(side="left", padx=10, pady=5)
        ctk.CTkLabel(physical_frame, text=f"{data['latest_record']['physical_progress']:.1f}%").pack(side="left", padx=5, pady=5)
        
        financial_frame = ctk.CTkFrame(progress_frame)
        financial_frame.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(financial_frame, text="Financial Progress:", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=10, pady=5)
        financial_progress_bar = ctk.CTkProgressBar(financial_frame, width=300)
        financial_progress_bar.set(data['latest_record']['financial_progress'] / 100)
        financial_progress_bar.pack(side="left", padx=10, pady=5)
        ctk.CTkLabel(financial_frame, text=f"{data['latest_record']['financial_progress']:.1f}%").pack(side="left", padx=5, pady=5)
        
        # Delay analysis
        delay_frame = ctk.CTkFrame(self.analysis_frame)
        delay_frame.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(delay_frame, text="Delay Analysis", font=ctk.CTkFont(weight="bold", size=16)).pack(pady=(10, 5))
        
        # Physical delay
        phys_delay_frame = ctk.CTkFrame(delay_frame)
        phys_delay_frame.pack(fill="x", padx=10, pady=2)
        
        ctk.CTkLabel(phys_delay_frame, text="Physical Delay:", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=10, pady=3)
        delay_color = "#EF4444" if data['physical_delay'] > 0 else "#10B981"
        delay_text = f"{data['physical_delay']:.1f}%" if data['physical_delay'] > 0 else "On Schedule"
        ctk.CTkLabel(phys_delay_frame, text=delay_text, text_color=delay_color).pack(side="right", padx=10, pady=3)
        
        # Financial delay
        fin_delay_frame = ctk.CTkFrame(delay_frame)
        fin_delay_frame.pack(fill="x", padx=10, pady=2)
        
        ctk.CTkLabel(fin_delay_frame, text="Financial Delay:", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=10, pady=3)
        fin_delay_color = "#EF4444" if data['financial_delay'] > 0 else "#10B981"
        fin_delay_text = f"{data['financial_delay']:.1f}%" if data['financial_delay'] > 0 else "On Schedule"
        ctk.CTkLabel(fin_delay_frame, text=fin_delay_text, text_color=fin_delay_color).pack(side="right", padx=10, pady=3)
        
        # Liquidity damages
        if data['ld_amount'] > 0:
            ld_frame = ctk.CTkFrame(self.analysis_frame)
            ld_frame.pack(fill="x", padx=10, pady=5)
            
            ctk.CTkLabel(ld_frame, text="Liquidity Damages", font=ctk.CTkFont(weight="bold", size=16)).pack(pady=(10, 5))
            
            ld_details = [
                ("Delay Period", f"{data['delay_weeks']:.1f} weeks"),
                ("LD Rate", f"{data['project']['ld_rate']}% per week"),
                ("Total LD Amount", f"₹ {data['ld_amount']:,.0f}")
            ]
            
            for label, value in ld_details:
                ld_detail_frame = ctk.CTkFrame(ld_frame)
                ld_detail_frame.pack(fill="x", padx=10, pady=1)
                
                ctk.CTkLabel(ld_detail_frame, text=f"{label}:", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=10, pady=3)
                color = "#EF4444" if "LD Amount" in label else None
                ctk.CTkLabel(ld_detail_frame, text=value, text_color=color).pack(side="right", padx=10, pady=3)
    
    def generate_report(self):
        """Generate progress report"""
        try:
            if not hasattr(self, 'current_project') or not self.progress_records:
                messagebox.showerror("Error", "Please set up project and add progress records first.")
                return
            
            # Create report data
            report_data = {
                'project_name': self.current_project['name'],
                'contractor': self.current_project['contractor'],
                'contract_value': self.current_project['contract_value'],
                'start_date': self.current_project['start_date'].strftime('%d/%m/%Y'),
                'completion_date': self.current_project['completion_date'].strftime('%d/%m/%Y'),
                'progress_records': []
            }
            
            for record in sorted(self.progress_records, key=lambda x: x['date']):
                report_data['progress_records'].append({
                    'date': record['date'].strftime('%d/%m/%Y'),
                    'physical_progress': record['physical_progress'],
                    'amount_paid': record['amount_paid'],
                    'financial_progress': record['financial_progress'],
                    'remarks': record['remarks']
                })
            
            # Generate PDF using utility
            from utils.pdf_generator import PDFGenerator
            pdf_gen = PDFGenerator()
            
            filename = f"Financial_Progress_Report_{self.current_project['name'].replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.pdf"
            
            if pdf_gen.generate_financial_progress_report(report_data, filename):
                messagebox.showinfo("Success", f"Progress report generated: {filename}")
            else:
                messagebox.showerror("Error", "Failed to generate progress report.")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate report: {str(e)}")
    
    def focus(self):
        """Bring window to focus"""
        self.window.lift()
        self.window.focus_force()
