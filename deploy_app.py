#!/usr/bin/env python3
"""
One-click deployment script for PWD Tools
"""

import os
import sys
import subprocess
import webbrowser
import time

def check_python():
    """Check if Python is available"""
    try:
        result = subprocess.run([sys.executable, "--version"], 
                              capture_output=True, text=True)
        print(f"✅ Python available: {result.stdout.strip()}")
        return True
    except Exception as e:
        print(f"❌ Python not available: {e}")
        return False

def install_dependencies():
    """Install required dependencies"""
    print("Installing dependencies...")
    try:
        result = subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Dependencies installed successfully")
            return True
        else:
            print(f"❌ Failed to install dependencies: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def test_streamlit():
    """Test if Streamlit is available"""
    try:
        result = subprocess.run([sys.executable, "-c", "import streamlit; print(streamlit.__version__)"],
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Streamlit available: {result.stdout.strip()}")
            return True
        else:
            print("❌ Streamlit not available")
            return False
    except Exception as e:
        print(f"❌ Error testing Streamlit: {e}")
        return False

def run_streamlit_app():
    """Run the Streamlit web application"""
    print("Starting Streamlit app...")
    try:
        # Open browser first
        webbrowser.open("http://localhost:8501")
        
        # Start Streamlit app
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])
        return True
    except Exception as e:
        print(f"❌ Error running Streamlit app: {e}")
        return False

def run_desktop_app():
    """Run the desktop application"""
    print("Starting desktop app...")
    try:
        subprocess.run([sys.executable, "run_app.py"])
        return True
    except Exception as e:
        print(f"❌ Error running desktop app: {e}")
        return False

def show_menu():
    """Show deployment options menu"""
    print("\nPWD Tools Deployment Options")
    print("=" * 30)
    print("1. Run Streamlit Web App")
    print("2. Run Desktop App")
    print("3. Install Dependencies")
    print("4. Exit")
    print("=" * 30)

def main():
    """Main deployment function"""
    print("PWD Tools One-Click Deployment")
    print("=" * 40)
    
    # Check Python
    if not check_python():
        print("Please install Python 3.9 or higher.")
        return 1
    
    # Main loop
    while True:
        show_menu()
        choice = input("Select option (1-4): ").strip()
        
        if choice == "1":
            # Install dependencies first
            if install_dependencies():
                if test_streamlit():
                    run_streamlit_app()
                else:
                    print("Streamlit is required for web deployment.")
            else:
                print("Failed to install dependencies.")
        elif choice == "2":
            # Install dependencies first
            if install_dependencies():
                run_desktop_app()
            else:
                print("Failed to install dependencies.")
        elif choice == "3":
            install_dependencies()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please select 1-4.")

if __name__ == "__main__":
    main()