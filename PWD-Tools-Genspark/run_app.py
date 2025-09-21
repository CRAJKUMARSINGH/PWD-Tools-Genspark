#!/usr/bin/env python3
"""
PWD Tools Desktop - Application Launcher
Run this script to start the PWD Tools Desktop application
"""

import sys
import os
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def check_dependencies():
    """Check if all required dependencies are installed"""
    required_packages = [
        'customtkinter',
        'pandas',
        'openpyxl',
        'reportlab',
        'numpy'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("❌ Missing required packages:")
        for package in missing_packages:
            print(f"   - {package}")
        print("\n📦 Please install missing packages using:")
        print(f"   pip install {' '.join(missing_packages)}")
        print("\n   Or install all requirements:")
        print("   pip install -r requirements.txt")
        return False
    
    return True

def main():
    """Main entry point"""
    print("🏗️ PWD Tools Desktop - Starting Application...")
    print("=" * 50)
    
    # Check Python version
    if sys.version_info < (3, 9):
        print("❌ Error: Python 3.9 or higher is required.")
        print(f"   Current version: {sys.version}")
        input("Press Enter to exit...")
        return
    
    print(f"✅ Python version: {sys.version.split()[0]}")
    
    # Check dependencies
    if not check_dependencies():
        input("Press Enter to exit...")
        return
    
    print("✅ All dependencies are installed")
    
    try:
        # Import and run the main application
        from main import PWDToolsApp
        
        print("🚀 Launching PWD Tools Desktop...")
        print("   - Complete offline functionality")
        print("   - Zero web dependencies")
        print("   - Local data storage")
        print("=" * 50)
        
        # Create and run application
        app = PWDToolsApp()
        app.run()
        
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("   Please ensure all files are in the correct location.")
        input("Press Enter to exit...")
    except Exception as e:
        print(f"❌ Application Error: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
