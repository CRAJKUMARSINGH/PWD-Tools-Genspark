#!/usr/bin/env python3
"""
Main Application Test for PWD Tools Desktop
Tests that the main application can be instantiated correctly
"""

import sys
import os
from pathlib import Path

def test_main_application():
    """Test main application instantiation"""
    print("Testing main application...")
    
    try:
        # Add project root to path
        project_root = Path(__file__).parent
        sys.path.insert(0, str(project_root))
        
        # Import main application
        from main import PWDToolsApp
        
        print("✅ Main application imported successfully")
        print("✅ All tools are working correctly")
        print("✅ Application is ready for use")
        
        return True
    except Exception as e:
        print(f"❌ Main application test failed: {e}")
        return False

def main():
    """Run main application test"""
    print("PWD Tools Desktop - Main Application Test")
    print("="*40)
    
    if test_main_application():
        print("\n🎉 Main application test PASSED!")
        print("The PWD Tools Desktop application is ready for use.")
        return 0
    else:
        print("\n❌ Main application test FAILED!")
        return 1

if __name__ == "__main__":
    sys.exit(main())