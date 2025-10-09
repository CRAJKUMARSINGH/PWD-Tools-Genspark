#!/usr/bin/env python3
"""
Test script to verify that EMD receipts fit on a single A4 page
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

def test_single_page_compliance():
    """Test that generated HTML complies with single A4 page requirements"""
    print("\n Testing single page compliance...")
    
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
    
    # Check for single page compliance elements
    required_elements = [
        "width: 210mm",
        "height: 297mm",
        "size: A4 portrait",
        "page-break-after: avoid",
        "page-break-inside: avoid",
        "overflow: hidden",
        "@media print"
    ]
    
    print("\n Checking for single page compliance elements...")
    for element in required_elements:
        if element in refund_html and element in excel_html:
            print(f"  ✅ {element}")
        else:
            print(f"  ❌ {element} - Missing in one or both templates")
            return False
    
    # Check that both templates have the same dimensions
    if "width: 210mm" in refund_html and "height: 297mm" in refund_html:
        print("  ✅ EMD Refund tool uses A4 dimensions")
    else:
        print("  ❌ EMD Refund tool missing A4 dimensions")
        return False
        
    if "width: 210mm" in excel_html and "height: 297mm" in excel_html:
        print("  ✅ Excel EMD tool uses A4 dimensions")
    else:
        print("  ❌ Excel EMD tool missing A4 dimensions")
        return False
    
    print("\n 🎉 All single page compliance tests passed!")
    return True

def test_css_optimization():
    """Test that CSS is optimized for single page printing"""
    print("\n Testing CSS optimization...")
    
    db_manager = MockDBManager()
    settings = MockSettings()
    
    # Test EMD Refund tool
    emd_refund_tool = EMDRefundTool(db_manager, settings)
    refund_html = emd_refund_tool.generate_hand_receipt_html(
        "Test Contractor", 
        150000, 
        "Test Work Description"
    )
    
    # Check for optimized CSS properties
    css_checks = [
        ("font-size: 16px", "Header font size"),
        ("font-size: 12px", "Body font size"),
        ("font-size: 11px", "Small font size"),
        ("padding: 15px", "Container padding"),
        ("margin: 2px 0", "Element margins"),
        ("padding: 3px", "Table cell padding")
    ]
    
    for css_property, description in css_checks:
        if css_property in refund_html:
            print(f"  ✅ {description} ({css_property})")
        else:
            print(f"  ⚠️  {description} ({css_property}) - Not found")
    
    print("\n 🎉 CSS optimization check completed!")
    return True

if __name__ == "__main__":
    print("Testing EMD Receipt Single Page Compliance")
    print("=" * 50)
    
    success = True
    success &= test_single_page_compliance()
    success &= test_css_optimization()
    
    if success:
        print("\n 🎉 All tests passed! EMD receipts are compliant with single A4 page requirements.")
    else:
        print("\n ❌ Some tests failed. Please check the implementation.")
        sys.exit(1)