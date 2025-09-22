"""
Bill & Deviation Generator - COMBINED TOOL
Single unit for both bill generation and deviation tracking
Redirects to web application at https://raj-bill-generator-v01.streamlit.app/
"""

import webbrowser
import tkinter as tk
from tkinter import messagebox


class BillDeviationCombinedTool:
    def __init__(self):
        """Initialize Bill & Deviation Combined tool"""
        self.root = tk.Tk()
        self.root.title("Bill & Deviation Generator")
        self.root.geometry("500x300")
        self.root.minsize(500, 300)
        
        # Create interface
        self.create_interface()
    
    def create_interface(self):
        """Create interface"""
        # Header
        header = tk.Label(
            self.root,
            text="Bill & Deviation Generator",
            font=("Arial", 20, "bold"),
            fg="blue"
        )
        header.pack(pady=20)
        
        # Main frame
        main_frame = tk.Frame(self.root)
        main_frame.pack(pady=20)
        
        # Info label
        info_label = tk.Label(
            main_frame,
            text="Combined Bill Generation & Deviation Tracking",
            font=("Arial", 12),
            fg="green"
        )
        info_label.pack(pady=10)
        
        # Description
        desc_label = tk.Label(
            main_frame,
            text="This tool handles both:\n• Bill Generation\n• Deviation Tracking\n• Infrastructure Billing",
            font=("Arial", 11),
            justify="center"
        )
        desc_label.pack(pady=10)
        
        # Redirect button
        redirect_btn = tk.Button(
            main_frame, 
            text="Open Bill & Deviation Generator Online", 
            command=self.open_web_app,
            width=30, 
            height=2, 
            font=("Arial", 12, "bold"), 
            bg="lightblue"
        )
        redirect_btn.pack(pady=20)
        
        # URL label
        url_label = tk.Label(
            main_frame,
            text="https://raj-bill-generator-v01.streamlit.app/",
            font=("Arial", 10),
            fg="blue",
            cursor="hand2"
        )
        url_label.pack(pady=5)
        url_label.bind("<Button-1>", lambda e: self.open_web_app())
    
    def open_web_app(self):
        """Open the web application"""
        try:
            webbrowser.open("https://raj-bill-generator-v01.streamlit.app/")
            messagebox.showinfo("Success", "Opening Bill & Deviation Generator in browser...")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open browser: {str(e)}")
    
    def run(self):
        """Start the application"""
        self.root.mainloop()


if __name__ == "__main__":
    app = BillDeviationCombinedTool()
    app.run()
