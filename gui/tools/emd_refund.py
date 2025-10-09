"""
EMD Refund Tool - Generate EMD refund receipts and documentation
Desktop implementation for EMD refund processing
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime, timedelta
import os
from pathlib import Path
from utils.pdf_generator import PDFGenerator

class EMDRefundTool:
    def __init__(self, db_manager, settings, parent=None):
        """Initialize EMD Refund tool window"""
        self.db_manager = db_manager
        self.settings = settings
        self.pdf_generator = PDFGenerator(settings)
        
        # Create tool window
        if parent is not None:
            self.window = ctk.CTkToplevel(parent)
        else:
            self.window = ctk.CTkToplevel()
        self.setup_window()
        self.create_interface()
    
    def setup_window(self):
        """Configure tool window"""
        self.window.title("EMD Refund - Generate EMD refund receipts and documentation")
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
            text="💰 EMD Refund Calculator & Generator",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color="white"
        )
        title_label.pack(pady=15)
        
        # Main content
        main_frame = ctk.CTkFrame(self.window)
        main_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Input form
        self.create_input_form(main_frame)
        
        # Calculation results
        self.create_results_section(main_frame)
        
        # Action buttons
        self.create_action_buttons(main_frame)
        
        # Recent EMD records
        self.create_recent_records_section(main_frame)
    
    def create_input_form(self, parent):
        """Create input form for EMD details"""
        form_frame = ctk.CTkFrame(parent)
        form_frame.pack(fill="x", padx=10, pady=5)
        
        # Form title
        form_title = ctk.CTkLabel(
            form_frame,
            text="EMD Details",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        form_title.pack(pady=(10, 15))
        
        # Input fields
        fields_frame = ctk.CTkFrame(form_frame)
        fields_frame.pack(fill="x", padx=10, pady=5)
        
        # Tender Number
        ctk.CTkLabel(fields_frame, text="Tender Number:", font=ctk.CTkFont(weight="bold")).grid(
            row=0, column=0, padx=10, pady=5, sticky="w"
        )
        self.tender_number_entry = ctk.CTkEntry(fields_frame, width=250, placeholder_text="Enter tender number")
        self.tender_number_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        
        # Contractor Name
        ctk.CTkLabel(fields_frame, text="Contractor Name:", font=ctk.CTkFont(weight="bold")).grid(
            row=1, column=0, padx=10, pady=5, sticky="w"
        )
        self.contractor_entry = ctk.CTkEntry(fields_frame, width=250, placeholder_text="Enter contractor name")
        self.contractor_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        # EMD Amount
        ctk.CTkLabel(fields_frame, text="EMD Amount (₹):", font=ctk.CTkFont(weight="bold")).grid(
            row=2, column=0, padx=10, pady=5, sticky="w"
        )
        self.emd_amount_entry = ctk.CTkEntry(fields_frame, width=250, placeholder_text="Enter EMD amount")
        self.emd_amount_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        
        # Bank Name
        ctk.CTkLabel(fields_frame, text="Bank Name:", font=ctk.CTkFont(weight="bold")).grid(
            row=0, column=2, padx=10, pady=5, sticky="w"
        )
        self.bank_name_entry = ctk.CTkEntry(fields_frame, width=250, placeholder_text="Enter bank name")
        self.bank_name_entry.grid(row=0, column=3, padx=10, pady=5, sticky="ew")
        
        # Guarantee Number
        ctk.CTkLabel(fields_frame, text="Guarantee Number:", font=ctk.CTkFont(weight="bold")).grid(
            row=1, column=2, padx=10, pady=5, sticky="w"
        )
        self.guarantee_number_entry = ctk.CTkEntry(fields_frame, width=250, placeholder_text="Enter guarantee number")
        self.guarantee_number_entry.grid(row=1, column=3, padx=10, pady=5, sticky="ew")
        
        # Validity Date
        ctk.CTkLabel(fields_frame, text="Validity Date:", font=ctk.CTkFont(weight="bold")).grid(
            row=2, column=2, padx=10, pady=5, sticky="w"
        )
        self.validity_date_entry = ctk.CTkEntry(fields_frame, width=250, placeholder_text="YYYY-MM-DD")
        self.validity_date_entry.grid(row=2, column=3, padx=10, pady=5, sticky="ew")
        
        # Calculate button
        calc_btn = ctk.CTkButton(
            fields_frame,
            text="🧮 Calculate Refund",
            command=self.calculate_refund,
            width=200,
            height=35
        )
        calc_btn.grid(row=3, column=1, columnspan=2, pady=15)
        
        # Configure grid weights
        fields_frame.grid_columnconfigure(1, weight=1)
        fields_frame.grid_columnconfigure(3, weight=1)
    
    def create_results_section(self, parent):
        """Create results display section"""
        self.results_frame = ctk.CTkFrame(parent, height=150)
        self.results_frame.pack(fill="x", padx=10, pady=5)
        self.results_frame.pack_propagate(False)
        
        # Results title
        results_title = ctk.CTkLabel(
            self.results_frame,
            text="Refund Calculation Results",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        results_title.pack(pady=(10, 5))
        
        # Results display area
        self.results_display = ctk.CTkFrame(self.results_frame)
        self.results_display.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Initial message
        self.no_calc_label = ctk.CTkLabel(
            self.results_display,
            text="Enter EMD details above and click 'Calculate Refund' to see results",
            font=ctk.CTkFont(size=14),
            text_color="#666666"
        )
        self.no_calc_label.pack(pady=40)
    
    def create_action_buttons(self, parent):
        """Create action buttons with magenta color scheme"""
        button_frame = ctk.CTkFrame(parent, height=80)
        button_frame.pack(fill="x", padx=10, pady=5)
        button_frame.pack_propagate(False)
        
        # Button container
        btn_container = ctk.CTkFrame(button_frame)
        btn_container.pack(pady=15)
        
        # Save EMD button (Magenta)
        self.save_btn = ctk.CTkButton(
            btn_container,
            text="💾 Save EMD Record",
            command=self.save_emd_record,
            width=150,
            height=35,
            state="disabled",
            fg_color="#c71585",        # Magenta
            hover_color="#9b0e66"      # Darker magenta
        )
        self.save_btn.pack(side="left", padx=5)
        
        # Generate PDF button (Bright magenta)
        self.pdf_btn = ctk.CTkButton(
            btn_container,
            text="📄 Generate PDF",
            command=self.generate_pdf,
            width=150,
            height=35,
            state="disabled",
            fg_color="#ff00ff",        # Bright magenta
            hover_color="#cc00cc"      # Darker bright magenta
        )
        self.pdf_btn.pack(side="left", padx=5)
        
        # Preview Receipt button (Hot pink)
        self.preview_btn = ctk.CTkButton(
            btn_container,
            text="👁️ Preview Receipt",
            command=self.preview_hand_receipt,
            width=150,
            height=35,
            state="disabled",
            fg_color="#ff69b4",        # Hot pink
            hover_color="#ff1493"      # Deep pink
        )
        self.preview_btn.pack(side="left", padx=5)
        
        # Clear form button (Gray)
        clear_btn = ctk.CTkButton(
            btn_container,
            text="🗑️ Clear Form",
            command=self.clear_form,
            width=150,
            height=35,
            fg_color="gray",
            hover_color="#555555"
        )
        clear_btn.pack(side="left", padx=5)
    
    def create_recent_records_section(self, parent):
        """Create recent EMD records section"""
        recent_frame = ctk.CTkFrame(parent)
        recent_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Section title
        recent_title = ctk.CTkLabel(
            recent_frame,
            text="Recent EMD Records",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        recent_title.pack(pady=(10, 5))
        
        # Records list
        self.records_listbox = ctk.CTkScrollableFrame(recent_frame, height=120)
        self.records_listbox.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Load recent records
        self.load_recent_records()
    
    def display_calculation_results(self, emd_amount, refund_amount, penalty, status, color, days_diff):
        """Display calculation results"""
        # Clear previous results
        for widget in self.results_display.winfo_children():
            widget.destroy()
        
        # Results grid
        results_grid = ctk.CTkFrame(self.results_display)
        results_grid.pack(fill="both", expand=True, padx=10, pady=10)
        
        # EMD Amount
        ctk.CTkLabel(results_grid, text="Original EMD Amount:", font=ctk.CTkFont(weight="bold")).grid(
            row=0, column=0, padx=10, pady=5, sticky="w"
        )
        ctk.CTkLabel(results_grid, text=f"₹ {emd_amount:,.2f}", font=ctk.CTkFont(size=14)).grid(
            row=0, column=1, padx=10, pady=5, sticky="w"
        )
        
        # Penalty
        if penalty > 0:
            ctk.CTkLabel(results_grid, text="Penalty Amount:", font=ctk.CTkFont(weight="bold")).grid(
                row=1, column=0, padx=10, pady=5, sticky="w"
            )
            ctk.CTkLabel(results_grid, text=f"₹ {penalty:,.2f}", font=ctk.CTkFont(size=14), text_color="#EF4444").grid(
                row=1, column=1, padx=10, pady=5, sticky="w"
            )
        
        # Refund Amount
        ctk.CTkLabel(results_grid, text="Refund Amount:", font=ctk.CTkFont(weight="bold", size=16)).grid(
            row=2, column=0, padx=10, pady=10, sticky="w"
        )
        ctk.CTkLabel(results_grid, text=f"₹ {refund_amount:,.2f}", 
                    font=ctk.CTkFont(size=18, weight="bold"), text_color=color).grid(
            row=2, column=1, padx=10, pady=10, sticky="w"
        )
        
        # Status
        ctk.CTkLabel(results_grid, text="Status:", font=ctk.CTkFont(weight="bold")).grid(
            row=3, column=0, padx=10, pady=5, sticky="w"
        )
        status_label = ctk.CTkLabel(results_grid, text=status, font=ctk.CTkFont(size=12), text_color=color)
        status_label.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        
        # Configure grid
        results_grid.grid_columnconfigure(1, weight=1)
    
    def calculate_refund(self):
        """Calculate EMD refund based on validity and rules"""
        try:
            # Validate inputs
            tender_number = self.tender_number_entry.get().strip()
            contractor_name = self.contractor_entry.get().strip()
            emd_amount_str = self.emd_amount_entry.get().strip()
            validity_date_str = self.validity_date_entry.get().strip()
            
            if not all([tender_number, contractor_name, emd_amount_str, validity_date_str]):
                messagebox.showerror("Validation Error", "Please fill in all required fields.")
                return
            
            try:
                emd_amount = float(emd_amount_str)
            except ValueError:
                messagebox.showerror("Validation Error", "Please enter a valid EMD amount.")
                return
            
            try:
                validity_date = datetime.strptime(validity_date_str, "%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Validation Error", "Please enter validity date in YYYY-MM-DD format.")
                return
            
            # Calculate refund
            current_date = datetime.now()
            days_difference = (current_date - validity_date).days
            
            # Determine refund eligibility and amount
            if validity_date >= current_date:
                # Valid EMD - full refund
                refund_amount = emd_amount
                refund_status = "Eligible for Full Refund"
                status_color = "#10B981"  # Green
                penalty = 0
            elif days_difference <= 30:
                # Expired but within 30 days - 90% refund
                penalty = emd_amount * 0.10
                refund_amount = emd_amount - penalty
                refund_status = f"Eligible for Refund with 10% penalty ({days_difference} days late)"
                status_color = "#F59E0B"  # Orange
            elif days_difference <= 90:
                # Expired 31-90 days - 50% refund
                penalty = emd_amount * 0.50
                refund_amount = emd_amount - penalty
                refund_status = f"Eligible for 50% Refund ({days_difference} days late)"
                status_color = "#EF4444"  # Red
            else:
                # Expired more than 90 days - no refund
                penalty = emd_amount
                refund_amount = 0
                refund_status = f"Not eligible for refund ({days_difference} days expired)"
                status_color = "#DC2626"  # Dark red
            
            # Display results
            self.display_calculation_results(
                emd_amount, refund_amount, penalty, refund_status, status_color, days_difference
            )
            
            # Store calculation data
            self.current_calculation = {
                'tender_number': tender_number,
                'contractor_name': contractor_name,
                'emd_amount': emd_amount,
                'bank_name': self.bank_name_entry.get().strip(),
                'guarantee_number': self.guarantee_number_entry.get().strip(),
                'validity_date': validity_date_str,
                'refund_amount': refund_amount,
                'refund_status': refund_status,
                'penalty': penalty,
                'days_difference': days_difference
            }
            
            # Enable action buttons
            self.save_btn.configure(state="normal")
            self.pdf_btn.configure(state="normal")
            self.preview_btn.configure(state="normal")
            
        except Exception as e:
            messagebox.showerror("Calculation Error", f"Failed to calculate refund: {str(e)}")

    def save_emd_record(self):
        """Save EMD record to database"""
        if not hasattr(self, 'current_calculation'):
            messagebox.showerror("Error", "Please calculate refund first.")
            return
        
        try:
            calc = self.current_calculation
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            success = self.db_manager.execute_query('''
                INSERT INTO emd_records (
                    tender_number, contractor_name, emd_amount, bank_name,
                    guarantee_number, validity_date, refund_status, refund_amount, date_created
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                calc['tender_number'], calc['contractor_name'], calc['emd_amount'],
                calc['bank_name'], calc['guarantee_number'], calc['validity_date'],
                calc['refund_status'], calc['refund_amount'], current_time
            ))
            
            if success:
                messagebox.showinfo("Success", "EMD record saved successfully!")
                self.load_recent_records()  # Refresh the list
            else:
                messagebox.showerror("Error", "Failed to save EMD record.")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save EMD record: {str(e)}")
    
    def generate_pdf(self):
        """Generate PDF for EMD refund using the new hand receipt format"""
        if not hasattr(self, 'current_calculation'):
            messagebox.showerror("Error", "Please calculate refund first.")
            return
        
        try:
            calc = self.current_calculation
            
            # Choose save location
            file_path = filedialog.asksaveasfilename(
                title="Save EMD Refund Hand Receipt PDF",
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf")],
                initialfile=f"EMD_Refund_{calc['tender_number']}_{datetime.now().strftime('%Y%m%d')}.pdf"
            )
            
            if file_path:
                # Generate HTML receipt first
                html_content = self.generate_hand_receipt_html(
                    calc['contractor_name'],
                    calc['refund_amount'],
                    f"EMD Refund for Tender {calc['tender_number']}"
                )
                
                # Save HTML temporarily
                temp_html_path = file_path.replace('.pdf', '.html')
                with open(temp_html_path, 'w', encoding='utf-8') as f:
                    f.write(html_content)
                
                # Convert HTML to PDF
                if self.pdf_generator.html_to_pdf(temp_html_path, file_path):
                    # Remove temporary HTML file
                    try:
                        os.remove(temp_html_path)
                    except:
                        pass
                    
                    messagebox.showinfo("Success", f"Hand receipt PDF generated successfully!\nSaved to: {file_path}")
                    
                    # Ask if user wants to open the file
                    if messagebox.askyesno("Open File", "Would you like to open the generated hand receipt PDF?"):
                        os.startfile(file_path)
                else:
                    # Remove temporary HTML file
                    try:
                        os.remove(temp_html_path)
                    except:
                        pass
                    messagebox.showerror("Error", "Failed to generate PDF from HTML.")
                    
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate hand receipt PDF: {str(e)}")
    
    def preview_hand_receipt(self):
        """Preview the hand receipt HTML in browser"""
        if not hasattr(self, 'current_calculation'):
            messagebox.showerror("Error", "Please calculate refund first.")
            return
        
        try:
            calc = self.current_calculation
            
            # Generate HTML receipt
            html_content = self.generate_hand_receipt_html(
                calc['contractor_name'],
                calc['refund_amount'],
                f"EMD Refund for Tender {calc['tender_number']}"
            )
            
            # Save preview file
            preview_path = Path("exports") / "preview_hand_receipt.html"
            preview_path.parent.mkdir(exist_ok=True)
            
            with open(preview_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            # Open preview
            os.startfile(str(preview_path))
            
        except Exception as e:
            messagebox.showerror("Preview Error", f"Failed to generate preview:\n{str(e)}")

    def clear_form(self):
        """Clear all form fields"""
        self.tender_number_entry.delete(0, "end")
        self.contractor_entry.delete(0, "end")
        self.emd_amount_entry.delete(0, "end")
        self.bank_name_entry.delete(0, "end")
        self.guarantee_number_entry.delete(0, "end")
        self.validity_date_entry.delete(0, "end")
        
        # Clear results
        for widget in self.results_display.winfo_children():
            widget.destroy()
        
        self.no_calc_label = ctk.CTkLabel(
            self.results_display,
            text="Enter EMD details above and click 'Calculate Refund' to see results",
            font=ctk.CTkFont(size=14),
            text_color="#666666"
        )
        self.no_calc_label.pack(pady=40)
        
        # Disable action buttons
        self.save_btn.configure(state="disabled")
        self.pdf_btn.configure(state="disabled")
        self.preview_btn.configure(state="disabled")
        
        # Clear calculation data
        if hasattr(self, 'current_calculation'):
            delattr(self, 'current_calculation')
    
    def load_recent_records(self):
        """Load and display recent EMD records"""
        try:
            # Clear existing items
            for widget in self.records_listbox.winfo_children():
                widget.destroy()
            
            # Fetch recent records
            records = self.db_manager.fetch_all('''
                SELECT tender_number, contractor_name, emd_amount, refund_amount, refund_status, date_created
                FROM emd_records 
                ORDER BY date_created DESC 
                LIMIT 10
            ''')
            
            if records:
                for record in records:
                    record_frame = ctk.CTkFrame(self.records_listbox)
                    record_frame.pack(fill="x", padx=5, pady=2)
                    
                    # Record info
                    info_text = f"Tender: {record[0]} | Contractor: {record[1]} | EMD: ₹{record[2]:,.2f} | Refund: ₹{record[3]:,.2f}"
                    info_label = ctk.CTkLabel(
                        record_frame,
                        text=info_text,
                        font=ctk.CTkFont(size=11)
                    )
                    info_label.pack(side="left", padx=10, pady=5)
                    
                    # Status
                    status_color = "#10B981" if "Full Refund" in record[4] else "#F59E0B" if "penalty" in record[4] else "#EF4444"
                    status_label = ctk.CTkLabel(
                        record_frame,
                        text=record[4][:30] + "..." if len(record[4]) > 30 else record[4],
                        font=ctk.CTkFont(size=10),
                        text_color=status_color
                    )
                    status_label.pack(side="right", padx=10, pady=5)
            else:
                no_records_label = ctk.CTkLabel(
                    self.records_listbox,
                    text="No EMD records found. Calculate and save your first EMD refund above.",
                    font=ctk.CTkFont(size=12),
                    text_color="#666666"
                )
                no_records_label.pack(pady=20)
                
        except Exception as e:
            print(f"Error loading recent records: {e}")
    
    def generate_hand_receipt_html(self, contractor_name, amount, work_description="EMD Refund"):
        """Generate HTML content for hand receipt using the new format"""
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
            <h2>Payable to: - {contractor_name} ( Electric Contractor)</h2>
            <h2>HAND RECEIPT (RPWA 28)</h2>
            <p>(Referred to in PWF&A Rules 418,424,436 & 438)</p>
            <p>Division - PWD Electric Division, Udaipur</p>
        </div>
        <div class="details">
            <p>(1)Cash Book Voucher No. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Date &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
            <p>(2)Cheque No. and Date &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
            <p>(3) Pay for ECS Rs.{amount}/- (Rupees <span id="amount-words" class="amount-words">{self.convert_number_to_words(float(amount))} only</span>)</p>
            <p>(4) Paid by me</p>
            <p>(5) Received from The Executive Engineer PWD Electric Division, Udaipur the sum of Rs. {amount}/- (Rupees <span id="amount-words" class="amount-words">{self.convert_number_to_words(float(amount))} only</span>)</p>
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
            <p class="blue-text"> In Words Rupees: {self.convert_number_to_words(float(amount))} Only</p>
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

    def convert_number_to_words(self, num):
        """Convert number to words in Indian numbering system"""
        if num == 0:
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
        if num // 10000000:
            crores = num // 10000000
            if crores > 9:
                words += self.convert_number_to_words(crores) + crore
            else:
                words += ones[crores] + crore
            num %= 10000000

        # Lakhs
        if num // 100000:
            lakhs = num // 100000
            if lakhs > 9:
                words += self.convert_number_to_words(lakhs) + lakh
            else:
                words += ones[lakhs] + lakh
            num %= 100000

        # Thousands
        if num // 1000:
            thousands = num // 1000
            if thousands > 9:
                words += self.convert_number_to_words(thousands) + thousand
            else:
                words += ones[thousands] + thousand
            num %= 1000

        # Hundreds
        if num // 100:
            hundreds = num // 100
            if hundreds > 9:
                words += self.convert_number_to_words(hundreds) + hundred
            else:
                words += ones[hundreds] + hundred
            num %= 100

        # Tens and ones
        if num > 0:
            if words:
                words += and_
            if num < 10:
                words += ones[num]
            elif num < 20:
                words += teens[num - 10]
            else:
                words += tens[num // 10]
                if num % 10:
                    words += " " + ones[num % 10]

        return words.strip()
