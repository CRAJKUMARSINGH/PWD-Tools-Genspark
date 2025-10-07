#!/usr/bin/env python3
"""
Optimized PWD Tools Desktop - Main Application Launcher
Unified entry point with improved performance and user experience
"""

import sys
import os
from pathlib import Path
import tkinter as tk
from tkinter import messagebox
import importlib.util

def check_dependencies():
    """Check if all required dependencies are available"""
    missing_deps = []
    
    # Core dependencies that are essential
    dependencies = {
        'tkinter': 'GUI framework',
        'customtkinter': 'Modern UI components',
        'pandas': 'Data processing',
        'reportlab': 'PDF generation',
        'PIL': 'Image processing'
    }
    
    for dep, description in dependencies.items():
        try:
            if dep == 'tkinter':
                __import__('tkinter')
            elif dep == 'customtkinter':
                __import__('customtkinter')
            elif dep == 'pandas':
                __import__('pandas')
            elif dep == 'reportlab':
                __import__('reportlab')
            elif dep == 'PIL':
                __import__('PIL.Image')
        except ImportError:
            missing_deps.append(f"{dep} ({description})")
    
    return missing_deps

def show_splash_screen():
    """Show a simple splash screen during startup"""
    splash = tk.Tk()
    splash.title("PWD Tools Desktop")
    splash.geometry("400x300")
    splash.resizable(False, False)
    
    # Center the window
    splash.update_idletasks()
    x = (splash.winfo_screenwidth() // 2) - (400 // 2)
    y = (splash.winfo_screenheight() // 2) - (300 // 2)
    splash.geometry(f"400x300+{x}+{y}")
    
    # Simple splash content
    frame = tk.Frame(splash, bg="#f0f4f8")
    frame.pack(fill="both", expand=True)
    
    title = tk.Label(
        frame,
        text="PWD Tools Desktop",
        font=("Arial", 20, "bold"),
        bg="#f0f4f8",
        fg="#2d3748"
    )
    title.pack(pady=50)
    
    status = tk.Label(
        frame,
        text="Initializing application...",
        font=("Arial", 12),
        bg="#f0f4f8",
        fg="#4a5568"
    )
    status.pack(pady=20)
    
    progress = tk.Label(
        frame,
        text="Checking dependencies...",
        font=("Arial", 10),
        bg="#f0f4f8",
        fg="#718096"
    )
    progress.pack(pady=10)
    
    splash.update()
    return splash, progress

def launch_application():
    """Launch the main application with version selection"""
    try:
        # Add project root to Python path
        project_root = Path(__file__).parent
        sys.path.insert(0, str(project_root))
        
        # Check if launcher exists and use it for version selection
        if os.path.exists("launcher.py"):
            # Import and run launcher
            spec = importlib.util.spec_from_file_location("launcher", "launcher.py")
            if spec is not None and spec.loader is not None:
                launcher_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(launcher_module)
                
                launcher = launcher_module.PWDToolsLauncher()
                launcher.run()
            else:
                raise ImportError("Could not load launcher module")
        else:
            # Fallback to optimized version
            ctk = __import__('customtkinter')
            ctk.set_appearance_mode("light")
            ctk.set_default_color_theme("blue")
            
            from pwd_tools_optimized import PWDToolsOptimized
            app = PWDToolsOptimized()
            app.run()
            
    except ImportError as e:
        error_msg = f"Failed to import required modules:\n{str(e)}\n\n"
        error_msg += "Please ensure all dependencies are installed:\npip install -r requirements.txt"
        
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Import Error", error_msg)
        root.destroy()
        return 1
        
    except Exception as e:
        error_msg = f"Failed to start application:\n{str(e)}"
        
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Application Error", error_msg)
        root.destroy()
        return 1
    
    return 0

def main():
    """Main application entry point"""
    # Show splash screen
    splash, progress_label = show_splash_screen()
    
    try:
        # Check dependencies
        progress_label.config(text="Checking dependencies...")
        splash.update()
        
        missing_deps = check_dependencies()
        if missing_deps:
            splash.destroy()
            error_msg = "The following required dependencies are missing:\n\n" + "\n".join(missing_deps)
            error_msg += "\n\nPlease run INSTALL_DEPS.bat to install all dependencies."
            
            root = tk.Tk()
            root.withdraw()  # Hide the root window
            messagebox.showerror("Missing Dependencies", error_msg)
            root.destroy()
            return 1
        
        # Update splash
        progress_label.config(text="Loading application...")
        splash.update()
        
        # Close splash screen
        splash.destroy()
        
        # Launch the application
        return launch_application()
        
    except Exception as e:
        splash.destroy()
        error_msg = f"Failed to start application:\n{str(e)}"
        
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Application Error", error_msg)
        root.destroy()
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())