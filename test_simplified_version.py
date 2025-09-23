#!/usr/bin/env python3
"""
Test script for the simplified PWD Tools version
"""

import os
import sys
from pathlib import Path

def test_files_exist():
    """Test that all required files exist"""
    required_files = [
        "pwd_main_landing.py",
        "run_pwd_tools.py",
        "START_PWD_TOOLS.bat",
        "core_requirements.txt",
        "README.md"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"ERROR: Missing files: {missing_files}")
        return False
    else:
        print("✓ All required files exist")
        return True

def test_simplified_directory():
    """Test that simplified version directory exists and has files"""
    if not os.path.exists("simplified_version"):
        print("ERROR: simplified_version directory does not exist")
        return False
    
    files = os.listdir("simplified_version")
    required_files = ["pwd_main_landing.py", "run_pwd_tools.py", "START_PWD_TOOLS.bat", "core_requirements.txt", "README.md"]
    
    missing_files = []
    for file in required_files:
        if file not in files:
            missing_files.append(file)
    
    if missing_files:
        print(f"ERROR: Missing files in simplified_version: {missing_files}")
        return False
    else:
        print("✓ All files exist in simplified_version directory")
        return True

def test_zip_file():
    """Test that the zip file exists"""
    if os.path.exists("PWD_Tools_Simplified.zip"):
        print("✓ PWD_Tools_Simplified.zip exists")
        return True
    else:
        print("ERROR: PWD_Tools_Simplified.zip does not exist")
        return False

def main():
    """Run all tests"""
    print("Testing Simplified PWD Tools Version...")
    print("=" * 50)
    
    tests = [
        test_files_exist,
        test_simplified_directory,
        test_zip_file
    ]
    
    passed = 0
    for test in tests:
        if test():
            passed += 1
        print()
    
    print(f"Tests passed: {passed}/{len(tests)}")
    
    if passed == len(tests):
        print("🎉 All tests passed! The simplified version is ready.")
        return 0
    else:
        print("❌ Some tests failed. Please check the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())