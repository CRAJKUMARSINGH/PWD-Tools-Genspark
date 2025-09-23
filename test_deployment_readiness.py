#!/usr/bin/env python3
"""
Test deployment readiness by running the PWD Tools application programmatically three times
"""

import subprocess
import sys
import time
import os
from pathlib import Path

def run_application_instance(run_number):
    """Run the PWD Tools application once and monitor its execution"""
    print(f"🚀 Starting application instance #{run_number}...")
    
    try:
        # Run the application using the main entry point
        process = subprocess.Popen([
            sys.executable, 
            "run_app.py"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        print(f"✅ Application instance #{run_number} started with PID: {process.pid}")
        
        # Give the application time to initialize (splash screen + main window)
        time.sleep(10)
        
        # Check if the process is still running
        if process.poll() is None:
            print(f"✅ Application instance #{run_number} is running normally")
            # Let it run for a bit to ensure stability
            time.sleep(5)
            # Terminate the process
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()
            print(f"✅ Application instance #{run_number} terminated successfully")
            return True
        else:
            # Process has exited
            stdout, stderr = process.communicate()
            if process.returncode == 0:
                print(f"✅ Application instance #{run_number} completed successfully")
                return True
            else:
                print(f"❌ Application instance #{run_number} failed with return code: {process.returncode}")
                print(f"STDOUT: {stdout}")
                print(f"STDERR: {stderr}")
                return False
                
    except Exception as e:
        print(f"❌ Failed to start application instance #{run_number}: {e}")
        return False

def check_dependencies():
    """Check if all required dependencies are installed"""
    print("🔍 Checking dependencies...")
    
    required_packages = [
        'customtkinter',
        'pandas',
        'openpyxl',
        'reportlab',
        'numpy',
        'PIL'
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
        return False
    else:
        print("✅ All dependencies are installed")
        return True

def verify_required_files():
    """Verify that all required files exist"""
    print("🔍 Checking required files...")
    
    required_files = [
        "run_app.py",
        "main.py",
        "requirements.txt"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
            print(f"❌ Missing: {file_path}")
        else:
            print(f"✅ Found: {file_path}")
    
    if missing_files:
        print(f"\n⚠️  {len(missing_files)} required files are missing")
        return False
    else:
        print("✅ All required files are present")
        return True

def create_deployment_report():
    """Create a deployment readiness report"""
    print("📝 Creating deployment readiness report...")
    
    report_content = f"""
PWD Tools Deployment Readiness Report
=====================================
Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}

✅ Application tested successfully 3 times
✅ All dependencies verified
✅ Required files verified
✅ No critical errors detected

Deployment Status: READY FOR DEPLOYMENT

Next Steps:
1. Create executable using PyInstaller:
   pyinstaller --onefile --windowed run_app.py

2. Package the application with all required files

3. Test the executable on a clean system

4. Create installation package if needed
"""
    
    with open("DEPLOYMENT_READINESS_REPORT.txt", "w", encoding="utf-8") as f:
        f.write(report_content)
    
    print("✅ Deployment readiness report created: DEPLOYMENT_READINESS_REPORT.txt")
    return True

def main():
    """Main function to test deployment readiness"""
    print("🏗️ PWD Tools - Deployment Readiness Test")
    print("=" * 50)
    
    # Check Python version
    if sys.version_info < (3, 9):
        print("❌ Error: Python 3.9 or higher is required.")
        print(f"   Current version: {sys.version}")
        return False
    
    print(f"✅ Python version: {sys.version.split()[0]}")
    
    # Verify required files
    if not verify_required_files():
        return False
    
    # Check dependencies
    if not check_dependencies():
        return False
    
    # Run the application three times
    print("\n🔁 Running application programmatically 3 times...")
    print("-" * 50)
    
    success_count = 0
    for i in range(1, 4):
        print(f"\n🧪 Test Run #{i}")
        print("-" * 20)
        if run_application_instance(i):
            success_count += 1
            print(f"✅ Test Run #{i} completed successfully")
        else:
            print(f"❌ Test Run #{i} failed")
    
    print("\n" + "=" * 50)
    print("📊 Test Results Summary")
    print("=" * 50)
    print(f"Successful runs: {success_count}/3")
    
    if success_count == 3:
        print("🎉 All test runs completed successfully!")
        print("✅ Application is stable and ready for deployment")
        
        # Create deployment report
        if create_deployment_report():
            print("\n✅ Deployment readiness verification completed successfully!")
            print("📁 Deployment files created:")
            print("   - DEPLOYMENT_READINESS_REPORT.txt")
            return True
    else:
        print(f"❌ {3 - success_count} test run(s) failed")
        print("⚠️  Application needs further testing before deployment")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)