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
        header_frame = ctk.CTkFrame(self.window, height=60, fg_color="#c71585")  # Magenta
        header_frame.pack(fill="x", padx=10, pady=5)
        header_frame.pack_propagate(False)
        
        title_label = ctk.CTkLabel(
            header_frame,
            text="📊 Excel se EMD - Hand Receipt Generator",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color="white"
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
        upload_title = ctk.CTkLabel(
            upload_frame,
            text="📁 Step 1: Upload Excel File",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        upload_title.pack(pady=(10, 5))
        
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
            width=100,
            fg_color="#c71585",        # Magenta
            hover_color="#9b0e66"      # Darker magenta
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
            width=200,
            fg_color="#c71585",        # Magenta
            hover_color="#9b0e66"      # Darker magenta
        )
        self.process_btn.pack(side="left", padx=5)
        
        self.preview_btn = ctk.CTkButton(
            button_frame,
            text="Preview Single Receipt",
            command=self.preview_single_receipt,
            state="disabled",
            width=200,
            fg_color="#ff69b4",        # Hot pink
            hover_color="#ff1493"      # Deep pink
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
            width=150,
            fg_color="#ff00ff",        # Bright magenta
            hover_color="#cc00cc"      # Darker bright magenta
        )
        self.open_folder_btn.pack(side="left", padx=5)
        
        self.save_to_db_btn = ctk.CTkButton(
            self.export_frame,
            text="Save to Database",
            command=self.save_to_database,
            width=150,
            fg_color="#da70d6",        # Orchid
            hover_color="#ba55d3"      # Medium orchid
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
        """Generate HTML content for receipt using the standardized template"""
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=210mm, height=297mm">
    <title>Hand Receipt (RPWA 28)</title>
    <style>
        body {{
            font-family: sans-serif;
            margin: 0;
            width: 210mm;
            height: 297mm;
            overflow: hidden;
        }}

        .container {{
            width: 210mm;
            height: 297mm;
            margin: 0 auto;
            border: 2px solid #ccc;
            padding: 15px;
            box-sizing: border-box;
            position: relative;
            page-break-after: avoid;
            page-break-inside: avoid;
        }}

        .header {{
            text-align: center;
            margin-bottom: 2px;
        }}

        .header h2 {{
            margin: 2px 0;
            font-size: 16px;
        }}

        .header p {{
            margin: 1px 0;
            font-size: 12px;
        }}

        .details {{
            margin-bottom: 1px;
            font-size: 12px;
        }}

        .details p {{
            margin: 2px 0;
        }}

        .amount-words {{
            font-style: italic;
        }}

        .signature-area {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
            font-size: 12px;
        }}

        .signature-area td, .signature-area th {{
            border: 1px solid #ccc;
            padding: 3px;
            text-align: left;
        }}

        .offices {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
            font-size: 11px;
        }}

        .offices td, .offices th {{
            border: 1px solid black;
            padding: 3px;
            text-align: left;
            word-wrap: break-word;
        }}

        .input-field {{
            border-bottom: 1px dotted #ccc;
            padding: 2px;
            width: calc(100% - 4px);
            display: inline-block;
            font-size: 12px;
        }}

        @media print {{
            .container {{
                border: none;
                width: 210mm;
                height: 297mm;
                margin: 0;
                padding: 10mm;
                page-break-after: avoid;
                page-break-inside: avoid;
            }}

            .input-field {{
                border: none;
            }}

            body {{
                margin: 0;
                width: 210mm;
                height: 297mm;
                overflow: hidden;
            }}

            @page {{
                size: A4 portrait;
                margin: 0;
                page-break-after: avoid;
            }}
        }}

        .seal-container {{
            position: absolute;
            left: 10mm;
            bottom: 10mm;
            width: 40mm;
            height: 25mm;
            z-index: 10;
        }}

        .seal {{
            max-width: 100%;
            max-height: 100%;
            text-align: center;
            line-height: 40mm;
            color: blue;
            display: flex;
            justify-content: space-around;
            align-items: center;
            font-size: 10px;
        }}

        .bottom-left-box {{
            position: absolute;
            bottom: 40mm;
            left: 40mm;
            border: 2px solid black;
            padding: 8px;
            width: 300px;
            text-align: left;
            height: auto;
            font-size: 12px;
        }}

        .bottom-left-box p {{
            margin: 2px 0;
        }}

        .bottom-left-box .blue-text {{
            color: blue;
        }}
    </style>
