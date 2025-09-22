#!/usr/bin/env python3
"""
Final deployment check script for PWD Tools
"""

import os
import sys
from datetime import datetime

def check_required_files():
    """Check if all required files for deployment exist"""
    print("🔍 Checking required deployment files...")
    
    required_files = [
        "app.py",
        "streamlit_landing.py",
        "requirements.txt",
        "runtime.txt",
        ".streamlit/config.toml",
        "pages/01_EMD_Refund.py",
        "pages/02_Deductions_Table.py",
        "pages/03_Delay_Calculator.py",
        "pages/04_Stamp_Duty.py"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
            print(f"❌ Missing: {file_path}")
        else:
            print(f"✅ Found: {file_path}")
    
    if missing_files:
        print(f"\n⚠️  {len(missing_files)} required files are missing")
        return False
    else:
        print("✅ All required files are present")
        return True

def check_test_results():
    """Check if comprehensive test results exist"""
    print("\n🔍 Checking comprehensive test results...")
    
    test_files = [
        "comprehensive_test_results_excel_se_emd.csv",
        "comprehensive_test_results_bill_deviation.csv",
        "comprehensive_test_results_tender_processing.csv",
        "comprehensive_test_results_bill_note_sheet.csv",
        "comprehensive_test_results_deductions_table.csv",
        "comprehensive_test_results_delay_calculator.csv",
        "comprehensive_test_results_emd_refund.csv",
        "comprehensive_test_results_financial_progress.csv",
        "comprehensive_test_results_security_refund.csv",
        "comprehensive_test_results_stamp_duty.csv"
    ]
    
    missing_tests = []
    for file_path in test_files:
        if not os.path.exists(file_path):
            missing_tests.append(file_path)
            print(f"❌ Missing: {file_path}")
        else:
            # Check if file has content
            try:
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                    if len(lines) > 1:  # Header + at least one data row
                        print(f"✅ Found with data: {file_path} ({len(lines)-1} test records)")
                    else:
                        print(f"⚠️  Found but empty: {file_path}")
            except Exception as e:
                print(f"❌ Error reading {file_path}: {e}")
                missing_tests.append(file_path)
    
    if missing_tests:
        print(f"\n⚠️  {len(missing_tests)} test result files are missing or invalid")
        return False
    else:
        print("✅ All test result files are present with data")
        return True

def check_documentation():
    """Check if documentation files exist"""
    print("\n🔍 Checking documentation files...")
    
    doc_files = [
        "README.md",
        "GITHUB_README.md",
        "STREAMLIT_CLOUD_DEPLOYMENT.md",
        "DEPLOY_TO_REMOTE.md",
        "COMPREHENSIVE_TESTING_REPORT.md"
    ]
    
    missing_docs = []
    for file_path in doc_files:
        if not os.path.exists(file_path):
            missing_docs.append(file_path)
            print(f"❌ Missing: {file_path}")
        else:
            print(f"✅ Found: {file_path}")
    
    if missing_docs:
        print(f"\n⚠️  {len(missing_docs)} documentation files are missing")
        return False
    else:
        print("✅ All documentation files are present")
        return True

def check_config_files():
    """Check configuration file contents"""
    print("\n🔍 Checking configuration files...")
    
    # Check runtime.txt
    try:
        with open("runtime.txt", "r") as f:
            content = f.read().strip()
            if content == "python-3.9":
                print("✅ runtime.txt has correct Python version")
            else:
                print(f"⚠️  runtime.txt has unexpected content: {content}")
    except Exception as e:
        print(f"❌ Error reading runtime.txt: {e}")
        return False
    
    # Check .streamlit/config.toml
    try:
        with open(".streamlit/config.toml", "r") as f:
            content = f.read()
            required_sections = ["[server]", "[theme]"]
            missing_sections = []
            for section in required_sections:
                if section in content:
                    print(f"✅ Found section: {section}")
                else:
                    missing_sections.append(section)
                    print(f"❌ Missing section: {section}")
            
            if missing_sections:
                return False
    except Exception as e:
        print(f"❌ Error reading .streamlit/config.toml: {e}")
        return False
    
    print("✅ Configuration files verified")
    return True

def check_git_repo():
    """Check if this is a valid git repository"""
    print("\n🔍 Checking git repository...")
    
    if os.path.exists(".git"):
        print("✅ Git repository initialized")
        return True
    else:
        print("❌ Git repository not found")
        return False

def main():
    """Main verification function"""
    print("✅ PWD Tools Final Deployment Check")
    print("=" * 40)
    print(f"Verification started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Run all checks
    checks = [
        ("Required Files", check_required_files),
        ("Test Results", check_test_results),
        ("Documentation", check_documentation),
        ("Configuration", check_config_files),
        ("Git Repository", check_git_repo)
    ]
    
    results = []
    for check_name, check_function in checks:
        print(f"\n📋 {check_name} Check")
        print("-" * 20)
        result = check_function()
        results.append((check_name, result))
    
    # Summary
    print("\n" + "=" * 40)
    print("📊 Final Verification Summary")
    print("=" * 40)
    
    passed = 0
    failed = 0
    
    for check_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {check_name}")
        if result:
            passed += 1
        else:
            failed += 1
    
    print("-" * 40)
    print(f"Total: {len(results)} checks")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    
    if failed == 0:
        print("\n🎉 All verification checks passed!")
        print("✅ Ready for remote repository upload and Streamlit Cloud deployment")
        print("\n🚀 Next steps:")
        print("1. Create a remote repository on GitHub/GitLab/Bitbucket")
        print("2. Add the remote: git remote add origin <repository-url>")
        print("3. Push to remote: git push -u origin master")
        print("4. Deploy to Streamlit Cloud")
    else:
        print(f"\n⚠️  {failed} check(s) failed")
        print("Please fix the issues before deployment")
    
    print(f"\n🏁 Verification completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()