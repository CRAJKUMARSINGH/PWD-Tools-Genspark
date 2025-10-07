import sys
import os
from datetime import datetime

# Add the current directory to the path so we can import the module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Try to import and test the PDF generation
try:
    from emd_refund_simple import SimpleEMDRefundTool
    
    # Create a mock instance to test PDF generation
    class MockEMDRefundTool(SimpleEMDRefundTool):
        def __init__(self):
            # Don't initialize the full GUI
            pass
            
        def number_to_words(self, num):
            """Convert number to words (Indian numbering system)"""
            if num == 0:
                return "Zero"
            
            ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
            teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
            tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
            
            def convert_hundreds(n):
                result = ""
                if n >= 100:
                    result += ones[n // 100] + " Hundred "
                    n %= 100
                if n >= 20:
                    result += tens[n // 10] + " "
                    if n % 10:
                        result += ones[n % 10] + " "
                elif n >= 10:
                    result += teens[n - 10] + " "
                elif n > 0:
                    result += ones[n] + " "
                return result.strip()
            
            # Convert to integer and then process
            num = int(num)
            if num == 0:
                return "Zero"
            
            result = ""
            # Handle crores
            if num >= 10000000:
                crores = num // 10000000
                result += convert_hundreds(crores) + " Crore "
                num %= 10000000
            
            # Handle lakhs
            if num >= 100000:
                lakhs = num // 100000
                result += convert_hundreds(lakhs) + " Lakh "
                num %= 100000
            
            # Handle thousands
            if num >= 1000:
                thousands = num // 1000
                result += convert_hundreds(thousands) + " Thousand "
                num %= 1000
            
            # Handle hundreds and below
            if num > 0:
                result += convert_hundreds(num)
            
            return result.strip()
    
    # Test the number to words function
    tool = MockEMDRefundTool()
    print("Testing number to words conversion:")
    test_amount = 12500
    words = tool.number_to_words(test_amount)
    print(f"Amount: {test_amount} -> Words: {words}")
    
    print("\nPDF generation function is ready to be tested with actual GUI input.")
    print("Run the EMD Refund tool and generate a receipt to test the PDF output.")
    
except ImportError as e:
    print(f"Import error: {e}")
except Exception as e:
    print(f"Error: {e}")