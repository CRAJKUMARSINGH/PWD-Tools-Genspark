"""
PDF Generation Utilities for PWD Tools Desktop Application
"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from datetime import datetime
import os

class PDFGenerator:
    """Utility class for generating PDF reports"""
    
    def __init__(self, settings=None):
        self.settings = settings
        self.styles = getSampleStyleSheet()
        self.page_width, self.page_height = A4
        
    def generate_bill_note_pdf(self, filename, bill_data):
        """Generate PDF for bill note sheet"""
        try:
            doc = SimpleDocTemplate(filename, pagesize=A4)
            story = []
            
            # Title
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=self.styles['Heading1'],
                fontSize=16,
                spaceAfter=30,
                alignment=1  # Center alignment
            )
            title = Paragraph("BILL NOTE SHEET", title_style)
            story.append(title)
            
            # Bill details
            data = [
                ['Bill Number:', bill_data.get('bill_number', '')],
                ['Contractor Name:', bill_data.get('contractor_name', '')],
                ['Work Description:', bill_data.get('work_description', '')],
                ['Bill Amount:', f"₹{bill_data.get('bill_amount', 0):,.2f}"],
                ['Date Created:', bill_data.get('date_created', datetime.now().strftime('%Y-%m-%d'))],
                ['Status:', bill_data.get('status', 'Active')]
            ]
            
            table = Table(data, colWidths=[2*inch, 4*inch])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (0, -1), colors.grey),
                ('TEXTCOLOR', (0, 0), (0, -1), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
                ('BACKGROUND', (1, 0), (1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            
            story.append(table)
            doc.build(story)
            return True
            
        except Exception as e:
            print(f"Error generating PDF: {e}")
            return False
    
    def create_bill_note_pdf(self, bill_data, file_path):
        """Create bill note PDF (wrapper method)"""
        return self.generate_bill_note_pdf(file_path, bill_data)
    
    def html_to_pdf(self, html_file, pdf_file):
        """Convert HTML file to PDF (placeholder implementation)"""
        try:
            # This is a simplified implementation
            # In production, you'd use weasyprint or similar
            from reportlab.pdfgen import canvas
            from reportlab.lib.pagesizes import A4
            
            c = canvas.Canvas(pdf_file, pagesize=A4)
            c.drawString(100, 750, "HTML to PDF conversion")
            c.drawString(100, 700, f"Source: {html_file}")
            c.drawString(100, 650, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            c.save()
            return True
        except Exception as e:
            print(f"Error converting HTML to PDF: {e}")
            return False
    
    def generate_emd_refund_pdf(self, filename, emd_data):
        """Generate PDF for EMD refund calculation"""
        try:
            doc = SimpleDocTemplate(filename, pagesize=A4)
            story = []
            
            # Title
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=self.styles['Heading1'],
                fontSize=16,
                spaceAfter=30,
                alignment=1
            )
            title = Paragraph("EMD REFUND CALCULATION", title_style)
            story.append(title)
            
            # EMD details
            data = [
                ['Tender Number:', emd_data.get('tender_number', '')],
                ['Contractor Name:', emd_data.get('contractor_name', '')],
                ['EMD Amount:', f"₹{emd_data.get('emd_amount', 0):,.2f}"],
                ['Bank Name:', emd_data.get('bank_name', '')],
                ['Validity Date:', emd_data.get('validity_date', '')],
                ['Refund Status:', emd_data.get('refund_status', '')],
                ['Refund Amount:', f"₹{emd_data.get('refund_amount', 0):,.2f}"]
            ]
            
            table = Table(data, colWidths=[2*inch, 4*inch])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (0, -1), colors.grey),
                ('TEXTCOLOR', (0, 0), (0, -1), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
                ('BACKGROUND', (1, 0), (1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            
            story.append(table)
            doc.build(story)
            return True
            
        except Exception as e:
            print(f"Error generating PDF: {e}")
            return False
    
    def generate_delay_calculation_pdf(self, filename, delay_data):
        """Generate PDF for delay calculation"""
        try:
            doc = SimpleDocTemplate(filename, pagesize=A4)
            story = []
            
            # Title
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=self.styles['Heading1'],
                fontSize=16,
                spaceAfter=30,
                alignment=1
            )
            title = Paragraph("DELAY CALCULATION REPORT", title_style)
            story.append(title)
            
            # Delay details
            data = [
                ['Work Name:', delay_data.get('work_name', '')],
                ['Start Date:', delay_data.get('start_date', '')],
                ['Completion Date:', delay_data.get('completion_date', '')],
                ['Total Days:', str(delay_data.get('total_days', 0))],
                ['Delay Days:', str(delay_data.get('delay_days', 0))],
                ['Status:', delay_data.get('status', '')],
                ['Penalty Amount:', f"₹{delay_data.get('penalty_amount', 0):,.2f}"]
            ]
            
            table = Table(data, colWidths=[2*inch, 4*inch])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (0, -1), colors.grey),
                ('TEXTCOLOR', (0, 0), (0, -1), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
                ('BACKGROUND', (1, 0), (1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            
            story.append(table)
            doc.build(story)
            return True
            
        except Exception as e:
            print(f"Error generating PDF: {e}")
            return False
    
    def create_bill_note_pdf(self, bill_data, file_path):
        """Create bill note PDF (wrapper method)"""
        return self.generate_bill_note_pdf(file_path, bill_data)
    
    def html_to_pdf(self, html_file, pdf_file):
        """Convert HTML file to PDF (placeholder implementation)"""
        try:
            # This is a simplified implementation
            # In production, you'd use weasyprint or similar
            from reportlab.pdfgen import canvas
            from reportlab.lib.pagesizes import A4
            
            c = canvas.Canvas(pdf_file, pagesize=A4)
            c.drawString(100, 750, "HTML to PDF conversion")
            c.drawString(100, 700, f"Source: {html_file}")
            c.drawString(100, 650, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            c.save()
            return True
        except Exception as e:
            print(f"Error converting HTML to PDF: {e}")
            return False
