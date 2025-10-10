#!/usr/bin/env python3
"""
Test script to verify installer script components.
"""

import os
import sys

def check_installer_script():
    """Check if the Inno Setup script has the required components."""
    script_path = os.path.join(os.path.dirname(__file__), "Bridge_GAD_Installer.iss")
    
    if not os.path.exists(script_path):
        print("❌ Inno Setup script not found")
        return False
    
    try:
        with open(script_path, 'r') as f:
            content = f.read()
        
        # Check for required sections
        required_sections = ['[Setup]', '[Files]', '[Icons]', '[Tasks]', '[Run]']
        missing_sections = []
        
        for section in required_sections:
            if section not in content:
                missing_sections.append(section)
        
        if missing_sections:
            print(f"❌ Missing sections in installer script: {missing_sections}")
            return False
        
        # Check for required files
        required_files = ['Bridge_GAD.exe', 'Bridge_GAD_GUI.exe']
        missing_files = []
        
        for file in required_files:
            if file not in content:
                missing_files.append(file)
        
        if missing_files:
            print(f"❌ Missing file references in installer script: {missing_files}")
            return False
        
        print("✅ Inno Setup script verified successfully")
        return True
        
    except Exception as e:
        print(f"❌ Error reading installer script: {e}")
        return False

def main():
    print("Testing installer script components...")
    print("=" * 40)
    
    success = check_installer_script()
    
    print("=" * 40)
    if success:
        print("✅ Installer script is ready for use!")
        print("You can now compile it with Inno Setup Compiler.")
    else:
        print("❌ Installer script has issues.")
        print("Please check the errors above.")
    
    return success

if __name__ == "__main__":
    main()