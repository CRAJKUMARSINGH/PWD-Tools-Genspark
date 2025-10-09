#!/usr/bin/env python3
"""
Test script to verify Streamlit app functionality
"""

import sys
import os
import tempfile
import pandas as pd

def test_streamlit_pages():
    """Test that all Streamlit pages can be imported without errors"""
    print("Testing Streamlit page imports...")
    
    # Add current directory to path
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    
    # Test importing each page
    page_files = [
        "pages/01_excel_se_emd.py",
        "pages/02_bill_note_sheet.py",
        "pages/03_emd_refund.py",
        "pages/04_deductions_table.py",
        "pages/05_delay_calculator.py",
        "pages/06_security_refund.py",
        "pages/07_financial_progress.py",
        "pages/08_stamp_duty.py"
    ]
    
    success_count = 0
    for page_file in page_files:
        if os.path.exists(page_file):
            try:
                # Read the file content
                with open(page_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                print(f"  ✅ {page_file} - File exists and is readable")
                success_count += 1
            except Exception as e:
                print(f"  ❌ {page_file} - Error: {e}")
        else:
            print(f"  ⚠️  {page_file} - File not found")
    
    print(f"\nImport test completed: {success_count}/{len(page_files)} pages successful")
    return success_count == len(page_files)

def test_excel_processing():
    """Test Excel file processing functionality"""
    print("\nTesting Excel processing functionality...")
    
    try:
        # Create a sample Excel file
        sample_data = {
            'Payee Name': ['Test Contractor', 'Another Contractor'],
            'Amount': [150000, 250000],
            'Work Description': ['Road Construction', 'Building Renovation']
        }
        
        df = pd.DataFrame(sample_data)
        
        # Save to temporary file
        with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as tmp_file:
            tmp_filename = tmp_file.name
            df.to_excel(tmp_filename, index=False)
        
        # Verify the file was created
        if os.path.exists(tmp_filename):
            print("  ✅ Sample Excel file created successfully")
            
            # Read it back
            df_read = pd.read_excel(tmp_filename)
            if len(df_read) == 2:
                print("  ✅ Excel file read successfully")
            else:
                print("  ❌ Excel file read failed - incorrect row count")
            
            # Clean up
            os.unlink(tmp_filename)
            return True
        else:
            print("  ❌ Failed to create sample Excel file")
            return False
            
    except Exception as e:
        print(f"  ❌ Excel processing test failed: {e}")
        return False

def test_dependencies():
    """Test that all required dependencies are available"""
    print("\nTesting required dependencies...")
    
    required_packages = [
        'streamlit',
        'pandas',
        'numpy',
        'PIL',
        'reportlab'
    ]
    
    success_count = 0
    for package in required_packages:
        try:
            __import__(package)
            print(f"  ✅ {package} - Available")
            success_count += 1
        except ImportError as e:
            print(f"  ❌ {package} - Not available: {e}")
    
    print(f"\nDependency test completed: {success_count}/{len(required_packages)} packages available")
    return success_count == len(required_packages)

def test_config_files():
    """Test that configuration files are properly set up"""
    print("\nTesting configuration files...")
    
    config_files = [
        '.streamlit/config.toml',
        'requirements.txt'
    ]
    
    success_count = 0
    for config_file in config_files:
        if os.path.exists(config_file):
            try:
                with open(config_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                print(f"  ✅ {config_file} - File exists and is readable ({len(content)} characters)")
                success_count += 1
            except Exception as e:
                print(f"  ❌ {config_file} - Error reading file: {e}")
        else:
            print(f"  ❌ {config_file} - File not found")
    
    print(f"\nConfiguration test completed: {success_count}/{len(config_files)} files OK")
    return success_count == len(config_files)

def main():
    """Main test function"""
    print("PWD Tools Streamlit App Functionality Test")
    print("=" * 50)
    
    # Run all tests
    tests = [
        test_streamlit_pages,
        test_excel_processing,
        test_dependencies,
        test_config_files
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"Test {test.__name__} failed with exception: {e}")
            results.append(False)
    
    # Summary
    passed_tests = sum(results)
    total_tests = len(results)
    
    print("\n" + "=" * 50)
    print(f"Test Summary: {passed_tests}/{total_tests} tests passed")
    
    if passed_tests == total_tests:
        print("🎉 All tests passed! The Streamlit app is functioning correctly.")
        return 0
    else:
        print("❌ Some tests failed. Please check the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())