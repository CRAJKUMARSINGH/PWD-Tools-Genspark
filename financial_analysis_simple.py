"""
Financial Analysis Tool - SIMPLE VERSION
For Lower Divisional Clerks - With Calendar
Very simple financial analysis
"""

import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import os
import sqlite3

class SimpleCalendarWidget:
    """Professional one-liner calendar widget"""
    def __init__(self, parent, callback=None):
        self.parent = parent
        self.callback = callback
        self.window = None
        
    def show_calendar(self, current_date=""):
        """Show professional one-liner calendar popup"""
        if self.window:
            self.window.destroy()
            
        self.window = tk.Toplevel(self.parent)
        self.window.title("Date Picker")
        self.window.geometry("400x120")
        self.window.transient(self.parent)
        self.window.grab_set()
        
        # Center the window
        self.window.update_idletasks()
        x = (self.window.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.window.winfo_screenheight() // 2) - (120 // 2)
        self.window.geometry(f"400x120+{x}+{y}")
        
        # Create calendar frame
        cal_frame = tk.Frame(self.window, bg="white")
        cal_frame.pack(fill="both", expand=True, padx=15, pady=15)
        
        # One-liner date selection
        date_frame = tk.Frame(cal_frame, bg="white")
        date_frame.pack(fill="x", pady=10)
        
        # Day selection
        tk.Label(date_frame, text="Day:", font=("Arial", 10, "bold"), bg="white").pack(side="left", padx=5)
        self.day_var = tk.StringVar(value="1")
        day_combo = ttk.Combobox(date_frame, values=[str(i).zfill(2) for i in range(1, 32)], 
                               textvariable=self.day_var, width=5, state="readonly")
        day_combo.pack(side="left", padx=5)
        
        # Month selection
        tk.Label(date_frame, text="Month:", font=("Arial", 10, "bold"), bg="white").pack(side="left", padx=5)
        self.month_var = tk.StringVar(value="1")
        month_combo = ttk.Combobox(date_frame, values=[str(i).zfill(2) for i in range(1, 13)], 
                                 textvariable=self.month_var, width=5, state="readonly")
        month_combo.pack(side="left", padx=5)
        
        # Year selection
        tk.Label(date_frame, text="Year:", font=("Arial", 10, "bold"), bg="white").pack(side="left", padx=5)
        current_year = datetime.now().year
        self.year_var = tk.StringVar(value=str(current_year))
        year_combo = ttk.Combobox(date_frame, 
                                values=[str(i) for i in range(current_year-10, current_year+5)], 
                                textvariable=self.year_var, width=8, state="readonly")
        year_combo.pack(side="left", padx=5)
        
        # Buttons in one line
        btn_frame = tk.Frame(cal_frame, bg="white")
        btn_frame.pack(fill="x", pady=5)
        
        select_btn = tk.Button(btn_frame, text="Select", command=self.select_date, 
                             width=12, height=1, font=("Arial", 9, "bold"), 
                             bg="#4CAF50", fg="white", relief="flat")
        select_btn.pack(side="left", padx=5)
        
        cancel_btn = tk.Button(btn_frame, text="Cancel", command=self.window.destroy, 
                             width=12, height=1, font=("Arial", 9, "bold"), 
                             bg="#f44336", fg="white", relief="flat")
        cancel_btn.pack(side="left", padx=5)
        
        # Set current date if provided
        if current_date:
            try:
                if "/" in current_date:
                    day, month, year = current_date.split("/")
                    self.day_var.set(day.zfill(2))
                    self.month_var.set(month.zfill(2))
                    self.year_var.set(year)
            except:
                pass
    
    def select_date(self):
        """Select the date and call callback"""
        try:
            day = self.day_var.get().zfill(2)
            month = self.month_var.get().zfill(2)
            year = self.year_var.get()
            selected_date = f"{day}/{month}/{year}"
            
            if self.callback:
                self.callback(selected_date)
            
            self.window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Invalid date: {e}")

class SimpleFinancialAnalysisTool:
    def __init__(self):
        """Initialize Simple Financial Analysis tool"""
        self.root = tk.Tk()
        self.root.title("Financial Analysis - सरल")
        
        # Make responsive for different screen sizes
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Adjust window size based on screen size
        if screen_width < 1024:  # Mobile/Tablet
            self.root.geometry(f"{min(screen_width-20, 400)}x{min(screen_height-50, 600)}")
        else:  # Desktop
            self.root.geometry("800x700")
        
        # Make window resizable
        self.root.minsize(400, 600)
        
        # Simple database
        self.init_database()
        
        # Create interface
        self.create_interface()
    
    def init_database(self):
        """Initialize simple database"""
        self.conn = sqlite3.connect('financial_analysis.db')
        self.cursor = self.conn.cursor()
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS financial_records (
                id INTEGER PRIMARY KEY,
                project_name TEXT,
                start_date TEXT,
                end_date TEXT,
                budget_amount REAL,
                spent_amount REAL,
                remaining_amount REAL,
                completion_percentage REAL,
                analysis_date TEXT
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
            text="Financial Analysis - सरल",
            font=("Arial", 18, "bold"),
            fg="blue"
        )
        header.pack(pady=10)
        
        # Main frame
        main_frame = tk.LabelFrame(self.scrollable_frame, text="Project Financial Analysis", font=("Arial", 12, "bold"))
        main_frame.pack(fill="x", padx=10, pady=5)
        
        # Project Name
        tk.Label(main_frame, text="Project Name:", font=("Arial", 10, "bold")).pack(pady=3)
        self.project_name_entry = tk.Entry(main_frame, width=40, font=("Arial", 10))
        self.project_name_entry.pack(pady=3)
        
        # Budget Amount
        tk.Label(main_frame, text="Budget Amount (₹):", font=("Arial", 10, "bold")).pack(pady=3)
        self.budget_entry = tk.Entry(main_frame, width=40, font=("Arial", 10))
        self.budget_entry.pack(pady=3)
        
        # Spent Amount
        tk.Label(main_frame, text="Spent Amount (₹):", font=("Arial", 10, "bold")).pack(pady=3)
        self.spent_entry = tk.Entry(main_frame, width=40, font=("Arial", 10))
        self.spent_entry.pack(pady=3)
        
        # Date fields with calendar
        self.create_date_fields(main_frame)
        
        # Calculate button
        calc_btn = tk.Button(main_frame, text="Analyze Financial Status", command=self.analyze_financials, 
                           width=25, height=2, font=("Arial", 10, "bold"), bg="lightblue")
        calc_btn.pack(pady=10)
        
        # Results section
        self.create_results_section(main_frame)
        
        # Action buttons
        self.create_action_buttons(main_frame)
    
    def create_date_fields(self, parent):
        """Create date fields with calendar"""
        # Initialize calendar widgets
        self.start_calendar = SimpleCalendarWidget(self.root, self.set_start_date)
        self.end_calendar = SimpleCalendarWidget(self.root, self.set_end_date)
        
        # Start Date with Calendar
        start_date_frame = tk.Frame(parent)
        start_date_frame.pack(fill="x", padx=5, pady=3)
        
        tk.Label(start_date_frame, text="Project Start Date (DD/MM/YYYY):", font=("Arial", 10, "bold")).pack(pady=3)
        start_input_frame = tk.Frame(start_date_frame)
        start_input_frame.pack(pady=3)
        
        self.start_date_entry = tk.Entry(start_input_frame, width=25, font=("Arial", 10))
        self.start_date_entry.pack(side="left", padx=5)
        
        start_cal_btn = tk.Button(start_input_frame, text="📅", command=self.show_start_calendar, width=3)
        start_cal_btn.pack(side="left", padx=5)
        
        # End Date with Calendar
        end_date_frame = tk.Frame(parent)
        end_date_frame.pack(fill="x", padx=5, pady=3)
        
        tk.Label(end_date_frame, text="Project End Date (DD/MM/YYYY):", font=("Arial", 10, "bold")).pack(pady=3)
        end_input_frame = tk.Frame(end_date_frame)
        end_input_frame.pack(pady=3)
        
        self.end_date_entry = tk.Entry(end_input_frame, width=25, font=("Arial", 10))
        self.end_date_entry.pack(side="left", padx=5)
        
        end_cal_btn = tk.Button(end_input_frame, text="📅", command=self.show_end_calendar, width=3)
        end_cal_btn.pack(side="left", padx=5)
    
    def show_start_calendar(self):
        """Show start date calendar"""
        self.start_calendar.show_calendar(self.start_date_entry.get())
    
    def show_end_calendar(self):
        """Show end date calendar"""
        self.end_calendar.show_calendar(self.end_date_entry.get())
    
    def set_start_date(self, date):
        """Set start date from calendar"""
        self.start_date_entry.delete(0, "end")
        self.start_date_entry.insert(0, date)
    
    def set_end_date(self, date):
        """Set end date from calendar"""
        self.end_date_entry.delete(0, "end")
        self.end_date_entry.insert(0, date)
    
    def create_results_section(self, parent):
        """Create results section"""
        results_frame = tk.LabelFrame(parent, text="Financial Analysis Results", font=("Arial", 12, "bold"))
        results_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Results display - shrunk vertically by 15%
        text_frame = tk.Frame(results_frame)
        text_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.results_text = tk.Text(text_frame, height=8, font=("Arial", 10), wrap="word")  # Reduced height
        scrollbar = tk.Scrollbar(text_frame, orient="vertical", command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=scrollbar.set)
        
        self.results_text.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        self.results_text.insert("1.0", "Enter project details and click 'Analyze Financial Status'")
    
    def create_action_buttons(self, parent):
        """Create action buttons"""
        button_frame = tk.Frame(parent)
        button_frame.pack(fill="x", padx=5, pady=5)
        
        save_btn = tk.Button(button_frame, text="Save Analysis", command=self.save_analysis, 
                           width=15, height=1, font=("Arial", 9), bg="lightgreen")
        save_btn.pack(side="left", padx=5)
        
        clear_btn = tk.Button(button_frame, text="Clear Form", command=self.clear_form, 
                            width=15, height=1, font=("Arial", 9), bg="lightgray")
        clear_btn.pack(side="left", padx=5)
        
        print_btn = tk.Button(button_frame, text="Print Analysis", command=self.print_analysis, 
                            width=15, height=1, font=("Arial", 9), bg="lightcoral")
        print_btn.pack(side="left", padx=5)
    
    def analyze_financials(self):
        """Analyze financial status"""
        try:
            project_name = self.project_name_entry.get().strip()
            budget_amount = float(self.budget_entry.get())
            spent_amount = float(self.spent_entry.get())
            start_date = self.start_date_entry.get()
            end_date = self.end_date_entry.get()
            
            if not project_name:
                messagebox.showerror("Error", "Please enter project name")
                return
            
            if budget_amount <= 0 or spent_amount < 0:
                messagebox.showerror("Error", "Please enter valid amounts")
                return
            
            # Calculate financial metrics
            remaining_amount = budget_amount - spent_amount
            completion_percentage = (spent_amount / budget_amount) * 100
            budget_utilization = completion_percentage
            
            # Calculate project duration
            duration_days = 0
            if start_date and end_date:
                try:
                    start_dt = datetime.strptime(start_date, "%d/%m/%Y")
                    end_dt = datetime.strptime(end_date, "%d/%m/%Y")
                    duration_days = (end_dt - start_dt).days
                except ValueError:
                    duration_days = 0
            
            # Generate analysis
            analysis = f"""
FINANCIAL ANALYSIS REPORT
========================

Project Name: {project_name}
Analysis Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}

BUDGET ANALYSIS
===============
Budget Amount: ₹ {budget_amount:,.2f}
Spent Amount: ₹ {spent_amount:,.2f}
Remaining Amount: ₹ {remaining_amount:,.2f}

PERFORMANCE METRICS
===================
Budget Utilization: {budget_utilization:.2f}%
Completion Status: {'Over Budget' if spent_amount > budget_amount else 'Within Budget'}

PROJECT TIMELINE
================
Start Date: {start_date if start_date else 'Not specified'}
End Date: {end_date if end_date else 'Not specified'}
Duration: {duration_days} days

FINANCIAL STATUS
================
"""
            
            if spent_amount > budget_amount:
                analysis += f"⚠️  OVER BUDGET by ₹ {abs(remaining_amount):,.2f}\n"
                analysis += "Recommendation: Review expenses and seek additional funding\n"
            elif budget_utilization > 90:
                analysis += f"⚠️  HIGH BUDGET UTILIZATION ({budget_utilization:.2f}%)\n"
                analysis += "Recommendation: Monitor expenses closely\n"
            elif budget_utilization > 75:
                analysis += f"✅  MODERATE BUDGET UTILIZATION ({budget_utilization:.2f}%)\n"
                analysis += "Recommendation: Continue current spending pattern\n"
            else:
                analysis += f"✅  LOW BUDGET UTILIZATION ({budget_utilization:.2f}%)\n"
                analysis += "Recommendation: Consider accelerating project activities\n"
            
            if remaining_amount > 0:
                analysis += f"\nRemaining Budget: ₹ {remaining_amount:,.2f} available for completion\n"
            else:
                analysis += f"\nBudget Exceeded: ₹ {abs(remaining_amount):,.2f} over budget\n"
            
            # Display results
            self.results_text.delete("1.0", "end")
            self.results_text.insert("1.0", analysis)
            
            # Store analysis
            self.current_analysis = {
                'project_name': project_name,
                'start_date': start_date,
                'end_date': end_date,
                'budget_amount': budget_amount,
                'spent_amount': spent_amount,
                'remaining_amount': remaining_amount,
                'completion_percentage': budget_utilization
            }
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for amounts")
        except Exception as e:
            messagebox.showerror("Error", f"Analysis error: {str(e)}")
    
    def save_analysis(self):
        """Save analysis record"""
        if not hasattr(self, 'current_analysis'):
            messagebox.showwarning("Warning", "Please analyze financials first")
            return
        
        try:
            analysis = self.current_analysis
            self.cursor.execute('''
                INSERT INTO financial_records (
                    project_name, start_date, end_date, budget_amount, 
                    spent_amount, remaining_amount, completion_percentage, analysis_date
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                analysis['project_name'],
                analysis['start_date'],
                analysis['end_date'],
                analysis['budget_amount'],
                analysis['spent_amount'],
                analysis['remaining_amount'],
                analysis['completion_percentage'],
                datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            ))
            
            self.conn.commit()
            messagebox.showinfo("Success", "Analysis saved successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Save error: {str(e)}")
    
    def clear_form(self):
        """Clear form"""
        self.project_name_entry.delete(0, "end")
        self.budget_entry.delete(0, "end")
        self.spent_entry.delete(0, "end")
        self.start_date_entry.delete(0, "end")
        self.end_date_entry.delete(0, "end")
        
        self.results_text.delete("1.0", "end")
        self.results_text.insert("1.0", "Enter project details and click 'Analyze Financial Status'")
        
        if hasattr(self, 'current_analysis'):
            delattr(self, 'current_analysis')
    
    def print_analysis(self):
        """Print analysis"""
        try:
            analysis = self.results_text.get("1.0", "end-1c")
            if analysis and analysis != "Enter project details and click 'Analyze Financial Status'":
                print("=" * 50)
                print("FINANCIAL ANALYSIS REPORT")
                print("=" * 50)
                print(analysis)
                print("=" * 50)
                messagebox.showinfo("Success", "Analysis printed to console!")
            else:
                messagebox.showwarning("Warning", "Please analyze financials first")
        except Exception as e:
            messagebox.showerror("Error", f"Print error: {str(e)}")
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = SimpleFinancialAnalysisTool()
    app.run()
