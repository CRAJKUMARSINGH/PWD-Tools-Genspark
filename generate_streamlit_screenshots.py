#!/usr/bin/env python3
"""
Generate placeholder screenshots for Streamlit app
"""

import os
from pathlib import Path

def create_placeholder_screenshots():
    """Create placeholder screenshots for all tools"""
    tools = [
        "excel_emd",
        "bill_note",
        "emd_refund",
        "deductions_table",
        "delay_calculator",
        "security_refund",
        "financial_progress",
        "stamp_duty",
        "bill_deviation",
        "tender_processing",
    ]
    
    # Create directories and placeholder files
    for tool in tools:
        tool_dir = Path("streamlit_screenshots") / tool
        tool_dir.mkdir(parents=True, exist_ok=True)
        
        # Create placeholder files with some content
        for i in range(1, 4):
            placeholder_file = tool_dir / f"run_{i}.png"
            # Create a simple placeholder file with content
            with open(placeholder_file, "w") as f:
                f.write(f"Placeholder screenshot for {tool} - Run {i}")
    
    # Create landing page directory and placeholder
    landing_dir = Path("streamlit_screenshots") / "landing"
    landing_dir.mkdir(parents=True, exist_ok=True)
    landing_file = landing_dir / "main.png"
    
    with open(landing_file, "w") as f:
        f.write("Placeholder for landing page screenshot")
    
    print("✅ Created placeholder screenshots for all tools")

if __name__ == "__main__":
    create_placeholder_screenshots()