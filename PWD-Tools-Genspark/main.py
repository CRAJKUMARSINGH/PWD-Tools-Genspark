"""
PWD Tools Desktop - Main Application Launcher
Inspired by the brilliant layouts from genspark.html
Complete standalone solution with zero web dependencies
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import os
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from config.database import DatabaseManager
from config.settings import AppSettings
from gui.main_window import PWDToolsMainWindow

class PWDToolsApp:
    def __init__(self):
        """Initialize the PWD Tools Desktop Application"""
        # Set appearance mode and color theme
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
        # Initialize settings and database
        self.settings = AppSettings()
        self.db_manager = DatabaseManager()
        
        # Create and configure main window
        self.root = ctk.CTk()
        self.setup_main_window()
        
        # Create splash screen
        self.create_splash_screen()
        
        # Initialize main application after splash
        self.root.after(2000, self.initialize_main_app)
    
    def setup_main_window(self):
        """Configure main window properties"""
        self.root.title("PWD Tools Desktop - Infrastructure Management Suite")
        self.root.geometry("1400x900")
        self.root.minsize(1200, 800)
        
        # Center window on screen
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (self.root.winfo_width() // 2)
        y = (self.root.winfo_screenheight() // 2) - (self.root.winfo_height() // 2)
        self.root.geometry(f"+{x}+{y}")
        
        # Set window icon (if available)
        try:
            self.root.iconbitmap("assets/icons/pwd_icon.ico")
        except:
            pass  # Icon file not found, continue without it
    
    def create_splash_screen(self):
        """Create beautiful splash screen inspired by genspark.html design"""
        # Main splash frame
        splash_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        splash_frame.pack(fill="both", expand=True)
        
        # Header section with purple gradient effect
        header_frame = ctk.CTkFrame(splash_frame, height=120, fg_color="#8B5CF6")
        header_frame.pack(fill="x", padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        # Title with icon
        title_label = ctk.CTkLabel(
            header_frame,
            text="🏗️ PWD Tools Desktop",
            font=ctk.CTkFont(size=32, weight="bold"),
            text_color="white"
        )
        title_label.pack(pady=(20, 5))
        
        # Subtitle
        subtitle_label = ctk.CTkLabel(
            header_frame,
            text="Complete Standalone Solution | Zero Web Dependencies",
            font=ctk.CTkFont(size=14),
            text_color="#E0E7FF"
        )
        subtitle_label.pack(pady=(0, 20))
        
        # Main content area
        content_frame = ctk.CTkFrame(splash_frame, fg_color="transparent")
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Executive summary section
        summary_frame = ctk.CTkFrame(content_frame, fg_color="#EBF8FF", border_color="#3B82F6", border_width=2)
        summary_frame.pack(fill="x", pady=(0, 20))
        
        summary_title = ctk.CTkLabel(
            summary_frame,
            text="💡 Executive Summary",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="#1E40AF"
        )
        summary_title.pack(pady=(15, 10))
        
        summary_text = ctk.CTkLabel(
            summary_frame,
            text="Transform your web-dependent PWD Tools into a fully standalone desktop application.\nEliminate hosting dependencies while maintaining complete functionality offline.",
            font=ctk.CTkFont(size=12),
            text_color="#1E40AF",
            wraplength=800
        )
        summary_text.pack(pady=(0, 15))
        
        # Tools overview section
        tools_frame = ctk.CTkFrame(content_frame)
        tools_frame.pack(fill="both", expand=True, pady=(0, 20))
        
        tools_title = ctk.CTkLabel(
            tools_frame,
            text="🛠️ Available Tools",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        tools_title.pack(pady=(15, 10))
        
        # Tools grid
        tools_grid = ctk.CTkFrame(tools_frame)
        tools_grid.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Financial Tools
        financial_frame = ctk.CTkFrame(tools_grid, fg_color="#F3E8FF", border_color="#8B5CF6", border_width=1)
        financial_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        financial_title = ctk.CTkLabel(
            financial_frame,
            text="💰 Financial Tools",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#7C3AED"
        )
        financial_title.pack(pady=(10, 5))
        
        financial_tools = [
            "• Bill Note Sheet",
            "• EMD Refund Calculator", 
            "• Security Refund",
            "• Financial Progress Tracker"
        ]
        
        for tool in financial_tools:
            tool_label = ctk.CTkLabel(
                financial_frame,
                text=tool,
                font=ctk.CTkFont(size=11),
                text_color="#6B21A8"
            )
            tool_label.pack(anchor="w", padx=10, pady=1)
        
        # Calculation Tools
        calc_frame = ctk.CTkFrame(tools_grid, fg_color="#ECFDF5", border_color="#10B981", border_width=1)
        calc_frame.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        
        calc_title = ctk.CTkLabel(
            calc_frame,
            text="🧮 Calculation Tools",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#059669"
        )
        calc_title.pack(pady=(10, 5))
        
        calc_tools = [
            "• Delay Calculator",
            "• Stamp Duty Calculator",
            "• Deductions Table",
            "• Bill & Deviation Generator"
        ]
        
        for tool in calc_tools:
            tool_label = ctk.CTkLabel(
                calc_frame,
                text=tool,
                font=ctk.CTkFont(size=11),
                text_color="#047857"
            )
            tool_label.pack(anchor="w", padx=10, pady=1)
        
        # Data Processing Tools
        data_frame = ctk.CTkFrame(tools_grid, fg_color="#FEF3C7", border_color="#F59E0B", border_width=1)
        data_frame.grid(row=0, column=2, padx=10, pady=10, sticky="ew")
        
        data_title = ctk.CTkLabel(
            data_frame,
            text="📊 Data Processing",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#D97706"
        )
        data_title.pack(pady=(10, 5))
        
        data_tools = [
            "• Excel se EMD Refund",
            "• Report Generation",
            "• Data Import/Export",
            "• Tender Processing"
        ]
        
        for tool in data_tools:
            tool_label = ctk.CTkLabel(
                data_frame,
                text=tool,
                font=ctk.CTkFont(size=11),
                text_color="#B45309"
            )
            tool_label.pack(anchor="w", padx=10, pady=1)
        
        # Configure grid weights
        tools_grid.grid_columnconfigure(0, weight=1)
        tools_grid.grid_columnconfigure(1, weight=1)
        tools_grid.grid_columnconfigure(2, weight=1)
        
        # Loading section
        loading_frame = ctk.CTkFrame(content_frame, height=80)
        loading_frame.pack(fill="x", pady=(0, 20))
        loading_frame.pack_propagate(False)
        
        loading_title = ctk.CTkLabel(
            loading_frame,
            text="🚀 Initializing Application...",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        loading_title.pack(pady=(20, 5))
        
        # Progress bar
        self.progress_bar = ctk.CTkProgressBar(loading_frame, width=400)
        self.progress_bar.pack(pady=10)
        self.progress_bar.set(0)
        
        # Animate progress bar
        self.animate_progress()
        
        # Footer
        footer_frame = ctk.CTkFrame(splash_frame, height=60, fg_color="#374151")
        footer_frame.pack(fill="x", side="bottom")
        footer_frame.pack_propagate(False)
        
        footer_text = ctk.CTkLabel(
            footer_frame,
            text="Prepared for Mrs. Premlata Jain, AAO, PWD Udaipur | Complete Independence from Web Dependencies",
            font=ctk.CTkFont(size=12),
            text_color="white"
        )
        footer_text.pack(pady=15)
    
    def animate_progress(self):
        """Animate the progress bar"""
        try:
            current_progress = self.progress_bar.get()
            if current_progress < 1.0:
                new_progress = current_progress + 0.1
                self.progress_bar.set(new_progress)
                self.root.after(200, self.animate_progress)
            else:
                self.progress_bar.set(1.0)
        except:
            # Progress bar was destroyed, stop animation
            pass
    
    def initialize_main_app(self):
        """Initialize the main application after splash screen"""
        try:
            # Clear splash screen
            for widget in self.root.winfo_children():
                widget.destroy()
            
            # Create main window
            self.main_window = PWDToolsMainWindow(self.db_manager, self.settings, self.root)
            
            # Don't call run() as it will start another mainloop
            # The main window is already created and will be managed by the main loop
            
        except Exception as e:
            messagebox.showerror("Initialization Error", f"Failed to initialize application:\n{str(e)}")
            self.root.quit()
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

def main():
    """Main entry point"""
    try:
        # Check Python version
        if sys.version_info < (3, 9):
            messagebox.showerror("Python Version Error", "Python 3.9 or higher is required.")
            return
        
        # Create and run application
        app = PWDToolsApp()
        app.run()
        
    except Exception as e:
        messagebox.showerror("Application Error", f"Failed to start application:\n{str(e)}")

if __name__ == "__main__":
    main()
