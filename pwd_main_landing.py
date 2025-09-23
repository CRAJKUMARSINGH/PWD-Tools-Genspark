"""
PWD Tools - Colorful Main Landing Page
For Lower Divisional Clerks - Beautiful and Simple
"""

import tkinter as tk
from tkinter import messagebox
import webbrowser
import os
import sys
import subprocess
import logging
from datetime import datetime
import traceback

class PWDMainLanding:
    def __init__(self):
        """Initialize colorful main landing page"""
        # Setup logging
        logging.basicConfig(filename='pwd_tools.log', level=logging.INFO,
                          format='%(asctime)s - %(levelname)s - %(message)s')
        
        self.root = tk.Tk()
        self.root.title("PWD Tools - Main Dashboard")
        self.root.geometry("1000x750")
        self.root.configure(bg="#f0f8ff")
        
        # Make window resizable
        self.root.minsize(800, 650)
        
        # Create colorful interface
        self.create_interface()
        
        # Log application start
        logging.info("PWD Tools application started")
    
    def create_interface(self):
        """Create colorful main interface"""
        # Header with gradient effect
        header_frame = tk.Frame(self.root, bg="#1E6B4E", height=80)  # Darker, more vivid green
        header_frame.pack(fill="x", padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        # Main title
        title_label = tk.Label(
            header_frame,
            text="🏗️ PWD Tools Dashboard",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#1E6B4E"
        )
        title_label.pack(pady=20)
        
        # Subtitle
        subtitle_label = tk.Label(
            header_frame,
            text="Infrastructure Management Suite for Lower Divisional Clerks",
            font=("Arial", 12),
            fg="#FFFFFF",  # Brighter white
            bg="#1E6B4E"
        )
        subtitle_label.pack(pady=5)
        
        # Main content area
        main_frame = tk.Frame(self.root, bg="#e0f0ff")  # More vivid blue background
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Welcome message
        welcome_frame = tk.Frame(main_frame, bg="#C0E0FF", relief="raised", bd=2)  # More vivid blue
        welcome_frame.pack(fill="x", pady=(0, 20))
        
        welcome_label = tk.Label(
            welcome_frame,
            text="🎉 Welcome to PWD Tools - Simple & Efficient!",
            font=("Arial", 16, "bold"),
            fg="#1E6B4E",  # Darker, more vivid green
            bg="#C0E0FF"
        )
        welcome_label.pack(pady=15)
        
        # Tools grid
        self.create_tools_grid(main_frame)
        
        # Footer
        self.create_footer(main_frame)
        
        # Status bar
        self.create_status_bar()
    
    def create_tools_grid(self, parent):
        """Create colorful tools grid"""
        tools_frame = tk.Frame(parent, bg="#e0f0ff")  # Match main background
        tools_frame.pack(fill="both", expand=True, pady=10)
        
        # Tool buttons with more vivid colors
        tools = [
            {
                "name": "Hindi Bill Note",
                "description": "Generate Running & Final Bills in Hindi",
                "color": "#FF5252",  # More vivid red
                "command": self.open_hindi_bill,
                "icon": "📝"
            },
            {
                "name": "Stamp Duty Calculator",
                "description": "Calculate stamp duty with predefined rates",
                "color": "#00BCD4",  # More vivid teal
                "command": self.open_stamp_duty,
                "icon": "💰"
            },
            {
                "name": "EMD Refund",
                "description": "Simple EMD refund with 3 inputs only",
                "color": "#2196F3",  # More vivid blue
                "command": self.open_emd_refund,
                "icon": "💳"
            },
            {
                "name": "Delay Calculator",
                "description": "Calculate project delays easily",
                "color": "#4CAF50",  # More vivid green
                "command": self.open_delay_calculator,
                "icon": "⏰"
            },
            {
                "name": "Financial Analysis",
                "description": "Advanced web-based financial analysis with liquidity damages",
                "color": "#FFC107",  # More vivid yellow
                "command": self.open_financial_analysis,
                "icon": "📊"
            },
            {
                "name": "Bill Generator Link",
                "description": "Open online bill generator",
                "color": "#9C27B0",  # More vivid purple
                "command": self.open_bill_generator,
                "icon": "🌐"
            },
            {
                "name": "Excel EMD Processor",
                "description": "Process EMD data from Excel files",
                "color": "#3F51B5",  # More vivid indigo
                "command": self.open_excel_emd,
                "icon": "📊"
            },
            {
                "name": "Deductions Calculator",
                "description": "Calculate tax and other deductions",
                "color": "#009688",  # More vivid teal
                "command": self.open_deductions_table,
                "icon": "🧮"
            },
            {
                "name": "Tender Processing",
                "description": "Manage and process tender documents",
                "color": "#FF9800",  # More vivid orange
                "command": self.open_tender_processing,
                "icon": "📋"
            },
            {
                "name": "Security Refund",
                "description": "Process security deposit refunds",
                "color": "#673AB7",  # More vivid deep purple
                "command": self.open_security_refund,
                "icon": "🔒"
            }
        ]
        
        # Create grid of tool buttons
        for i, tool in enumerate(tools):
            row = i // 3  # Changed to 3 columns per row
            col = i % 3
            
            tool_frame = tk.Frame(tools_frame, bg="white", relief="raised", bd=2)
            tool_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            
            # Configure grid weights
            tools_frame.grid_rowconfigure(row, weight=1)
            tools_frame.grid_columnconfigure(col, weight=1)
            
            # Tool icon and name
            icon_label = tk.Label(
                tool_frame,
                text=tool["icon"],
                font=("Arial", 24),
                bg="white"
            )
            icon_label.pack(pady=(15, 5))
            
            name_label = tk.Label(
                tool_frame,
                text=tool["name"],
                font=("Arial", 14, "bold"),
                fg=tool["color"],
                bg="white"
            )
            name_label.pack(pady=5)
            
            # Tool description
            desc_label = tk.Label(
                tool_frame,
                text=tool["description"],
                font=("Arial", 10),
                fg="#666666",
                bg="white",
                wraplength=200
            )
            desc_label.pack(pady=5)
            
            # Tool button
            tool_btn = tk.Button(
                tool_frame,
                text=f"Open {tool['name']}",
                command=tool["command"],
                width=20,
                height=2,
                font=("Arial", 10, "bold"),
                bg=tool["color"],
                fg="white",
                relief="flat",
                cursor="hand2"
            )
            tool_btn.pack(pady=15)
    
    def create_footer(self, parent):
        """Create colorful footer"""
        footer_frame = tk.Frame(parent, bg="#1E6B4E", height=60)  # Match header color
        footer_frame.pack(fill="x", pady=(20, 0))
        footer_frame.pack_propagate(False)
        
        # Footer content
        footer_content = tk.Frame(footer_frame, bg="#1E6B4E")
        footer_content.pack(expand=True)
        
        # Left side - Version info
        version_label = tk.Label(
            footer_content,
            text="Version 1.0.0 | Simple & Efficient",
            font=("Arial", 10),
            fg="white",
            bg="#1E6B4E"
        )
        version_label.pack(side="left", padx=20, pady=20)
        
        # Right side - Quick actions
        quick_frame = tk.Frame(footer_content, bg="#1E6B4E")
        quick_frame.pack(side="right", padx=20, pady=20)
        
        help_btn = tk.Button(
            quick_frame,
            text="Help",
            command=self.show_help,
            width=8,
            height=1,
            font=("Arial", 9),
            bg="#43A047",  # More vivid green
            fg="white",
            relief="flat"
        )
        help_btn.pack(side="left", padx=5)
        
        about_btn = tk.Button(
            quick_frame,
            text="About",
            command=self.show_about,
            width=8,
            height=1,
            font=("Arial", 9),
            bg="#1E88E5",  # More vivid blue
            fg="white",
            relief="flat"
        )
        about_btn.pack(side="left", padx=5)
    
    def open_hindi_bill(self):
        """Open Hindi Bill Note tool"""
        try:
            if os.path.exists("hindi_bill_simple.py"):
                # Get absolute path to be sure
                script_path = os.path.abspath("hindi_bill_simple.py")
                logging.info(f"Launching Hindi Bill Note from: {script_path}")
                logging.info(f"Current working directory: {os.getcwd()}")
                logging.info(f"Python executable: {sys.executable}")
                
                # Try different approaches
                try:
                    # Method 1: Direct subprocess
                    process = subprocess.Popen([sys.executable, script_path])
                    logging.info(f"Hindi Bill Note launched with PID: {process.pid}")
                except Exception as e1:
                    logging.error(f"Method 1 failed: {e1}")
                    try:
                        # Method 2: With shell=True
                        process = subprocess.Popen([sys.executable, script_path], shell=True)
                        logging.info(f"Hindi Bill Note launched with shell=True, PID: {process.pid}")
                    except Exception as e2:
                        logging.error(f"Method 2 failed: {e2}")
                        raise
                
                self.update_status("Hindi Bill Note tool opened successfully")
            else:
                error_msg = "Hindi Bill Note tool file not found"
                logging.error(error_msg)
                messagebox.showerror("Error", error_msg)
        except Exception as e:
            error_msg = f"Could not open Hindi Bill Note: {str(e)}"
            logging.error(error_msg + "\n" + traceback.format_exc())
            messagebox.showerror("Error", error_msg)
    
    def open_stamp_duty(self):
        """Open Stamp Duty tool"""
        try:
            if os.path.exists("stamp_duty_simple.py"):
                # Get absolute path to be sure
                script_path = os.path.abspath("stamp_duty_simple.py")
                logging.info(f"Launching Stamp Duty from: {script_path}")
                
                # Try different approaches
                try:
                    # Method 1: Direct subprocess
                    process = subprocess.Popen([sys.executable, script_path])
                    logging.info(f"Stamp Duty launched with PID: {process.pid}")
                except Exception as e1:
                    logging.error(f"Method 1 failed: {e1}")
                    try:
                        # Method 2: With shell=True
                        process = subprocess.Popen([sys.executable, script_path], shell=True)
                        logging.info(f"Stamp Duty launched with shell=True, PID: {process.pid}")
                    except Exception as e2:
                        logging.error(f"Method 2 failed: {e2}")
                        raise
                
                self.update_status("Stamp Duty Calculator tool opened successfully")
            else:
                error_msg = "Stamp Duty Calculator tool file not found"
                logging.error(error_msg)
                messagebox.showerror("Error", error_msg)
        except Exception as e:
            error_msg = f"Could not open Stamp Duty Calculator: {str(e)}"
            logging.error(error_msg + "\n" + traceback.format_exc())
            messagebox.showerror("Error", error_msg)
    
    def open_emd_refund(self):
        """Open EMD Refund tool"""
        try:
            if os.path.exists("emd_refund_simple.py"):
                # Get absolute path to be sure
                script_path = os.path.abspath("emd_refund_simple.py")
                logging.info(f"Launching EMD Refund from: {script_path}")
                
                # Try different approaches
                try:
                    # Method 1: Direct subprocess
                    process = subprocess.Popen([sys.executable, script_path])
                    logging.info(f"EMD Refund launched with PID: {process.pid}")
                except Exception as e1:
                    logging.error(f"Method 1 failed: {e1}")
                    try:
                        # Method 2: With shell=True
                        process = subprocess.Popen([sys.executable, script_path], shell=True)
                        logging.info(f"EMD Refund launched with shell=True, PID: {process.pid}")
                    except Exception as e2:
                        logging.error(f"Method 2 failed: {e2}")
                        raise
                
                self.update_status("EMD Refund tool opened successfully")
            else:
                error_msg = "EMD Refund tool file not found"
                logging.error(error_msg)
                messagebox.showerror("Error", error_msg)
        except Exception as e:
            error_msg = f"Could not open EMD Refund: {str(e)}"
            logging.error(error_msg + "\n" + traceback.format_exc())
            messagebox.showerror("Error", error_msg)
    
    def open_delay_calculator(self):
        """Open Delay Calculator tool"""
        try:
            if os.path.exists("delay_calculator_simple.py"):
                # Get absolute path to be sure
                script_path = os.path.abspath("delay_calculator_simple.py")
                logging.info(f"Launching Delay Calculator from: {script_path}")
                
                # Try different approaches
                try:
                    # Method 1: Direct subprocess
                    process = subprocess.Popen([sys.executable, script_path])
                    logging.info(f"Delay Calculator launched with PID: {process.pid}")
                except Exception as e1:
                    logging.error(f"Method 1 failed: {e1}")
                    try:
                        # Method 2: With shell=True
                        process = subprocess.Popen([sys.executable, script_path], shell=True)
                        logging.info(f"Delay Calculator launched with shell=True, PID: {process.pid}")
                    except Exception as e2:
                        logging.error(f"Method 2 failed: {e2}")
                        raise
                
                self.update_status("Delay Calculator tool opened successfully")
            else:
                error_msg = "Delay Calculator tool file not found"
                logging.error(error_msg)
                messagebox.showerror("Error", error_msg)
        except Exception as e:
            error_msg = f"Could not open Delay Calculator: {str(e)}"
            logging.error(error_msg + "\n" + traceback.format_exc())
            messagebox.showerror("Error", error_msg)
    
    def open_financial_analysis(self):
        """Open Financial Analysis tool"""
        try:
            if os.path.exists("financial_analysis_simple.py"):
                # Get absolute path to be sure
                script_path = os.path.abspath("financial_analysis_simple.py")
                logging.info(f"Launching Financial Analysis from: {script_path}")
                
                # Try different approaches
                try:
                    # Method 1: Direct subprocess
                    process = subprocess.Popen([sys.executable, script_path])
                    logging.info(f"Financial Analysis launched with PID: {process.pid}")
                except Exception as e1:
                    logging.error(f"Method 1 failed: {e1}")
                    try:
                        # Method 2: With shell=True
                        process = subprocess.Popen([sys.executable, script_path], shell=True)
                        logging.info(f"Financial Analysis launched with shell=True, PID: {process.pid}")
                    except Exception as e2:
                        logging.error(f"Method 2 failed: {e2}")
                        raise
                
                self.update_status("Financial Analysis tool opened successfully")
            else:
                error_msg = "Financial Analysis tool file not found"
                logging.error(error_msg)
                messagebox.showerror("Error", error_msg)
        except Exception as e:
            error_msg = f"Could not open Financial Analysis: {str(e)}"
            logging.error(error_msg + "\n" + traceback.format_exc())
            messagebox.showerror("Error", error_msg)
    
    def open_bill_generator(self):
        """Open Bill Generator in browser"""
        try:
            webbrowser.open("https://raj-bill-generator-v01.streamlit.app/")
            messagebox.showinfo("Success", "Opening Bill Generator in browser...")
            logging.info("Opened Bill Generator in browser")
            self.update_status("Bill Generator opened in browser")
        except Exception as e:
            error_msg = f"Could not open browser: {str(e)}"
            logging.error(error_msg + "\n" + traceback.format_exc())
            messagebox.showerror("Error", error_msg)
    
    def open_excel_emd(self):
        """Open Excel EMD Processor tool"""
        try:
            if os.path.exists("excel_emd_tool.py"):
                # Get absolute path to be sure
                script_path = os.path.abspath("excel_emd_tool.py")
                logging.info(f"Launching Excel EMD Processor from: {script_path}")
                
                # Try different approaches
                try:
                    # Method 1: Direct subprocess
                    process = subprocess.Popen([sys.executable, script_path])
                    logging.info(f"Excel EMD Processor launched with PID: {process.pid}")
                except Exception as e1:
                    logging.error(f"Method 1 failed: {e1}")
                    try:
                        # Method 2: With shell=True
                        process = subprocess.Popen([sys.executable, script_path], shell=True)
                        logging.info(f"Excel EMD Processor launched with shell=True, PID: {process.pid}")
                    except Exception as e2:
                        logging.error(f"Method 2 failed: {e2}")
                        raise
                
                self.update_status("Excel EMD Processor tool opened successfully")
            else:
                error_msg = "Excel EMD Processor tool file not found"
                logging.error(error_msg)
                messagebox.showerror("Error", error_msg)
        except Exception as e:
            error_msg = f"Could not open Excel EMD Processor: {str(e)}"
            logging.error(error_msg + "\n" + traceback.format_exc())
            messagebox.showerror("Error", error_msg)
    
    def open_deductions_table(self):
        """Open Deductions Table Calculator tool"""
        try:
            if os.path.exists("deductions_table_tool.py"):
                # Get absolute path to be sure
                script_path = os.path.abspath("deductions_table_tool.py")
                logging.info(f"Launching Deductions Table Calculator from: {script_path}")
                
                # Try different approaches
                try:
                    # Method 1: Direct subprocess
                    process = subprocess.Popen([sys.executable, script_path])
                    logging.info(f"Deductions Table Calculator launched with PID: {process.pid}")
                except Exception as e1:
                    logging.error(f"Method 1 failed: {e1}")
                    try:
                        # Method 2: With shell=True
                        process = subprocess.Popen([sys.executable, script_path], shell=True)
                        logging.info(f"Deductions Table Calculator launched with shell=True, PID: {process.pid}")
                    except Exception as e2:
                        logging.error(f"Method 2 failed: {e2}")
                        raise
                
                self.update_status("Deductions Table Calculator tool opened successfully")
            else:
                error_msg = "Deductions Table Calculator tool file not found"
                logging.error(error_msg)
                messagebox.showerror("Error", error_msg)
        except Exception as e:
            error_msg = f"Could not open Deductions Table Calculator: {str(e)}"
            logging.error(error_msg + "\n" + traceback.format_exc())
            messagebox.showerror("Error", error_msg)
    
    def open_tender_processing(self):
        """Open Tender Processing tool"""
        try:
            if os.path.exists("gui/tools/tender_processing.py"):
                # Get absolute path to be sure
                script_path = os.path.abspath("gui/tools/tender_processing.py")
                logging.info(f"Launching Tender Processing from: {script_path}")
                
                # Try different approaches
                try:
                    # Method 1: Direct subprocess
                    process = subprocess.Popen([sys.executable, script_path])
                    logging.info(f"Tender Processing launched with PID: {process.pid}")
                except Exception as e1:
                    logging.error(f"Method 1 failed: {e1}")
                    try:
                        # Method 2: With shell=True
                        process = subprocess.Popen([sys.executable, script_path], shell=True)
                        logging.info(f"Tender Processing launched with shell=True, PID: {process.pid}")
                    except Exception as e2:
                        logging.error(f"Method 2 failed: {e2}")
                        raise
                
                self.update_status("Tender Processing tool opened successfully")
            else:
                error_msg = "Tender Processing tool file not found"
                logging.error(error_msg)
                messagebox.showerror("Error", error_msg)
        except Exception as e:
            error_msg = f"Could not open Tender Processing: {str(e)}"
            logging.error(error_msg + "\n" + traceback.format_exc())
            messagebox.showerror("Error", error_msg)
    
    def open_security_refund(self):
        """Open Security Refund tool"""
        try:
            from security_refund_simple import open_security_refund_html
            open_security_refund_html()
            self.update_status("Security Refund tool opened successfully")
            logging.info("Security Refund tool opened successfully")
        except Exception as e:
            error_msg = f"Could not open Security Refund tool: {str(e)}"
            logging.error(error_msg + "\n" + traceback.format_exc())
            messagebox.showerror("Error", error_msg)
    
    def show_help(self):
        """Show help dialog"""
        help_text = """
PWD Tools - Help

1. Hindi Bill Note: Generate running and final bills in Hindi
2. Stamp Duty Calculator: Calculate stamp duty with predefined rates
3. EMD Refund: Simple EMD refund with minimal inputs
4. Delay Calculator: Calculate project delays
5. Financial Analysis: Advanced web-based financial analysis with liquidity damages calculator
6. Bill Generator Link: Open online bill generator
7. Excel EMD Processor: Process EMD data from Excel files
8. Deductions Calculator: Calculate tax and other deductions
9. Tender Processing: Manage and process tender documents
10. Security Refund: Process security deposit refunds

All tools are designed for lower divisional clerks with minimal complexity.

If a tool doesn't open, check that the corresponding .py file exists in the application directory.
        """
        messagebox.showinfo("Help", help_text)
        logging.info("Help dialog shown")
    
    def show_about(self):
        """Show about dialog"""
        about_text = """
PWD Tools Dashboard
Version 1.0.0

Designed for Lower Divisional Clerks
Simple, Efficient, and User-Friendly

Features:
- Hindi Bill Note Generation
- Stamp Duty Calculation
- EMD Refund Processing
- Delay Calculation
- Advanced Financial Analysis with Liquidity Damages
- Online Bill Generator Access
- Excel EMD Processing
- Deductions Calculation
- Tender Processing
- Security Refund Processing

All tools work offline and are optimized for ease of use.

Developed for Mrs. Premlata Jain, AAO, PWD Udaipur
        """
        messagebox.showinfo("About", about_text)
        logging.info("About dialog shown")
    
    def create_status_bar(self):
        """Create status bar"""
        self.status_frame = tk.Frame(self.root, bg="#1E6B4E", height=25)  # Match header/footer
        self.status_frame.pack(fill="x", side="bottom")
        self.status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(
            self.status_frame,
            text="Ready | PWD Tools Dashboard | " + datetime.now().strftime("%Y-%m-%d %H:%M"),
            font=("Arial", 9),
            fg="white",
            bg="#1E6B4E"
        )
        self.status_label.pack(side="left", padx=10, pady=5)
        
        # Update time every minute
        self.update_time()
    
    def update_time(self):
        """Update time in status bar"""
        try:
            self.status_label.config(text="Ready | PWD Tools Dashboard | " + datetime.now().strftime("%Y-%m-%d %H:%M"))
            self.root.after(60000, self.update_time)  # Update every minute
        except:
            pass  # Ignore errors when window is closed
    
    def update_status(self, message):
        """Update status message"""
        try:
            self.status_label.config(text=message + " | " + datetime.now().strftime("%Y-%m-%d %H:%M"))
        except:
            pass  # Ignore errors when window is closed
    
    def run(self):
        """Start the application"""
        self.root.mainloop()
        logging.info("PWD Tools application closed")

if __name__ == "__main__":
    app = PWDMainLanding()
    app.run()