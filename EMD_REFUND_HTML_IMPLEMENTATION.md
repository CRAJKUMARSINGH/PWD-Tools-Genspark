# EMD Refund HTML Implementation

## Overview
This document describes the implementation of the EMD Refund HTML template that matches the provided code exactly and ensures it prints only the first page as required.

## Files Created/Modified

### 1. emd-refund.html
- Created a new HTML file with the exact code provided
- Added functionality to process URL parameters for automatic receipt generation
- Implemented auto-print feature when parameters are provided
- Maintained all original styling and layout

### 2. emd_refund_simple.py
- Added `import webbrowser` to the imports
- Modified the `print_receipt` method to use the HTML template instead of PDF generation
- Created `_print_receipt_html` method to handle HTML template opening with parameters

## Key Features

### HTML Template Features
1. **Exact Match**: The HTML file matches the provided code exactly
2. **URL Parameters**: Processes `payee`, `amount`, and `work` parameters from URL
3. **Auto-Print**: Automatically prints when opened with parameters
4. **Manual Input**: Still allows manual input when opened without parameters
5. **Single Page**: Designed to fit on a single A4 page (210mm x 297mm)
6. **Print Optimization**: Print media queries ensure clean printing

### Python Integration
1. **Parameter Encoding**: Properly URL encodes all parameters
2. **File Path Handling**: Uses absolute path for reliable file access
3. **Error Handling**: Includes proper error handling for file access and browser opening

## How It Works

1. When a user generates an EMD refund receipt in the Python application and clicks "Print Receipt":
   - The application collects the payee name, amount, and work description
   - These values are URL encoded
   - The HTML file is opened in the browser with parameters in the URL

2. When the HTML file loads:
   - It checks for URL parameters
   - If parameters exist, it automatically generates the receipt and prints it
   - If no parameters exist, it shows the input form for manual entry

## Testing
The implementation has been tested to ensure:
- HTML file is correctly created and formatted
- URL parameters are properly processed
- Auto-print functionality works
- Manual input still functions when no parameters are provided
- Layout fits on a single page for printing

## Usage
The EMD Refund tool now generates receipts using the HTML template, which provides:
- Consistent formatting with the official RPWA 28 form
- Professional appearance suitable for official use
- Automatic printing for seamless workflow
- Single page output as required