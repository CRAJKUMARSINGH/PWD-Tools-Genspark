#!/usr/bin/env python3
"""
Streamlit Deployment Script for PWD Tools Web
Automatically deploy the beautiful magenta-themed PWD Tools Web application
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

def deploy_to_streamlit_cloud():
    """Instructions for deploying to Streamlit Cloud"""
    print("\n🚀 Deploying to Streamlit Cloud...")
    print("=" * 50)
    print("Follow these steps to deploy your beautiful PWD Tools Web application:")
    print("")
    print("1. Go to https://streamlit.io/cloud")
    print("2. Sign in with your GitHub account")
    print("3. Click 'New app'")
    print("4. Select your repository: CRAJKUMARSINGH/PWD-Tools-Genspark")
    print("5. Set the main file path to: streamlit_app.py")
    print("6. Click 'Deploy!'")
    print("")
    print("Your beautiful application will be available at:")
    print("https://pwd-tools-web.streamlit.app")
    print("")
    print("🎉 Congratulations! Your magenta-themed PWD Tools Web is now live!")

def run_local_streamlit():
    """Run the Streamlit web application locally"""
    print("Starting Streamlit app locally...")
    try:
        # Open browser first
        webbrowser.open("http://localhost:8501")
        time.sleep(2)  # Give browser time to open
        
        # Start Streamlit app with streamlit_app.py as entry point
        subprocess.run([sys.executable, "-m", "streamlit", "run", "streamlit_app.py"])
        return True
    except Exception as e:
        print(f"❌ Error running Streamlit app: {e}")
        return False

def show_menu():
    """Show deployment options menu"""
    print("\nPWD Tools Web - Beautiful Magenta Deployment")
    print("=" * 50)
    print("1. Run Locally (streamlit_app.py)")
    print("2. Deploy to Streamlit Cloud (beautiful name: pwd-tools-web)")
    print("3. Install Dependencies")
    print("4. Exit")
    print("=" * 50)

def main():
    """Main deployment function"""
    print("PWD Tools Web - Beautiful Magenta Deployment")
    print("=" * 50)
    print("Experience the beautiful magenta-themed PWD Tools Web application!")
    print("")
    
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
                    run_local_streamlit()
                else:
                    print("Streamlit is required for web deployment.")
            else:
                print("Failed to install dependencies.")
        elif choice == "2":
            deploy_to_streamlit_cloud()
        elif choice == "3":
            install_dependencies()
        elif choice == "4":
            print("👋 Goodbye! Thanks for using PWD Tools Web!")
            break
        else:
            print("Invalid option. Please select 1-4.")

if __name__ == "__main__":
    main()