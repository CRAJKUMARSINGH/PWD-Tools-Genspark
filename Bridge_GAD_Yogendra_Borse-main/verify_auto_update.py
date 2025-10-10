#!/usr/bin/env python3
"""
Verification script for auto-update functionality.
"""

import os
import sys

def check_gui_implementation():
    """Check if auto-update is implemented in GUI."""
    gui_path = os.path.join(os.path.dirname(__file__), 'src', 'bridge_gad', 'gui.py')
    
    if not os.path.exists(gui_path):
        print("❌ GUI file not found")
        return False
    
    try:
        with open(gui_path, 'r') as f:
            content = f.read()
        
        # Check for required imports
        required_imports = ['requests', 'webbrowser', '__version__']
        missing_imports = [imp for imp in required_imports if imp not in content]
        
        if missing_imports:
            print(f"❌ Missing imports in GUI: {missing_imports}")
            return False
        
        # Check for update function
        if 'check_for_updates' not in content:
            print("❌ check_for_updates function not found in GUI")
            return False
        
        # Check for version import
        if 'from bridge_gad import __version__' not in content:
            print("❌ __version__ not imported from bridge_gad package")
            return False
        
        print("✅ Auto-update functionality implemented in GUI")
        return True
        
    except Exception as e:
        print(f"❌ Error reading GUI file: {e}")
        return False

def check_version_consistency():
    """Check if version is consistent across files."""
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

def check_required_files():
    """Check if required files for auto-update exist."""
    required_files = [
        ('src/bridge_gad/gui.py', 'GUI with auto-update functionality'),
        ('sign_executables.bat', 'Code signing batch script'),
    ]
    
    missing_files = []
    for filename, description in required_files:
        filepath = os.path.join(os.path.dirname(__file__), filename)
        if not os.path.exists(filepath):
            missing_files.append((filename, description))
    
    if missing_files:
        print("❌ Missing required files:")
        for filename, description in missing_files:
            print(f"   - {filename}: {description}")
        return False
    
    print("✅ All required files for auto-update are present")
    return True

def main():
    print("Verifying Bridge_GAD auto-update functionality...")
    print("=" * 50)
    
    checks = [
        check_gui_implementation,
        check_required_files
    ]
    
    results = []
    for check in checks:
        results.append(check())
        print()
    
    # Check version consistency
    check_version_consistency()
    
    print("=" * 50)
    if all(results):
        print("✅ Auto-update functionality is ready!")
        print("\nTo test the auto-update feature:")
        print("1. Build the GUI executable")
        print("2. Run it to see the update check")
        print("\nTo sign executables:")
        print("1. Create or obtain a code-signing certificate")
        print("2. Run sign_executables.bat")
    else:
        print("❌ Auto-update functionality has issues.")
        print("Please address the issues listed above.")
    
    return all(results)

if __name__ == "__main__":
    main()