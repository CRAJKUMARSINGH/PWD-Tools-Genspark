import sys
import os
import time
import pathlib
from datetime import datetime

# Add the current directory to the path so we can import the module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def number_to_words(num):
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

def generate_pdf(payee_name, amount, work_description, test_number):
    """Generate a single PDF with the given data"""
    try:
        print(f"\n--- Test {test_number} ---")
        print(f"Input: Payee='{payee_name}', Amount={amount}, Work='{work_description}'")
        
        # Import ReportLab components
        from reportlab.lib.pagesizes import A4
        from reportlab.pdfgen import canvas
        from reportlab.lib.units import mm
        
        # Convert amount to words
        amount_words = number_to_words(amount)
        
        # Get downloads folder path
        downloads_path = pathlib.Path.home() / "Downloads"
        
        # Make sure the downloads directory exists
        downloads_path.mkdir(parents=True, exist_ok=True)
        
        # Create PDF filename with full path
        filename = f"EMD_Refund_Comprehensive_Test_{test_number:02d}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        full_path = downloads_path / filename
        
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
        return True
        
    except Exception as e:
        print(f"FAILED: PDF generation error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def run_comprehensive_test():
    """Run comprehensive test with 24 different inputs"""
    print("Starting Comprehensive EMD Refund PDF Generation Test")
    print("=" * 60)
    
    # Test data - 24 different combinations
    test_data = [
        ("Rajesh Kumar", 15000.00, "Road Construction Work"),
        ("Sunita Sharma", 25000.50, "Building Renovation"),
        ("Amit Patel", 35000.75, "Water Pipeline Installation"),
        ("Priya Singh", 12500.25, "Electrical Wiring"),
        ("Vikram Verma", 45000.00, "Bridge Repair"),
        ("Anjali Mehta", 18000.00, "Drainage System"),
        ("Rahul Gupta", 32000.00, "Cement Supply"),
        ("Neha Reddy", 22000.00, "Painting Work"),
        ("Deepak Joshi", 27500.00, "Roofing Work"),
        ("Kavita Rao", 19500.50, "Plumbing Installation"),
        ("Sanjay Malhotra", 38000.00, "Flooring Work"),
        ("Pooja Desai", 14250.75, "Wall Plastering"),
        ("Manoj Tiwari", 31000.00, "Door and Window Fitting"),
        ("Sneha Nair", 26500.00, "Garden Landscaping"),
        ("Vijay Khanna", 42000.00, "Solar Panel Installation"),
        ("Ritu Choudhary", 17250.00, "Furniture Supply"),
        ("Arun Bhatia", 33500.00, "Air Conditioning"),
        ("Divya Pillai", 21000.00, "Security System"),
        ("Rohan Seth", 29000.00, "Internet Cabling"),
        ("Meera Iyer", 16750.00, "Lighting Installation"),
        ("Karan Shah", 39500.00, "Fire Safety Equipment"),
        ("Tanvi Agrawal", 23500.00, "Kitchen Renovation"),
        ("Aditya Bansal", 28000.00, "Office Interior"),
        ("Shalini Kulkarni", 20250.00, "Parking Lot Construction")
    ]
    
    success_count = 0
    
    # Run all 24 tests
    for i, (payee, amount, work) in enumerate(test_data, 1):
        try:
            success = generate_pdf(payee, amount, work, i)
            if success:
                success_count += 1
            # Small delay to ensure unique timestamps
            time.sleep(1)
        except Exception as e:
            print(f"Test {i}: FAILED - Unexpected error: {str(e)}")
    
    # Summary
    print("\n" + "=" * 60)
    print("COMPREHENSIVE TEST SUMMARY")
    print("=" * 60)
    print(f"Total tests run: {len(test_data)}")
    print(f"Successful PDF generations: {success_count}")
    print(f"Failed PDF generations: {len(test_data) - success_count}")
    
    if success_count == len(test_data):
        print("\n🎉 ALL TESTS PASSED! All 24 PDFs were successfully generated and saved to the Downloads folder.")
        return True
    else:
        print(f"\n⚠️  {len(test_data) - success_count} tests failed. Please check the errors above.")
        return False

# Run the comprehensive test
if __name__ == "__main__":
    success = run_comprehensive_test()
    
    # List all generated PDFs
    try:
        downloads_path = pathlib.Path.home() / "Downloads"
        pdf_files = list(downloads_path.glob("EMD_Refund_Comprehensive_Test_*.pdf"))
        print(f"\nFound {len(pdf_files)} EMD Refund comprehensive test PDFs in Downloads folder:")
        for pdf_file in sorted(pdf_files):
            print(f"  - {pdf_file.name}")
    except Exception as e:
        print(f"\nCould not list PDF files in Downloads folder: {str(e)}")