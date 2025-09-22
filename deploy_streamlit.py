#!/usr/bin/env python3
"""
Deployment script for PWD Tools Streamlit App
Runs the app three times on different ports for redundancy
"""

import subprocess
import sys
import time
import os

def install_requirements():
    """Install required packages"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        return False

def run_streamlit_instance(port, instance_name):
    """Run a Streamlit instance on specified port"""
    try:
        print(f"🚀 Starting {instance_name} on port {port}...")
        # Use Popen to run in background
        process = subprocess.Popen([
            sys.executable, "-m", "streamlit", "run", 
            "streamlit_app.py",  # This is correct now
            "--server.port", str(port),
            "--server.headless", "true"
        ])
        print(f"✅ {instance_name} started successfully on port {port}")
        return process
    except Exception as e:
        print(f"❌ Error starting {instance_name} on port {port}: {e}")
        return None

def main():
    """Main deployment function"""
    print("🏗️ PWD Tools Streamlit Deployment")
    print("=" * 40)
    
    # Install requirements
    print("📦 Installing requirements...")
    if not install_requirements():
        print("❌ Failed to install requirements. Exiting.")
        return
    
    # Run three instances
    processes = []
    ports = [8501, 8502, 8503]
    instance_names = ["Primary Instance", "Secondary Instance", "Tertiary Instance"]
    
    print("\n🔄 Starting Streamlit instances...")
    for i, (port, name) in enumerate(zip(ports, instance_names)):
        process = run_streamlit_instance(port, name)
        if process:
            processes.append(process)
        time.sleep(2)  # Small delay between starts
    
    if not processes:
        print("❌ No instances started successfully")
        return
    
    print(f"\n✅ Successfully started {len(processes)} Streamlit instance(s)")
    print("\n🌐 Access the applications at:")
    for i, port in enumerate(ports[:len(processes)]):
        print(f"   • {instance_names[i]}: http://localhost:{port}")
    
    print("\n💡 Tips:")
    print("   • Use different ports for redundancy")
    print("   • Primary instance (8501) is recommended for regular use")
    print("   • Other instances can be used for backup or load distribution")
    print("   • Press Ctrl+C to stop all instances")
    
    try:
        # Keep the script running
        print("\n⏳ Keeping instances running... (Press Ctrl+C to stop)")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Stopping all instances...")
        for i, process in enumerate(processes):
            try:
                process.terminate()
                process.wait(timeout=5)
                print(f"✅ {instance_names[i]} stopped")
            except subprocess.TimeoutExpired:
                process.kill()
                print(f"⚠️  {instance_names[i]} force killed")
        print("👋 All instances stopped. Goodbye!")

if __name__ == "__main__":
    main()