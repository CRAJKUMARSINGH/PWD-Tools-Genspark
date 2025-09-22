"""
Main Window for PWD Tools Desktop Application
Provides the primary user interface and navigation
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime
from gui.tools.excel_emd import ExcelEMDTool
from gui.tools.bill_note import BillNoteTool
from gui.tools.emd_refund import EMDRefundTool
from gui.tools.deductions_table import DeductionsTableTool
from gui.tools.delay_calculator import DelayCalculatorTool
from gui.tools.security_refund import SecurityRefundTool
from gui.tools.financial_progress import FinancialProgressTool
from gui.tools.stamp_duty import StampDutyTool
from gui.tools.bill_deviation import BillDeviationTool
from gui.tools.tender_processing import TenderProcessingTool

class PWDToolsMainWindow:
    def __init__(self, db_manager, settings, root=None):
        """Initialize the main application window"""
        self.db_manager = db_manager
        self.settings = settings
        
        # Use provided root window or create new one
        if root is not None:
            self.root = root
        else:
            self.root = ctk.CTk()
        
        self.setup_window()
        self.create_interface()
        
        # Tool windows tracking
        self.open_tools = {}
    
    def setup_window(self):
        """Configure main window properties"""
        ui_settings = self.settings.get_ui_settings()
        
        self.root.title("PWD Tools Desktop - Infrastructure Management Suite")
        self.root.geometry(f"{ui_settings.get('window_width', 1200)}x{ui_settings.get('window_height', 800)}")
        self.root.minsize(1000, 700)
        
        # Set window icon (if available)
        try:
            self.root.iconbitmap("assets/icons/pwd_icon.ico")
        except:
            pass  # Icon file not found, continue without it
    
    def create_interface(self):
        """Create the main user interface"""
        # Header frame
        self.create_header()
        
        # Main content area
        self.create_main_content()
        
        # Status bar
        self.create_status_bar()
        
        # Menu bar
        self.create_menu_bar()
    
    def create_header(self):
        """Create application header with branding"""
        header_frame = ctk.CTkFrame(self.root, height=100, corner_radius=0)
        header_frame.pack(fill="x", padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        # Title
        title_label = ctk.CTkLabel(
            header_frame,
            text="PWD Tools Desktop",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="#1f538d"
        )
        title_label.pack(pady=(15, 5))
        
        # Subtitle
        dept_info = self.settings.get_department_info()
        subtitle_text = f"Infrastructure Management Suite | {dept_info.get('name', 'PWD')} - {dept_info.get('office', 'Udaipur')}"
        subtitle_label = ctk.CTkLabel(
            header_frame,
            text=subtitle_text,
            font=ctk.CTkFont(size=14),
            text_color="#666666"
        )
        subtitle_label.pack(pady=(0, 15))
    
    def create_main_content(self):
        """Create main content area with tool grid"""
        # Main container
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Welcome section
        welcome_frame = ctk.CTkFrame(main_frame, height=60)
        welcome_frame.pack(fill="x", padx=10, pady=(10, 5))
        welcome_frame.pack_propagate(False)
        
        welcome_label = ctk.CTkLabel(
            welcome_frame,
            text="🎯 Select a tool to begin working with PWD operations",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        welcome_label.pack(pady=15)
        
        # Tools grid
        self.create_tools_grid(main_frame)
    
    def create_tools_grid(self, parent):
        """Create grid of tool buttons"""
        # Tools configuration
        tools_config = [
            {
                "name": "Excel se EMD",
                "description": "Hand Receipt Generator from Excel files",
                "icon": "📊",
                "color": "#8B5CF6",
                "command": self.open_excel_emd
            },
            {
                "name": "Bill Note Sheet",
                "description": "Bill Note Sheet Generator for PWD documentation",
                "icon": "📝",
                "color": "#10B981",
                "command": self.open_bill_note
            },
            {
                "name": "EMD Refund",
                "description": "Generate EMD refund receipts and documentation",
                "icon": "💰",
                "color": "#F59E0B",
                "command": self.open_emd_refund
            },
            {
                "name": "Deductions Table",
                "description": "Calculate all standard deductions for bill amounts",
                "icon": "📊",
                "color": "#EF4444",
                "command": self.open_deductions_table
            },
            {
                "name": "Delay Calculator",
                "description": "Calculate project delays and timeline analysis",
                "icon": "⏰",
                "color": "#6366F1",
                "command": self.open_delay_calculator
            },
            {
                "name": "Security Refund",
                "description": "Process security deposit refund calculations",
                "icon": "🔒",
                "color": "#8B5CF6",
                "command": self.open_security_refund
            },
            {
                "name": "Financial Progress",
                "description": "Track financial progress and liquidity damages",
                "icon": "📈",
                "color": "#10B981",
                "command": self.open_financial_progress
            },
            {
                "name": "Stamp Duty",
                "description": "Calculate stamp duty for work orders",
                "icon": "📋",
                "color": "#F59E0B",
                "command": self.open_stamp_duty
            },
            {
                "name": "Bill & Deviation",
                "description": "Infrastructure Billing System with deviation tracking",
                "icon": "💰",
                "color": "#EF4444",
                "command": self.open_bill_deviation
            },
            {
                "name": "Tender Processing",
                "description": "Comprehensive tender management system",
                "icon": "📋",
                "color": "#6366F1",
                "command": self.open_tender_processing
            }
        ]
        
        # Create scrollable frame for tools
        tools_frame = ctk.CTkScrollableFrame(parent, label_text="Available Tools")
        tools_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Create tool buttons in grid (4 columns)
        columns = 4
        for i, tool in enumerate(tools_config):
            row = i // columns
            col = i % columns
            
            # Tool button frame
            tool_frame = ctk.CTkFrame(tools_frame, width=250, height=120)
            tool_frame.grid(row=row, column=col, padx=10, pady=10, sticky="ew")
            tool_frame.grid_propagate(False)
            
            # Icon and title
            icon_label = ctk.CTkLabel(
                tool_frame,
                text=tool["icon"],
                font=ctk.CTkFont(size=32)
            )
            icon_label.pack(pady=(10, 5))
            
            title_label = ctk.CTkLabel(
                tool_frame,
                text=tool["name"],
                font=ctk.CTkFont(size=14, weight="bold")
            )
            title_label.pack()
            
            # Description
            desc_label = ctk.CTkLabel(
                tool_frame,
                text=tool["description"],
                font=ctk.CTkFont(size=10),
                wraplength=220
            )
            desc_label.pack(pady=(2, 5))
            
            # Open button
            open_btn = ctk.CTkButton(
                tool_frame,
                text="Open",
                command=tool["command"],
                fg_color=tool["color"],
                hover_color=self.darken_color(tool["color"]),
                width=100,
                height=25
            )
            open_btn.pack(pady=(0, 10))
        
        # Configure grid weights
        for i in range(columns):
            tools_frame.grid_columnconfigure(i, weight=1)
    
    def darken_color(self, color):
        """Darken a hex color for hover effect"""
        # Simple darkening by reducing each RGB component
        if color.startswith('#'):
            color = color[1:]
        
        rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        darkened = tuple(max(0, int(c * 0.8)) for c in rgb)
        return f"#{darkened[0]:02x}{darkened[1]:02x}{darkened[2]:02x}"
    
    def create_status_bar(self):
        """Create status bar at bottom"""
        status_frame = ctk.CTkFrame(self.root, height=30, corner_radius=0)
        status_frame.pack(fill="x", side="bottom")
        status_frame.pack_propagate(False)
        
        # Status text
        self.status_label = ctk.CTkLabel(
            status_frame,
            text="Ready | PWD Tools Desktop v1.0.0 | All tools offline and independent",
            font=ctk.CTkFont(size=11)
        )
        self.status_label.pack(side="left", padx=10, pady=5)
        
        # Current time
        self.update_time()
    
    def update_time(self):
        """Update current time in status bar"""
        try:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            time_label = ctk.CTkLabel(
                self.status_label.master,
                text=current_time,
                font=ctk.CTkFont(size=11)
            )
            time_label.pack(side="right", padx=10, pady=5)
            
            # Schedule next update
            self.root.after(1000, self.update_time)
        except:
            # Window was destroyed, stop updating
            pass
    
    def create_menu_bar(self):
        """Create application menu bar"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Backup Database", command=self.backup_database)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # Tools menu
        tools_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_command(label="Excel se EMD", command=self.open_excel_emd)
        tools_menu.add_command(label="Bill Note Sheet", command=self.open_bill_note)
        tools_menu.add_command(label="EMD Refund", command=self.open_emd_refund)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
    
    # Tool opening methods
    def open_excel_emd(self):
        """Open Excel EMD tool"""
        if "excel_emd" not in self.open_tools:
            self.open_tools["excel_emd"] = ExcelEMDTool(self.db_manager, self.settings, self.root)
        else:
            self.open_tools["excel_emd"].focus()
    
    def open_bill_note(self):
        """Open Bill Note Sheet tool"""
        if "bill_note" not in self.open_tools:
            self.open_tools["bill_note"] = BillNoteTool(self.db_manager, self.settings, self.root)
        else:
            self.open_tools["bill_note"].focus()
    
    def open_emd_refund(self):
        """Open EMD Refund tool"""
        if "emd_refund" not in self.open_tools:
            self.open_tools["emd_refund"] = EMDRefundTool(self.db_manager, self.settings, self.root)
        else:
            self.open_tools["emd_refund"].focus()
    
    def open_deductions_table(self):
        """Open Deductions Table tool"""
        if "deductions_table" not in self.open_tools:
            self.open_tools["deductions_table"] = DeductionsTableTool(self.db_manager, self.settings, self.root)
        else:
            self.open_tools["deductions_table"].focus()
    
    def open_delay_calculator(self):
        """Open Delay Calculator tool"""
        if "delay_calculator" not in self.open_tools:
            self.open_tools["delay_calculator"] = DelayCalculatorTool(self.db_manager, self.settings, self.root)
        else:
            self.open_tools["delay_calculator"].focus()
    
    def open_security_refund(self):
        """Open Security Refund tool"""
        if "security_refund" not in self.open_tools:
            self.open_tools["security_refund"] = SecurityRefundTool(self.db_manager, self.settings, self.root)
        else:
            self.open_tools["security_refund"].focus()
    
    def open_financial_progress(self):
        """Open Financial Progress tool"""
        if "financial_progress" not in self.open_tools:
            self.open_tools["financial_progress"] = FinancialProgressTool(self.db_manager, self.settings, self.root)
        else:
            self.open_tools["financial_progress"].focus()
    
    def open_stamp_duty(self):
        """Open Stamp Duty tool"""
        if "stamp_duty" not in self.open_tools:
            self.open_tools["stamp_duty"] = StampDutyTool(self.db_manager, self.settings, self.root)
        else:
            self.open_tools["stamp_duty"].focus()
    
    def open_bill_deviation(self):
        """Open Bill & Deviation tool"""
        if "bill_deviation" not in self.open_tools:
            self.open_tools["bill_deviation"] = BillDeviationTool(self.db_manager, self.settings, self.root)
        else:
            self.open_tools["bill_deviation"].focus()
    
    def open_tender_processing(self):
        """Open Tender Processing tool"""
        if "tender_processing" not in self.open_tools:
            self.open_tools["tender_processing"] = TenderProcessingTool(self.db_manager, self.settings, self.root)
        else:
            self.open_tools["tender_processing"].focus()
    
    def backup_database(self):
        """Create database backup"""
        try:
            if self.db_manager.backup_database():
                messagebox.showinfo("Success", "Database backup created successfully!")
            else:
                messagebox.showerror("Error", "Failed to create database backup.")
        except Exception as e:
            messagebox.showerror("Error", f"Backup failed: {str(e)}")
    
    def show_about(self):
        """Show about dialog"""
        about_text = """PWD Tools Desktop v1.0.0

Infrastructure Management Suite
Standalone desktop application for PWD operations

Developed for:
Mrs. Premlata Jain, AAO
Public Works Department, Udaipur

Features:
• Complete offline functionality
• Zero web dependencies
• Local data storage
• PDF/Excel generation
• Comprehensive PWD tools

© 2024 PWD Tools Desktop"""
        
        messagebox.showinfo("About PWD Tools Desktop", about_text)
    
    def run(self):
        """Start the application main loop"""
        # Don't start mainloop here as it's already running in the main app
        pass
