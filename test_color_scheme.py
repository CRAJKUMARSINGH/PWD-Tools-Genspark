"""
Test script to verify the color scheme changes
"""

import tkinter as tk
from tkinter import messagebox

def show_color_palette():
    """Display the new color palette"""
    root = tk.Tk()
    root.title("PWD Tools - New Color Scheme")
    root.geometry("600x400")
    
    # Main background
    root.configure(bg="#e0f0ff")
    
    # Header
    header_frame = tk.Frame(root, bg="#1E6B4E", height=60)
    header_frame.pack(fill="x", padx=10, pady=10)
    header_frame.pack_propagate(False)
    
    header_label = tk.Label(
        header_frame,
        text="New Color Scheme Preview",
        font=("Arial", 16, "bold"),
        fg="white",
        bg="#1E6B4E"
    )
    header_label.pack(pady=15)
    
    # Color swatches
    colors = [
        ("Hindi Bill Note", "#FF5252"),
        ("Stamp Duty Calculator", "#00BCD4"),
        ("EMD Refund", "#2196F3"),
        ("Delay Calculator", "#4CAF50"),
        ("Financial Analysis", "#FFC107"),
        ("Bill Generator Link", "#9C27B0"),
        ("Excel EMD Processor", "#3F51B5"),
        ("Deductions Calculator", "#009688"),
        ("Tender Processing", "#FF9800"),
        ("Security Refund", "#673AB7")
    ]
    
    # Display color swatches
    swatch_frame = tk.Frame(root, bg="#e0f0ff")
    swatch_frame.pack(fill="both", expand=True, padx=20, pady=10)
    
    for i, (name, color) in enumerate(colors):
        row = i // 2
        col = i % 2
        
        color_frame = tk.Frame(swatch_frame, bg="white", relief="raised", bd=2)
        color_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
        
        # Configure grid weights
        swatch_frame.grid_rowconfigure(row, weight=1)
        swatch_frame.grid_columnconfigure(col, weight=1)
        
        # Color display
        color_display = tk.Frame(color_frame, bg=color, height=50)
        color_display.pack(fill="x", padx=5, pady=5)
        color_display.pack_propagate(False)
        
        # Color name and hex
        name_label = tk.Label(
            color_frame,
            text=name,
            font=("Arial", 10, "bold"),
            fg=color,
            bg="white"
        )
        name_label.pack(pady=2)
        
        hex_label = tk.Label(
            color_frame,
            text=color,
            font=("Arial", 9),
            fg="#666666",
            bg="white"
        )
        hex_label.pack(pady=2)
    
    # Footer
    footer_frame = tk.Frame(root, bg="#1E6B4E", height=40)
    footer_frame.pack(fill="x", padx=10, pady=10)
    footer_frame.pack_propagate(False)
    
    footer_label = tk.Label(
        footer_frame,
        text="PWD Tools - Vibrant Color Scheme",
        font=("Arial", 10),
        fg="white",
        bg="#1E6B4E"
    )
    footer_label.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    show_color_palette()