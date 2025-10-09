#!/usr/bin/env python3
"""
Test script for hand receipt generation
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from gui.tools.emd_refund import EMDRefundTool
import tempfile
import tkinter as tk
from tkinter import messagebox

class MockDBManager:
    def execute_query(self, query, params=None):
        print(f"Mock DB Query: {query}")
        print(f"Mock DB Params: {params}")
        return True
    
    def fetch_all(self, query):
        print(f"Mock DB Fetch All: {query}")
        return []

class MockSettings:
    def get_department_info(self):
        return {
            'name': 'Public Works Department',
            'office': 'PWD Office, Udaipur'
        }

def test_hand_receipt_generation():
    """Test the hand receipt generation functionality"""
    print("Testing hand receipt generation...")
    
    # Create a simple Tkinter root for testing
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    # Create mock dependencies
    db_manager = MockDBManager()
    settings = MockSettings()
    
    # Create EMD Refund tool instance
    tool = EMDRefundTool(db_manager, settings)
    
    # Test number to words conversion
    print("\nTesting number to words conversion:")
    test_amounts = [0, 1, 15, 25, 100, 1000, 15000, 250000, 1500000, 25000000]
    for amount in test_amounts:
        words = tool.convert_number_to_words(amount)
        print(f"  {amount:,} -> {words}")
    
    # Test HTML generation
    print("\nTesting HTML generation:")
    html_content = tool.generate_hand_receipt_html(
        "Test Contractor",
        150000,
        "Test Work Description"
    )
    
    # Save to a temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
        f.write(html_content)
        temp_path = f.name
    
    print(f"  HTML receipt generated and saved to: {temp_path}")
    print(f"  HTML content length: {len(html_content)} characters")
    
    # Clean up
    os.unlink(temp_path)
    
    print("\nAll tests completed successfully!")

if __name__ == "__main__":
    test_hand_receipt_generation()