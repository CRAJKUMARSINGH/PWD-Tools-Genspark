"""
PWD Tools - Colorful Main Landing Page
For Lower Divisional Clerks - Beautiful and Simple
"""

import tkinter as tk
from tkinter import messagebox
import webbrowser
import os
import sys

class PWDMainLanding:
    def __init__(self):
        """Initialize colorful main landing page"""
        self.root = tk.Tk()
        self.root.title("PWD Tools - Main Dashboard")
        self.root.geometry("1000x700")
        self.root.configure(bg="#f0f8ff")
        
        # Make window resizable
        self.root.minsize(800, 600)
        
        # Create colorful interface
        self.create_interface()
    
    def create_interface(self):
        """Create colorful main interface"""
        # Header with gradient effect
        header_frame = tk.Frame(self.root, bg="#2E8B57", height=80)
        header_frame.pack(fill="x", padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        # Main title
        title_label = tk.Label(
            header_frame,
            text="🏗️ PWD Tools Dashboard",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#2E8B57"
        )
        title_label.pack(pady=20)
        
        # Subtitle
        subtitle_label = tk.Label(
            header_frame,
            text="Infrastructure Management Suite for Lower Divisional Clerks",
            font=("Arial", 12),
            fg="#E0FFFF",
            bg="#2E8B57"
        )
        subtitle_label.pack(pady=5)
        
        # Main content area
        main_frame = tk.Frame(self.root, bg="#f0f8ff")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Welcome message
        welcome_frame = tk.Frame(main_frame, bg="#E6F3FF", relief="raised", bd=2)
        welcome_frame.pack(fill="x", pady=(0, 20))
        
        welcome_label = tk.Label(
            welcome_frame,
            text="🎉 Welcome to PWD Tools - Simple & Efficient!",
            font=("Arial", 16, "bold"),
            fg="#2E8B57",
            bg="#E6F3FF"
        )
        welcome_label.pack(pady=15)
        
        # Tools grid
        self.create_tools_grid(main_frame)
        
        # Footer
        self.create_footer(main_frame)
    
    def create_tools_grid(self, parent):
        """Create colorful tools grid"""
        tools_frame = tk.Frame(parent, bg="#f0f8ff")
        tools_frame.pack(fill="both", expand=True, pady=10)
        
        # Tool buttons with colors
        tools = [
            {
                "name": "Hindi Bill Note",
                "description": "Generate Running & Final Bills in Hindi",
                "color": "#FF6B6B",
                "command": self.open_hindi_bill,
                "icon": "📝"
            },
            {
                "name": "Stamp Duty Calculator",
                "description": "Calculate stamp duty with predefined rates",
                "color": "#4ECDC4",
                "command": self.open_stamp_duty,
                "icon": "💰"
            },
            {
                "name": "EMD Refund",
                "description": "Simple EMD refund with 3 inputs only",
                "color": "#45B7D1",
                "command": self.open_emd_refund,
                "icon": "💳"
            },
            {
                "name": "Delay Calculator",
                "description": "Calculate project delays easily",
                "color": "#96CEB4",
                "command": self.open_delay_calculator,
                "icon": "⏰"
            },
            {
                "name": "Financial Analysis",
                "description": "Simple financial analysis with calendar",
                "color": "#FFEAA7",
                "command": self.open_financial_analysis,
                "icon": "📊"
            },
            {
                "name": "Bill Generator Link",
                "description": "Open online bill generator",
                "color": "#DDA0DD",
                "command": self.open_bill_generator,
                "icon": "🌐"
            }
        ]
        
        # Create grid of tool buttons
        for i, tool in enumerate(tools):
            row = i // 2
            col = i % 2
            
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
        footer_frame = tk.Frame(parent, bg="#2E8B57", height=60)
        footer_frame.pack(fill="x", pady=(20, 0))
        footer_frame.pack_propagate(False)
        
        # Footer content
        footer_content = tk.Frame(footer_frame, bg="#2E8B57")
        footer_content.pack(expand=True)
        
        # Left side - Version info
        version_label = tk.Label(
            footer_content,
            text="Version 1.0.0 | Simple & Efficient",
            font=("Arial", 10),
            fg="white",
            bg="#2E8B57"
        )
        version_label.pack(side="left", padx=20, pady=20)
        
        # Right side - Quick actions
        quick_frame = tk.Frame(footer_content, bg="#2E8B57")
        quick_frame.pack(side="right", padx=20, pady=20)
        
        help_btn = tk.Button(
            quick_frame,
            text="Help",
            command=self.show_help,
            width=8,
            height=1,
            font=("Arial", 9),
            bg="#4CAF50",
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
            bg="#2196F3",
            fg="white",
            relief="flat"
        )
        about_btn.pack(side="left", padx=5)
    
    def open_hindi_bill(self):
        """Open Hindi Bill Note tool"""
        try:
            os.system("python hindi_bill_simple.py")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Hindi Bill Note: {e}")
    
    def open_stamp_duty(self):
        """Open Stamp Duty tool"""
        try:
            os.system("python stamp_duty_simple.py")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Stamp Duty Calculator: {e}")
    
    def open_emd_refund(self):
        """Open EMD Refund tool"""
        try:
            os.system("python simple_app.py")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open EMD Refund: {e}")
    
    def open_delay_calculator(self):
        """Open Delay Calculator tool"""
        try:
            os.system("python simple_app.py")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Delay Calculator: {e}")
    
    def open_financial_analysis(self):
        """Open Financial Analysis tool"""
        try:
            os.system("python simple_app.py")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Financial Analysis: {e}")
    
    def open_bill_generator(self):
        """Open Bill Generator in browser"""
        try:
            webbrowser.open("https://raj-bill-generator-v01.streamlit.app/")
            messagebox.showinfo("Success", "Opening Bill Generator in browser...")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open browser: {e}")
    
    def show_help(self):
        """Show help dialog"""
        help_text = """
PWD Tools - Help

1. Hindi Bill Note: Generate running and final bills in Hindi
2. Stamp Duty Calculator: Calculate stamp duty with predefined rates
3. EMD Refund: Simple EMD refund with minimal inputs
4. Delay Calculator: Calculate project delays
5. Financial Analysis: Simple financial analysis
6. Bill Generator Link: Open online bill generator

All tools are designed for lower divisional clerks with minimal complexity.
        """
        messagebox.showinfo("Help", help_text)
    
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
- Financial Analysis
- Online Bill Generator Access

All tools work offline and are optimized for ease of use.
        """
        messagebox.showinfo("About", about_text)
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = PWDMainLanding()
    app.run()
