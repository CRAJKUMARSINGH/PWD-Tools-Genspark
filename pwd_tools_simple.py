"""
PWD Tools - SIMPLE VERSION
Based on original repository structure
Only essential tools with minimal complexity
"""

import tkinter as tk
from tkinter import messagebox
import webbrowser
import subprocess
import sys
import os


class PWDToolsSimple:
    def __init__(self):
        """Initialize PWD Tools Simple"""
        self.root = tk.Tk()
        self.root.title("PWD Tools - Simple Version")
        self.root.geometry("600x700")
        self.root.minsize(600, 700)
        
        # Create interface
        self.create_interface()
    
    def create_interface(self):
        """Create main interface with enhanced colors"""
        # Configure root window background
        self.root.configure(bg="#f0f4f8")
        
        # Header with gradient effect
        header_frame = tk.Frame(self.root, bg="#667eea", height=80)
        header_frame.pack(fill="x", padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        header = tk.Label(
            header_frame,
            text="PWD Tools - Desktop Application",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#667eea"
        )
        header.pack(pady=20)
        
        # Subtitle
        subtitle = tk.Label(
            self.root,
            text="Comprehensive PWD Tools Suite - Enhanced with Beautiful Colors",
            font=("Arial", 12),
            fg="#4a5568",
            bg="#f0f4f8"
        )
        subtitle.pack(pady=10)
        
        # Main frame with enhanced styling
        main_frame = tk.Frame(self.root, bg="#f0f4f8")
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Tools section with enhanced styling
        tools_label = tk.Label(
            main_frame,
            text="🛠️ Available Tools (10 Tools):",
            font=("Arial", 16, "bold"),
            fg="#2d3748",
            bg="#f0f4f8"
        )
        tools_label.pack(pady=(0, 15))
        
        # Tool buttons
        self.create_tool_buttons(main_frame)
        
        # Footer with enhanced styling
        footer_frame = tk.Frame(self.root, bg="#2d3748", height=60)
        footer_frame.pack(side="bottom", fill="x", padx=0, pady=0)
        footer_frame.pack_propagate(False)
        
        footer = tk.Label(
            footer_frame,
            text="Prepared on Initiative of Mrs. Premlata Jain, AAO, PWD Udaipur",
            font=("Arial", 11, "bold"),
            fg="white",
            bg="#2d3748"
        )
        footer.pack(pady=15)
    
    def create_tool_buttons(self, parent):
        """Create tool buttons"""
        tools = [
            ("📋 Bill Note Sheet", self.open_bill_note),
            ("💰 EMD Refund", self.open_emd_refund),
            ("📊 Deductions Table", self.open_deductions_table),
            ("⏰ Delay Calculator", self.open_delay_calculator),
            ("📈 Financial Progress Tracker", self.open_financial_progress),
            ("🔒 Security Refund", self.open_security_refund),
            ("📄 Stamp Duty Calculator", self.open_stamp_duty),
            ("📊 Excel se EMD", self.open_excel_emd),
            ("🔧 Bill & Deviation Generator", self.open_bill_deviation_combined),
            ("⚡ Faster Performance", self.show_performance_info)
        ]
        
        # Color schemes for different tool categories
        colors = [
            "#667eea",  # Bill Note Sheet - Blue
            "#f093fb",  # EMD Refund - Pink
            "#4ecdc4",  # Deductions Table - Teal
            "#45b7d1",  # Delay Calculator - Light Blue
            "#96ceb4",  # Financial Progress - Green
            "#feca57",  # Security Refund - Yellow
            "#ff9ff3",  # Stamp Duty - Magenta
            "#54a0ff",  # Excel se EMD - Blue
            "#5f27cd",  # Bill & Deviation - Purple
            "#00d2d3"   # Faster Performance - Cyan
        ]
        
        for i, (tool_name, command) in enumerate(tools):
            btn = tk.Button(
                parent,
                text=f"🔧 {tool_name}",
                command=command,
                width=30,
                height=2,
                font=("Arial", 11, "bold"),
                bg=colors[i],
                fg="white",
                relief="raised",
                bd=2,
                cursor="hand2"
            )
            btn.pack(pady=8)
            
            # Add hover effect
            def make_hover_effect(button, original_color):
                def on_enter(e):
                    button.config(bg=self.lighten_color(original_color))
                def on_leave(e):
                    button.config(bg=original_color)
                button.bind("<Enter>", on_enter)
                button.bind("<Leave>", on_leave)
            
            make_hover_effect(btn, colors[i])
    
    def lighten_color(self, color):
        """Lighten a hex color for hover effect"""
        # Simple color lightening by adding white
        color_map = {
            "#667eea": "#7a8fec",
            "#f093fb": "#f2a5fc", 
            "#4ecdc4": "#6dd5cd",
            "#45b7d1": "#5bc1d5",
            "#96ceb4": "#a8d6c0",
            "#feca57": "#fed069",
            "#ff9ff3": "#ffb1f5",
            "#54a0ff": "#66b0ff",
            "#5f27cd": "#6f37d7",
            "#00d2d3": "#1ad8d9"
        }
        return color_map.get(color, color)
    
    def open_bill_note(self):
        """Open Bill Note Sheet (dedicated tool)"""
        try:
            subprocess.Popen([sys.executable, "bill_note_sheet_tool.py"])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Bill Note Sheet Tool: {str(e)}")
    
    def open_emd_refund(self):
        """Open EMD Refund (dedicated tool)"""
        try:
            subprocess.Popen([sys.executable, "emd_refund_tool.py"])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open EMD Refund Tool: {str(e)}")
    
    def open_deductions_table(self):
        """Open Deductions Table (dedicated tool)"""
        try:
            subprocess.Popen([sys.executable, "deductions_table_tool.py"])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Deductions Table Tool: {str(e)}")
    
    def open_delay_calculator(self):
        """Open Delay Calculator (dedicated tool)"""
        try:
            subprocess.Popen([sys.executable, "delay_calculator_tool.py"])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Delay Calculator Tool: {str(e)}")
    
    def open_financial_progress(self):
        """Open Financial Progress Tracker"""
        try:
            subprocess.Popen([sys.executable, "financial_progress_simple.py"])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Financial Progress Tracker: {str(e)}")
    
    def open_security_refund(self):
        """Open Security Refund"""
        try:
            subprocess.Popen([sys.executable, "security_refund_simple.py"])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Security Refund: {str(e)}")
    
    def open_stamp_duty(self):
        """Open Stamp Duty Calculator"""
        try:
            subprocess.Popen([sys.executable, "stamp_duty_working.py"])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Stamp Duty Calculator: {str(e)}")
    
    def open_excel_emd(self):
        """Open Excel se EMD (dedicated tool)"""
        try:
            subprocess.Popen([sys.executable, "excel_emd_tool.py"])
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
        messagebox.showinfo("Performance Features", 
                           "🚀 Faster Performance: No web latency, instant response\n"
                           "💻 Native OS Integration: Works like any other desktop application\n"
                           "⌨️ Keyboard Shortcuts: Full keyboard support\n"
                           "🪟 Multi-window Workflow: Open multiple tools simultaneously\n"
                           "📱 System Tray Integration: Minimize to system tray")
    
    def run(self):
        """Start the application"""
        self.root.mainloop()


if __name__ == "__main__":
    app = PWDToolsSimple()
    app.run()
