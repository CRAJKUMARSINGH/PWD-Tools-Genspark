"""
Bill Note Sheet Tool - SEPARATE from Bill & Deviation
Dedicated tool for bill note sheet generation
"""

import tkinter as tk
from tkinter import messagebox
import webbrowser
import subprocess
import sys


class BillNoteSheetTool:
    def __init__(self):
        """Initialize Bill Note Sheet tool"""
        self.root = tk.Tk()
        self.root.title("Bill Note Sheet Generator")
        self.root.geometry("500x400")
        self.root.minsize(500, 400)
        
        # Create interface
        self.create_interface()
    
    def create_interface(self):
        """Create interface"""
        # Configure root window background
        self.root.configure(bg="#f0f4f8")
        
        # Header with gradient effect
        header_frame = tk.Frame(self.root, bg="#667eea", height=80)
        header_frame.pack(fill="x", padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        header = tk.Label(
            header_frame,
            text="Bill Note Sheet Generator",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#667eea"
        )
        header.pack(pady=20)
        
        # Main frame
        main_frame = tk.Frame(self.root, bg="#f0f4f8")
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Description
        desc_label = tk.Label(
            main_frame,
            text="📋 Generate Professional Bill Note Sheets",
            font=("Arial", 16, "bold"),
            fg="#2d3748",
            bg="#f0f4f8"
        )
        desc_label.pack(pady=(0, 20))
        
        # Features list
        features_text = """
🔧 Features:
• Professional bill formatting
• Multiple bill types support
• PDF generation capability
• Excel integration
• Custom templates
• Print-ready output
        """
        
        features_label = tk.Label(
            main_frame,
            text=features_text,
            font=("Arial", 12),
            fg="#4a5568",
            bg="#f0f4f8",
            justify="left"
        )
        features_label.pack(pady=10)
        
        # Buttons frame
        buttons_frame = tk.Frame(main_frame, bg="#f0f4f8")
        buttons_frame.pack(pady=20)
        
        # Open Web Tool button
        web_btn = tk.Button(
            buttons_frame,
            text="🌐 Open Bill Note Sheet Web Tool",
            command=self.open_web_tool,
            width=30,
            height=2,
            font=("Arial", 12, "bold"),
            bg="#4ecdc4",
            fg="white",
            relief="raised",
            bd=2,
            cursor="hand2"
        )
        web_btn.pack(pady=10)
        
        # Open Desktop Tool button
        desktop_btn = tk.Button(
            buttons_frame,
            text="💻 Open Desktop Bill Note Tool",
            command=self.open_desktop_tool,
            width=30,
            height=2,
            font=("Arial", 12, "bold"),
            bg="#96ceb4",
            fg="white",
            relief="raised",
            bd=2,
            cursor="hand2"
        )
        desktop_btn.pack(pady=10)
        
        # Info button
        info_btn = tk.Button(
            buttons_frame,
            text="ℹ️ About Bill Note Sheets",
            command=self.show_info,
            width=30,
            height=2,
            font=("Arial", 12, "bold"),
            bg="#feca57",
            fg="white",
            relief="raised",
            bd=2,
            cursor="hand2"
        )
        info_btn.pack(pady=10)
        
        # Footer
        footer_label = tk.Label(
            main_frame,
            text="Bill Note Sheet Generator - PWD Tools",
            font=("Arial", 10),
            fg="#718096",
            bg="#f0f4f8"
        )
        footer_label.pack(side="bottom", pady=10)
    
    def open_web_tool(self):
        """Open Bill Note Sheet web tool"""
        try:
            webbrowser.open("https://raj-bill-generator-v01.streamlit.app/")
            messagebox.showinfo("Success", "Opening Bill Note Sheet Web Tool in browser...")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open browser: {str(e)}")
    
    def open_desktop_tool(self):
        """Open desktop bill note tool"""
        try:
            # Try to open the GUI bill note tool
            subprocess.Popen([sys.executable, "gui/tools/bill_note.py"])
        except Exception as e:
            messagebox.showinfo("Info", "Desktop tool not available. Using web tool instead.")
            self.open_web_tool()
    
    def show_info(self):
        """Show information about bill note sheets"""
        info_text = """
📋 Bill Note Sheet Generator

Purpose:
Generate professional bill note sheets for PWD projects

Features:
• Multiple bill formats
• Professional templates
• PDF/Excel export
• Print-ready output
• Custom fields support

Usage:
1. Click "Open Web Tool" for full features
2. Select bill type and template
3. Enter project details
4. Generate and download

This tool is SEPARATE from Bill & Deviation Generator
        """
        messagebox.showinfo("Bill Note Sheet Information", info_text)
    
    def run(self):
        """Start the application"""
        self.root.mainloop()


def main():
    """Main entry point"""
    try:
        app = BillNoteSheetTool()
        app.run()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start Bill Note Sheet Tool: {str(e)}")


if __name__ == "__main__":
    main()
