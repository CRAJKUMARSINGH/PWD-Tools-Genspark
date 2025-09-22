"""
Hindi Bill Note Tool - SIMPLIFIED for Lower Divisional Clerks
Based on original repository - Handles Running and Final Bills in Hindi
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
from datetime import datetime
import os
import sqlite3

class CalendarWidget:
    """Simple calendar widget for date selection"""
    def __init__(self, parent, callback=None):
        self.parent = parent
        self.callback = callback
        self.window = None
        
    def show_calendar(self, current_date=""):
        """Show calendar popup"""
        if self.window:
            self.window.destroy()
            
        self.window = ctk.CTkToplevel(self.parent)
        self.window.title("तिथि चुनें")
        self.window.geometry("300x300")
        self.window.transient(self.parent)
        self.window.grab_set()
        
        # Center the window
        self.window.update_idletasks()
        x = (self.window.winfo_screenwidth() // 2) - (300 // 2)
        y = (self.window.winfo_screenheight() // 2) - (300 // 2)
        self.window.geometry(f"300x300+{x}+{y}")
        
        # Create calendar frame
        cal_frame = ctk.CTkFrame(self.window)
        cal_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Month and Year selection
        month_year_frame = ctk.CTkFrame(cal_frame)
        month_year_frame.pack(fill="x", padx=5, pady=5)
        
        # Month selection
        ctk.CTkLabel(month_year_frame, text="महीना:", font=ctk.CTkFont(size=12)).pack(side="left", padx=5)
        self.month_var = tk.StringVar(value="1")
        month_combo = ctk.CTkComboBox(month_year_frame, values=[str(i) for i in range(1, 13)], 
                                    variable=self.month_var, width=80)
        month_combo.pack(side="left", padx=5)
        
        # Year selection
        ctk.CTkLabel(month_year_frame, text="साल:", font=ctk.CTkFont(size=12)).pack(side="left", padx=5)
        current_year = datetime.now().year
        self.year_var = tk.StringVar(value=str(current_year))
        year_combo = ctk.CTkComboBox(month_year_frame, 
                                   values=[str(i) for i in range(current_year-5, current_year+5)], 
                                   variable=self.year_var, width=80)
        year_combo.pack(side="left", padx=5)
        
        # Day selection
        ctk.CTkLabel(cal_frame, text="दिन:", font=ctk.CTkFont(size=12)).pack(pady=5)
        self.day_var = tk.StringVar(value="1")
        day_combo = ctk.CTkComboBox(cal_frame, values=[str(i) for i in range(1, 32)], 
                                  variable=self.day_var, width=100)
        day_combo.pack(pady=5)
        
        # Buttons
        btn_frame = ctk.CTkFrame(cal_frame)
        btn_frame.pack(fill="x", padx=5, pady=10)
        
        select_btn = ctk.CTkButton(btn_frame, text="चुनें", command=self.select_date, width=100)
        select_btn.pack(side="left", padx=5)
        
        cancel_btn = ctk.CTkButton(btn_frame, text="रद्द करें", command=self.window.destroy, 
                                 width=100, fg_color="gray")
        cancel_btn.pack(side="left", padx=5)
        
        # Set current date if provided
        if current_date:
            try:
                if "/" in current_date:
                    day, month, year = current_date.split("/")
                    self.day_var.set(day)
                    self.month_var.set(month)
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

class HindiBillNoteTool:
    def __init__(self):
        """Initialize Hindi Bill Note tool"""
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
        self.root = ctk.CTk()
        self.root.title("बिल नोट शीट - हिन्दी")
        
        # Make responsive for different screen sizes
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Adjust window size based on screen size
        if screen_width < 1024:  # Mobile/Tablet
            self.root.geometry(f"{min(screen_width-20, 400)}x{min(screen_height-50, 600)}")
        else:  # Desktop
            self.root.geometry("1000x800")
        
        # Make window resizable
        self.root.minsize(400, 600)
        
        # Simple database
        self.init_database()
        
        # Create interface
        self.create_interface()
    
    def init_database(self):
        """Initialize simple database"""
        self.conn = sqlite3.connect('hindi_bills.db')
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
        self.main_scroll = ctk.CTkScrollableFrame(self.root)
        self.main_scroll.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Header
        header = ctk.CTkLabel(
            self.main_scroll,
            text="बिल नोट शीट जेनरेटर (हिन्दी)",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        header.pack(pady=10)
        
        # Main frame
        main_frame = ctk.CTkFrame(self.main_scroll)
        main_frame.pack(fill="x", padx=5, pady=5)
        
        # Bill Type Selection
        bill_type_frame = ctk.CTkFrame(main_frame)
        bill_type_frame.pack(fill="x", padx=5, pady=5)
        
        ctk.CTkLabel(bill_type_frame, text="बिल का प्रकार:", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)
        
        self.bill_type_var = tk.StringVar(value="running")
        radio_frame = ctk.CTkFrame(bill_type_frame)
        radio_frame.pack(pady=5)
        
        running_radio = ctk.CTkRadioButton(radio_frame, text="रनिंग बिल", variable=self.bill_type_var, value="running")
        running_radio.pack(side="left", padx=10, pady=5)
        
        final_radio = ctk.CTkRadioButton(radio_frame, text="फाइनल बिल", variable=self.bill_type_var, value="final")
        final_radio.pack(side="left", padx=10, pady=5)
        
        # Input fields
        self.create_input_fields(main_frame)
        
        # Buttons
        self.create_buttons(main_frame)
        
        # Results
        self.create_results_section(main_frame)
    
    def create_input_fields(self, parent):
        """Create input fields"""
        fields_frame = ctk.CTkFrame(parent)
        fields_frame.pack(fill="x", padx=5, pady=5)
        
        # Work Order Amount
        ctk.CTkLabel(fields_frame, text="वर्क ऑर्डर राशि (₹):", font=ctk.CTkFont(size=12, weight="bold")).pack(pady=3)
        self.work_order_entry = ctk.CTkEntry(fields_frame, width=250, font=ctk.CTkFont(size=12))
        self.work_order_entry.pack(pady=3)
        
        # Upto Date Bill Amount
        ctk.CTkLabel(fields_frame, text="अब तक की बिल राशि (₹):", font=ctk.CTkFont(size=12, weight="bold")).pack(pady=3)
        self.upto_date_entry = ctk.CTkEntry(fields_frame, width=250, font=ctk.CTkFont(size=12))
        self.upto_date_entry.pack(pady=3)
        
        # Extra Items
        ctk.CTkLabel(fields_frame, text="Extra Items शामिल:", font=ctk.CTkFont(size=12, weight="bold")).pack(pady=3)
        self.extra_items_var = tk.StringVar(value="No")
        extra_frame = ctk.CTkFrame(fields_frame)
        extra_frame.pack(pady=3)
        
        ctk.CTkRadioButton(extra_frame, text="नहीं", variable=self.extra_items_var, value="No").pack(side="left", padx=5)
        ctk.CTkRadioButton(extra_frame, text="हाँ", variable=self.extra_items_var, value="Yes").pack(side="left", padx=5)
        
        # Extra Items Amount
        ctk.CTkLabel(fields_frame, text="Extra Items राशि (₹):", font=ctk.CTkFont(size=12, weight="bold")).pack(pady=3)
        self.extra_amount_entry = ctk.CTkEntry(fields_frame, width=250, font=ctk.CTkFont(size=12))
        self.extra_amount_entry.insert(0, "0")
        self.extra_amount_entry.pack(pady=3)
        
        # Final Bill Fields (initially hidden)
        self.final_fields_frame = ctk.CTkFrame(fields_frame)
        
        # Initialize calendar widgets
        self.start_calendar = CalendarWidget(self.root, self.set_start_date)
        self.schedule_calendar = CalendarWidget(self.root, self.set_schedule_date)
        self.actual_calendar = CalendarWidget(self.root, self.set_actual_date)
        
        # Start Date with Calendar
        start_date_frame = ctk.CTkFrame(self.final_fields_frame)
        start_date_frame.pack(fill="x", padx=5, pady=3)
        
        ctk.CTkLabel(start_date_frame, text="प्रारंभ तिथि (DD/MM/YYYY):", font=ctk.CTkFont(size=12, weight="bold")).pack(pady=3)
        start_input_frame = ctk.CTkFrame(start_date_frame)
        start_input_frame.pack(pady=3)
        
        self.start_date_entry = ctk.CTkEntry(start_input_frame, width=200, font=ctk.CTkFont(size=12))
        self.start_date_entry.pack(side="left", padx=5)
        
        start_cal_btn = ctk.CTkButton(start_input_frame, text="📅", command=self.show_start_calendar, width=30)
        start_cal_btn.pack(side="left", padx=5)
        
        # Schedule Completion Date with Calendar
        schedule_date_frame = ctk.CTkFrame(self.final_fields_frame)
        schedule_date_frame.pack(fill="x", padx=5, pady=3)
        
        ctk.CTkLabel(schedule_date_frame, text="निर्धारित समापन तिथि (DD/MM/YYYY):", font=ctk.CTkFont(size=12, weight="bold")).pack(pady=3)
        schedule_input_frame = ctk.CTkFrame(schedule_date_frame)
        schedule_input_frame.pack(pady=3)
        
        self.schedule_completion_entry = ctk.CTkEntry(schedule_input_frame, width=200, font=ctk.CTkFont(size=12))
        self.schedule_completion_entry.pack(side="left", padx=5)
        
        schedule_cal_btn = ctk.CTkButton(schedule_input_frame, text="📅", command=self.show_schedule_calendar, width=30)
        schedule_cal_btn.pack(side="left", padx=5)
        
        # Actual Completion Date with Calendar
        actual_date_frame = ctk.CTkFrame(self.final_fields_frame)
        actual_date_frame.pack(fill="x", padx=5, pady=3)
        
        ctk.CTkLabel(actual_date_frame, text="वास्तविक समापन तिथि (DD/MM/YYYY):", font=ctk.CTkFont(size=12, weight="bold")).pack(pady=3)
        actual_input_frame = ctk.CTkFrame(actual_date_frame)
        actual_input_frame.pack(pady=3)
        
        self.actual_completion_entry = ctk.CTkEntry(actual_input_frame, width=200, font=ctk.CTkFont(size=12))
        self.actual_completion_entry.pack(side="left", padx=5)
        
        actual_cal_btn = ctk.CTkButton(actual_input_frame, text="📅", command=self.show_actual_calendar, width=30)
        actual_cal_btn.pack(side="left", padx=5)
        
        # Repair Work
        ctk.CTkLabel(self.final_fields_frame, text="मरम्मत कार्य:", font=ctk.CTkFont(size=12, weight="bold")).pack(pady=3)
        self.repair_work_var = tk.StringVar(value="No")
        repair_frame = ctk.CTkFrame(self.final_fields_frame)
        repair_frame.pack(pady=3)
        
        ctk.CTkRadioButton(repair_frame, text="नहीं", variable=self.repair_work_var, value="No").pack(side="left", padx=5)
        ctk.CTkRadioButton(repair_frame, text="हाँ", variable=self.repair_work_var, value="Yes").pack(side="left", padx=5)
        
        # Excess Quantity
        ctk.CTkLabel(self.final_fields_frame, text="अधिक मात्रा (Excess Quantity):", font=ctk.CTkFont(size=12, weight="bold")).pack(pady=3)
        self.excess_quantity_var = tk.StringVar(value="No")
        excess_frame = ctk.CTkFrame(self.final_fields_frame)
        excess_frame.pack(pady=3)
        
        ctk.CTkRadioButton(excess_frame, text="नहीं", variable=self.excess_quantity_var, value="No").pack(side="left", padx=5)
        ctk.CTkRadioButton(excess_frame, text="हाँ", variable=self.excess_quantity_var, value="Yes").pack(side="left", padx=5)
        
        # Delay Comment
        ctk.CTkLabel(self.final_fields_frame, text="बिल देर से जमा (>6 माह):", font=ctk.CTkFont(size=12, weight="bold")).pack(pady=3)
        self.delay_comment_var = tk.StringVar(value="No")
        delay_frame = ctk.CTkFrame(self.final_fields_frame)
        delay_frame.pack(pady=3)
        
        ctk.CTkRadioButton(delay_frame, text="नहीं", variable=self.delay_comment_var, value="No").pack(side="left", padx=5)
        ctk.CTkRadioButton(delay_frame, text="हाँ", variable=self.delay_comment_var, value="Yes").pack(side="left", padx=5)
        
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
        button_frame = ctk.CTkFrame(parent)
        button_frame.pack(fill="x", padx=5, pady=5)
        
        # Responsive button layout
        btn_container = ctk.CTkFrame(button_frame)
        btn_container.pack(pady=5)
        
        generate_btn = ctk.CTkButton(
            btn_container,
            text="नोट शीट जनरेट करें",
            command=self.generate_note,
            width=180,
            height=35,
            font=ctk.CTkFont(size=14, weight="bold")
        )
        generate_btn.pack(side="left", padx=5)
        
        save_btn = ctk.CTkButton(
            btn_container,
            text="सेव करें",
            command=self.save_note,
            width=120,
            height=35,
            font=ctk.CTkFont(size=14, weight="bold")
        )
        save_btn.pack(side="left", padx=5)
        
        clear_btn = ctk.CTkButton(
            btn_container,
            text="क्लियर करें",
            command=self.clear_form,
            width=120,
            height=35,
            fg_color="gray",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        clear_btn.pack(side="left", padx=5)
    
    def create_results_section(self, parent):
        """Create results section"""
        results_frame = ctk.CTkFrame(parent)
        results_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        ctk.CTkLabel(results_frame, text="जनरेटेड नोट:", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)
        
        # Responsive textbox with scrollbar
        self.results_text = ctk.CTkTextbox(results_frame, height=150, font=ctk.CTkFont(size=11))
        self.results_text.pack(fill="both", expand=True, padx=5, pady=5)
        self.results_text.insert("1.0", "फॉर्म भरें और 'नोट शीट जनरेट करें' पर क्लिक करें।")
        
        # Copy and Print buttons
        action_btn_frame = ctk.CTkFrame(results_frame)
        action_btn_frame.pack(fill="x", padx=5, pady=5)
        
        copy_btn = ctk.CTkButton(
            action_btn_frame,
            text="कॉपी करें",
            command=self.copy_to_clipboard,
            width=100,
            height=30,
            font=ctk.CTkFont(size=12)
        )
        copy_btn.pack(side="left", padx=5)
        
        print_btn = ctk.CTkButton(
            action_btn_frame,
            text="प्रिंट करें",
            command=self.print_note,
            width=100,
            height=30,
            font=ctk.CTkFont(size=12)
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
                # Create a simple print dialog
                print_window = ctk.CTkToplevel(self.root)
                print_window.title("प्रिंट नोट")
                print_window.geometry("600x500")
                print_window.transient(self.root)
                print_window.grab_set()
                
                # Center the window
                print_window.update_idletasks()
                x = (print_window.winfo_screenwidth() // 2) - (600 // 2)
                y = (print_window.winfo_screenheight() // 2) - (500 // 2)
                print_window.geometry(f"600x500+{x}+{y}")
                
                # Print content
                print_frame = ctk.CTkFrame(print_window)
                print_frame.pack(fill="both", expand=True, padx=10, pady=10)
                
                ctk.CTkLabel(print_frame, text="प्रिंट करने के लिए तैयार नोट:", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)
                
                print_text = ctk.CTkTextbox(print_frame, font=ctk.CTkFont(size=12))
                print_text.pack(fill="both", expand=True, padx=10, pady=10)
                print_text.insert("1.0", note_text)
                print_text.configure(state="disabled")
                
                # Print buttons
                btn_frame = ctk.CTkFrame(print_frame)
                btn_frame.pack(fill="x", padx=10, pady=10)
                
                print_btn = ctk.CTkButton(btn_frame, text="प्रिंट करें", command=lambda: self.actual_print(note_text), width=120)
                print_btn.pack(side="left", padx=5)
                
                close_btn = ctk.CTkButton(btn_frame, text="बंद करें", command=print_window.destroy, width=120, fg_color="gray")
                close_btn.pack(side="left", padx=5)
            else:
                messagebox.showwarning("Warning", "पहले नोट जनरेट करें")
        except Exception as e:
            messagebox.showerror("Error", f"प्रिंट करने में त्रुटि: {str(e)}")
    
    def actual_print(self, text):
        """Actually print the text"""
        try:
            # Simple print to console (in real app, you'd use proper printing)
            print("=" * 50)
            print("HINDI BILL NOTE")
            print("=" * 50)
            print(text)
            print("=" * 50)
            messagebox.showinfo("Success", "नोट प्रिंट किया गया! (कंसोल में देखें)")
        except Exception as e:
            messagebox.showerror("Error", f"प्रिंट करने में त्रुटि: {str(e)}")
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = HindiBillNoteTool()
    app.run()
