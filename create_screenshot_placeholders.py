#!/usr/bin/env python3
"""
Create placeholder files for screenshots
"""

import os
from pathlib import Path

def ensure_dir(path: Path) -> None:
    """Ensure directory exists"""
    path.mkdir(parents=True, exist_ok=True)

def create_placeholder_file(path: Path, content: str = "") -> None:
    """Create a placeholder file"""
    ensure_dir(path.parent)
    with open(path, "w") as f:
        f.write(content if content else f"Placeholder for {path.name}\n")

def main():
    """Main function to create screenshot placeholders"""
    print("📂 Creating screenshot placeholder files...")
    
    # Create desktop app screenshot directories
    desktop_tools = [
        "excel_emd",
        "bill_note",
        "emd_refund",
        "deductions_table",
        "delay_calculator",
        "security_refund",
        "financial_progress",
        "stamp_duty",
        "bill_deviation",
        "tender_processing"
    ]
    
    # Create directories and placeholder files for desktop app
    for tool in desktop_tools:
        tool_dir = Path("screenshots") / tool
        ensure_dir(tool_dir)
        
        # Create 3 run placeholders for each tool
        for i in range(1, 4):
            placeholder_path = tool_dir / f"run_{i}.png"
            create_placeholder_file(placeholder_path, f"Placeholder screenshot for {tool} - Run {i}")
            print(f"✅ Created: {placeholder_path}")
    
    # Create landing page directory
    landing_dir = Path("screenshots") / "landing"
    ensure_dir(landing_dir)
    
    # Create main landing page placeholder
    main_landing = landing_dir / "main.png"
    create_placeholder_file(main_landing, "Placeholder screenshot for main landing page")
    print(f"✅ Created: {main_landing}")
    
    # Create Streamlit screenshot directory
    streamlit_dir = Path("streamlit_screenshots")
    ensure_dir(streamlit_dir)
    
    # Create Streamlit placeholders
    streamlit_pages = [
        "landing_page.png",
        "hindi_bill_note.png",
        "stamp_duty_calculator.png",
        "emd_refund.png",
        "delay_calculator.png",
        "financial_analysis.png",
        "deductions_table.png",
        "delay_calculator_page.png",
        "stamp_duty_page.png"
    ]
    
    for page in streamlit_pages:
        placeholder_path = streamlit_dir / page
        create_placeholder_file(placeholder_path, f"Placeholder screenshot for {page}")
        print(f"✅ Created: {placeholder_path}")
    
    print(f"\n🎉 Created placeholder files for {len(desktop_tools)*3 + 1 + len(streamlit_pages)} screenshots")
    print("📁 Screenshot directories and placeholders are ready")
    print("📝 Note: These are placeholder files. Replace with actual screenshots when generated.")

if __name__ == "__main__":
    main()