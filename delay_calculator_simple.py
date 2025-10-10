"""
Delay Calculator Tool - SIMPLE VERSION
For Lower Divisional Clerks - With Calendar
Very simple delay calculation
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

class SimpleDelayCalculatorTool:
    def __init__(self):
        """Initialize Simple Delay Calculator tool"""
        self.root = tk.Tk()
        self.root.title("Delay Calculator - सरल")
        
        # Make responsive for different screen sizes
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Adjust window size based on screen size
        if screen_width < 1024:  # Mobile/Tablet
            self.root.geometry(f"{min(screen_width-20, 400)}x{min(screen_height-50, 600)}")
        else:  # Desktop
            self.root.geometry("700x600")
        
        # Make window resizable
        self.root.minsize(400, 600)
        
        # Simple database
        self.init_database()
        
        # Create interface
        self.create_interface()
    
    def init_database(self):
        """Initialize simple database"""
        self.conn = sqlite3.connect('delay_calculator.db')
        self.cursor = self.conn.cursor()
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS delay_records (
                id INTEGER PRIMARY KEY,
                project_name TEXT,
                planned_start_date TEXT,
                actual_start_date TEXT,
                planned_completion_date TEXT,
                actual_completion_date TEXT,
                delay_days INTEGER,
                delay_reason TEXT,
                penalty_amount REAL,
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
            text="Delay Calculator - सरल",
            font=("Arial", 18, "bold"),
            fg="blue"
        )
        header.pack(pady=10)
        
        # Main frame
        main_frame = tk.LabelFrame(self.scrollable_frame, text="Project Delay Calculation", font=("Arial", 12, "bold"))
        main_frame.pack(fill="x", padx=10, pady=5)
        
        # Project Name
        tk.Label(main_frame, text="Project Name:", font=("Arial", 10, "bold")).pack(pady=3)
        self.project_name_entry = tk.Entry(main_frame, width=50, font=("Arial", 10))
        self.project_name_entry.pack(pady=3)
        
        # Date fields with calendar
        self.create_date_fields(main_frame)
        
        # Delay Reason
        tk.Label(main_frame, text="Delay Reason (Optional):", font=("Arial", 10, "bold")).pack(pady=3)
        self.delay_reason_entry = tk.Entry(main_frame, width=50, font=("Arial", 10))
        self.delay_reason_entry.pack(pady=3)
        
        # Calculate button
        calc_btn = tk.Button(main_frame, text="Calculate Delay", command=self.calculate_delay, 
                           width=20, height=2, font=("Arial", 10, "bold"), bg="lightblue")
        calc_btn.pack(pady=10)
        
        # Results section
        self.create_results_section(main_frame)
        
        # Action buttons
        self.create_action_buttons(main_frame)
    
    def create_date_fields(self, parent):
        """Create date fields with calendar"""
        # Initialize calendar widgets
        self.planned_start_calendar = SimpleCalendarWidget(self.root, self.set_planned_start_date)
        self.actual_start_calendar = SimpleCalendarWidget(self.root, self.set_actual_start_date)
        self.planned_completion_calendar = SimpleCalendarWidget(self.root, self.set_planned_completion_date)
        self.actual_completion_calendar = SimpleCalendarWidget(self.root, self.set_actual_completion_date)
        
        # Planned Start Date
        planned_start_frame = tk.Frame(parent)
        planned_start_frame.pack(fill="x", padx=5, pady=3)
        
        tk.Label(planned_start_frame, text="Planned Start Date (DD/MM/YYYY):", font=("Arial", 10, "bold")).pack(pady=3)
        planned_start_input_frame = tk.Frame(planned_start_frame)
        planned_start_input_frame.pack(pady=3)
        
        self.planned_start_entry = tk.Entry(planned_start_input_frame, width=25, font=("Arial", 10))
        self.planned_start_entry.pack(side="left", padx=5)
        
        planned_start_cal_btn = tk.Button(planned_start_input_frame, text="📅", command=self.show_planned_start_calendar, width=3)
        planned_start_cal_btn.pack(side="left", padx=5)
        
        # Actual Start Date
        actual_start_frame = tk.Frame(parent)
        actual_start_frame.pack(fill="x", padx=5, pady=3)
        
        tk.Label(actual_start_frame, text="Actual Start Date (DD/MM/YYYY):", font=("Arial", 10, "bold")).pack(pady=3)
        actual_start_input_frame = tk.Frame(actual_start_frame)
        actual_start_input_frame.pack(pady=3)
        
        self.actual_start_entry = tk.Entry(actual_start_input_frame, width=25, font=("Arial", 10))
        self.actual_start_entry.pack(side="left", padx=5)
        
        actual_start_cal_btn = tk.Button(actual_start_input_frame, text="📅", command=self.show_actual_start_calendar, width=3)
        actual_start_cal_btn.pack(side="left", padx=5)
        
        # Planned Completion Date
        planned_completion_frame = tk.Frame(parent)
        planned_completion_frame.pack(fill="x", padx=5, pady=3)
        
        tk.Label(planned_completion_frame, text="Planned Completion Date (DD/MM/YYYY):", font=("Arial", 10, "bold")).pack(pady=3)
        planned_completion_input_frame = tk.Frame(planned_completion_frame)
        planned_completion_input_frame.pack(pady=3)
        
        self.planned_completion_entry = tk.Entry(planned_completion_input_frame, width=25, font=("Arial", 10))
        self.planned_completion_entry.pack(side="left", padx=5)
        
        planned_completion_cal_btn = tk.Button(planned_completion_input_frame, text="📅", command=self.show_planned_completion_calendar, width=3)
        planned_completion_cal_btn.pack(side="left", padx=5)
        
        # Actual Completion Date
        actual_completion_frame = tk.Frame(parent)
        actual_completion_frame.pack(fill="x", padx=5, pady=3)
        
        tk.Label(actual_completion_frame, text="Actual Completion Date (DD/MM/YYYY):", font=("Arial", 10, "bold")).pack(pady=3)
        actual_completion_input_frame = tk.Frame(actual_completion_frame)
        actual_completion_input_frame.pack(pady=3)
        
        self.actual_completion_entry = tk.Entry(actual_completion_input_frame, width=25, font=("Arial", 10))
        self.actual_completion_entry.pack(side="left", padx=5)
        
        actual_completion_cal_btn = tk.Button(actual_completion_input_frame, text="📅", command=self.show_actual_completion_calendar, width=3)
        actual_completion_cal_btn.pack(side="left", padx=5)
    
    def show_planned_start_calendar(self):
        """Show planned start date calendar"""
        self.planned_start_calendar.show_calendar(self.planned_start_entry.get())
    
    def show_actual_start_calendar(self):
        """Show actual start date calendar"""
        self.actual_start_calendar.show_calendar(self.actual_start_entry.get())
    
    def show_planned_completion_calendar(self):
        """Show planned completion date calendar"""
        self.planned_completion_calendar.show_calendar(self.planned_completion_entry.get())
    
    def show_actual_completion_calendar(self):
        """Show actual completion date calendar"""
        self.actual_completion_calendar.show_calendar(self.actual_completion_entry.get())
    
    def set_planned_start_date(self, date):
        """Set planned start date from calendar"""
        self.planned_start_entry.delete(0, "end")
        self.planned_start_entry.insert(0, date)
    
    def set_actual_start_date(self, date):
        """Set actual start date from calendar"""
        self.actual_start_entry.delete(0, "end")
        self.actual_start_entry.insert(0, date)
    
    def set_planned_completion_date(self, date):
        """Set planned completion date from calendar"""
        self.planned_completion_entry.delete(0, "end")
        self.planned_completion_entry.insert(0, date)
    
    def set_actual_completion_date(self, date):
        """Set actual completion date from calendar"""
        self.actual_completion_entry.delete(0, "end")
        self.actual_completion_entry.insert(0, date)
    
    def create_results_section(self, parent):
        """Create results section"""
        results_frame = tk.LabelFrame(parent, text="Delay Calculation Results", font=("Arial", 12, "bold"))
        results_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Results display - shrunk vertically by 15%
        text_frame = tk.Frame(results_frame)
        text_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.results_text = tk.Text(text_frame, height=8, font=("Arial", 10), wrap="word")  # Reduced height
        scrollbar = tk.Scrollbar(text_frame, orient="vertical", command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=scrollbar.set)
        
        self.results_text.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        self.results_text.insert("1.0", "Enter project details and click 'Calculate Delay'")
    
    def create_action_buttons(self, parent):
        """Create action buttons"""
        button_frame = tk.Frame(parent)
        button_frame.pack(fill="x", padx=5, pady=5)
        
        save_btn = tk.Button(button_frame, text="Save Calculation", command=self.save_calculation, 
                           width=18, height=1, font=("Arial", 9), bg="lightgreen")
        save_btn.pack(side="left", padx=5)
        
        clear_btn = tk.Button(button_frame, text="Clear Form", command=self.clear_form, 
                            width=15, height=1, font=("Arial", 9), bg="lightgray")
        clear_btn.pack(side="left", padx=5)
        
        print_btn = tk.Button(button_frame, text="Print Results", command=self.print_results, 
                            width=15, height=1, font=("Arial", 9), bg="lightcoral")
        print_btn.pack(side="left", padx=5)
    
    def calculate_delay(self):
        """Calculate project delay"""
        try:
            project_name = self.project_name_entry.get().strip()
            planned_start = self.planned_start_entry.get().strip()
            actual_start = self.actual_start_entry.get().strip()
            planned_completion = self.planned_completion_entry.get().strip()
            actual_completion = self.actual_completion_entry.get().strip()
            delay_reason = self.delay_reason_entry.get().strip()
            
            if not project_name:
                messagebox.showerror("Error", "Please enter project name")
                return
            
            if not all([planned_start, actual_start, planned_completion, actual_completion]):
                messagebox.showerror("Error", "Please fill all date fields")
                return
            
            # Parse dates
            try:
                planned_start_dt = datetime.strptime(planned_start, "%d/%m/%Y")
                actual_start_dt = datetime.strptime(actual_start, "%d/%m/%Y")
                planned_completion_dt = datetime.strptime(planned_completion, "%d/%m/%Y")
                actual_completion_dt = datetime.strptime(actual_completion, "%d/%m/%Y")
            except ValueError:
                messagebox.showerror("Error", "Please enter dates in DD/MM/YYYY format")
                return
            
            # Calculate delays
            start_delay = (actual_start_dt - planned_start_dt).days
            completion_delay = (actual_completion_dt - planned_completion_dt).days
            total_delay = completion_delay
            
            # Calculate project duration
            planned_duration = (planned_completion_dt - planned_start_dt).days
            actual_duration = (actual_completion_dt - actual_start_dt).days
            
            # Generate analysis
            analysis = f"""
