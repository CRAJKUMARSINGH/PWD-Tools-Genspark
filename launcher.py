"""
PWD Tools Launcher - Allows users to choose which version to run
"""

import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

class PWDToolsLauncher:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PWD Tools Launcher")
        self.root.geometry("550x450")
        self.root.resizable(False, False)
        
        # Center the window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (550 // 2)
        y = (self.root.winfo_screenheight() // 2) - (450 // 2)
        self.root.geometry(f"550x450+{x}+{y}")
        
        self.create_interface()
    
    def create_interface(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg="#f8fafc")
        main_frame.pack(fill="both", expand=True, padx=30, pady=30)
        
        # Title
        title = tk.Label(
            main_frame,
            text="🏗️ PWD Tools Desktop",
            font=("Arial", 28, "bold"),
            fg="#4f46e5",
            bg="#f8fafc"
        )
        title.pack(pady=(25, 15))
        
        subtitle = tk.Label(
            main_frame,
            text="Choose Your Preferred Version",
            font=("Arial", 16),
            fg="#64748b",
            bg="#f8fafc"
        )
        subtitle.pack(pady=(0, 35))
        
        # Version options
        versions_frame = tk.Frame(main_frame, bg="#f8fafc")
        versions_frame.pack(fill="both", expand=True)
        
        # Optimized Version
        opt_frame = tk.Frame(versions_frame, bg="#eff6ff", relief="solid", bd=2)
        opt_frame.pack(fill="x", pady=15)
        
        opt_title = tk.Label(
            opt_frame,
            text="⚡ Optimized Version",
            font=("Arial", 18, "bold"),
            fg="#1e40af",
            bg="#eff6ff"
        )
        opt_title.pack(pady=(20, 10))
        
        opt_desc = tk.Label(
            opt_frame,
            text="• Faster performance\n• Enhanced UI with categories\n• Process management\n• Modern design",
            font=("Arial", 12),
            fg="#334155",
            bg="#eff6ff",
            justify="left"
        )
        opt_desc.pack(pady=(0, 20))
        
        opt_btn = tk.Button(
            opt_frame,
            text="Launch Optimized Version",
            command=self.launch_optimized,
            bg="#4f46e5",
            fg="white",
            font=("Arial", 14, "bold"),
            width=28,
            height=2,
            relief="flat",
            bd=0,
            cursor="hand2"
        )
        opt_btn.pack(pady=(0, 25))
        
        # Add hover effect
        self.make_hover_effect(opt_btn, "#4f46e5")
        
        # Simple Version
        simple_frame = tk.Frame(versions_frame, bg="#f0fdf4", relief="solid", bd=2)
        simple_frame.pack(fill="x", pady=15)
        
        simple_title = tk.Label(
            simple_frame,
            text="📋 Simple Version",
            font=("Arial", 18, "bold"),
            fg="#15803d",
            bg="#f0fdf4"
        )
        simple_title.pack(pady=(20, 10))
        
        simple_desc = tk.Label(
            simple_frame,
            text="• Original interface\n• Lightweight\n• Familiar layout",
            font=("Arial", 12),
            fg="#334155",
            bg="#f0fdf4",
            justify="left"
        )
        simple_desc.pack(pady=(0, 20))
        
        simple_btn = tk.Button(
            simple_frame,
            text="Launch Simple Version",
            command=self.launch_simple,
            bg="#10b981",
            fg="white",
            font=("Arial", 14, "bold"),
            width=28,
            height=2,
            relief="flat",
            bd=0,
            cursor="hand2"
        )
        simple_btn.pack(pady=(0, 25))
        
        # Add hover effect
        self.make_hover_effect(simple_btn, "#10b981")
        
        # Footer
        footer = tk.Label(
            main_frame,
            text="Prepared for Mrs. Premlata Jain, AAO, PWD Udaipur",
            font=("Arial", 11),
            fg="#94a3b8",
            bg="#f8fafc"
        )
        footer.pack(side="bottom", pady=20)
    
    def make_hover_effect(self, button, original_color):
        """Create hover effect for a button"""
        def on_enter(e):
            # Lighten the color for hover effect
            lightened_color = self.lighten_color(original_color)
            button.config(bg=lightened_color)
        def on_leave(e):
            button.config(bg=original_color)
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
    
    def lighten_color(self, color):
        """Lighten a hex color for hover effect"""
        color_map = {
            "#4f46e5": "#6366f8",   # Purple
            "#10b981": "#34d399"    # Green
        }
        return color_map.get(color, color)
    
    def launch_optimized(self):
        """Launch the optimized version"""
        try:
            if os.path.exists("pwd_tools_optimized.py"):
                subprocess.Popen([sys.executable, "pwd_tools_optimized.py"])
                self.root.destroy()
            else:
                messagebox.showerror("Error", "Optimized version not found")
        except Exception as e:
            messagebox.showerror("Error", f"Could not launch optimized version: {str(e)}")
    
    def launch_simple(self):
        """Launch the simple version"""
        try:
            if os.path.exists("pwd_tools_simple.py"):
                subprocess.Popen([sys.executable, "pwd_tools_simple.py"])
                self.root.destroy()
            else:
                messagebox.showerror("Error", "Simple version not found")
        except Exception as e:
            messagebox.showerror("Error", f"Could not launch simple version: {str(e)}")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    launcher = PWDToolsLauncher()
    launcher.run()