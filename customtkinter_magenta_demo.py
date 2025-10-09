#!/usr/bin/env python3
"""
CustomTkinter Button Demo with Magenta Color Scheme
- Grid layout with 3 columns per row
- Specific colors and hover effects
- Magenta color used predominantly
"""

import customtkinter as ctk
from tkinter import messagebox
import sys
import os

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class MagentaButtonDemo:
    def __init__(self):
        # Set appearance mode and color theme
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")  # We'll override this with custom colors
        
        # Create main window
        self.root = ctk.CTk()
        self.root.title("CustomTkinter Magenta Button Demo")
        self.root.geometry("800x600")
        self.root.minsize(600, 400)
        
        # Center window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (800 // 2)
        y = (self.root.winfo_screenheight() // 2) - (600 // 2)
        self.root.geometry(f"800x600+{x}+{y}")
        
        self.create_interface()
    
    def create_interface(self):
        # Header
        header_frame = ctk.CTkFrame(self.root, height=80, fg_color="#c71585")  # Magenta
        header_frame.pack(fill="x", padx=10, pady=10)
        header_frame.pack_propagate(False)
        
        title_label = ctk.CTkLabel(
            header_frame,
            text="🎨 Magenta Button Demo",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="white"
        )
        title_label.pack(pady=20)
        
        # Main content
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Description
        desc_label = ctk.CTkLabel(
            main_frame,
            text="CustomTkinter buttons with magenta color scheme and hover effects",
            font=ctk.CTkFont(size=14)
        )
        desc_label.pack(pady=10)
        
        # Button grid container
        button_container = ctk.CTkFrame(main_frame)
        button_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Create button grid (3 columns per row)
        self.create_button_grid(button_container)
        
        # Status bar
        status_frame = ctk.CTkFrame(self.root, height=40, fg_color="#f8f9fa")
        status_frame.pack(fill="x", side="bottom")
        status_frame.pack_propagate(False)
        
        self.status_label = ctk.CTkLabel(
            status_frame,
            text="Ready",
            font=ctk.CTkFont(size=12),
            text_color="#666666"
        )
        self.status_label.pack(pady=10)
    
    def create_button_grid(self, parent):
        """Create a grid of buttons with 3 columns per row"""
        # Define button configurations with magenta variations
        button_configs = [
            {
                "text": "💾 Save Record",
                "fg_color": "#c71585",      # Magenta
                "hover_color": "#9b0e66",   # Darker magenta
                "command": lambda: self.button_clicked("Save Record")
            },
            {
                "text": "📄 Generate PDF",
                "fg_color": "#ff00ff",      # Bright magenta
                "hover_color": "#cc00cc",   # Darker bright magenta
                "command": lambda: self.button_clicked("Generate PDF")
            },
            {
                "text": "📧 Send Email",
                "fg_color": "#ff69b4",      # Hot pink
                "hover_color": "#ff1493",   # Deep pink
                "command": lambda: self.button_clicked("Send Email")
            },
            {
                "text": "🔍 Search Data",
                "fg_color": "#da70d6",      # Orchid
                "hover_color": "#ba55d3",   # Medium orchid
                "command": lambda: self.button_clicked("Search Data")
            },
            {
                "text": "📊 View Report",
                "fg_color": "#d8bfd8",      # Thistle
                "hover_color": "#dda0dd",   # Plum
                "command": lambda: self.button_clicked("View Report")
            },
            {
                "text": "⚙️ Settings",
                "fg_color": "#8b008b",      # Dark magenta
                "hover_color": "#800080",   # Purple
                "command": lambda: self.button_clicked("Settings")
            },
            {
                "text": "📤 Export Data",
                "fg_color": "#ff1493",      # Deep pink
                "hover_color": "#ff69b4",   # Hot pink
                "command": lambda: self.button_clicked("Export Data")
            },
            {
                "text": "📥 Import Data",
                "fg_color": "#c71585",      # Magenta
                "hover_color": "#8b008b",   # Dark magenta
                "command": lambda: self.button_clicked("Import Data")
            },
            {
                "text": "🗑️ Delete Record",
                "fg_color": "#ff00ff",      # Bright magenta
                "hover_color": "#8b008b",   # Dark magenta
                "command": lambda: self.button_clicked("Delete Record")
            }
        ]
        
        # Create grid with 3 columns per row
        row, col = 0, 0
        for i, config in enumerate(button_configs):
            # Create button with custom styling
            button = ctk.CTkButton(
                parent,
                text=config["text"],
                fg_color=config["fg_color"],
                hover_color=config["hover_color"],
                command=config["command"],
                width=180,
                height=45,
                font=ctk.CTkFont(size=14, weight="bold"),
                corner_radius=8,
                text_color="white"
            )
            
            # Position in grid (3 columns per row)
            button.grid(row=row, column=col, padx=15, pady=15, sticky="ew")
            
            # Update row/col counters
            col += 1
            if col >= 3:  # 3 columns per row
                col = 0
                row += 1
        
        # Configure grid weights for responsive layout
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
        parent.grid_columnconfigure(2, weight=1)
    
    def button_clicked(self, button_name):
        """Handle button click events"""
        self.status_label.configure(text=f"Clicked: {button_name}")
        messagebox.showinfo("Button Clicked", f"You clicked the '{button_name}' button!")
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

def main():
    """Main entry point"""
    try:
        app = MagentaButtonDemo()
        app.run()
    except Exception as e:
        messagebox.showerror("Application Error", f"Failed to start application:\n{str(e)}")

if __name__ == "__main__":
    main()