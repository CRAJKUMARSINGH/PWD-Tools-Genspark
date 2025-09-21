"""
Bill & Deviation Generator - Generate bills with deviation tracking
Desktop implementation for infrastructure billing with deviation management
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime
import json

class BillDeviationTool:
    def __init__(self, db_manager, settings, parent=None):
        """Initialize Bill & Deviation Generator tool window"""
        self.db_manager = db_manager
        self.settings = settings
        
        # Create tool window
        if parent is not None:
            self.window = ctk.CTkToplevel(parent)
        else:
            self.window = ctk.CTkToplevel()
        self.setup_window()
        self.create_interface()
        
        # Initialize data
        self.bill_items = []
        self.deviation_items = []
    
    def setup_window(self):
        """Configure tool window"""
        self.window.title("Bill & Deviation Generator - Infrastructure billing with deviation tracking")
        self.window.geometry("1000x700")
        self.window.minsize(900, 600)
        
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
            text="🏗️ Bill & Deviation Generator",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        title_label.pack(pady=15)
        
        # Main content with notebook
        main_frame = ctk.CTkFrame(self.window)
        main_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Create tabbed interface
        from tkinter import ttk
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Bill Details Tab
        self.create_bill_tab()
        
        # Deviations Tab
        self.create_deviation_tab()
        
        # Generate Tab
        self.create_generate_tab()
    
    def create_bill_tab(self):
        """Create bill details tab"""
        bill_frame = ctk.CTkFrame(self.notebook)
        self.notebook.add(bill_frame, text="Bill Details")
        
        # Bill information form
        form_frame = ctk.CTkFrame(bill_frame)
        form_frame.pack(fill="x", padx=10, pady=10)
        
        ctk.CTkLabel(form_frame, text="Bill Information", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(10, 15))
        
        # Input fields
        fields_frame = ctk.CTkFrame(form_frame)
        fields_frame.pack(fill="x", padx=10, pady=5)
        
        # Bill Number
        ctk.CTkLabel(fields_frame, text="Bill Number:", font=ctk.CTkFont(weight="bold")).grid(
            row=0, column=0, padx=10, pady=5, sticky="w"
        )
        self.bill_number_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Enter bill number")
        self.bill_number_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        
        # Work Description
        ctk.CTkLabel(fields_frame, text="Work Description:", font=ctk.CTkFont(weight="bold")).grid(
            row=1, column=0, padx=10, pady=5, sticky="w"
        )
        self.work_description_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Enter work description")
        self.work_description_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        # Contractor Name
        ctk.CTkLabel(fields_frame, text="Contractor Name:", font=ctk.CTkFont(weight="bold")).grid(
            row=2, column=0, padx=10, pady=5, sticky="w"
        )
        self.contractor_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Enter contractor name")
        self.contractor_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        
        # Agreement Number
        ctk.CTkLabel(fields_frame, text="Agreement Number:", font=ctk.CTkFont(weight="bold")).grid(
            row=3, column=0, padx=10, pady=5, sticky="w"
        )
        self.agreement_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Enter agreement number")
        self.agreement_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")
        
        # Bill Period
        ctk.CTkLabel(fields_frame, text="Bill Period:", font=ctk.CTkFont(weight="bold")).grid(
            row=4, column=0, padx=10, pady=5, sticky="w"
        )
        self.bill_period_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="e.g., April 2024")
        self.bill_period_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")
        
        # Configure grid weights
        fields_frame.grid_columnconfigure(1, weight=1)
        
        # Bill items section
        items_frame = ctk.CTkFrame(bill_frame)
        items_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        ctk.CTkLabel(items_frame, text="Bill Items", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(10, 5))
        
        # Add item controls
        add_item_frame = ctk.CTkFrame(items_frame)
        add_item_frame.pack(fill="x", padx=10, pady=5)
        
        # Item entry fields
        item_fields_frame = ctk.CTkFrame(add_item_frame)
        item_fields_frame.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(item_fields_frame, text="Item Description:").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.item_desc_entry = ctk.CTkEntry(item_fields_frame, width=200, placeholder_text="Item description")
        self.item_desc_entry.grid(row=0, column=1, padx=5, pady=2)
        
        ctk.CTkLabel(item_fields_frame, text="Quantity:").grid(row=0, column=2, padx=5, pady=2, sticky="w")
        self.item_qty_entry = ctk.CTkEntry(item_fields_frame, width=100, placeholder_text="Qty")
        self.item_qty_entry.grid(row=0, column=3, padx=5, pady=2)
        
        ctk.CTkLabel(item_fields_frame, text="Rate:").grid(row=1, column=0, padx=5, pady=2, sticky="w")
        self.item_rate_entry = ctk.CTkEntry(item_fields_frame, width=100, placeholder_text="Rate")
        self.item_rate_entry.grid(row=1, column=1, padx=5, pady=2)
        
        ctk.CTkLabel(item_fields_frame, text="Unit:").grid(row=1, column=2, padx=5, pady=2, sticky="w")
        self.item_unit_entry = ctk.CTkEntry(item_fields_frame, width=100, placeholder_text="Unit")
        self.item_unit_entry.grid(row=1, column=3, padx=5, pady=2)
        
        # Add item button
        add_item_btn = ctk.CTkButton(
            add_item_frame,
            text="➕ Add Item",
            command=self.add_bill_item,
            width=120,
            height=30
        )
        add_item_btn.pack(pady=10)
    
    def create_deviation_tab(self):
        """Create deviation tracking tab"""
        deviation_frame = ctk.CTkFrame(self.notebook)
        self.notebook.add(deviation_frame, text="Deviations")
        
        # Deviation form
        form_frame = ctk.CTkFrame(deviation_frame)
        form_frame.pack(fill="x", padx=10, pady=10)
        
        ctk.CTkLabel(form_frame, text="Deviation Details", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(10, 15))
        
        # Deviation fields
        dev_fields_frame = ctk.CTkFrame(form_frame)
        dev_fields_frame.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(dev_fields_frame, text="Deviation Type:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.deviation_type_var = ctk.StringVar(value="Addition")
        deviation_type_menu = ctk.CTkOptionMenu(
            dev_fields_frame,
            variable=self.deviation_type_var,
            values=["Addition", "Deletion", "Modification", "Rate Change"],
            width=200
        )
        deviation_type_menu.grid(row=0, column=1, padx=5, pady=5)
        
        ctk.CTkLabel(dev_fields_frame, text="Description:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.deviation_desc_entry = ctk.CTkEntry(dev_fields_frame, width=300, placeholder_text="Deviation description")
        self.deviation_desc_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ctk.CTkLabel(dev_fields_frame, text="Original Amount:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.original_amount_entry = ctk.CTkEntry(dev_fields_frame, width=150, placeholder_text="Original amount")
        self.original_amount_entry.grid(row=2, column=1, padx=5, pady=5)
        
        ctk.CTkLabel(dev_fields_frame, text="Revised Amount:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.revised_amount_entry = ctk.CTkEntry(dev_fields_frame, width=150, placeholder_text="Revised amount")
        self.revised_amount_entry.grid(row=3, column=1, padx=5, pady=5)
        
        ctk.CTkLabel(dev_fields_frame, text="Justification:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.justification_entry = ctk.CTkEntry(dev_fields_frame, width=300, placeholder_text="Justification for deviation")
        self.justification_entry.grid(row=4, column=1, padx=5, pady=5)
        
        # Add deviation button
        add_dev_btn = ctk.CTkButton(
            dev_fields_frame,
            text="➕ Add Deviation",
            command=self.add_deviation,
            width=150,
            height=30
        )
        add_dev_btn.grid(row=5, column=0, columnspan=2, pady=15)
    
    def create_generate_tab(self):
        """Create generation and output tab"""
        generate_frame = ctk.CTkFrame(self.notebook)
        self.notebook.add(generate_frame, text="Generate Bill")
        
        # Summary section
        summary_frame = ctk.CTkFrame(generate_frame)
        summary_frame.pack(fill="x", padx=10, pady=10)
        
        ctk.CTkLabel(summary_frame, text="Bill Summary", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(10, 5))
        
        self.summary_display = ctk.CTkFrame(summary_frame)
        self.summary_display.pack(fill="x", padx=10, pady=5)
        
        # Initial summary message
        self.no_summary_label = ctk.CTkLabel(
            self.summary_display,
            text="Add bill items and deviations to see summary",
            font=ctk.CTkFont(size=14),
            text_color="#666666"
        )
        self.no_summary_label.pack(pady=20)
        
        # Generation controls
        controls_frame = ctk.CTkFrame(generate_frame)
        controls_frame.pack(fill="x", padx=10, pady=10)
        
        ctk.CTkLabel(controls_frame, text="Generate Documents", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(10, 15))
        
        # Generation buttons
        btn_frame = ctk.CTkFrame(controls_frame)
        btn_frame.pack(pady=10)
        
        update_summary_btn = ctk.CTkButton(
            btn_frame,
            text="🔄 Update Summary",
            command=self.update_summary,
            width=150,
            height=35
        )
        update_summary_btn.pack(side="left", padx=5)
        
        generate_pdf_btn = ctk.CTkButton(
            btn_frame,
            text="📄 Generate PDF",
            command=self.generate_bill_pdf,
            width=150,
            height=35
        )
        generate_pdf_btn.pack(side="left", padx=5)
        
        save_bill_btn = ctk.CTkButton(
            btn_frame,
            text="💾 Save Bill",
            command=self.save_bill,
            width=150,
            height=35
        )
        save_bill_btn.pack(side="left", padx=5)
    
    def add_bill_item(self):
        """Add item to bill"""
        try:
            description = self.item_desc_entry.get().strip()
            quantity_str = self.item_qty_entry.get().strip()
            rate_str = self.item_rate_entry.get().strip()
            unit = self.item_unit_entry.get().strip()
            
            if not all([description, quantity_str, rate_str, unit]):
                messagebox.showerror("Validation Error", "Please fill in all item fields.")
                return
            
            try:
                quantity = float(quantity_str)
                rate = float(rate_str)
            except ValueError:
                messagebox.showerror("Validation Error", "Please enter valid numeric values for quantity and rate.")
                return
            
            amount = quantity * rate
            
            item = {
                'description': description,
                'quantity': quantity,
                'rate': rate,
                'unit': unit,
                'amount': amount
            }
            
            self.bill_items.append(item)
            
            # Clear form
            self.item_desc_entry.delete(0, "end")
            self.item_qty_entry.delete(0, "end")
            self.item_rate_entry.delete(0, "end")
            self.item_unit_entry.delete(0, "end")
            
            messagebox.showinfo("Success", f"Item added: {description}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add item: {str(e)}")
    
    def add_deviation(self):
        """Add deviation to tracking"""
        try:
            deviation_type = self.deviation_type_var.get()
            description = self.deviation_desc_entry.get().strip()
            original_str = self.original_amount_entry.get().strip()
            revised_str = self.revised_amount_entry.get().strip()
            justification = self.justification_entry.get().strip()
            
            if not all([description, original_str, revised_str, justification]):
                messagebox.showerror("Validation Error", "Please fill in all deviation fields.")
                return
            
            try:
                original_amount = float(original_str)
                revised_amount = float(revised_str)
            except ValueError:
                messagebox.showerror("Validation Error", "Please enter valid numeric values for amounts.")
                return
            
            deviation_amount = revised_amount - original_amount
            
            deviation = {
                'type': deviation_type,
                'description': description,
                'original_amount': original_amount,
                'revised_amount': revised_amount,
                'deviation_amount': deviation_amount,
                'justification': justification
            }
            
            self.deviation_items.append(deviation)
            
            # Clear form
            self.deviation_desc_entry.delete(0, "end")
            self.original_amount_entry.delete(0, "end")
            self.revised_amount_entry.delete(0, "end")
            self.justification_entry.delete(0, "end")
            
            messagebox.showinfo("Success", f"Deviation added: {description}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add deviation: {str(e)}")
    
    def update_summary(self):
        """Update bill summary display"""
        # Clear previous summary
        for widget in self.summary_display.winfo_children():
            widget.destroy()
        
        if not self.bill_items and not self.deviation_items:
            self.no_summary_label = ctk.CTkLabel(
                self.summary_display,
                text="Add bill items and deviations to see summary",
                font=ctk.CTkFont(size=14),
                text_color="#666666"
            )
            self.no_summary_label.pack(pady=20)
            return
        
        # Calculate totals
        bill_total = sum(item['amount'] for item in self.bill_items)
        deviation_total = sum(dev['deviation_amount'] for dev in self.deviation_items)
        final_total = bill_total + deviation_total
        
        # Display summary
        ctk.CTkLabel(self.summary_display, text="Bill Summary", font=ctk.CTkFont(weight="bold", size=14)).pack(pady=(10, 5))
        
        # Bill items summary
        if self.bill_items:
            items_frame = ctk.CTkFrame(self.summary_display)
            items_frame.pack(fill="x", padx=10, pady=5)
            
            ctk.CTkLabel(items_frame, text=f"Bill Items ({len(self.bill_items)} items):", font=ctk.CTkFont(weight="bold")).pack(anchor="w", padx=10, pady=2)
            ctk.CTkLabel(items_frame, text=f"Total Amount: ₹ {bill_total:,.2f}", font=ctk.CTkFont(size=12)).pack(anchor="w", padx=20, pady=2)
        
        # Deviations summary
        if self.deviation_items:
            dev_frame = ctk.CTkFrame(self.summary_display)
            dev_frame.pack(fill="x", padx=10, pady=5)
            
            ctk.CTkLabel(dev_frame, text=f"Deviations ({len(self.deviation_items)} items):", font=ctk.CTkFont(weight="bold")).pack(anchor="w", padx=10, pady=2)
            ctk.CTkLabel(dev_frame, text=f"Net Deviation: ₹ {deviation_total:,.2f}", font=ctk.CTkFont(size=12)).pack(anchor="w", padx=20, pady=2)
        
        # Final total
        total_frame = ctk.CTkFrame(self.summary_display)
        total_frame.pack(fill="x", padx=10, pady=10)
        
        ctk.CTkLabel(total_frame, text="Final Bill Amount:", font=ctk.CTkFont(weight="bold", size=16)).pack(anchor="w", padx=10, pady=5)
        ctk.CTkLabel(total_frame, text=f"₹ {final_total:,.2f}", font=ctk.CTkFont(weight="bold", size=18), text_color="#10B981").pack(anchor="w", padx=20, pady=2)
    
    def generate_bill_pdf(self):
        """Generate PDF bill document"""
        try:
            if not self.bill_items:
                messagebox.showerror("Error", "Please add at least one bill item.")
                return
            
            # Collect bill data
            bill_data = {
                'bill_number': self.bill_number_entry.get().strip(),
                'work_description': self.work_description_entry.get().strip(),
                'contractor_name': self.contractor_entry.get().strip(),
                'agreement_number': self.agreement_entry.get().strip(),
                'bill_period': self.bill_period_entry.get().strip(),
                'bill_items': self.bill_items,
                'deviations': self.deviation_items,
                'generation_date': datetime.now().strftime('%d/%m/%Y')
            }
            
            # Generate PDF using utility
            from utils.pdf_generator import PDFGenerator
            pdf_gen = PDFGenerator()
            
            filename = f"Bill_Deviation_{bill_data['bill_number'].replace('/', '_')}_{datetime.now().strftime('%Y%m%d')}.pdf"
            
            if pdf_gen.generate_bill_deviation_report(bill_data, filename):
                messagebox.showinfo("Success", f"Bill PDF generated: {filename}")
            else:
                messagebox.showerror("Error", "Failed to generate bill PDF.")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate PDF: {str(e)}")
    
    def save_bill(self):
        """Save bill to database"""
        try:
            if not self.bill_items:
                messagebox.showerror("Error", "Please add at least one bill item.")
                return
            
            # Calculate totals
            bill_total = sum(item['amount'] for item in self.bill_items)
            deviation_total = sum(dev['deviation_amount'] for dev in self.deviation_items)
            final_total = bill_total + deviation_total
            
            # Save to database
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            success = self.db_manager.execute_query('''
                INSERT INTO bills (
                    bill_number, contractor_name, work_description, bill_amount,
                    date_created, status
                ) VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                self.bill_number_entry.get().strip(),
                self.contractor_entry.get().strip(),
                self.work_description_entry.get().strip(),
                final_total,
                current_time,
                'Generated'
            ))
            
            if success:
                messagebox.showinfo("Success", "Bill saved successfully!")
            else:
                messagebox.showerror("Error", "Failed to save bill.")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save bill: {str(e)}")
    
    def focus(self):
        """Bring window to focus"""
        self.window.lift()
        self.window.focus_force()
