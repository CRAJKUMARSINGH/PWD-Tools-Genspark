"""
Financial Analysis Tool - WEB VERSION
For Lower Divisional Clerks - With Calendar
Launches the advanced HTML/JavaScript financial analysis tool
"""

import tkinter as tk
from tkinter import messagebox
import webbrowser
import os

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
            self.root.geometry(f"{min(screen_width-20, 400)}x{min(screen_height-50, 300)}")
        else:  # Desktop
            self.root.geometry("500x200")
        
        # Make window resizable
        self.root.minsize(400, 200)
        
        # Create interface
        self.create_interface()
    
    def create_interface(self):
        """Create interface"""
        # Configure root window background
        self.root.configure(bg="#f0f8ff")
        
        # Header with gradient effect
        header_frame = tk.Frame(self.root, bg="#4ECDC4", height=80)
        header_frame.pack(fill="x", padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        header = tk.Label(
            header_frame,
            text="💰 Financial Analysis - सरल",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#4ECDC4"
        )
        header.pack(pady=20)
        
        # Main frame with colored background
        main_frame = tk.Frame(self.root, bg="#f0f8ff")
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Form container with border and shadow effect
        form_container = tk.Frame(main_frame, bg="#ffffff", relief="raised", bd=2)
        form_container.pack(pady=10, padx=10, fill="both", expand=True)
        
        # Title
        title_label = tk.Label(
            form_container,
            text="Advanced Financial Analysis Tool",
            font=("Arial", 16, "bold"),
            fg="#4ECDC4",
            bg="#ffffff"
        )
        title_label.pack(pady=20)
        
        # Description
        desc_label = tk.Label(
            form_container,
            text="Launch the advanced web-based financial analysis tool with liquidity damages calculator",
            font=("Arial", 12),
            fg="#2E8B57",
            bg="#ffffff",
            wraplength=400
        )
        desc_label.pack(pady=10)
        
        # Launch button with improved styling
        launch_btn = tk.Button(form_container, text="Launch Financial Analysis Tool", command=self.launch_web_tool, 
                           width=30, height=2, font=("Arial", 12, "bold"), 
                           bg="#4ECDC4", fg="white", relief="raised", bd=2)
        launch_btn.pack(pady=20)
        
        # Footer
        footer_frame = tk.Frame(main_frame, bg="#2E8B57", height=40)
        footer_frame.pack(fill="x", pady=(10, 0))
        footer_frame.pack_propagate(False)
        
        footer_label = tk.Label(
            footer_frame,
            text="Financial Analysis - PWD Tools | Designed for Lower Divisional Clerks",
            font=("Arial", 9),
            fg="white",
            bg="#2E8B57"
        )
        footer_label.pack(pady=10)
    
    def launch_web_tool(self):
        """Launch the web-based financial analysis tool"""
        try:
            # Get the absolute path to the HTML file
            html_file_path = os.path.abspath("financial_analysis_web.html")
            
            # Check if the file exists
            if os.path.exists(html_file_path):
                # Open the HTML file in the default web browser
                webbrowser.open(f"file://{html_file_path}")
                messagebox.showinfo("Success", "Financial Analysis Tool launched in your web browser!")
            else:
                # Fallback to online version if local file not found
                messagebox.showerror("Error", "Local HTML file not found. Please ensure financial_analysis_web.html exists in the application directory.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch Financial Analysis Tool: {str(e)}")
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = SimpleFinancialAnalysisTool()
    app.run()
