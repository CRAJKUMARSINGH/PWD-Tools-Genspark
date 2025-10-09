#!/usr/bin/env python3
"""
Test script to verify that both EMD tools use the same receipt template
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Test imports
try:
    from gui.tools.emd_refund import EMDRefundTool
    from gui.tools.excel_emd import ExcelEMDTool
    print("✅ Both modules imported successfully!")
except Exception as e:
    print(f"❌ Import failed: {e}")
    sys.exit(1)

# Mock classes for testing
class MockDBManager:
    def execute_query(self, query, params=None):
        return True
    
    def fetch_all(self, query):
        return []

class MockSettings:
    def get_department_info(self):
        return {
            'name': 'Public Works Department',
            'office': 'PWD Office, Udaipur'
        }

class MockExcelHandler:
    pass

def test_template_consistency():
    """Test that both tools generate consistent HTML templates"""
    print("\n Testing template consistency...")
    
    # Create mock instances
    db_manager = MockDBManager()
    settings = MockSettings()
    
    # Test EMD Refund tool
    try:
        emd_refund_tool = EMDRefundTool(db_manager, settings)
        refund_html = emd_refund_tool.generate_hand_receipt_html(
            "Test Contractor", 
            150000, 
            "Test Work Description"
        )
        print("✅ EMD Refund tool HTML generation works")
    except Exception as e:
        print(f"❌ EMD Refund tool failed: {e}")
        return False
    
    # Test Excel EMD tool
    try:
        excel_emd_tool = ExcelEMDTool(db_manager, settings)
        excel_html = excel_emd_tool.generate_receipt_html(
            "Test Payee",
            150000,
            "Test Work Description"
        )
        print("✅ Excel EMD tool HTML generation works")
    except Exception as e:
        print(f"❌ Excel EMD tool failed: {e}")
        return False
    
    # Check that both contain key elements from the template
    key_elements = [
        "Hand Receipt (RPWA 28)",
        "PWD Electric Division, Udaipur",
        "Cash Book Voucher No",
        "Cheque No. and Date",
        "Pay for ECS Rs",
        "Received from The Executive Engineer",
        "Name of work for which payment is made",
        "Chargeable to Head:- 8443 [EMD-Refund]",
        "signature-area",
        "offices",
        "seal-container",
        "bottom-left-box"
    ]
    
    print("\n Checking for required template elements...")
    for element in key_elements:
        if element in refund_html and element in excel_html:
            print(f"  ✅ {element}")
        else:
            print(f"  ❌ {element} - Missing in one or both templates")
            return False
    
    print("\n 🎉 All tests passed! Both tools use consistent templates.")
    return True

def test_number_conversion():
    """Test number to words conversion in both tools"""
    print("\n Testing number to words conversion...")
    
    db_manager = MockDBManager()
    settings = MockSettings()
    
    # Test EMD Refund tool
    emd_refund_tool = EMDRefundTool(db_manager, settings)
    refund_words = emd_refund_tool.convert_number_to_words(150000)
    print(f"  EMD Refund: 150000 -> {refund_words}")
    
    # Test Excel EMD tool
    excel_emd_tool = ExcelEMDTool(db_manager, settings)
    excel_words = excel_emd_tool.amount_to_words(150000)
    print(f"  Excel EMD: 150000 -> {excel_words}")
    
    # They should be the same
    if refund_words == excel_words:
        print("  ✅ Both tools produce the same number to words conversion")
        return True
    else:
        print("  ❌ Tools produce different conversions")
        return False

if __name__ == "__main__":
    print("Testing EMD Receipt Template Consistency")
    print("=" * 50)
    
    success = True
    success &= test_template_consistency()
    success &= test_number_conversion()
    
    if success:
        print("\n 🎉 All tests passed! Both EMD tools are now consistent.")
    else:
        print("\n ❌ Some tests failed. Please check the implementation.")
        sys.exit(1)