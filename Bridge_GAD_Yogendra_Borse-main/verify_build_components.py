#!/usr/bin/env python3
"""
Verification script for build components.
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

def main():
    print("Verifying Bridge_GAD build components...")
    print("=" * 50)
    
    # Check core build files
    build_files = [
        ("build_exe.bat", "Main build script"),
        ("simple_build.bat", "Simple build script"),
        ("build_all.bat", "Complete build script"),
        ("Bridge_GAD_Installer.iss", "Inno Setup installer script"),
        ("VERSION.txt", "Version file"),
        ("bridge.ico", "Application icon"),
    ]
    
    all_found = True
    for filename, description in build_files:
        filepath = os.path.join(os.path.dirname(__file__), filename)
        if not check_file_exists(filepath, description):
            all_found = False
    
    print("\n" + "=" * 50)
    
    if all_found:
        print("✅ All build components are in place!")
        print("You can now run build_all.bat to create the complete package.")
    else:
        print("❌ Some build components are missing.")
        print("Please check the files listed above.")
    
    return all_found

if __name__ == "__main__":
    main()