</head>

<body>
    <div class="container">
        <div class="header">
            <h2>Payable to: - {payee} ( Electric Contractor)</h2>
            <h2>HAND RECEIPT (RPWA 28)</h2>
            <p>(Referred to in PWF&A Rules 418,424,436 & 438)</p>
            <p>Division - PWD Electric Division, Udaipur</p>
        </div>
        <div class="details">
            <p>(1)Cash Book Voucher No. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Date &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
            <p>(2)Cheque No. and Date &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
            <p>(3) Pay for ECS Rs.{amount}/- (Rupees <span id="amount-words" class="amount-words">{self.amount_to_words(float(amount))} only</span>)</p>
            <p>(4) Paid by me</p>
            <p>(5) Received from The Executive Engineer PWD Electric Division, Udaipur the sum of Rs. {amount}/- (Rupees <span id="amount-words" class="amount-words">{self.amount_to_words(float(amount))} only</span>)</p>
            <p> Name of work for which payment is made: <span id="work-name" class="input-field">{work_description}</span></p>
            <p> Chargeable to Head:- 8443 [EMD-Refund] </p>   
            <table class="signature-area">
                <tr>
                    <td>Witness</td>
                    <td>Stamp</td>
                    <td>Signature of payee</td>
                </tr>
                <tr>
                    <td>Cash Book No. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Page No. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
                    <td></td>
                    <td></td>
                </tr>
            </table>
            <table class="offices">
                <tr>
                    <td>For use in the Divisional Office</td>
                    <td>For use in the Accountant General's office</td>
                </tr>
                <tr>
                    <td>Checked</td>
                    <td>Audited/Reviewed</td>
                </tr>
                <tr>
                    <td>Accounts Clerk</td>
                    <td>
                        DA &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Auditor &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Supdt. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; G.O.
                    </td>
                </tr>
            </table>
        </div>
        <div class="seal-container">
            <div class="seal">
                <p></p>
                <p></p>
                <p></p>
            </div>
        </div>
        <div class="bottom-left-box">
            <p class="blue-text"> Passed for Rs. {amount}</p>
            <p class="blue-text"> In Words Rupees: {self.amount_to_words(float(amount))} Only</p>
            <p class="blue-text"> Chargeable to Head:- 8443 [EMD-Refund]</p>
            <div class="seal">
                <p>Ar.</p>
                <p>D.A.</p>
                <p>E.E.</p>
            </div>
        </div>
    </div>
</body>
</html>"""
        
        return html_content
    
    def amount_to_words(self, amount):
        """Convert amount to words in Indian numbering system"""
        # Convert to integer to handle the amount properly
        amount = int(amount)
        
        if amount == 0:
            return "Zero"

        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        crore = " Crore "
        lakh = " Lakh "
        thousand = " Thousand "
        hundred = " Hundred "
        and_ = " and "

        words = ""

        # Crores
        if amount // 10000000:
            crores = amount // 10000000
            if crores > 9:
                words += self.amount_to_words(crores) + crore
            else:
                words += ones[crores] + crore
            amount %= 10000000

        # Lakhs
        if amount // 100000:
            lakhs = amount // 100000
            if lakhs > 9:
                words += self.amount_to_words(lakhs) + lakh
            else:
                words += ones[lakhs] + lakh
            amount %= 100000

        # Thousands
        if amount // 1000:
            thousands = amount // 1000
            if thousands > 9:
                words += self.amount_to_words(thousands) + thousand
            else:
                words += ones[thousands] + thousand
            amount %= 1000

        # Hundreds
        if amount // 100:
            hundreds = amount // 100
            if hundreds > 9:
                words += self.amount_to_words(hundreds) + hundred
            else:
                words += ones[hundreds] + hundred
            amount %= 100

        # Tens and ones
        if amount > 0:
            if words:
                words += and_
            if amount < 10:
                words += ones[amount]
            elif amount < 20:
                words += teens[amount - 10]
            else:
                words += tens[amount // 10]
                if amount % 10:
                    words += " " + ones[amount % 10]

        return words.strip()

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
