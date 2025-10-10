#!/usr/bin/env python3
"""
Verification script for auto-build components.
"""

import os
import sys

def check_file_exists(filepath, description):
    """Check if a file exists and print status."""
    if os.path.exists(filepath):
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description}: {filepath} (NOT FOUND)")
        return False

def check_version_consistency():
    """Check if version numbers are consistent across files."""
    print("\nChecking version consistency...")
    
    # Check __init__.py
    init_path = os.path.join(os.path.dirname(__file__), 'src', 'bridge_gad', '__init__.py')
    if os.path.exists(init_path):
        with open(init_path, 'r') as f:
            init_content = f.read()
            if '__version__' in init_content:
                version_line = [line for line in init_content.split('\n') if '__version__' in line][0]
                print(f"✅ __init__.py version: {version_line.strip()}")
    
    # Check pyproject.toml
    pyproject_path = os.path.join(os.path.dirname(__file__), 'pyproject.toml')
    if os.path.exists(pyproject_path):
        with open(pyproject_path, 'r') as f:
            pyproject_content = f.read()
            if 'version =' in pyproject_content:
                version_line = [line for line in pyproject_content.split('\n') if 'version =' in line][0]
                print(f"✅ pyproject.toml version: {version_line.strip()}")
    
    # Check VERSION.txt
    version_path = os.path.join(os.path.dirname(__file__), 'VERSION.txt')
    if os.path.exists(version_path):
        with open(version_path, 'r') as f:
            version_content = f.read().strip()
            print(f"✅ VERSION.txt version: {version_content}")

def main():
    print("Verifying Bridge_GAD auto-build components...")
    print("=" * 50)
    
    # Check core auto-build files
    build_files = [
        ("auto_build.bat", "Auto-build script"),
        ("build_all.bat", "Complete build script"),
        ("src/bridge_gad/__init__.py", "Package initialization with version"),
        ("pyproject.toml", "Package metadata with version"),
        ("VERSION.txt", "Version file"),
    ]
    
    all_found = True
    for filename, description in build_files:
        filepath = os.path.join(os.path.dirname(__file__), filename)
        if not check_file_exists(filepath, description):
            all_found = False
    
    # Check version consistency
    check_version_consistency()
    
    print("\n" + "=" * 50)
    
    if all_found:
        print("✅ All auto-build components are in place!")
        print("You can now run auto_build.bat to create a complete build.")
    else:
        print("❌ Some auto-build components are missing.")
        print("Please check the files listed above.")
    
    return all_found

if __name__ == "__main__":
    main()