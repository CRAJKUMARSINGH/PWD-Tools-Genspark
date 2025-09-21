"""
Hindi Bill Note Tool - SIMPLE VERSION (Standard Tkinter)
For Lower Divisional Clerks - NO COMPLEXITY
Uses standard tkinter to avoid CustomTkinter issues
"""

import tkinter as tk
from tkinter import messagebox, filedialog, ttk
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

class SimpleHindiBillNoteTool:
    def __init__(self):
        """Initialize Simple Hindi Bill Note tool"""
        self.root = tk.Tk()
        self.root.title("बिल नोट शीट - हिन्दी (सरल)")
        
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
        self.conn = sqlite3.connect('simple_hindi_bills.db')
        self.cursor = self.conn.cursor()
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS hindi_bills (
                id INTEGER PRIMARY KEY,
                bill_type TEXT,
                work_order_amount REAL,
                upto_date_amount REAL,
                extra_items TEXT,
                extra_amount REAL,
                start_date TEXT,
                completion_date TEXT,
                actual_completion TEXT,
                repair_work TEXT,
                excess_quantity TEXT,
                delay_comment TEXT,
                generated_note TEXT,
                date_created TEXT
            )
        ''')
        self.conn.commit()
    
    def create_interface(self):
        """Create Hindi interface"""
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
            text="बिल नोट शीट जेनरेटर (हिन्दी)",
            font=("Arial", 18, "bold"),
            fg="blue"
        )
        header.pack(pady=10)
        
        # Main frame
        main_frame = tk.Frame(self.scrollable_frame)
        main_frame.pack(fill="x", padx=10, pady=5)
        
        # Bill Type Selection
        bill_type_frame = tk.LabelFrame(main_frame, text="बिल का प्रकार", font=("Arial", 12, "bold"))
        bill_type_frame.pack(fill="x", padx=5, pady=5)
        
        self.bill_type_var = tk.StringVar(value="running")
        radio_frame = tk.Frame(bill_type_frame)
        radio_frame.pack(pady=5)
        
        running_radio = tk.Radiobutton(radio_frame, text="रनिंग बिल", variable=self.bill_type_var, value="running")
        running_radio.pack(side="left", padx=10, pady=5)
        
        final_radio = tk.Radiobutton(radio_frame, text="फाइनल बिल", variable=self.bill_type_var, value="final")
        final_radio.pack(side="left", padx=10, pady=5)
        
        # Input fields
        self.create_input_fields(main_frame)
        
        # Buttons
        self.create_buttons(main_frame)
        
        # Results
        self.create_results_section(main_frame)
    
    def create_input_fields(self, parent):
        """Create input fields"""
        fields_frame = tk.LabelFrame(parent, text="बिल विवरण", font=("Arial", 12, "bold"))
        fields_frame.pack(fill="x", padx=5, pady=5)
        
        # Work Order Amount
        tk.Label(fields_frame, text="वर्क ऑर्डर राशि (₹):", font=("Arial", 10, "bold")).pack(pady=3)
        self.work_order_entry = tk.Entry(fields_frame, width=30, font=("Arial", 10))
        self.work_order_entry.pack(pady=3)
        
        # Upto Date Bill Amount
        tk.Label(fields_frame, text="अब तक की बिल राशि (₹):", font=("Arial", 10, "bold")).pack(pady=3)
        self.upto_date_entry = tk.Entry(fields_frame, width=30, font=("Arial", 10))
        self.upto_date_entry.pack(pady=3)
        
        # Extra Items
        tk.Label(fields_frame, text="Extra Items शामिल:", font=("Arial", 10, "bold")).pack(pady=3)
        self.extra_items_var = tk.StringVar(value="No")
        extra_frame = tk.Frame(fields_frame)
        extra_frame.pack(pady=3)
        
        tk.Radiobutton(extra_frame, text="नहीं", variable=self.extra_items_var, value="No").pack(side="left", padx=5)
        tk.Radiobutton(extra_frame, text="हाँ", variable=self.extra_items_var, value="Yes").pack(side="left", padx=5)
        
        # Extra Items Amount
        tk.Label(fields_frame, text="Extra Items राशि (₹):", font=("Arial", 10, "bold")).pack(pady=3)
        self.extra_amount_entry = tk.Entry(fields_frame, width=30, font=("Arial", 10))
        self.extra_amount_entry.insert(0, "0")
        self.extra_amount_entry.pack(pady=3)
        
        # Final Bill Fields (initially hidden)
        self.final_fields_frame = tk.LabelFrame(fields_frame, text="फाइनल बिल विवरण", font=("Arial", 10, "bold"))
        
        # Initialize calendar widgets
        self.start_calendar = SimpleCalendarWidget(self.root, self.set_start_date)
        self.schedule_calendar = SimpleCalendarWidget(self.root, self.set_schedule_date)
        self.actual_calendar = SimpleCalendarWidget(self.root, self.set_actual_date)
        
        # Start Date with Calendar
        start_date_frame = tk.Frame(self.final_fields_frame)
        start_date_frame.pack(fill="x", padx=5, pady=3)
        
        tk.Label(start_date_frame, text="प्रारंभ तिथि (DD/MM/YYYY):", font=("Arial", 9, "bold")).pack(pady=3)
        start_input_frame = tk.Frame(start_date_frame)
        start_input_frame.pack(pady=3)
        
        self.start_date_entry = tk.Entry(start_input_frame, width=20, font=("Arial", 9))
        self.start_date_entry.pack(side="left", padx=5)
        
        start_cal_btn = tk.Button(start_input_frame, text="📅", command=self.show_start_calendar, width=3)
        start_cal_btn.pack(side="left", padx=5)
        
        # Schedule Completion Date with Calendar
        schedule_date_frame = tk.Frame(self.final_fields_frame)
        schedule_date_frame.pack(fill="x", padx=5, pady=3)
        
        tk.Label(schedule_date_frame, text="निर्धारित समापन तिथि (DD/MM/YYYY):", font=("Arial", 9, "bold")).pack(pady=3)
        schedule_input_frame = tk.Frame(schedule_date_frame)
        schedule_input_frame.pack(pady=3)
        
        self.schedule_completion_entry = tk.Entry(schedule_input_frame, width=20, font=("Arial", 9))
        self.schedule_completion_entry.pack(side="left", padx=5)
        
        schedule_cal_btn = tk.Button(schedule_input_frame, text="📅", command=self.show_schedule_calendar, width=3)
        schedule_cal_btn.pack(side="left", padx=5)
        
        # Actual Completion Date with Calendar
        actual_date_frame = tk.Frame(self.final_fields_frame)
        actual_date_frame.pack(fill="x", padx=5, pady=3)
        
        tk.Label(actual_date_frame, text="वास्तविक समापन तिथि (DD/MM/YYYY):", font=("Arial", 9, "bold")).pack(pady=3)
        actual_input_frame = tk.Frame(actual_date_frame)
        actual_input_frame.pack(pady=3)
        
        self.actual_completion_entry = tk.Entry(actual_input_frame, width=20, font=("Arial", 9))
        self.actual_completion_entry.pack(side="left", padx=5)
        
        actual_cal_btn = tk.Button(actual_input_frame, text="📅", command=self.show_actual_calendar, width=3)
        actual_cal_btn.pack(side="left", padx=5)
        
        # Repair Work
        tk.Label(self.final_fields_frame, text="मरम्मत कार्य:", font=("Arial", 9, "bold")).pack(pady=3)
        self.repair_work_var = tk.StringVar(value="No")
        repair_frame = tk.Frame(self.final_fields_frame)
        repair_frame.pack(pady=3)
        
        tk.Radiobutton(repair_frame, text="नहीं", variable=self.repair_work_var, value="No").pack(side="left", padx=5)
        tk.Radiobutton(repair_frame, text="हाँ", variable=self.repair_work_var, value="Yes").pack(side="left", padx=5)
        
        # Excess Quantity
        tk.Label(self.final_fields_frame, text="अधिक मात्रा (Excess Quantity):", font=("Arial", 9, "bold")).pack(pady=3)
        self.excess_quantity_var = tk.StringVar(value="No")
        excess_frame = tk.Frame(self.final_fields_frame)
        excess_frame.pack(pady=3)
        
        tk.Radiobutton(excess_frame, text="नहीं", variable=self.excess_quantity_var, value="No").pack(side="left", padx=5)
        tk.Radiobutton(excess_frame, text="हाँ", variable=self.excess_quantity_var, value="Yes").pack(side="left", padx=5)
        
        # Delay Comment
        tk.Label(self.final_fields_frame, text="बिल देर से जमा (>6 माह):", font=("Arial", 9, "bold")).pack(pady=3)
        self.delay_comment_var = tk.StringVar(value="No")
        delay_frame = tk.Frame(self.final_fields_frame)
        delay_frame.pack(pady=3)
        
        tk.Radiobutton(delay_frame, text="नहीं", variable=self.delay_comment_var, value="No").pack(side="left", padx=5)
        tk.Radiobutton(delay_frame, text="हाँ", variable=self.delay_comment_var, value="Yes").pack(side="left", padx=5)
        
        # Show/hide final fields based on bill type
        self.bill_type_var.trace('w', self.toggle_final_fields)
    
    def toggle_final_fields(self, *args):
        """Show/hide final bill fields"""
        if self.bill_type_var.get() == "final":
            self.final_fields_frame.pack(fill="x", padx=5, pady=5)
        else:
            self.final_fields_frame.pack_forget()
    
    def show_start_calendar(self):
        """Show start date calendar"""
        self.start_calendar.show_calendar(self.start_date_entry.get())
    
    def show_schedule_calendar(self):
        """Show schedule completion calendar"""
        self.schedule_calendar.show_calendar(self.schedule_completion_entry.get())
    
    def show_actual_calendar(self):
        """Show actual completion calendar"""
        self.actual_calendar.show_calendar(self.actual_completion_entry.get())
    
    def set_start_date(self, date):
        """Set start date from calendar"""
        self.start_date_entry.delete(0, "end")
        self.start_date_entry.insert(0, date)
    
    def set_schedule_date(self, date):
        """Set schedule date from calendar"""
        self.schedule_completion_entry.delete(0, "end")
        self.schedule_completion_entry.insert(0, date)
    
    def set_actual_date(self, date):
        """Set actual date from calendar"""
        self.actual_completion_entry.delete(0, "end")
        self.actual_completion_entry.insert(0, date)
    
    def create_buttons(self, parent):
        """Create buttons"""
        button_frame = tk.Frame(parent)
        button_frame.pack(fill="x", padx=5, pady=5)
        
        generate_btn = tk.Button(
            button_frame,
            text="नोट शीट जनरेट करें",
            command=self.generate_note,
            width=20,
            height=2,
            font=("Arial", 10, "bold"),
            bg="lightblue"
        )
        generate_btn.pack(side="left", padx=5)
        
        save_btn = tk.Button(
            button_frame,
            text="सेव करें",
            command=self.save_note,
            width=15,
            height=2,
            font=("Arial", 10, "bold"),
            bg="lightgreen"
        )
        save_btn.pack(side="left", padx=5)
        
        clear_btn = tk.Button(
            button_frame,
            text="क्लियर करें",
            command=self.clear_form,
            width=15,
            height=2,
            font=("Arial", 10, "bold"),
            bg="lightgray"
        )
        clear_btn.pack(side="left", padx=5)
    
    def create_results_section(self, parent):
        """Create results section"""
        results_frame = tk.LabelFrame(parent, text="जनरेटेड नोट", font=("Arial", 12, "bold"))
        results_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Responsive textbox with scrollbar - shrunk vertically by 15%
        text_frame = tk.Frame(results_frame)
        text_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.results_text = tk.Text(text_frame, height=8, font=("Arial", 10), wrap="word")  # Reduced from 10 to 8 (15% reduction)
        scrollbar = tk.Scrollbar(text_frame, orient="vertical", command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=scrollbar.set)
        
        self.results_text.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        self.results_text.insert("1.0", "फॉर्म भरें और 'नोट शीट जनरेट करें' पर क्लिक करें।")
        
        # Copy and Print buttons
        action_btn_frame = tk.Frame(results_frame)
        action_btn_frame.pack(fill="x", padx=5, pady=5)
        
        copy_btn = tk.Button(
            action_btn_frame,
            text="कॉपी करें",
            command=self.copy_to_clipboard,
            width=12,
            height=1,
            font=("Arial", 9),
            bg="lightyellow"
        )
        copy_btn.pack(side="left", padx=5)
        
        print_btn = tk.Button(
            action_btn_frame,
            text="प्रिंट करें",
            command=self.print_note,
            width=12,
            height=1,
            font=("Arial", 9),
            bg="lightcoral"
        )
        print_btn.pack(side="left", padx=5)
    
    def generate_note(self):
        """Generate Hindi bill note"""
        try:
            # Get form values
            bill_type = self.bill_type_var.get()
            work_order_amount = float(self.work_order_entry.get())
            upto_date_amount = float(self.upto_date_entry.get())
            extra_items = self.extra_items_var.get()
            extra_amount = float(self.extra_amount_entry.get())
            
            # Calculate percentage
            percentage_work_done = (upto_date_amount / work_order_amount) * 100
            
            # Generate note
            note = ""
            serial_number = 1
            
            if bill_type == "running":
                note += f"{serial_number}. इस Stage में कार्य {percentage_work_done:.2f}% संपादित हुआ है।\n"
                serial_number += 1
                note += f"{serial_number}. कार्य प्रगति पर है।\n"
                serial_number += 1
                
                if extra_items == "Yes":
                    extra_percentage = (extra_amount / work_order_amount) * 100
                    if extra_percentage > 5:
                        note += f"{serial_number}. ₹{extra_amount:.2f} की Extra Items कार्यान्वित किए गए हैं, जो वर्क ऑर्डर राशि का {extra_percentage:.2f}% है, जो 5% से अधिक है। जिसकी स्वीकृति Superintending Engineer, Electric Circle Udaipur कार्यालय के क्षेत्राधिकार में है।\n"
                    elif extra_percentage == 5:
                        note += f"{serial_number}. ₹{extra_amount:.2f} की Extra Items कार्यान्वित किए गए हैं, जो वर्क ऑर्डर राशि का {extra_percentage:.2f}% है, जो 5% के बराबर है। जिसकी स्वीकृति इस कार्यालय के क्षेत्राधिकार में है।\n"
                    else:
                        note += f"{serial_number}. ₹{extra_amount:.2f} की Extra Items कार्यान्वित किए गए हैं, जो वर्क ऑर्डर राशि का {extra_percentage:.2f}% है, जो 5% से कम है। जिसकी स्वीकृति इस कार्यालय के क्षेत्राधिकार में है।\n"
                    serial_number += 1
                
                note += f"{serial_number}. उपरोक्त विवरण के सन्दर्भ में समुचित निर्णय हेतु प्रस्तुत है।"
            
            else:  # Final bill
                start_date = self.start_date_entry.get()
                schedule_completion = self.schedule_completion_entry.get()
                actual_completion = self.actual_completion_entry.get()
                repair_work = self.repair_work_var.get()
                excess_quantity = self.excess_quantity_var.get()
                delay_comment = self.delay_comment_var.get()
                
                note += f"{serial_number}. कार्य {percentage_work_done:.2f}% पूर्ण हुआ है।\n"
                serial_number += 1
                
                # Work completion percentage logic
                if percentage_work_done < 90:
                    note += f"{serial_number}. कार्य का वांछित Deviation Statement भी स्वीकृति हेतु प्राप्त हुआ है, जिसकी स्वीकृति इसी कार्यालय के क्षेत्राधिकार में निहित है।\n"
                    serial_number += 1
                elif percentage_work_done > 90 and percentage_work_done <= 100:
                    note += f"{serial_number}. कार्य पूर्णता का प्रतिशत ({percentage_work_done:.2f}%) 90% से अधिक किंतु 100% तक है।\n"
                    serial_number += 1
                elif percentage_work_done == 100:
                    note += f"{serial_number}. कार्य ({percentage_work_done:.2f}%) पूर्ण हुआ है।\n"
                    serial_number += 1
                elif percentage_work_done > 100 and percentage_work_done <= 105:
                    note += f"{serial_number}. कार्य का वांछित Deviation Statement भी स्वीकृति हेतु प्राप्त हुआ है, Overall Excess कार्य की मात्रा 5% से कम/बराबर है, जिसकी स्वीकृति इसी कार्यालय के क्षेत्राधिकार में निहित है।\n"
                    serial_number += 1
                elif percentage_work_done > 105:
                    note += f"{serial_number}. कार्य का वांछित Deviation Statement भी स्वीकृति हेतु प्राप्त हुआ है, Overall Excess कार्य की मात्रा 5% से अधिक है, जिसकी स्वीकृति Superintending Engineer, PWD Electric Circle, Udaipur के क्षेत्राधिकार में निहित है।\n"
                    serial_number += 1
                
                # Delay calculation
                if start_date and schedule_completion and actual_completion:
                    try:
                        start_dt = datetime.strptime(start_date, "%d/%m/%Y")
                        schedule_dt = datetime.strptime(schedule_completion, "%d/%m/%Y")
                        actual_dt = datetime.strptime(actual_completion, "%d/%m/%Y")
                        
                        delay_days = (actual_dt - schedule_dt).days
                        if actual_dt > schedule_dt:
                            note += f"{serial_number}. कार्य में {delay_days} दिन की देरी हुई है।\n"
                            serial_number += 1
                            
                            schedule_duration = (schedule_dt - start_dt).days
                            if delay_days > (schedule_duration / 2 + 1):
                                note += f"{serial_number}. Time Extension केस Superintending Engineer, Electric Circle, Udaipur कार्यालय द्वारा अनुमोदित किया जाना है।\n"
                            else:
                                note += f"{serial_number}. Time Extension केस इस कार्यालय द्वारा अनुमोदित किया जाना है।\n"
                            serial_number += 1
                        else:
                            note += f"{serial_number}. कार्य समय पर संपादित हुआ है।\n"
                            serial_number += 1
                    except ValueError:
                        note += f"{serial_number}. तिथि प्रारूप गलत है।\n"
                        serial_number += 1
                
                # Extra items
                if extra_items == "Yes":
                    extra_percentage = (extra_amount / work_order_amount) * 100
                    if extra_percentage > 5:
                        note += f"{serial_number}. ₹{extra_amount:.2f} की Extra Items कार्यान्वित किए गए हैं, जो वर्क ऑर्डर राशि का {extra_percentage:.2f}% है, जो 5% से अधिक है। जिसकी स्वीकृति Superintending Engineer, Electric Circle, Udaipur कार्यालय के क्षेत्राधिकार में है।\n"
                    elif extra_percentage == 5:
                        note += f"{serial_number}. ₹{extra_amount:.2f} की Extra Items कार्यान्वित किए गए हैं, जो वर्क ऑर्डर राशि का {extra_percentage:.2f}% है, अथवा (5% के बराबर है)। जिसकी स्वीकृति इस कार्यालय के क्षेत्राधिकार में है।\n"
                    else:
                        note += f"{serial_number}. ₹{extra_amount:.2f} की Extra Items कार्यान्वित किए गए हैं, जो वर्क ऑर्डर राशि का {extra_percentage:.2f}% है, जो 5% से कम है। जिसकी स्वीकृति इस कार्यालय के क्षेत्राधिकार में है।\n"
                    serial_number += 1
                
                # Excess quantity
                if excess_quantity == "Yes":
                    note += f"{serial_number}. Work Order के कुछ आइटम में अतिरिक्त मात्रा (Excess Quantity) संपादित की गई है। इसके लिए Deviation Statement भी स्वीकृति हेतु प्राप्त हुआ है।\n"
                    serial_number += 1
                
                # Quality control
                note += f"{serial_number}. गुणवत्ता नियंत्रण (Q.C.) परीक्षण रिपोर्ट (Test Reports) संलग्न हैं।\n"
                serial_number += 1
                
                # Hand over statement
                if repair_work == "No":
                    note += f"{serial_number}. हस्तांतरण विवरण Hand Over Statement संलग्न है।\n"
                    serial_number += 1
                
                # Delay comment
                if delay_comment == "Yes":
                    note += f"{serial_number}. कार्य समाप्ति के करीब 6 महीने बाद फाइनल बिल इस कार्यालय में प्रस्तुत किया गया है। इस अप्रत्याशित देरी के लिए सहायक अभियंता से स्पष्टीकरण मांगा जाए, ऐसी प्रस्तावना है।\n"
                    serial_number += 1
                
                note += f"{serial_number}. उचित निर्णय के लिए उपर्युक्त विवरण संलग्न है।"
            
            # Display results
            self.results_text.delete("1.0", "end")
            self.results_text.insert("1.0", note)
            
            # Store generated note
            self.generated_note = note
            
        except ValueError:
            messagebox.showerror("Error", "कृपया सभी राशि फ़ील्ड में मान्य संख्या दर्ज करें")
        except Exception as e:
            messagebox.showerror("Error", f"नोट जनरेट करने में त्रुटि: {str(e)}")
    
    def save_note(self):
        """Save generated note"""
        if not hasattr(self, 'generated_note'):
            messagebox.showwarning("Warning", "पहले नोट जनरेट करें")
            return
        
        try:
            self.cursor.execute('''
                INSERT INTO hindi_bills (
                    bill_type, work_order_amount, upto_date_amount, extra_items, extra_amount,
                    start_date, completion_date, actual_completion, repair_work, excess_quantity,
                    delay_comment, generated_note, date_created
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                self.bill_type_var.get(),
                float(self.work_order_entry.get()),
                float(self.upto_date_entry.get()),
                self.extra_items_var.get(),
                float(self.extra_amount_entry.get()),
                self.start_date_entry.get() if self.bill_type_var.get() == "final" else "",
                self.schedule_completion_entry.get() if self.bill_type_var.get() == "final" else "",
                self.actual_completion_entry.get() if self.bill_type_var.get() == "final" else "",
                self.repair_work_var.get() if self.bill_type_var.get() == "final" else "",
                self.excess_quantity_var.get() if self.bill_type_var.get() == "final" else "",
                self.delay_comment_var.get() if self.bill_type_var.get() == "final" else "",
                self.generated_note,
                datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            ))
            
            self.conn.commit()
            messagebox.showinfo("Success", "नोट सफलतापूर्वक सेव हो गया!")
            
        except Exception as e:
            messagebox.showerror("Error", f"सेव करने में त्रुटि: {str(e)}")
    
    def clear_form(self):
        """Clear all form fields"""
        self.work_order_entry.delete(0, "end")
        self.upto_date_entry.delete(0, "end")
        self.extra_amount_entry.delete(0, "end")
        self.extra_amount_entry.insert(0, "0")
        self.start_date_entry.delete(0, "end")
        self.schedule_completion_entry.delete(0, "end")
        self.actual_completion_entry.delete(0, "end")
        
        self.bill_type_var.set("running")
        self.extra_items_var.set("No")
        self.repair_work_var.set("No")
        self.excess_quantity_var.set("No")
        self.delay_comment_var.set("No")
        
        self.results_text.delete("1.0", "end")
        self.results_text.insert("1.0", "फॉर्म भरें और 'नोट शीट जनरेट करें' पर क्लिक करें।")
        
        if hasattr(self, 'generated_note'):
            delattr(self, 'generated_note')
    
    def copy_to_clipboard(self):
        """Copy generated note to clipboard"""
        try:
            note_text = self.results_text.get("1.0", "end-1c")
            if note_text and note_text != "फॉर्म भरें और 'नोट शीट जनरेट करें' पर क्लिक करें।":
                self.root.clipboard_clear()
                self.root.clipboard_append(note_text)
                messagebox.showinfo("Success", "नोट क्लिपबोर्ड पर कॉपी किया गया!")
            else:
                messagebox.showwarning("Warning", "पहले नोट जनरेट करें")
        except Exception as e:
            messagebox.showerror("Error", f"कॉपी करने में त्रुटि: {str(e)}")
    
    def print_note(self):
        """Print the generated note"""
        try:
            note_text = self.results_text.get("1.0", "end-1c")
            if note_text and note_text != "फॉर्म भरें और 'नोट शीट जनरेट करें' पर क्लिक करें।":
                # Simple print to console
                print("=" * 50)
                print("HINDI BILL NOTE")
                print("=" * 50)
                print(note_text)
                print("=" * 50)
                messagebox.showinfo("Success", "नोट प्रिंट किया गया! (कंसोल में देखें)")
            else:
                messagebox.showwarning("Warning", "पहले नोट जनरेट करें")
        except Exception as e:
            messagebox.showerror("Error", f"प्रिंट करने में त्रुटि: {str(e)}")
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = SimpleHindiBillNoteTool()
    app.run()
