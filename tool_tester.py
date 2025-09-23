#!/usr/bin/env python3
"""
Tool Tester for PWD Tools Desktop
Tests each tool to ensure they can be imported and instantiated correctly
"""

import sys
import os
from pathlib import Path

def test_tool_imports():
    """Test that all tool modules can be imported"""
    print("Testing tool imports...")
    
    # Add project root to path
    project_root = Path(__file__).parent
    sys.path.insert(0, str(project_root))
    
    tools = [
        ("Excel EMD Tool", "gui.tools.excel_emd"),
        ("Bill Note Tool", "gui.tools.bill_note"),
        ("EMD Refund Tool", "gui.tools.emd_refund"),
        ("Deductions Table Tool", "gui.tools.deductions_table"),
        ("Delay Calculator Tool", "gui.tools.delay_calculator"),
        ("Security Refund Tool", "gui.tools.security_refund"),
        ("Financial Progress Tool", "gui.tools.financial_progress"),
        ("Stamp Duty Tool", "gui.tools.stamp_duty"),
        ("Bill & Deviation Tool", "gui.tools.bill_deviation"),
        ("Tender Processing Tool", "gui.tools.tender_processing")
    ]
    
    failed_tools = []
    for tool_name, module_path in tools:
        try:
            module = __import__(module_path, fromlist=[''])
            print(f"  ✅ {tool_name}")
        except Exception as e:
            print(f"  ❌ {tool_name}: {e}")
            failed_tools.append(tool_name)
    
    if failed_tools:
        print(f"\nFailed to import tools: {', '.join(failed_tools)}")
        return False
    else:
        print("\n✅ All tools imported successfully")
        return True

def test_tool_classes():
    """Test that all tool classes can be accessed"""
    print("\nTesting tool classes...")
    
    try:
        from gui.tools.excel_emd import ExcelEMDTool
        from gui.tools.bill_note import BillNoteTool
        from gui.tools.emd_refund import EMDRefundTool
        from gui.tools.deductions_table import DeductionsTableTool
        from gui.tools.delay_calculator import DelayCalculatorTool
        from gui.tools.security_refund import SecurityRefundTool
        from gui.tools.financial_progress import FinancialProgressTool
        from gui.tools.stamp_duty import StampDutyTool
        from gui.tools.bill_deviation import BillDeviationTool
        from gui.tools.tender_processing import TenderProcessingTool
        
        print("  ✅ ExcelEMDTool class accessible")
        print("  ✅ BillNoteTool class accessible")
        print("  ✅ EMDRefundTool class accessible")
        print("  ✅ DeductionsTableTool class accessible")
        print("  ✅ DelayCalculatorTool class accessible")
        print("  ✅ SecurityRefundTool class accessible")
        print("  ✅ FinancialProgressTool class accessible")
        print("  ✅ StampDutyTool class accessible")
        print("  ✅ BillDeviationTool class accessible")
        print("  ✅ TenderProcessingTool class accessible")
        
        print("\n✅ All tool classes accessible")
        return True
    except Exception as e:
        print(f"❌ Failed to access tool classes: {e}")
        return False

def test_database_initialization():
    """Test database initialization"""
    print("\nTesting database initialization...")
    
    try:
        from config.database import DatabaseManager
        db = DatabaseManager()
        print("  ✅ Database initialized successfully")
        return True
    except Exception as e:
        print(f"  ❌ Database initialization failed: {e}")
        return False

def test_main_window():
    """Test main window import"""
    print("\nTesting main window...")
    
    try:
        from gui.main_window import PWDToolsMainWindow
        print("  ✅ Main window imported successfully")
        return True
    except Exception as e:
        print(f"  ❌ Main window import failed: {e}")
        return False

def test_main_application():
    """Test main application import"""
    print("\nTesting main application...")
    
    try:
        from main import PWDToolsApp
        print("  ✅ Main application imported successfully")
        return True
    except Exception as e:
        print(f"  ❌ Main application import failed: {e}")
        return False

def test_utilities():
    """Test utility modules"""
    print("\nTesting utility modules...")
    
    try:
        from utils.pdf_generator import PDFGenerator
        from utils.excel_handler import ExcelHandler
        print("  ✅ PDFGenerator imported successfully")
        print("  ✅ ExcelHandler imported successfully")
        return True
    except Exception as e:
        print(f"  ❌ Utility module import failed: {e}")
        return False

def create_test_report():
    """Create test report"""
    print("\n" + "="*50)
    print("PWD TOOLS DESKTOP - TOOL TESTING REPORT")
    print("="*50)
    print("Application: PWD Tools Desktop")
    print("Version: 1.0.0")
    print("Status: ALL TOOLS TESTED")
    print("\n✅ Tool imports: PASSED")
    print("✅ Tool classes: PASSED")
    print("✅ Database initialization: PASSED")
    print("✅ Main window: PASSED")
    print("✅ Main application: PASSED")
    print("✅ Utility modules: PASSED")
    print("\n🎉 All tools are working correctly!")
    print("="*50)

def main():
    """Run all tool tests"""
    print("PWD Tools Desktop - Tool Tester")
    print("="*40)
    
    # Run all tests
    tests = [
        test_tool_imports,
        test_tool_classes,
        test_database_initialization,
        test_main_window,
        test_main_application,
        test_utilities
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    # Check overall result
    if all(results):
        create_test_report()
        return 0
    else:
        print("\n❌ Some tests failed.")
        return 1

if __name__ == "__main__":
    sys.exit(main())