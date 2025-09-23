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
            
            if self.window:
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
                start_date TEXT,
                completion_date TEXT,
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
        # Configure root window background
        self.root.configure(bg="#f0f8ff")
        
        # Create scrollable frame for mobile compatibility
        self.main_canvas = tk.Canvas(self.root, bg="#f0f8ff")
        self.main_scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.main_canvas.yview)
        self.scrollable_frame = tk.Frame(self.main_canvas, bg="#f0f8ff")
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all"))
        )
        
        self.main_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.main_canvas.configure(yscrollcommand=self.main_scrollbar.set)
        
        self.main_canvas.pack(side="left", fill="both", expand=True)
        self.main_scrollbar.pack(side="right", fill="y")
        
        # Header with gradient effect
        header_frame = tk.Frame(self.scrollable_frame, bg="#ff6b6b", height=80)
        header_frame.pack(fill="x", padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        header = tk.Label(
            header_frame,
            text="⏰ Delay Calculator - सरल",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#ff6b6b"
        )
        header.pack(pady=20)
        
        # Main frame with colored background
        main_frame = tk.Frame(self.scrollable_frame, bg="#f0f8ff")
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Form container with border and shadow effect
        form_container = tk.Frame(main_frame, bg="#ffffff", relief="raised", bd=2)
        form_container.pack(pady=10, padx=10, fill="both", expand=True)
        
        # Title
        title_label = tk.Label(
            form_container,
            text="Project Delay Calculation",
            font=("Arial", 16, "bold"),
            fg="#ff6b6b",
            bg="#ffffff"
        )
        title_label.pack(pady=20)
        
        # Date fields with calendar
        self.create_date_fields(form_container)
        
        # Delay Reason
        tk.Label(form_container, text="Delay Reason (Optional):", font=("Arial", 12, "bold"), bg="#ffffff", fg="#4ecdc4").pack(pady=3)
        self.delay_reason_entry = tk.Entry(form_container, width=50, font=("Arial", 12))
        self.delay_reason_entry.pack(pady=3)
        
        # Calculate button with improved styling
        calc_btn = tk.Button(form_container, text="Calculate Delay", command=self.calculate_delay, 
                           width=20, height=2, font=("Arial", 12, "bold"), 
                           bg="#4ecdc4", fg="white", relief="raised", bd=2)
        calc_btn.pack(pady=15)
        
        # Results section
        self.create_results_section(main_frame)
        
        # Action buttons
        self.create_action_buttons(main_frame)
        
        # Footer
        footer_frame = tk.Frame(main_frame, bg="#2E8B57", height=40)
        footer_frame.pack(fill="x", pady=(10, 0))
        footer_frame.pack_propagate(False)
        
        footer_label = tk.Label(
            footer_frame,
            text="Delay Calculator - PWD Tools | Designed for Lower Divisional Clerks",
            font=("Arial", 9),
            fg="white",
            bg="#2E8B57"
        )
        footer_label.pack(pady=10)
    
    def create_date_fields(self, parent):
        """Create date fields with calendar"""
        # Initialize calendar widgets
        self.start_calendar = SimpleCalendarWidget(self.root, self.set_start_date)
        self.completion_calendar = SimpleCalendarWidget(self.root, self.set_completion_date)
        self.actual_completion_calendar = SimpleCalendarWidget(self.root, self.set_actual_completion_date)
        
        # Start Date
        start_frame = tk.Frame(parent)
        start_frame.pack(fill="x", padx=5, pady=3)
        
        tk.Label(start_frame, text="Start Date (DD/MM/YYYY):", font=("Arial", 10, "bold")).pack(pady=3)
        start_input_frame = tk.Frame(start_frame)
        start_input_frame.pack(pady=3)
        
        self.start_entry = tk.Entry(start_input_frame, width=25, font=("Arial", 10))
        self.start_entry.pack(side="left", padx=5)
        
        start_cal_btn = tk.Button(start_input_frame, text="📅", command=self.show_start_calendar, width=3)
        start_cal_btn.pack(side="left", padx=5)
        
        # Completion Date
        completion_frame = tk.Frame(parent)
        completion_frame.pack(fill="x", padx=5, pady=3)
        
        tk.Label(completion_frame, text="Completion Date (DD/MM/YYYY):", font=("Arial", 10, "bold")).pack(pady=3)
        completion_input_frame = tk.Frame(completion_frame)
        completion_input_frame.pack(pady=3)
        
        self.completion_entry = tk.Entry(completion_input_frame, width=25, font=("Arial", 10))
        self.completion_entry.pack(side="left", padx=5)
        
        completion_cal_btn = tk.Button(completion_input_frame, text="📅", command=self.show_completion_calendar, width=3)
        completion_cal_btn.pack(side="left", padx=5)
        
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
    
    def show_start_calendar(self):
        """Show start date calendar"""
        self.start_calendar.show_calendar(self.start_entry.get())
    
    def show_completion_calendar(self):
        """Show completion date calendar"""
        self.completion_calendar.show_calendar(self.completion_entry.get())
    
    def show_actual_completion_calendar(self):
        """Show actual completion date calendar"""
        self.actual_completion_calendar.show_calendar(self.actual_completion_entry.get())
    
    def set_start_date(self, date):
        """Set start date from calendar"""
        self.start_entry.delete(0, "end")
        self.start_entry.insert(0, date)
    
    def set_completion_date(self, date):
        """Set completion date from calendar"""
        self.completion_entry.delete(0, "end")
        self.completion_entry.insert(0, date)
    
    def set_actual_completion_date(self, date):
        """Set actual completion date from calendar"""
        self.actual_completion_entry.delete(0, "end")
        self.actual_completion_entry.insert(0, date)
    
    def create_results_section(self, parent):
        """Create results section"""
        results_frame = tk.LabelFrame(parent, text="Delay Calculation Results", font=("Arial", 12, "bold"), fg="#ff6b6b")
        results_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Results display
        text_frame = tk.Frame(results_frame)
        text_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.results_text = tk.Text(text_frame, height=12, font=("Arial", 10), wrap="word")
        scrollbar = tk.Scrollbar(text_frame, orient="vertical", command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=scrollbar.set)
        
        self.results_text.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        self.results_text.insert("1.0", "Enter dates and click 'Calculate Delay'")
    
    def create_action_buttons(self, parent):
        """Create action buttons"""
        button_frame = tk.Frame(parent, bg="#f0f8ff")
        button_frame.pack(fill="x", padx=5, pady=10)
        
        save_btn = tk.Button(button_frame, text="💾 Save Calculation", command=self.save_calculation, 
                           width=18, height=2, font=("Arial", 9, "bold"), 
                           bg="#96CEB4", fg="white", relief="raised", bd=2)
        save_btn.pack(side="left", padx=5)
        
        clear_btn = tk.Button(button_frame, text="🔄 Clear Form", command=self.clear_form, 
                            width=15, height=2, font=("Arial", 9, "bold"), 
                            bg="#FFEAA7", fg="black", relief="raised", bd=2)
        clear_btn.pack(side="left", padx=5)
        
        print_btn = tk.Button(button_frame, text="🖨️ Print Results", command=self.print_results, 
                            width=15, height=2, font=("Arial", 9, "bold"), 
                            bg="#DDA0DD", fg="white", relief="raised", bd=2)
        print_btn.pack(side="left", padx=5)
    
    def calculate_delay(self):
        """Calculate delay based on three dates"""
        try:
            start_date_str = self.start_entry.get().strip()
            completion_date_str = self.completion_entry.get().strip()
            actual_completion_date_str = self.actual_completion_entry.get().strip()
            delay_reason = self.delay_reason_entry.get().strip()
            
            if not all([start_date_str, completion_date_str, actual_completion_date_str]):
                messagebox.showerror("Error", "Please fill all required fields: Start Date, Completion Date, and Actual Completion Date")
                return
            
            # Parse dates
            try:
                start_date = datetime.strptime(start_date_str, "%d/%m/%Y")
                completion_date = datetime.strptime(completion_date_str, "%d/%m/%Y")
                actual_completion_date = datetime.strptime(actual_completion_date_str, "%d/%m/%Y")
            except ValueError:
                messagebox.showerror("Error", "Please enter dates in DD/MM/YYYY format")
                return
            
            # Calculate delay
            planned_duration = (completion_date - start_date).days
            actual_duration = (actual_completion_date - start_date).days
            delay_days = max(0, actual_duration - planned_duration)
            
            # Calculate penalty (assuming 0.5% per day delay)
            penalty_rate = 0.005  # 0.5%
            penalty_amount = 0
            if delay_days > 0:
                # Using a default value for penalty calculation
                default_value = 100000  # Default value for calculation
                penalty_amount = default_value * penalty_rate * delay_days
            
            # Display results
            result_text = f"""
Delay Calculation Report
========================

Start Date: {start_date_str}
Completion Date: {completion_date_str}
Actual Completion Date: {actual_completion_date_str}

Planned Duration: {planned_duration} days
Actual Duration: {actual_duration} days
Delay: {delay_days} days

Penalty Amount: ₹ {penalty_amount:,.2f}
Delay Reason: {delay_reason if delay_reason else 'Not specified'}
            """
            
            self.results_text.delete("1.0", "end")
            self.results_text.insert("1.0", result_text)
            
            # Save to database with new structure (no project_name)
            self.cursor.execute('''
                INSERT INTO delay_records (
                    start_date, completion_date, actual_completion_date,
                    delay_days, delay_reason, penalty_amount, date_created
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                start_date_str, completion_date_str, actual_completion_date_str,
                delay_days, delay_reason, penalty_amount,
                datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            ))
            
            self.conn.commit()
            
            messagebox.showinfo("Success", f"Delay calculated successfully!\nDelay: {delay_days} days")
            
        except Exception as e:
            messagebox.showerror("Error", f"Calculation error: {str(e)}")
    
    def save_calculation(self):
        """Save calculation record"""
        # Since we're now saving directly in calculate_delay, this method can be simplified
        # or we can remove it entirely. For now, let's just show a message.
        messagebox.showinfo("Info", "Calculation already saved during delay calculation.")
    
    def clear_form(self):
        """Clear form"""
        self.start_entry.delete(0, "end")
        self.completion_entry.delete(0, "end")
        self.actual_completion_entry.delete(0, "end")
        self.delay_reason_entry.delete(0, "end")
        
        self.results_text.delete("1.0", "end")
        self.results_text.insert("1.0", "Enter dates and click 'Calculate Delay'")
    
    def print_results(self):
        """Print results"""
        try:
            results = self.results_text.get("1.0", "end-1c")
            if results and results != "Enter dates and click 'Calculate Delay'":
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