DELAY CALCULATION REPORT
========================

Project Name: {project_name}
Analysis Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}

SCHEDULE ANALYSIS
=================
Planned Start: {planned_start}
Actual Start: {actual_start}
Start Delay: {start_delay} days

Planned Completion: {planned_completion}
Actual Completion: {actual_completion}
Completion Delay: {completion_delay} days

PROJECT DURATION
================
Planned Duration: {planned_duration} days
Actual Duration: {actual_duration} days
Duration Difference: {actual_duration - planned_duration} days

DELAY SUMMARY
=============
Total Delay: {total_delay} days
Delay Status: {'DELAYED' if total_delay > 0 else 'ON TIME' if total_delay == 0 else 'EARLY'}

DELAY ANALYSIS
==============
"""
            
            if total_delay > 0:
                analysis += f"⚠️  PROJECT DELAYED by {total_delay} days\n"
                if total_delay > 30:
                    analysis += "🔴  MAJOR DELAY - Requires immediate attention\n"
                elif total_delay > 15:
                    analysis += "🟡  MODERATE DELAY - Monitor closely\n"
                else:
                    analysis += "🟢  MINOR DELAY - Within acceptable limits\n"
            elif total_delay == 0:
                analysis += "✅  PROJECT COMPLETED ON TIME\n"
            else:
                analysis += f"🎉  PROJECT COMPLETED EARLY by {abs(total_delay)} days\n"
            
            if delay_reason:
                analysis += f"\nDelay Reason: {delay_reason}\n"
            
            # Penalty calculation (simple)
            if total_delay > 0:
                penalty_rate = 0.1  # 0.1% per day
                analysis += f"\nPENALTY CALCULATION\n"
                analysis += f"===================\n"
                analysis += f"Delay Days: {total_delay}\n"
                analysis += f"Penalty Rate: {penalty_rate}% per day\n"
                analysis += f"Note: Actual penalty calculation depends on contract terms\n"
            
            analysis += f"\nRECOMMENDATIONS\n"
            analysis += f"===============\n"
            if total_delay > 0:
                analysis += f"• Review project timeline and resource allocation\n"
                analysis += f"• Implement corrective measures for future projects\n"
                analysis += f"• Document delay reasons for future reference\n"
            else:
                analysis += f"• Maintain current project management practices\n"
                analysis += f"• Use this project as a benchmark for future planning\n"
            
            # Display results
            self.results_text.delete("1.0", "end")
            self.results_text.insert("1.0", analysis)
            
            # Store calculation
            self.current_calculation = {
                'project_name': project_name,
                'planned_start_date': planned_start,
                'actual_start_date': actual_start,
                'planned_completion_date': planned_completion,
                'actual_completion_date': actual_completion,
                'delay_days': total_delay,
                'delay_reason': delay_reason
            }
            
        except Exception as e:
            messagebox.showerror("Error", f"Calculation error: {str(e)}")
    
    def save_calculation(self):
        """Save calculation record"""
        if not hasattr(self, 'current_calculation'):
            messagebox.showwarning("Warning", "Please calculate delay first")
            return
        
        try:
            calc = self.current_calculation
            self.cursor.execute('''
                INSERT INTO delay_records (
                    project_name, planned_start_date, actual_start_date, 
                    planned_completion_date, actual_completion_date, 
                    delay_days, delay_reason, penalty_amount, date_created
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                calc['project_name'],
                calc['planned_start_date'],
                calc['actual_start_date'],
                calc['planned_completion_date'],
                calc['actual_completion_date'],
                calc['delay_days'],
                calc['delay_reason'],
                0.0,  # Simple penalty calculation
                datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            ))
            
            self.conn.commit()
            messagebox.showinfo("Success", "Calculation saved successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Save error: {str(e)}")
    
    def clear_form(self):
        """Clear form"""
        self.project_name_entry.delete(0, "end")
        self.planned_start_entry.delete(0, "end")
        self.actual_start_entry.delete(0, "end")
        self.planned_completion_entry.delete(0, "end")
        self.actual_completion_entry.delete(0, "end")
        self.delay_reason_entry.delete(0, "end")
        
        self.results_text.delete("1.0", "end")
        self.results_text.insert("1.0", "Enter project details and click 'Calculate Delay'")
        
        if hasattr(self, 'current_calculation'):
            delattr(self, 'current_calculation')
    
    def print_results(self):
        """Print results"""
        try:
            results = self.results_text.get("1.0", "end-1c")
            if results and results != "Enter project details and click 'Calculate Delay'":
                print("=" * 50)
                print("DELAY CALCULATION REPORT")
                print("=" * 50)
                print(results)
                print("=" * 50)
                messagebox.showinfo("Success", "Results printed to console!")
            else:
                messagebox.showwarning("Warning", "Please calculate delay first")
        except Exception as e:
            messagebox.showerror("Error", f"Print error: {str(e)}")
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = SimpleDelayCalculatorTool()
    app.run()
