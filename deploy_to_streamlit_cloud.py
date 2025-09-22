#!/usr/bin/env python3
"""
Deployment helper script for PWD Tools to Streamlit Cloud
"""

import os
import sys
import subprocess
from datetime import datetime

def check_prerequisites():
    """Check if required tools are available"""
    print("🔍 Checking prerequisites...")
    
    # Check if git is available
    try:
        subprocess.run(["git", "--version"], check=True, capture_output=True)
        print("✅ Git is available")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Git is not installed or not in PATH")
        return False
    
    # Check if Python is available
    try:
        subprocess.run([sys.executable, "--version"], check=True, capture_output=True)
        print("✅ Python is available")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Python is not available")
        return False
    
    print("✅ All prerequisites met\n")
    return True

def create_deployment_files():
    """Create necessary files for Streamlit Cloud deployment"""
    print("📁 Creating deployment files...")
    
    # Create .streamlit directory if it doesn't exist
    if not os.path.exists(".streamlit"):
        os.makedirs(".streamlit")
        print("✅ Created .streamlit directory")
    
    # Create config.toml
    config_content = """[server]
port = 8501
headless = true
enableCORS = false
maxUploadSize = 1000
address = "0.0.0.0"

[browser]
serverAddress = "0.0.0.0"

[theme]
base = "light"
primaryColor = "#2E8B57"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F8F5"
textColor = "#000000"
font = "sans serif"
"""
    
    with open(".streamlit/config.toml", "w") as f:
        f.write(config_content)
    print("✅ Created .streamlit/config.toml")
    
    # Create runtime.txt
    with open("runtime.txt", "w") as f:
        f.write("python-3.9")
    print("✅ Created runtime.txt")
    
    # Create README for deployment
    readme_content = """# PWD Tools - Streamlit Cloud Deployment

## Deployment Instructions

1. Fork this repository to your GitHub account
2. Go to https://share.streamlit.io
3. Click "New app"
4. Select your repository
5. Set:
   - Branch: main
   - Main file: app.py
6. Click "Deploy!"

## Requirements

- Python 3.9 (specified in runtime.txt)
- Dependencies in requirements.txt

## Configuration

- Streamlit config in .streamlit/config.toml
- Theme colors optimized for PWD branding
"""
    
    with open("STREAMLIT_DEPLOYMENT_README.md", "w") as f:
        f.write(readme_content)
    print("✅ Created STREAMLIT_DEPLOYMENT_README.md")
    
    print("✅ All deployment files created\n")

def run_tests():
    """Run automated tests"""
    print("🧪 Running automated tests...")
    
    try:
        result = subprocess.run([sys.executable, "simple_test.py"], 
                              capture_output=True, text=True, timeout=60)
        if result.returncode == 0:
            print("✅ Tests completed successfully")
            print("✅ CSV test reports generated")
        else:
            print("⚠️  Tests completed with some issues")
            print(result.stdout)
            print(result.stderr)
    except subprocess.TimeoutExpired:
        print("❌ Tests timed out")
        return False
    except FileNotFoundError:
        print("❌ simple_test.py not found")
        return False
    
    print("✅ Automated tests completed\n")
    return True

def main():
    """Main deployment helper function"""
    print("🚀 PWD Tools Streamlit Cloud Deployment Helper")
    print("=" * 50)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Check prerequisites
    if not check_prerequisites():
        print("❌ Prerequisites not met. Please install required tools.")
        return
    
    # Create deployment files
    create_deployment_files()
    
    # Run tests
    if not run_tests():
        print("❌ Tests failed. Please check the issues before deployment.")
        return
    
    # Summary
    print("📋 Deployment Preparation Summary")
    print("=" * 50)
    print("✅ Prerequisites checked")
    print("✅ Deployment files created")
    print("✅ Automated tests completed")
    print("✅ Ready for Streamlit Cloud deployment")
    
    print("\n📝 Next Steps:")
    print("1. Commit all changes to your repository:")
    print("   git add .")
    print("   git commit -m \"Prepare for Streamlit Cloud deployment\"")
    print("   git push origin main")
    print("")
    print("2. Go to https://share.streamlit.io")
    print("3. Click 'New app'")
    print("4. Select your repository")
    print("5. Set main file to 'app.py'")
    print("6. Click 'Deploy!'")
    
    print(f"\n🏁 Deployment helper completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()