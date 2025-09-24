"""
Script to generate placeholder images for PWD Tools
"""

import os
from PIL import Image, ImageDraw, ImageFont

# Create directories if they don't exist
os.makedirs("screenshots/landing", exist_ok=True)

# Define tools and their colors
tools = [
    {"name": "excel_se_emd", "icon": "📊", "color": "#8B5CF6"},
    {"name": "bill_note_sheet", "icon": "📝", "color": "#10B981"},
    {"name": "emd_refund", "icon": "💰", "color": "#F59E0B"},
    {"name": "deductions_table", "icon": "📊", "color": "#EF4444"},
    {"name": "delay_calculator", "icon": "⏰", "color": "#6366F1"},
    {"name": "security_refund", "icon": "🔒", "color": "#8B5CF6"},
    {"name": "financial_progress", "icon": "📈", "color": "#10B981"},
    {"name": "stamp_duty", "icon": "📋", "color": "#F59E0B"},
    {"name": "bill_deviation", "icon": "💰", "color": "#EF4444"},
    {"name": "tender_processing", "icon": "📋", "color": "#6366F1"},
]

# Generate landing page image
landing_img = Image.new('RGB', (800, 600), color='#f0f8ff')
landing_draw = ImageDraw.Draw(landing_img)

# Add title
try:
    title_font = ImageFont.truetype("arial.ttf", 36)
    subtitle_font = ImageFont.truetype("arial.ttf", 24)
    text_font = ImageFont.truetype("arial.ttf", 18)
except:
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    text_font = ImageFont.load_default()

landing_draw.rectangle([0, 0, 800, 100], fill='#2E8B57')
landing_draw.text((50, 30), "🏗️ PWD Tools Dashboard", fill='white', font=title_font)
landing_draw.text((50, 70), "Infrastructure Management Suite", fill='#E0FFFF', font=subtitle_font)

# Add tool grid
tool_width = 200
tool_height = 120
margin = 20
start_x = 50
start_y = 150

for i, tool in enumerate(tools[:6]):  # Only first 6 tools for landing
    row = i // 3
    col = i % 3
    
    x = start_x + col * (tool_width + margin)
    y = start_y + row * (tool_height + margin)
    
    # Draw tool card
    landing_draw.rectangle([x, y, x + tool_width, y + tool_height], fill='white', outline='#ccc')
    landing_draw.rectangle([x, y, x + tool_width, y + 30], fill=tool["color"])
    landing_draw.text((x + 10, y + 5), tool["icon"] + " " + tool["name"].replace("_", " ").title(), fill='white', font=text_font)
    landing_draw.text((x + 10, y + 40), "Tool description here", fill='#666', font=text_font)

landing_img.save("screenshots/landing/main.png")

# Generate individual tool images
for tool in tools:
    img = Image.new('RGB', (400, 300), color='#f8f9fa')
    draw = ImageDraw.Draw(img)
    
    # Header
    draw.rectangle([0, 0, 400, 60], fill=tool["color"])
    draw.text((20, 20), tool["icon"] + " " + tool["name"].replace("_", " ").title(), fill='white', font=title_font)
    
    # Content area
    draw.rectangle([20, 80, 380, 250], outline='#ccc', width=2)
    draw.text((40, 100), f"This is the {tool['name'].replace('_', ' ')} tool.", fill='#333', font=text_font)
    draw.text((40, 140), "It helps with PWD operations.", fill='#333', font=text_font)
    draw.text((40, 180), "Functional and elegant design.", fill='#333', font=text_font)
    
    # Save image
    os.makedirs(f"screenshots/{tool['name']}", exist_ok=True)
    img.save(f"screenshots/{tool['name']}/run_1.png")
    img.save(f"screenshots/{tool['name']}/run_2.png")
    img.save(f"screenshots/{tool['name']}/run_3.png")

print("Placeholder images generated successfully!")