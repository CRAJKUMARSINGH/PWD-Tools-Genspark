"""
Bill Note Sheet Tool - PWD documentation generator
Desktop implementation for creating bill note sheets
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime
import os
from pathlib import Path
from utils.pdf_generator import PDFGenerator

class BillNoteTool:
    def __init__(self, db_manager, settings, parent=None):
        """Initialize Bill Note Sheet tool window"""
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
        self.window.title("Bill Note Sheet - PWD Documentation Generator")
        self.window.geometry("800x600")
        self.window.minsize(700, 500)
        
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
            text="📝 Bill Note Sheet Generator",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        title_label.pack(pady=15)
        
        # Main content
        main_frame = ctk.CTkFrame(self.window)
        main_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Input form
        self.create_input_form(main_frame)
        
        # Action buttons
        self.create_action_buttons(main_frame)
        
        # Recent bills section
        self.create_recent_bills_section(main_frame)
    
    def create_input_form(self, parent):
        """Create input form for bill details"""
        form_frame = ctk.CTkFrame(parent)
        form_frame.pack(fill="x", padx=10, pady=5)
        
        # Form title
        form_title = ctk.CTkLabel(
            form_frame,
            text="Bill Details",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        form_title.pack(pady=(10, 15))
        
        # Input fields
        fields_frame = ctk.CTkFrame(form_frame)
        fields_frame.pack(fill="x", padx=10, pady=5)
        
        # Bill Number
        ctk.CTkLabel(fields_frame, text="Bill Number:", font=ctk.CTkFont(weight="bold")).grid(
            row=0, column=0, padx=10, pady=5, sticky="w"
        )
        self.bill_number_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Enter bill number")
        self.bill_number_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        
        # Contractor Name
        ctk.CTkLabel(fields_frame, text="Contractor Name:", font=ctk.CTkFont(weight="bold")).grid(
            row=1, column=0, padx=10, pady=5, sticky="w"
        )
        self.contractor_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Enter contractor name")
        self.contractor_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        # Work Description
        ctk.CTkLabel(fields_frame, text="Work Description:", font=ctk.CTkFont(weight="bold")).grid(
            row=2, column=0, padx=10, pady=5, sticky="w"
        )
        self.work_desc_entry = ctk.CTkTextbox(fields_frame, width=300, height=80)
        self.work_desc_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        
        # Bill Amount
        ctk.CTkLabel(fields_frame, text="Bill Amount (₹):", font=ctk.CTkFont(weight="bold")).grid(
            row=3, column=0, padx=10, pady=5, sticky="w"
        )
        self.bill_amount_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Enter bill amount")
        self.bill_amount_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")
        
        # Remarks
        ctk.CTkLabel(fields_frame, text="Remarks:", font=ctk.CTkFont(weight="bold")).grid(
            row=4, column=0, padx=10, pady=5, sticky="w"
        )
        self.remarks_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Optional remarks")
        self.remarks_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")
        
        # Configure grid weights
        fields_frame.grid_columnconfigure(1, weight=1)
    
    def create_action_buttons(self, parent):
        """Create action buttons"""
        button_frame = ctk.CTkFrame(parent, height=80)
        button_frame.pack(fill="x", padx=10, pady=5)
        button_frame.pack_propagate(False)
        
        # Button container
        btn_container = ctk.CTkFrame(button_frame)
        btn_container.pack(pady=15)
        
        # Save button
        save_btn = ctk.CTkButton(
            btn_container,
            text="💾 Save Bill",
            command=self.save_bill,
            width=150,
            height=35
        )
        save_btn.pack(side="left", padx=5)
        
        # Generate PDF button
        pdf_btn = ctk.CTkButton(
            btn_container,
            text="📄 Generate PDF",
            command=self.generate_pdf,
            width=150,
            height=35
        )
        pdf_btn.pack(side="left", padx=5)
        
        # Clear form button
        clear_btn = ctk.CTkButton(
            btn_container,
            text="🗑️ Clear Form",
            command=self.clear_form,
            width=150,
            height=35,
            fg_color="gray"
        )
        clear_btn.pack(side="left", padx=5)
    
    def create_recent_bills_section(self, parent):
        """Create recent bills section"""
        recent_frame = ctk.CTkFrame(parent)
        recent_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Section title
        recent_title = ctk.CTkLabel(
            recent_frame,
            text="Recent Bills",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        recent_title.pack(pady=(10, 5))
        
        # Bills list
        self.bills_listbox = ctk.CTkScrollableFrame(recent_frame, height=150)
        self.bills_listbox.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Load recent bills
        self.load_recent_bills()
    
    def save_bill(self):
        """Save bill to database"""
        try:
            # Validate inputs
            bill_number = self.bill_number_entry.get().strip()
            contractor_name = self.contractor_entry.get().strip()
            work_description = self.work_desc_entry.get("1.0", "end-1c").strip()
            bill_amount_str = self.bill_amount_entry.get().strip()
            remarks = self.remarks_entry.get().strip()
            
            if not all([bill_number, contractor_name, work_description, bill_amount_str]):
                messagebox.showerror("Validation Error", "Please fill in all required fields.")
                return
            
            try:
                bill_amount = float(bill_amount_str)
            except ValueError:
                messagebox.showerror("Validation Error", "Please enter a valid bill amount.")
                return
            
            # Save to database
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            success = self.db_manager.execute_query('''
                INSERT INTO bills (bill_number, contractor_name, work_description, 
                                 bill_amount, date_created, status, remarks)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (bill_number, contractor_name, work_description, bill_amount, 
                  current_time, 'Active', remarks))
            
            if success:
                messagebox.showinfo("Success", "Bill saved successfully!")
                self.load_recent_bills()  # Refresh the list
            else:
                messagebox.showerror("Error", "Failed to save bill. Bill number might already exist.")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save bill: {str(e)}")
    
    def generate_pdf(self):
        """Generate PDF for the current bill"""
        try:
            # Validate inputs
            bill_number = self.bill_number_entry.get().strip()
            contractor_name = self.contractor_entry.get().strip()
            work_description = self.work_desc_entry.get("1.0", "end-1c").strip()
            bill_amount_str = self.bill_amount_entry.get().strip()
            remarks = self.remarks_entry.get().strip()
            
            if not all([bill_number, contractor_name, work_description, bill_amount_str]):
                messagebox.showerror("Validation Error", "Please fill in all required fields.")
                return
            
            try:
                bill_amount = float(bill_amount_str)
            except ValueError:
                messagebox.showerror("Validation Error", "Please enter a valid bill amount.")
                return
            
            # Prepare bill data
            bill_data = {
                'bill_number': bill_number,
                'contractor_name': contractor_name,
                'work_description': work_description,
                'bill_amount': bill_amount,
                'remarks': remarks,
                'date_created': datetime.now().strftime('%d/%m/%Y')
            }
            
            # Choose save location
            file_path = filedialog.asksaveasfilename(
                title="Save Bill Note Sheet PDF",
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf")],
                initialname=f"Bill_Note_{bill_number}_{datetime.now().strftime('%Y%m%d')}.pdf"
            )
            
            if file_path:
                # Generate PDF
                if self.pdf_generator.create_bill_note_pdf(bill_data, file_path):
                    messagebox.showinfo("Success", f"PDF generated successfully!\nSaved to: {file_path}")
                    
                    # Ask if user wants to open the file
                    if messagebox.askyesno("Open File", "Would you like to open the generated PDF?"):
                        os.startfile(file_path)
                else:
                    messagebox.showerror("Error", "Failed to generate PDF.")
                    
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate PDF: {str(e)}")
    
    def clear_form(self):
        """Clear all form fields"""
        self.bill_number_entry.delete(0, "end")
        self.contractor_entry.delete(0, "end")
        self.work_desc_entry.delete("1.0", "end")
        self.bill_amount_entry.delete(0, "end")
        self.remarks_entry.delete(0, "end")
    
    def load_recent_bills(self):
        """Load and display recent bills"""
        try:
            # Clear existing items
            for widget in self.bills_listbox.winfo_children():
                widget.destroy()
            
            # Fetch recent bills
            bills = self.db_manager.fetch_all('''
                SELECT bill_number, contractor_name, bill_amount, date_created, status
                FROM bills 
                ORDER BY date_created DESC 
                LIMIT 10
            ''')
            
            if bills:
                for bill in bills:
                    bill_frame = ctk.CTkFrame(self.bills_listbox)
                    bill_frame.pack(fill="x", padx=5, pady=2)
                    
                    # Bill info
                    info_text = f"Bill: {bill[0]} | Contractor: {bill[1]} | Amount: ₹{bill[2]:,.2f} | Date: {bill[3]}"
                    info_label = ctk.CTkLabel(
                        bill_frame,
                        text=info_text,
                        font=ctk.CTkFont(size=11)
                    )
                    info_label.pack(side="left", padx=10, pady=5)
                    
                    # Load button
                    load_btn = ctk.CTkButton(
                        bill_frame,
                        text="Load",
                        command=lambda b=bill: self.load_bill_data(b),
                        width=60,
                        height=25
                    )
                    load_btn.pack(side="right", padx=10, pady=5)
            else:
                no_bills_label = ctk.CTkLabel(
                    self.bills_listbox,
                    text="No bills found. Create your first bill above.",
                    font=ctk.CTkFont(size=12),
                    text_color="#666666"
                )
                no_bills_label.pack(pady=20)
                
        except Exception as e:
            print(f"Error loading recent bills: {e}")
    
    def load_bill_data(self, bill_tuple):
        """Load bill data into form"""
        try:
            # Get full bill data
            bill_data = self.db_manager.fetch_one('''
                SELECT bill_number, contractor_name, work_description, bill_amount, remarks
                FROM bills 
                WHERE bill_number = ?
            ''', (bill_tuple[0],))
            
            if bill_data:
                # Clear form first
                self.clear_form()
                
                # Load data
                self.bill_number_entry.insert(0, bill_data[0])
                self.contractor_entry.insert(0, bill_data[1])
                self.work_desc_entry.insert("1.0", bill_data[2])
                self.bill_amount_entry.insert(0, str(bill_data[3]))
                if bill_data[4]:  # remarks
                    self.remarks_entry.insert(0, bill_data[4])
                    
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load bill data: {str(e)}")
    
    def focus(self):
        """Bring window to focus"""
        self.window.lift()
        self.window.focus_force()
