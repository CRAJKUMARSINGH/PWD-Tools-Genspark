# PWD Simple Tools Organization

This document explains the organization of the PWD Simple Tools project.

## Main Entry Point

- **[pwd_simple_tools_launcher.py](file:///c:/Users/Rajkumar/PWD-Tools-Genspark/pwd_simple_tools_launcher.py)** - Unified launcher for all simple PWD tools
- **[run_simple_launcher.bat](file:///c:/Users/Rajkumar/PWD-Tools-Genspark/run_simple_launcher.bat)** - Batch file to easily run the launcher

## Simple Tools Included

1. **[delay_calculator_simple.py](file:///c:/Users/Rajkumar/PWD-Tools-Genspark/delay_calculator_simple.py)** - Calculate project delays with 3 simple dates (Start, Completion, Actual Completion)
2. **[stamp_duty_simple.py](file:///c:/Users/Rajkumar/PWD-Tools-Genspark/stamp_duty_simple.py)** - Calculate stamp duty with predefined rates
3. **[emd_refund_simple.py](file:///c:/Users/Rajkumar/PWD-Tools-Genspark/emd_refund_simple.py)** - Simple EMD refund with 3 inputs only
4. **[deductions_table_tool.py](file:///c:/Users/Rajkumar/PWD-Tools-Genspark/deductions_table_tool.py)** - Calculate all standard deductions for bill amounts
5. **[hindi_bill_simple.py](file:///c:/Users/Rajkumar/PWD-Tools-Genspark/hindi_bill_simple.py)** - Generate Running & Final Bills in Hindi
6. **[excel_emd_tool.py](file:///c:/Users/Rajkumar/PWD-Tools-Genspark/excel_emd_tool.py)** - Process EMD data from Excel files

## How to Use

1. Double-click on **[run_simple_launcher.bat](file:///c:/Users/Rajkumar/PWD-Tools-Genspark/run_simple_launcher.bat)** to start the launcher
2. Or run from command line: `python pwd_simple_tools_launcher.py`
3. Click on any tool button to open that specific tool
4. All tools will return to the main launcher when closed

## Design Principles

- **Simplicity**: Each tool has minimal inputs appropriate for Lower Divisional Clerks
- **Consistency**: All tools follow a similar color scheme and design pattern
- **Offline Operation**: All tools work without internet connection
- **User-Friendly**: Clear labels, intuitive interfaces, and helpful error messages

## Color Scheme

- **Headers**: Distinct colors for each tool (#2E8B57, #FF6B6B, #4ECDC4, etc.)
- **Backgrounds**: Light blue (#f0f8ff) for main windows
- **Containers**: White backgrounds with raised borders
- **Buttons**: Vibrant accent colors for primary actions
- **Text**: Clear hierarchy with colored labels

## File Organization

The project is organized to separate concerns:
- **Simple tools**: Files ending with `_simple.py` or named as `*_tool.py`
- **Complex tools**: Files with more complex functionality (not included in launcher)
- **Utilities**: Helper scripts for testing, deployment, and automation
- **Documentation**: README files and usage guides

This organization makes it easy to maintain and extend the simple tools while keeping the complex ones separate.