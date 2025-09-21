"""
Excel EMD Tool - Hand Receipt Generator from Excel files
Desktop implementation of the Excel se EMD functionality
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog
import pandas as pd
from datetime import datetime
import os
from pathlib import Path
from utils.pdf_generator import PDFGenerator
from utils.excel_handler import ExcelHandler

class ExcelEMDTool:
    def __init__(self, db_manager, settings, parent=None):
        """Initialize Excel EMD tool window"""
        self.db_manager = db_manager
        self.settings = settings
        self.pdf_generator = PDFGenerator(settings)
        self.excel_handler = ExcelHandler()
        
        # Create tool window
        if parent is not None:
            self.window = ctk.CTkToplevel(parent)
        else:
            self.window = ctk.CTkToplevel()
        self.setup_window()
        self.create_interface()
        
        # Data storage
        self.loaded_data = None
        self.processed_receipts = []
    
    def setup_window(self):
        """Configure tool window"""
        self.window.title("Excel se EMD - Hand Receipt Generator")
        self.window.geometry("900x700")
        self.window.minsize(800, 600)
        
        # Disable icon to prevent errors
        try:
            self.window.iconbitmap("")
        except:
            pass
        
        # Make window modal
        self.window.transient()
        self.window.grab_set()
    
    def focus(self):
        """Bring window to focus"""
        self.window.lift()
        self.window.focus_force()
    
    def create_interface(self):
        """Create the tool interface"""
        # Header
        header_frame = ctk.CTkFrame(self.window, height=60)
        header_frame.pack(fill="x", padx=10, pady=5)
        header_frame.pack_propagate(False)
        
        title_label = ctk.CTkLabel(
            header_frame,
            text="📊 Excel se EMD - Hand Receipt Generator",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        title_label.pack(pady=15)
        
        # Main content
        main_frame = ctk.CTkFrame(self.window)
        main_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # File upload section
        self.create_file_upload_section(main_frame)
        
        # Data preview section
        self.create_data_preview_section(main_frame)
        
        # Processing section
        self.create_processing_section(main_frame)
        
        # Results section
        self.create_results_section(main_frame)
    
    def create_file_upload_section(self, parent):
        """Create file upload section"""
        upload_frame = ctk.CTkFrame(parent)
        upload_frame.pack(fill="x", padx=10, pady=5)
        
        # Section title
        title_label = ctk.CTkLabel(
            upload_frame,
            text="📁 Step 1: Upload Excel File",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        title_label.pack(pady=(10, 5))
        
        # File selection
        file_frame = ctk.CTkFrame(upload_frame)
        file_frame.pack(fill="x", padx=10, pady=5)
        
        self.file_path_var = tk.StringVar()
        self.file_entry = ctk.CTkEntry(
            file_frame,
            textvariable=self.file_path_var,
            placeholder_text="Select Excel file containing EMD data...",
            width=500
        )
        self.file_entry.pack(side="left", padx=(10, 5), pady=10, expand=True, fill="x")
        
        browse_btn = ctk.CTkButton(
            file_frame,
            text="Browse",
            command=self.browse_file,
            width=100
        )
        browse_btn.pack(side="right", padx=(5, 10), pady=10)
        
        # Instructions
        instructions_label = ctk.CTkLabel(
            upload_frame,
            text="Expected columns: Payee Name, Amount, Work Description",
            font=ctk.CTkFont(size=12),
            text_color="#666666"
        )
        instructions_label.pack(pady=(0, 10))
    
    def create_data_preview_section(self, parent):
        """Create data preview section"""
        self.preview_frame = ctk.CTkFrame(parent)
        self.preview_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Section title
        preview_title = ctk.CTkLabel(
            self.preview_frame,
            text="👀 Step 2: Data Preview",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        preview_title.pack(pady=(10, 5))
        
        # Preview text widget (initially hidden)
        self.preview_text = ctk.CTkTextbox(
            self.preview_frame,
            height=200,
            state="disabled"
        )
        
        # No data message
        self.no_data_label = ctk.CTkLabel(
            self.preview_frame,
            text="No data loaded. Please select an Excel file above.",
            font=ctk.CTkFont(size=14),
            text_color="#888888"
        )
        self.no_data_label.pack(pady=50)
    
    def create_processing_section(self, parent):
        """Create processing controls section"""
        self.processing_frame = ctk.CTkFrame(parent, height=100)
        self.processing_frame.pack(fill="x", padx=10, pady=5)
        self.processing_frame.pack_propagate(False)
        
        # Section title
        process_title = ctk.CTkLabel(
            self.processing_frame,
            text="⚙️ Step 3: Generate Receipts",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        process_title.pack(pady=(10, 5))
        
        # Processing buttons
        button_frame = ctk.CTkFrame(self.processing_frame)
        button_frame.pack(pady=10)
        
        self.process_btn = ctk.CTkButton(
            button_frame,
            text="Generate All Receipts",
            command=self.process_all_receipts,
            state="disabled",
            width=200
        )
        self.process_btn.pack(side="left", padx=5)
        
        self.preview_btn = ctk.CTkButton(
            button_frame,
            text="Preview Single Receipt",
            command=self.preview_single_receipt,
            state="disabled",
            width=200
        )
        self.preview_btn.pack(side="left", padx=5)
    
    def create_results_section(self, parent):
        """Create results section"""
        self.results_frame = ctk.CTkFrame(parent, height=120)
        self.results_frame.pack(fill="x", padx=10, pady=5)
        self.results_frame.pack_propagate(False)
        
        # Section title
        results_title = ctk.CTkLabel(
            self.results_frame,
            text="📋 Step 4: Results",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        results_title.pack(pady=(10, 5))
        
        # Results display
        self.results_label = ctk.CTkLabel(
            self.results_frame,
            text="No receipts generated yet.",
            font=ctk.CTkFont(size=12),
            text_color="#666666"
        )
        self.results_label.pack(pady=10)
        
        # Export buttons (initially hidden)
        self.export_frame = ctk.CTkFrame(self.results_frame)
        
        self.open_folder_btn = ctk.CTkButton(
            self.export_frame,
            text="Open Export Folder",
            command=self.open_export_folder,
            width=150
        )
        self.open_folder_btn.pack(side="left", padx=5)
        
        self.save_to_db_btn = ctk.CTkButton(
            self.export_frame,
            text="Save to Database",
            command=self.save_to_database,
            width=150
        )
        self.save_to_db_btn.pack(side="left", padx=5)
    
    def browse_file(self):
        """Browse and select Excel file"""
        file_path = filedialog.askopenfilename(
            title="Select Excel File",
            filetypes=[
                ("Excel files", "*.xlsx *.xls"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            self.file_path_var.set(file_path)
            self.load_excel_data(file_path)
    
    def load_excel_data(self, file_path):
        """Load and validate Excel data"""
        try:
            # Load Excel file
            df = pd.read_excel(file_path)
            
            # Validate required columns
            required_columns = ['Payee Name', 'Amount', 'Work Description']
            missing_columns = [col for col in required_columns if col not in df.columns]
            
            if missing_columns:
                messagebox.showerror(
                    "Invalid File Format",
                    f"Missing required columns: {', '.join(missing_columns)}\n\n"
                    f"Expected columns: {', '.join(required_columns)}"
                )
                return
            
            # Clean and validate data
            df = df.dropna(subset=required_columns)
            df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
            df = df.dropna(subset=['Amount'])
            
            if df.empty:
                messagebox.showerror("No Valid Data", "No valid data found in the Excel file.")
                return
            
            self.loaded_data = df
            self.display_data_preview()
            self.enable_processing_buttons()
            
        except Exception as e:
            messagebox.showerror("Error Loading File", f"Failed to load Excel file:\n{str(e)}")
    
    def display_data_preview(self):
        """Display preview of loaded data"""
        if self.loaded_data is not None:
            # Hide no data message
            self.no_data_label.pack_forget()
            
            # Show preview
            self.preview_text.pack(fill="both", expand=True, padx=10, pady=(0, 10))
            
            # Populate preview
            preview_content = f"Loaded {len(self.loaded_data)} records:\n\n"
            preview_content += self.loaded_data.head(10).to_string(index=False)
            
            if len(self.loaded_data) > 10:
                preview_content += f"\n\n... and {len(self.loaded_data) - 10} more records"
            
            self.preview_text.configure(state="normal")
            self.preview_text.delete("1.0", "end")
            self.preview_text.insert("1.0", preview_content)
            self.preview_text.configure(state="disabled")
    
    def enable_processing_buttons(self):
        """Enable processing buttons when data is loaded"""
        self.process_btn.configure(state="normal")
        self.preview_btn.configure(state="normal")
    
    def preview_single_receipt(self):
        """Preview a single receipt"""
        if self.loaded_data is None or self.loaded_data.empty:
            return
        
        # Get first record for preview
        record = self.loaded_data.iloc[0]
        
        try:
            # Generate preview HTML
            html_content = self.generate_receipt_html(
                record['Payee Name'],
                record['Amount'],
                record['Work Description']
            )
            
            # Save preview file
            preview_path = Path("exports") / "preview_receipt.html"
            preview_path.parent.mkdir(exist_ok=True)
            
            with open(preview_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            # Open preview
            os.startfile(str(preview_path))
            
        except Exception as e:
            messagebox.showerror("Preview Error", f"Failed to generate preview:\n{str(e)}")
    
    def process_all_receipts(self):
        """Process all receipts from loaded data"""
        if self.loaded_data is None or self.loaded_data.empty:
            return
        
        try:
            # Create export directory
            export_dir = Path("exports") / f"emd_receipts_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            export_dir.mkdir(parents=True, exist_ok=True)
            
            processed_count = 0
            self.processed_receipts = []
            
            # Process each record
            for index, record in self.loaded_data.iterrows():
                try:
                    payee = str(record['Payee Name']).strip()
                    amount = float(record['Amount'])
                    work_desc = str(record['Work Description']).strip()
                    
                    # Generate HTML receipt
                    html_content = self.generate_receipt_html(payee, amount, work_desc)
                    
                    # Save HTML file
                    safe_filename = self.sanitize_filename(payee)
                    html_file = export_dir / f"{safe_filename}_receipt.html"
                    
                    with open(html_file, 'w', encoding='utf-8') as f:
                        f.write(html_content)
                    
                    # Generate PDF
                    pdf_file = export_dir / f"{safe_filename}_receipt.pdf"
                    self.pdf_generator.html_to_pdf(str(html_file), str(pdf_file))
                    
                    # Track processed receipt
                    self.processed_receipts.append({
                        'payee': payee,
                        'amount': amount,
                        'work_description': work_desc,
                        'html_file': str(html_file),
                        'pdf_file': str(pdf_file),
                        'date_generated': datetime.now().isoformat()
                    })
                    
                    processed_count += 1
                    
                except Exception as e:
                    print(f"Error processing record {index}: {e}")
                    continue
            
            # Update results
            self.update_results_display(processed_count, export_dir)
            
        except Exception as e:
            messagebox.showerror("Processing Error", f"Failed to process receipts:\n{str(e)}")
    
    def generate_receipt_html(self, payee, amount, work_description):
        """Generate HTML content for receipt"""
        dept_info = self.settings.get_department_info()
        
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hand Receipt (RPWA 28)</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 0; padding: 20px; }}
        .container {{ max-width: 800px; margin: 0 auto; border: 2px solid #000; padding: 20px; }}
        .header {{ text-align: center; margin-bottom: 20px; }}
        .title {{ font-size: 24px; font-weight: bold; margin-bottom: 10px; }}
        .subtitle {{ font-size: 18px; margin-bottom: 20px; }}
        .content {{ margin-bottom: 20px; }}
        .field {{ margin-bottom: 15px; }}
        .field-label {{ font-weight: bold; display: inline-block; width: 150px; }}
        .field-value {{ display: inline-block; border-bottom: 1px solid #000; min-width: 300px; }}
        .amount-section {{ background-color: #f0f0f0; padding: 15px; border: 1px solid #000; margin: 20px 0; }}
        .signature-section {{ margin-top: 40px; }}
        .signature-box {{ border: 1px solid #000; height: 60px; width: 200px; display: inline-block; margin-right: 50px; }}
        .footer {{ text-align: center; margin-top: 30px; font-size: 12px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="title">{dept_info.get('name', 'Public Works Department')}</div>
            <div class="subtitle">{dept_info.get('office', 'PWD Office, Udaipur')}</div>
            <div class="subtitle">HAND RECEIPT (RPWA 28)</div>
        </div>
        
        <div class="content">
            <div class="field">
                <span class="field-label">Receipt No.:</span>
                <span class="field-value">EMD-{datetime.now().strftime('%Y%m%d')}-{abs(hash(payee)) % 10000:04d}</span>
            </div>
            
            <div class="field">
                <span class="field-label">Date:</span>
                <span class="field-value">{datetime.now().strftime('%d/%m/%Y')}</span>
            </div>
            
            <div class="field">
                <span class="field-label">Received from:</span>
                <span class="field-value">{payee}</span>
            </div>
            
            <div class="field">
                <span class="field-label">Work Description:</span>
                <span class="field-value">{work_description}</span>
            </div>
            
            <div class="amount-section">
                <div class="field">
                    <span class="field-label">Amount (₹):</span>
                    <span class="field-value" style="font-size: 18px; font-weight: bold;">₹ {amount:,.2f}</span>
                </div>
                
                <div class="field">
                    <span class="field-label">Amount in Words:</span>
                    <span class="field-value">{self.amount_to_words(amount)} Rupees Only</span>
                </div>
            </div>
            
            <div class="field">
                <span class="field-label">Purpose:</span>
                <span class="field-value">Earnest Money Deposit (EMD)</span>
            </div>
            
            <div class="signature-section">
                <div style="float: left;">
                    <div>Received by:</div>
                    <div class="signature-box"></div>
                    <div>Signature & Stamp</div>
                </div>
                
                <div style="float: right;">
                    <div>Submitted by:</div>
                    <div class="signature-box"></div>
                    <div>Contractor Signature</div>
                </div>
                
                <div style="clear: both;"></div>
            </div>
        </div>
        
        <div class="footer">
            <p>This is a computer-generated receipt | PWD Tools Desktop v1.0.0</p>
            <p>Generated on: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</p>
        </div>
    </div>
</body>
</html>"""
        
        return html_content
    
    def amount_to_words(self, amount):
        """Convert amount to words (simplified version)"""
        # This is a simplified implementation
        # In production, you'd use a proper number-to-words library
        
        ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        
        def convert_hundreds(n):
            result = ''
            if n >= 100:
                result += ones[n // 100] + ' Hundred '
                n %= 100
            if n >= 20:
                result += tens[n // 10] + ' '
                n %= 10
            elif n >= 10:
                result += teens[n - 10] + ' '
                n = 0
            if n > 0:
                result += ones[n] + ' '
            return result.strip()
        
        if amount == 0:
            return 'Zero'
        
        # Handle crores, lakhs, thousands, hundreds
        crores = int(amount // 10000000)
        lakhs = int((amount % 10000000) // 100000)
        thousands = int((amount % 100000) // 1000)
        hundreds = int(amount % 1000)
        
        result = ''
        if crores > 0:
            result += convert_hundreds(crores) + ' Crore '
        if lakhs > 0:
            result += convert_hundreds(lakhs) + ' Lakh '
        if thousands > 0:
            result += convert_hundreds(thousands) + ' Thousand '
        if hundreds > 0:
            result += convert_hundreds(hundreds)
        
        return result.strip()
    
    def sanitize_filename(self, name):
        """Sanitize filename for safe file creation"""
        import re
        safe_name = re.sub(r'[^a-zA-Z0-9._-]', '_', name.strip())
        return safe_name[:50]  # Limit length
    
    def update_results_display(self, count, export_dir):
        """Update results display after processing"""
        self.results_label.configure(
            text=f"✅ Successfully generated {count} receipts\nExported to: {export_dir}",
            text_color="#10B981"
        )
        
        # Show export buttons
        self.export_frame.pack(pady=10)
        self.export_dir = export_dir
    
    def open_export_folder(self):
        """Open the export folder in file explorer"""
        if hasattr(self, 'export_dir'):
            os.startfile(str(self.export_dir))
    
    def save_to_database(self):
        """Save processed receipts to database"""
        if not self.processed_receipts:
            return
        
        try:
            for receipt in self.processed_receipts:
                # Insert into EMD records table
                self.db_manager.execute_query('''
                    INSERT INTO emd_records (
                        tender_number, contractor_name, emd_amount, bank_name,
                        guarantee_number, validity_date, refund_status, date_created
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    f"EMD-{datetime.now().strftime('%Y%m%d')}-{abs(hash(receipt['payee'])) % 10000:04d}",
                    receipt['payee'],
                    receipt['amount'],
                    'Cash/DD',  # Default bank
                    '',  # No guarantee number for cash
                    datetime.now().strftime('%Y-%m-%d'),  # Default validity
                    'Received',
                    receipt['date_generated']
                ))
            
            messagebox.showinfo("Success", f"Saved {len(self.processed_receipts)} records to database!")
            
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to save to database:\n{str(e)}")
    
    def focus(self):
        """Bring window to focus"""
        self.window.lift()
        self.window.focus_force()
