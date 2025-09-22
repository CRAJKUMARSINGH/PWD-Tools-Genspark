"""
Generate screenshots for simple PWD tools
"""

import os
import time
from pathlib import Path
import tkinter as tk
import webbrowser
import tempfile

try:
    from PIL import ImageGrab
except ImportError:
    print("Pillow is required for screenshots. Please install it with: pip install pillow")
    exit(1)

def ensure_dir(path: Path) -> None:
    """Ensure directory exists"""
    path.mkdir(parents=True, exist_ok=True)

def save_window_screenshot(window, out_path: Path) -> None:
    """Save screenshot of a tkinter window"""
    # Update and get geometry
    window.update()
    window.update_idletasks()
    
    # Get window coordinates
    x = window.winfo_rootx()
    y = window.winfo_rooty()
    width = window.winfo_width()
    height = window.winfo_height()
    
    # Define bounding box
    bbox = (x, y, x + width, y + height)
    
    # Capture screenshot
    img = ImageGrab.grab(bbox=bbox)
    ensure_dir(out_path.parent)
    img.save(str(out_path))
    print(f"Screenshot saved: {out_path}")

def generate_simple_tool_screenshots():
    """Generate screenshots for simple tools"""
    # Import simple tools
    from emd_refund_simple import SimpleEMDRefundTool
    from stamp_duty_simple import SimpleStampDutyTool
    from delay_calculator_simple import SimpleDelayCalculatorTool
    from hindi_bill_simple import SimpleHindiBillNoteTool
    from deductions_table_tool import DeductionsTableTool
    from excel_emd_tool import ExcelEMDTool
    from bill_note_sheet_tool import BillNoteSheetTool
    
    # Tkinter-based tools
    tkinter_tools = [
        ("emd_refund", SimpleEMDRefundTool),
        ("stamp_duty", SimpleStampDutyTool),
        ("delay_calculator", SimpleDelayCalculatorTool),
        ("bill_note", BillNoteSheetTool),
        ("deductions_table", DeductionsTableTool),
        ("excel_emd", ExcelEMDTool),
    ]
    
    # Generate screenshots for each Tkinter tool
    for tool_name, tool_class in tkinter_tools:
        print(f"Generating screenshots for {tool_name}...")
        
        # Create tool instance
        tool = tool_class()
        
        # Give time for window to render
        tool.root.update()
        tool.root.update_idletasks()
        time.sleep(1)
        
        # Generate 3 screenshots for each tool
        for i in range(1, 4):
            out_path = Path("screenshots") / tool_name / f"run_{i}.png"
            save_window_screenshot(tool.root, out_path)
        
        # Close the tool window
        tool.root.destroy()
    
    # HTML-based tools (financial progress and security refund)
    # For these, we'll create placeholder screenshots or use a different approach
    html_tools = ["financial_progress", "security_refund"]
    for tool_name in html_tools:
        print(f"Generating placeholder screenshots for {tool_name}...")
        # Create placeholder directory
        tool_dir = Path("screenshots") / tool_name
        ensure_dir(tool_dir)
        
        # Create simple placeholder images
        for i in range(1, 4):
            out_path = tool_dir / f"run_{i}.png"
            # Create a simple placeholder image
            placeholder_content = f"Placeholder for {tool_name} HTML tool - Screenshot {i}"
            with open(out_path, "w") as f:
                f.write(placeholder_content)
    
    print("Screenshot generation complete!")

if __name__ == "__main__":
    generate_simple_tool_screenshots()