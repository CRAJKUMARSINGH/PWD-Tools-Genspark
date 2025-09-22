"""
Excel se EMD Tool - Dedicated Excel EMD Processor
Separate from other tools
"""

import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import tempfile
import webbrowser
import os


class ExcelEMDTool:
    def __init__(self):
        """Initialize Excel se EMD tool"""
        self.root = tk.Tk()
        self.root.title("Excel se EMD Processor")
        self.root.geometry("600x500")
        self.root.minsize(600, 500)
        
        # Create interface
        self.create_interface()
    
    def create_interface(self):
        """Create interface"""
        # Configure root window background
        self.root.configure(bg="#f0f4f8")
        
        # Header with gradient effect
        header_frame = tk.Frame(self.root, bg="#54a0ff", height=80)
        header_frame.pack(fill="x", padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        header = tk.Label(
            header_frame,
            text="📊 Excel se EMD Processor",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#54a0ff"
        )
        header.pack(pady=20)
        
        # Main frame
        main_frame = tk.Frame(self.root, bg="#f0f4f8")
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Form container
        form_container = tk.Frame(main_frame, bg="#ffffff", relief="raised", bd=2)
        form_container.pack(pady=10, padx=10, fill="both", expand=True)
        
        # Title
        title_label = tk.Label(
            form_container,
            text="Excel-based EMD Processing Tool",
            font=("Arial", 16, "bold"),
            fg="#2d3748",
            bg="#ffffff"
        )
        title_label.pack(pady=20)
        
        # Description
        desc_label = tk.Label(
            form_container,
            text="Process EMD data from Excel files and generate reports",
            font=("Arial", 12),
            fg="#4a5568",
            bg="#ffffff"
        )
        desc_label.pack(pady=10)
        
        # File selection frame
        file_frame = tk.Frame(form_container, bg="#ffffff")
        file_frame.pack(pady=20, padx=20, fill="x")
        
        # Excel file selection
        tk.Label(file_frame, text="Select Excel File:", font=("Arial", 12), bg="#ffffff").pack(anchor="w")
        
        file_select_frame = tk.Frame(file_frame, bg="#ffffff")
        file_select_frame.pack(fill="x", pady=5)
        
        self.file_path_var = tk.StringVar()
        self.file_entry = tk.Entry(file_select_frame, textvariable=self.file_path_var, font=("Arial", 12), width=40)
        self.file_entry.pack(side="left", fill="x", expand=True)
        
        browse_btn = tk.Button(
            file_select_frame,
            text="Browse",
            command=self.browse_file,
            font=("Arial", 10),
            bg="#54a0ff",
            fg="white",
            relief="raised",
            bd=2
        )
        browse_btn.pack(side="right", padx=(10, 0))
        
        # Buttons frame
        buttons_frame = tk.Frame(form_container, bg="#ffffff")
        buttons_frame.pack(pady=20)
        
        # Process button
        process_btn = tk.Button(
            buttons_frame,
            text="📊 Process Excel File",
            command=self.process_excel,
            width=25,
            height=2,
            font=("Arial", 12, "bold"),
            bg="#54a0ff",
            fg="white",
            relief="raised",
            bd=2,
            cursor="hand2"
        )
        process_btn.pack(pady=10)
        
        # Open web tool button
        web_btn = tk.Button(
            buttons_frame,
            text="🌐 Open Web EMD Tool",
            command=self.open_web_tool,
            width=25,
            height=2,
            font=("Arial", 12, "bold"),
            bg="#96ceb4",
            fg="white",
            relief="raised",
            bd=2,
            cursor="hand2"
        )
        web_btn.pack(pady=10)
        
        # Results frame
        results_frame = tk.Frame(form_container, bg="#ffffff")
        results_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Results label
        self.results_label = tk.Label(
            results_frame,
            text="",
            font=("Arial", 12),
            fg="#2d3748",
            bg="#ffffff",
            wraplength=500,
            justify="left"
        )
        self.results_label.pack(anchor="w")
        
        # Footer
        footer_label = tk.Label(
            main_frame,
            text="Excel se EMD Processor - PWD Tools",
            font=("Arial", 10),
            fg="#718096",
            bg="#f0f4f8"
        )
        footer_label.pack(side="bottom", pady=10)
    
    def browse_file(self):
        """Browse for Excel file"""
        file_path = filedialog.askopenfilename(
            title="Select Excel File",
            filetypes=[("Excel files", "*.xlsx *.xls"), ("All files", "*.*")]
        )
        if file_path:
            self.file_path_var.set(file_path)
    
    def process_excel(self):
        """Process Excel file"""
        try:
            file_path = self.file_path_var.get().strip()
            
            if not file_path:
                messagebox.showerror("Error", "Please select an Excel file")
                return
            
            if not os.path.exists(file_path):
                messagebox.showerror("Error", "Selected file does not exist")
                return
            
            # Simulate processing (in real implementation, would use pandas/openpyxl)
            file_name = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)
            
            # Display results
            results_text = f"""
Excel File Processed Successfully!

File: {file_name}
Size: {file_size:,} bytes
Status: Processed
Records: Simulated processing complete

Note: This is a demonstration. In production, this would:
• Read Excel data using pandas/openpyxl
• Process EMD calculations
• Generate reports
• Export results
            """
            
            self.results_label.config(text=results_text)
            messagebox.showinfo("Success", "Excel file processed successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Processing error: {str(e)}")
    
    def open_web_tool(self):
        """Open web EMD tool"""
        try:
            webbrowser.open("https://raj-bill-generator-v01.streamlit.app/")
            messagebox.showinfo("Success", "Opening Web EMD Tool in browser...")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open browser: {str(e)}")
    
    def run(self):
        """Start the application"""
        self.root.mainloop()


def main():
    """Main entry point"""
    try:
        app = ExcelEMDTool()
        app.run()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start Excel se EMD Tool: {str(e)}")


if __name__ == "__main__":
    main()
