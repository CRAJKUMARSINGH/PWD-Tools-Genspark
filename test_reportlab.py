from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from datetime import datetime
import os

def test_pdf_generation():
    """Test PDF generation with ReportLab"""
    try:
        # Create a simple PDF
        filename = f"test_pdf_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        c = canvas.Canvas(filename, pagesize=A4)
        width, height = A4
        
        # Add some text
        c.setFont("Helvetica", 12)
        c.drawString(30*mm, height - 30*mm, "Test PDF Generation")
        c.drawString(30*mm, height - 40*mm, f"Generated at: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        
        # Save the PDF
        c.save()
        
        print(f"PDF created successfully: {filename}")
        print(f"File size: {os.path.getsize(filename)} bytes")
        
        # Clean up test file
        os.remove(filename)
        print("Test file cleaned up")
        
        return True
    except Exception as e:
        print(f"Error generating PDF: {e}")
        return False

if __name__ == "__main__":
    if test_pdf_generation():
        print("ReportLab is working correctly!")
    else:
        print("There was an issue with ReportLab.")