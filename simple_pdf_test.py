import sys
import os
import pathlib
from datetime import datetime

# Add the current directory to the path so we can import the module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Try to import and test the EMD Refund tool
try:
    from emd_refund_simple import SimpleEMDRefundTool
    
    # Create a mock instance to test PDF generation
    class TestEMDRefundTool(SimpleEMDRefundTool):
        def __init__(self):
            # Don't initialize the full GUI
            pass
            
        def number_to_words(self, num):
            """Convert number to words (Indian numbering system) - copied from the main class"""
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
        
        def test_pdf_generation(self):
            """Test PDF generation with sample data"""
            try:
                print("Testing PDF generation...")
                
                # Sample data
                self.current_receipt = {
                    'payee_name': 'Test User',
                    'amount': 15000.00,
                    'work_description': 'Test Work Description'
                }
                
                # Import ReportLab components locally to avoid issues if not available
                from reportlab.lib.pagesizes import A4
                from reportlab.pdfgen import canvas
                from reportlab.lib.units import mm
                
                # Get current receipt data
                receipt = self.current_receipt
                payee_name = receipt['payee_name']
                amount = receipt['amount']
                work_description = receipt['work_description']
                
                # Convert amount to words
                amount_words = self.number_to_words(amount)
                
                # Get downloads folder path
                downloads_path = pathlib.Path.home() / "Downloads"
                print(f"Downloads folder path: {downloads_path}")
                
                # Create PDF filename with full path
                filename = f"EMD_Refund_Test_Single_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
                full_path = downloads_path / filename
                print(f"Full path for PDF: {full_path}")
                
                # Create PDF
                c = canvas.Canvas(str(full_path), pagesize=A4)
                width, height = A4
                
                # Set margins (10mm on each side)
                left_margin = 10*mm
                right_margin = 10*mm
                top_margin = 10*mm
                bottom_margin = 10*mm
                
                # Draw border (2px solid #ccc)
                c.setStrokeColorRGB(0.8, 0.8, 0.8)  # Light gray color (#ccc)
                c.setLineWidth(2)
                c.rect(left_margin, bottom_margin, width - left_margin - right_margin, height - top_margin - bottom_margin)
                
                # Header section
                c.setFont("Helvetica-Bold", 16)
                c.drawCentredString(width/2, height - 50*mm, f"Payable to: - {payee_name} ( Electric Contractor)")
                c.setFont("Helvetica-Bold", 14)
                c.drawCentredString(width/2, height - 60*mm, "HAND RECEIPT (RPWA 28)")
                c.setFont("Helvetica", 10)
                c.drawCentredString(width/2, height - 65*mm, "(Referred to in PWF&A Rules 418,424,436 & 438)")
                c.drawCentredString(width/2, height - 70*mm, "Division - PWD Electric Division, Udaipur")
                
                # Details section
                c.setFont("Helvetica", 10)
                y_position = height - 80*mm
                
                # Line 1
                c.drawString(30*mm, y_position, "(1)Cash Book Voucher No.                Date")
                y_position -= 10*mm
                
                # Line 2
                c.drawString(30*mm, y_position, "(2)Cheque No. and Date")
                y_position -= 10*mm
                
                # Line 3
                c.drawString(30*mm, y_position, f"(3) Pay for ECS Rs.{amount}/- (Rupees {amount_words} Only)")
                y_position -= 10*mm
                
                # Line 4
                c.drawString(30*mm, y_position, "(4) Paid by me")
                y_position -= 10*mm
                
                # Line 5
                c.drawString(30*mm, y_position, f"(5) Received from The Executive Engineer PWD Electric Division, Udaipur the sum of Rs. {amount}/- (Rupees {amount_words} Only)")
                y_position -= 10*mm
                
                # Line 6
                c.drawString(30*mm, y_position, f" Name of work for which payment is made: {work_description}")
                y_position -= 10*mm
                
                # Line 7
                c.drawString(30*mm, y_position, " Chargeable to Head:- 8443 [EMD-Refund] ")
                y_position -= 15*mm
                
                # Signature area table
                # Table headers
                c.setFont("Helvetica", 10)
                c.drawString(30*mm, y_position, "Witness")
                c.drawString(90*mm, y_position, "Stamp")
                c.drawString(150*mm, y_position, "Signature of payee")
                y_position -= 10*mm
                
                # Table content
                c.drawString(30*mm, y_position, "Cash Book No.                Page No.")
                y_position -= 20*mm
                
                # Offices table
                # Table headers
                c.drawString(30*mm, y_position, "For use in the Divisional Office")
                c.drawString(120*mm, y_position, "For use in the Accountant General's office")
                y_position -= 10*mm
                
                # Second row
                c.drawString(30*mm, y_position, "Checked")
                c.drawString(120*mm, y_position, "Audited/Reviewed")
                y_position -= 10*mm
                
                # Third row
                c.drawString(30*mm, y_position, "Accounts Clerk")
                c.drawString(120*mm, y_position, "DA          Auditor          Supdt.          G.O.")
                y_position -= 30*mm
                
                # Bottom left box with blue border (no circular seal)
                c.setStrokeColorRGB(0, 0, 1)  # Blue color
                c.setLineWidth(2)
                c.rect(40*mm, 40*mm, 120*mm, 55*mm)  # Position and size matching the HTML
                
                # Text in bottom left box (blue color)
                c.setFillColorRGB(0, 0, 1)  # Blue color
                c.setFont("Helvetica", 10)
                y_position = 90*mm  # Starting position for text in the box
                c.drawString(45*mm, y_position, "")
                y_position -= 5*mm
                c.drawString(45*mm, y_position, "")
                y_position -= 5*mm
                c.drawString(45*mm, y_position, "")
                y_position -= 10*mm
                c.drawString(45*mm, y_position, f" Passed for Rs. {amount}")
                y_position -= 5*mm
                c.drawString(45*mm, y_position, f" In Words Rupees: {amount_words} Only")
                y_position -= 5*mm
                c.drawString(45*mm, y_position, " Chargeable to Head:- 8443 [EMD-Refund]")
                y_position -= 10*mm
                
                # Seal text in bottom left box
                c.drawString(45*mm, y_position, "Ar.                    D.A.                    E.E.")
                
                # Reset colors to default
                c.setFillColorRGB(0, 0, 0)  # Black color
                c.setStrokeColorRGB(0, 0, 0)  # Black color
                c.setLineWidth(1)
                
                # Save the PDF
                c.save()
                
                print(f"SUCCESS: PDF saved as {filename}")
                print(f"Full path: {full_path}")
                return True
                
            except Exception as e:
                print(f"FAILED: PDF generation error: {str(e)}")
                import traceback
                traceback.print_exc()
                return False
    
    # Create test instance and run test
    tool = TestEMDRefundTool()
    success = tool.test_pdf_generation()
    
    if success:
        print("\n✅ PDF generation test PASSED!")
    else:
        print("\n❌ PDF generation test FAILED!")

except ImportError as e:
    print(f"Import error: {e}")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()