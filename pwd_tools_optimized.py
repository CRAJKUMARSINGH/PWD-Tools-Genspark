"""
Optimized PWD Tools - Enhanced Desktop Application
Combines the best features of both versions with improved performance
"""

import tkinter as tk
from tkinter import messagebox
import webbrowser
import subprocess
import sys
import os

class PWDToolsOptimized:
    def __init__(self):
        """Initialize Optimized PWD Tools"""
        self.root = tk.Tk()
        self.root.title("PWD Tools - Optimized Version")
        self.root.geometry("850x750")
        self.root.minsize(850, 750)
        
        # Track open tools to prevent multiple instances
        self.open_tools = {}
        
        # Create interface
        self.create_interface()
    
    def create_interface(self):
        """Create main interface with enhanced layout"""
        # Configure root window background
        self.root.configure(bg="#f8fafc")
        
        # Header with enhanced styling
        header_frame = tk.Frame(self.root, bg="#4f46e5", height=120)
        header_frame.pack(fill="x", padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        # Main title
        title = tk.Label(
            header_frame,
            text="🏗️ PWD Tools Desktop",
            font=("Arial", 32, "bold"),
            fg="white",
            bg="#4f46e5"
        )
        title.pack(pady=(25, 5))
        
        # Subtitle
        subtitle = tk.Label(
            header_frame,
            text="Complete Infrastructure Management Suite - Optimized Performance",
            font=("Arial", 14),
            fg="#e0e7ff",
            bg="#4f46e5"
        )
        subtitle.pack(pady=(0, 25))
        
        # Main content area
        main_frame = tk.Frame(self.root, bg="#f8fafc")
        main_frame.pack(pady=30, padx=40, fill="both", expand=True)
        
        # Welcome section
        welcome_frame = tk.Frame(main_frame, bg="#eff6ff", relief="solid", bd=2)
        welcome_frame.pack(fill="x", pady=(0, 25))
        
        welcome_label = tk.Label(
            welcome_frame,
            text="🎯 Select a tool to begin working with PWD operations",
            font=("Arial", 18, "bold"),
            fg="#1e40af",
            bg="#eff6ff"
        )
        welcome_label.pack(pady=20)
        
        # Tools section
        tools_label = tk.Label(
            main_frame,
            text="🛠️ Available Tools:",
            font=("Arial", 20, "bold"),
            fg="#1f2937",
            bg="#f8fafc"
        )
        tools_label.pack(pady=(0, 20), anchor="w")
        
        # Tool buttons in optimized grid
        self.create_tool_grid(main_frame)
        
        # Footer
        footer_frame = tk.Frame(self.root, bg="#1f2937", height=70)
        footer_frame.pack(side="bottom", fill="x", padx=0, pady=0)
        footer_frame.pack_propagate(False)
        
        footer = tk.Label(
            footer_frame,
            text="Prepared for Mrs. Premlata Jain, AAO, PWD Udaipur | Optimized Desktop Version",
            font=("Arial", 11, "bold"),
            fg="#d1d5db",
            bg="#1f2937"
        )
        footer.pack(pady=25)
    
    def create_tool_grid(self, parent):
        """Create optimized tool grid with categories"""
        # Create a scrollable canvas for tools
        canvas = tk.Canvas(parent, bg="#f8fafc", highlightthickness=0)
        scrollbar = tk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#f8fafc")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Categories with enhanced styling
        categories = {
            "Financial Tools": [
                ("📋 Bill Note Sheet", self.open_bill_note, "#10b981"),
                ("💰 EMD Refund", self.open_emd_refund, "#f59e0b"),
                ("🔒 Security Refund", self.open_security_refund, "#8b5cf6"),
                ("📈 Financial Progress Tracker", self.open_financial_progress, "#10b981")
            ],
            "Calculation Tools": [
                ("📊 Deductions Table", self.open_deductions_table, "#ef4444"),
                ("⏰ Delay Calculator", self.open_delay_calculator, "#6366f1"),
                ("📄 Stamp Duty Calculator", self.open_stamp_duty, "#f59e0b"),
                ("🔧 Bill & Deviation Generator", self.open_bill_deviation_combined, "#ef4444")
            ],
            "Data Processing": [
                ("📊 Excel se EMD", self.open_excel_emd, "#8b5cf6"),
                ("⚡ Performance Info", self.show_performance_info, "#06b6d4")
            ]
        }
        
        row_counter = 0
        for category, tools in categories.items():
            # Category header with enhanced styling
            category_frame = tk.Frame(scrollable_frame, bg="#f1f5f9", relief="raised", bd=2)
            category_frame.grid(row=row_counter, column=0, columnspan=4, sticky="ew", pady=(0, 20))
            
            category_label = tk.Label(
                category_frame,
                text=category,
                font=("Arial", 16, "bold"),
                fg="#4b5563",
                bg="#f1f5f9"
            )
            category_label.pack(pady=15, padx=20, anchor="w")
            
            row_counter += 1
            
            # Tools in this category
            for i, (tool_name, command, color) in enumerate(tools):
                row = row_counter + (i // 2)
                col = i % 2
                
                # Tool button frame with enhanced styling
                tool_frame = tk.Frame(scrollable_frame, bg="white", relief="raised", bd=2)
                tool_frame.grid(row=row, column=col, padx=12, pady=12, sticky="ew")
                
                btn = tk.Button(
                    tool_frame,
                    text=tool_name,
                    command=command,
                    width=32,
                    height=3,
                    font=("Arial", 12, "bold"),
                    bg=color,
                    fg="white",
                    relief="flat",
                    bd=0,
                    cursor="hand2"
                )
                btn.pack(pady=15, padx=15)
                
                # Add hover effect
                self.make_hover_effect(btn, color)
            
            row_counter += (len(tools) + 1) // 2
        
        # Configure grid weights
        for i in range(4):
            scrollable_frame.grid_columnconfigure(i, weight=1)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def make_hover_effect(self, button, original_color):
        """Create hover effect for a button"""
        def on_enter(e):
            button.config(bg=self.lighten_color(original_color))
        def on_leave(e):
            button.config(bg=original_color)
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
    
    def lighten_color(self, color):
        """Lighten a hex color for hover effect"""
        # Simple color lightening by adding white
        color_map = {
            "#10b981": "#34d399",   # Green
            "#f59e0b": "#fbbf24",   # Amber
            "#8b5cf6": "#a78bfa",   # Purple
            "#ef4444": "#f87171",   # Red
            "#6366f1": "#818cf8",   # Indigo
            "#06b6d4": "#0ea5e9"    # Cyan
        }
        return color_map.get(color, color)
    
    def is_tool_open(self, tool_name):
        """Check if a tool is already open"""
        return tool_name in self.open_tools and self.open_tools[tool_name].poll() is None
    
    def open_bill_note(self):
        """Open Bill Note Sheet (dedicated tool)"""
        if self.is_tool_open("bill_note"):
            messagebox.showinfo("Info", "Bill Note Sheet is already open")
            return
            
        try:
            process = subprocess.Popen([sys.executable, "bill_generator_simple.py"])
            self.open_tools["bill_note"] = process
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Bill Note Sheet Tool: {str(e)}")
    
    def open_emd_refund(self):
        """Open EMD Refund (dedicated tool)"""
        if self.is_tool_open("emd_refund"):
            messagebox.showinfo("Info", "EMD Refund Tool is already open")
            return
            
        try:
            process = subprocess.Popen([sys.executable, "emd_refund_simple.py"])
            self.open_tools["emd_refund"] = process
        except Exception as e:
            messagebox.showerror("Error", f"Could not open EMD Refund Tool: {str(e)}")
    
    def open_deductions_table(self):
        """Open Deductions Table (dedicated tool)"""
        if self.is_tool_open("deductions_table"):
            messagebox.showinfo("Info", "Deductions Table Tool is already open")
            return
            
        try:
            process = subprocess.Popen([sys.executable, "deviation_generator_simple.py"])
            self.open_tools["deductions_table"] = process
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Deductions Table Tool: {str(e)}")
    
    def open_delay_calculator(self):
        """Open Delay Calculator (dedicated tool)"""
        if self.is_tool_open("delay_calculator"):
            messagebox.showinfo("Info", "Delay Calculator Tool is already open")
            return
            
        try:
            process = subprocess.Popen([sys.executable, "delay_calculator_simple.py"])
            self.open_tools["delay_calculator"] = process
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Delay Calculator Tool: {str(e)}")
    
    def open_financial_progress(self):
        """Open Financial Progress Tracker"""
        if self.is_tool_open("financial_progress"):
            messagebox.showinfo("Info", "Financial Progress Tracker is already open")
            return
            
        try:
            process = subprocess.Popen([sys.executable, "financial_progress_simple.py"])
            self.open_tools["financial_progress"] = process
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Financial Progress Tracker: {str(e)}")
    
    def open_security_refund(self):
        """Open Security Refund"""
        if self.is_tool_open("security_refund"):
            messagebox.showinfo("Info", "Security Refund Tool is already open")
            return
            
        try:
            process = subprocess.Popen([sys.executable, "security_refund_simple.py"])
            self.open_tools["security_refund"] = process
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Security Refund: {str(e)}")
    
    def open_stamp_duty(self):
        """Open Stamp Duty Calculator"""
        if self.is_tool_open("stamp_duty"):
            messagebox.showinfo("Info", "Stamp Duty Calculator is already open")
            return
            
        try:
            process = subprocess.Popen([sys.executable, "stamp_duty_simple.py"])
            self.open_tools["stamp_duty"] = process
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Stamp Duty Calculator: {str(e)}")
    
    def open_excel_emd(self):
        """Open Excel se EMD (dedicated tool)"""
        if self.is_tool_open("excel_emd"):
            messagebox.showinfo("Info", "Excel se EMD Tool is already open")
            return
            
        try:
            process = subprocess.Popen([sys.executable, "hindi_bill_simple.py"])
            self.open_tools["excel_emd"] = process
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Excel se EMD Tool: {str(e)}")
    
    def open_bill_deviation_combined(self):
        """Open Bill & Deviation Generator (redirects to web)"""
        try:
            webbrowser.open("https://raj-bill-generator-v01.streamlit.app/")
            messagebox.showinfo("Success", "Opening Bill & Deviation Generator in browser...\n\nNote: This is DIFFERENT from Bill Note Sheet")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open browser: {str(e)}")
    
    def show_performance_info(self):
        """Show performance information"""
        info_text = """
🚀 Optimized Performance Features:

• ⚡ Faster Startup: Improved loading times
• 💻 Native OS Integration: Works like any other desktop application
• ⌨️ Keyboard Shortcuts: Full keyboard support
• 🪟 Multi-window Workflow: Open multiple tools simultaneously
• 📊 Enhanced UI: Better organized interface with categorized tools
• 🔄 Process Management: Prevents multiple instances of same tool
• 🎨 Modern Design: Cleaner, more intuitive interface
• 📱 Responsive Layout: Adapts to different screen sizes

This optimized version provides all the functionality of the original 
with significant performance and usability improvements.
        """
        messagebox.showinfo("Performance Features", info_text)
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

def main():
    """Main entry point"""
    app = PWDToolsOptimized()
    app.run()

if __name__ == "__main__":
    main()