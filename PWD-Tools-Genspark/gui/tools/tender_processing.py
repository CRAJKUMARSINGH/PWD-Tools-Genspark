"""
Tender Processing Tool - Comprehensive tender management and processing
Desktop implementation for tender document processing and management
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime
import json

class TenderProcessingTool:
    def __init__(self, db_manager, settings, parent=None):
        """Initialize Tender Processing tool window"""
        self.db_manager = db_manager
        self.settings = settings
        
        # Create tool window
        if parent is not None:
            self.window = ctk.CTkToplevel(parent)
        else:
            self.window = ctk.CTkToplevel()
        self.setup_window()
        self.create_interface()
    
    def setup_window(self):
        """Configure tool window"""
        self.window.title("Tender Processing - Comprehensive tender management")
        self.window.geometry("900x600")
        self.window.minsize(800, 500)
        
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
            text="📋 Tender Processing Tool",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        title_label.pack(pady=15)
        
        # Main content
        main_frame = ctk.CTkFrame(self.window)
        main_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Input form
        self.create_input_form(main_frame)
        
        # Results section
        self.create_results_section(main_frame)
        
        # Action buttons
        self.create_action_buttons(main_frame)
    
    def create_input_form(self, parent):
        """Create input form for tender details"""
        form_frame = ctk.CTkFrame(parent)
        form_frame.pack(fill="x", padx=10, pady=5)
        
        # Form title
        form_title = ctk.CTkLabel(
            form_frame,
            text="Tender Information",
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
        self.tender_number_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Enter tender number")
        self.tender_number_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        
        # Work Description
        ctk.CTkLabel(fields_frame, text="Work Description:", font=ctk.CTkFont(weight="bold")).grid(
            row=1, column=0, padx=10, pady=5, sticky="w"
        )
        self.work_description_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Enter work description")
        self.work_description_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        # Estimated Cost
        ctk.CTkLabel(fields_frame, text="Estimated Cost (₹):", font=ctk.CTkFont(weight="bold")).grid(
            row=2, column=0, padx=10, pady=5, sticky="w"
        )
        self.estimated_cost_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="Enter estimated cost")
        self.estimated_cost_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        
        # Tender Type
        ctk.CTkLabel(fields_frame, text="Tender Type:", font=ctk.CTkFont(weight="bold")).grid(
            row=3, column=0, padx=10, pady=5, sticky="w"
        )
        self.tender_type_var = ctk.StringVar(value="Open Tender")
        tender_type_menu = ctk.CTkOptionMenu(
            fields_frame,
            variable=self.tender_type_var,
            values=["Open Tender", "Limited Tender", "Single Tender", "Emergency Tender"],
            width=300
        )
        tender_type_menu.grid(row=3, column=1, padx=10, pady=5, sticky="ew")
        
        # Publication Date
        ctk.CTkLabel(fields_frame, text="Publication Date:", font=ctk.CTkFont(weight="bold")).grid(
            row=4, column=0, padx=10, pady=5, sticky="w"
        )
        self.publication_date_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="YYYY-MM-DD")
        self.publication_date_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")
        
        # Submission Deadline
        ctk.CTkLabel(fields_frame, text="Submission Deadline:", font=ctk.CTkFont(weight="bold")).grid(
            row=5, column=0, padx=10, pady=5, sticky="w"
        )
        self.submission_deadline_entry = ctk.CTkEntry(fields_frame, width=300, placeholder_text="YYYY-MM-DD HH:MM")
        self.submission_deadline_entry.grid(row=5, column=1, padx=10, pady=5, sticky="ew")
        
        # Process button
        process_btn = ctk.CTkButton(
            fields_frame,
            text="🔄 Process Tender",
            command=self.process_tender,
            width=200,
            height=35
        )
        process_btn.grid(row=6, column=0, columnspan=2, pady=15)
        
        # Configure grid weights
        fields_frame.grid_columnconfigure(1, weight=1)
    
    def create_results_section(self, parent):
        """Create results display section"""
        self.results_frame = ctk.CTkFrame(parent)
        self.results_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Results title
        results_title = ctk.CTkLabel(
            self.results_frame,
            text="Tender Processing Results",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        results_title.pack(pady=(10, 5))
        
        # Results display area
        self.results_display = ctk.CTkFrame(self.results_frame)
        self.results_display.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Initial message
        self.no_process_label = ctk.CTkLabel(
            self.results_display,
            text="Enter tender details and click 'Process Tender' to see analysis",
            font=ctk.CTkFont(size=14),
            text_color="#666666"
        )
        self.no_process_label.pack(pady=40)
    
    def create_action_buttons(self, parent):
        """Create action buttons"""
        button_frame = ctk.CTkFrame(parent, height=80)
        button_frame.pack(fill="x", padx=10, pady=5)
        button_frame.pack_propagate(False)
        
        # Button container
        btn_container = ctk.CTkFrame(button_frame)
        btn_container.pack(pady=15)
        
        # Generate documents button
        self.generate_btn = ctk.CTkButton(
            btn_container,
            text="📄 Generate Documents",
            command=self.generate_documents,
            width=180,
            height=35,
            state="disabled"
        )
        self.generate_btn.pack(side="left", padx=5)
        
        # Save tender button
        self.save_btn = ctk.CTkButton(
            btn_container,
            text="💾 Save Tender",
            command=self.save_tender,
            width=150,
            height=35,
            state="disabled"
        )
        self.save_btn.pack(side="left", padx=5)
        
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
    
    def process_tender(self):
        """Process tender information and generate analysis"""
        try:
            # Validate inputs
            tender_number = self.tender_number_entry.get().strip()
            work_description = self.work_description_entry.get().strip()
            estimated_cost_str = self.estimated_cost_entry.get().strip()
            tender_type = self.tender_type_var.get()
            publication_date_str = self.publication_date_entry.get().strip()
            submission_deadline_str = self.submission_deadline_entry.get().strip()
            
            if not all([tender_number, work_description, estimated_cost_str, publication_date_str, submission_deadline_str]):
                messagebox.showerror("Validation Error", "Please fill in all required fields.")
                return
            
            try:
                estimated_cost = float(estimated_cost_str)
            except ValueError:
                messagebox.showerror("Validation Error", "Please enter a valid estimated cost.")
                return
            
            try:
                publication_date = datetime.strptime(publication_date_str, "%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Validation Error", "Please enter publication date in YYYY-MM-DD format.")
                return
            
            try:
                submission_deadline = datetime.strptime(submission_deadline_str, "%Y-%m-%d %H:%M")
            except ValueError:
                try:
                    submission_deadline = datetime.strptime(submission_deadline_str, "%Y-%m-%d")
                except ValueError:
                    messagebox.showerror("Validation Error", "Please enter submission deadline in YYYY-MM-DD or YYYY-MM-DD HH:MM format.")
                    return
            
            # Calculate tender analysis
            current_date = datetime.now()
            
            # Calculate timeline
            tender_duration = (submission_deadline - publication_date).days
            days_remaining = (submission_deadline - current_date).days
            
            # Determine tender status
            if days_remaining > 0:
                status = "Active"
                status_color = "#10B981"
            elif days_remaining == 0:
                status = "Due Today"
                status_color = "#F59E0B"
            else:
                status = "Expired"
                status_color = "#EF4444"
            
            # Calculate EMD and other requirements
            emd_amount = estimated_cost * 0.02  # 2% of estimated cost
            performance_guarantee = estimated_cost * 0.05  # 5% of estimated cost
            
            # Determine tender category based on cost
            if estimated_cost <= 100000:
                category = "Small Works"
                approval_level = "Executive Engineer"
            elif estimated_cost <= 1000000:
                category = "Medium Works"
                approval_level = "Superintending Engineer"
            elif estimated_cost <= 10000000:
                category = "Major Works"
                approval_level = "Chief Engineer"
            else:
                category = "Mega Projects"
                approval_level = "Government"
            
            # Display results
            self.display_tender_results({
                'tender_number': tender_number,
                'work_description': work_description,
                'estimated_cost': estimated_cost,
                'tender_type': tender_type,
                'publication_date': publication_date,
                'submission_deadline': submission_deadline,
                'tender_duration': tender_duration,
                'days_remaining': days_remaining,
                'status': status,
                'status_color': status_color,
                'emd_amount': emd_amount,
                'performance_guarantee': performance_guarantee,
                'category': category,
                'approval_level': approval_level
            })
            
            # Store processing data
            self.current_tender = {
                'tender_number': tender_number,
                'work_description': work_description,
                'estimated_cost': estimated_cost,
                'tender_type': tender_type,
                'publication_date': publication_date_str,
                'submission_deadline': submission_deadline_str,
                'status': status,
                'emd_amount': emd_amount,
                'category': category
            }
            
            # Enable action buttons
            self.generate_btn.configure(state="normal")
            self.save_btn.configure(state="normal")
            
        except Exception as e:
            messagebox.showerror("Processing Error", f"Failed to process tender: {str(e)}")
    
    def display_tender_results(self, data):
        """Display tender processing results"""
        # Clear previous results
        for widget in self.results_display.winfo_children():
            widget.destroy()
        
        # Tender information
        info_frame = ctk.CTkFrame(self.results_display)
        info_frame.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(info_frame, text="Tender Information", font=ctk.CTkFont(weight="bold", size=14)).pack(pady=(10, 5))
        
        info_details = [
            ("Tender Number", data['tender_number']),
            ("Work Description", data['work_description']),
            ("Estimated Cost", f"₹ {data['estimated_cost']:,.2f}"),
            ("Tender Type", data['tender_type']),
            ("Category", data['category']),
            ("Approval Level", data['approval_level'])
        ]
        
        for label, value in info_details:
            detail_frame = ctk.CTkFrame(info_frame)
            detail_frame.pack(fill="x", padx=10, pady=1)
            
            ctk.CTkLabel(detail_frame, text=f"{label}:", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=10, pady=3)
            ctk.CTkLabel(detail_frame, text=value).pack(side="right", padx=10, pady=3)
        
        # Timeline analysis
        timeline_frame = ctk.CTkFrame(self.results_display)
        timeline_frame.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(timeline_frame, text="Timeline Analysis", font=ctk.CTkFont(weight="bold", size=14)).pack(pady=(10, 5))
        
        # Status
        status_frame = ctk.CTkFrame(timeline_frame)
        status_frame.pack(fill="x", padx=10, pady=2)
        
        ctk.CTkLabel(status_frame, text="Status:", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=10, pady=3)
        ctk.CTkLabel(status_frame, text=data['status'], text_color=data['status_color'], font=ctk.CTkFont(weight="bold")).pack(side="right", padx=10, pady=3)
        
        # Timeline details
        timeline_details = [
            ("Publication Date", data['publication_date'].strftime('%d/%m/%Y')),
            ("Submission Deadline", data['submission_deadline'].strftime('%d/%m/%Y %H:%M')),
            ("Tender Duration", f"{data['tender_duration']} days"),
            ("Days Remaining", f"{data['days_remaining']} days" if data['days_remaining'] >= 0 else f"{abs(data['days_remaining'])} days overdue")
        ]
        
        for label, value in timeline_details:
            detail_frame = ctk.CTkFrame(timeline_frame)
            detail_frame.pack(fill="x", padx=10, pady=1)
            
            ctk.CTkLabel(detail_frame, text=f"{label}:", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=10, pady=3)
            ctk.CTkLabel(detail_frame, text=value).pack(side="right", padx=10, pady=3)
        
        # Financial requirements
        financial_frame = ctk.CTkFrame(self.results_display)
        financial_frame.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(financial_frame, text="Financial Requirements", font=ctk.CTkFont(weight="bold", size=14)).pack(pady=(10, 5))
        
        financial_details = [
            ("EMD Amount (2%)", f"₹ {data['emd_amount']:,.2f}"),
            ("Performance Guarantee (5%)", f"₹ {data['performance_guarantee']:,.2f}"),
            ("Estimated Cost", f"₹ {data['estimated_cost']:,.2f}")
        ]
        
        for label, value in financial_details:
            detail_frame = ctk.CTkFrame(financial_frame)
            detail_frame.pack(fill="x", padx=10, pady=1)
            
            ctk.CTkLabel(detail_frame, text=f"{label}:", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=10, pady=3)
            color = "#10B981" if "Amount" in label or "Guarantee" in label else None
            ctk.CTkLabel(detail_frame, text=value, text_color=color).pack(side="right", padx=10, pady=3)
    
    def generate_documents(self):
        """Generate tender documents"""
        try:
            if not hasattr(self, 'current_tender'):
                messagebox.showerror("Error", "Please process tender first.")
                return
            
            # Create document data
            doc_data = {
                'tender_number': self.current_tender['tender_number'],
                'work_description': self.current_tender['work_description'],
                'estimated_cost': self.current_tender['estimated_cost'],
                'tender_type': self.current_tender['tender_type'],
                'publication_date': self.current_tender['publication_date'],
                'submission_deadline': self.current_tender['submission_deadline'],
                'emd_amount': self.current_tender['emd_amount'],
                'category': self.current_tender['category'],
                'generation_date': datetime.now().strftime('%d/%m/%Y')
            }
            
            # Generate PDF using utility
            from utils.pdf_generator import PDFGenerator
            pdf_gen = PDFGenerator()
            
            filename = f"Tender_Document_{self.current_tender['tender_number'].replace('/', '_')}_{datetime.now().strftime('%Y%m%d')}.pdf"
            
            if pdf_gen.generate_tender_document(doc_data, filename):
                messagebox.showinfo("Success", f"Tender document generated: {filename}")
            else:
                messagebox.showerror("Error", "Failed to generate tender document.")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate documents: {str(e)}")
    
    def save_tender(self):
        """Save tender to database"""
        if not hasattr(self, 'current_tender'):
            messagebox.showerror("Error", "Please process tender first.")
            return
        
        try:
            tender = self.current_tender
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Note: This would require adding a tenders table to the database schema
            # For now, we'll save to a generic table or show a placeholder message
            
            messagebox.showinfo("Success", "Tender information processed successfully!\n\nNote: Database storage for tenders will be implemented in the next update.")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save tender: {str(e)}")
    
    def clear_form(self):
        """Clear all form fields"""
        self.tender_number_entry.delete(0, "end")
        self.work_description_entry.delete(0, "end")
        self.estimated_cost_entry.delete(0, "end")
        self.tender_type_var.set("Open Tender")
        self.publication_date_entry.delete(0, "end")
        self.submission_deadline_entry.delete(0, "end")
        
        # Clear results
        for widget in self.results_display.winfo_children():
            widget.destroy()
        
        self.no_process_label = ctk.CTkLabel(
            self.results_display,
            text="Enter tender details and click 'Process Tender' to see analysis",
            font=ctk.CTkFont(size=14),
            text_color="#666666"
        )
        self.no_process_label.pack(pady=40)
        
        # Disable action buttons
        self.generate_btn.configure(state="disabled")
        self.save_btn.configure(state="disabled")
        
        # Clear processing data
        if hasattr(self, 'current_tender'):
            delattr(self, 'current_tender')
    
    def focus(self):
        """Bring window to focus"""
        self.window.lift()
        self.window.focus_force()
