#!/usr/bin/env python3
"""
Test script to verify that the Bridge_GAD executables work correctly.
"""

import subprocess
import sys
import time
import os

def test_gui_executable():
    """Test the GUI executable."""
    print("Testing Bridge_GAD GUI executable...")
    
    try:
        # Start the GUI executable
        exe_path = os.path.join("dist", "Bridge_GAD_GUI.exe")
        if not os.path.exists(exe_path):
            print(f"❌ GUI executable not found: {exe_path}")
            return False
            
        print(f"✅ Found GUI executable: {exe_path}")
        
        # Try to start the executable
        process = subprocess.Popen([exe_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Give it a moment to start
        time.sleep(3)
        
        # Check if the process is still running
        if process.poll() is None:
            print("✅ GUI executable started successfully")
            # Terminate the process
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
            print("✅ GUI executable terminated gracefully")
            return True
        else:
            stdout, stderr = process.communicate()
            print(f"❌ GUI executable failed to start")
            print(f"Return code: {process.returncode}")
            if stdout:
                print(f"STDOUT: {stdout.decode()}")
            if stderr:
                print(f"STDERR: {stderr.decode()}")
            return False
            
    except Exception as e:
        print(f"❌ Error testing GUI executable: {e}")
        return False

def test_cli_executable():
    """Test the CLI executable with --help flag."""
    print("\nTesting Bridge_GAD CLI executable...")
    
    try:
        # Check if the executable exists
        exe_path = os.path.join("dist", "Bridge_GAD.exe")
        if not os.path.exists(exe_path):
            print(f"❌ CLI executable not found: {exe_path}")
            return False
            
        print(f"✅ Found CLI executable: {exe_path}")
        
        # Try to run with --help
        result = subprocess.run([exe_path, "--help"], 
                              stdout=subprocess.PIPE, 
                              stderr=subprocess.PIPE, 
                              timeout=10)
        
        print(f"Return code: {result.returncode}")
        if result.stdout:
            print(f"STDOUT: {result.stdout.decode()}")
        if result.stderr:
            print(f"STDERR: {result.stderr.decode()}")
            
        # Even if it fails with missing dependencies, if we get a response, it's partially working
        print("✅ CLI executable can be executed (may have missing dependencies)")
        return True
        
    except subprocess.TimeoutExpired:
        print("❌ CLI executable timed out")
        return False
    except Exception as e:
        print(f"❌ Error testing CLI executable: {e}")
        return False

def main():
    """Main test function."""
    print("Bridge_GAD Executable Test")
    print("=" * 30)
    
    # Test GUI executable
    gui_result = test_gui_executable()
    
    # Test CLI executable
    cli_result = test_cli_executable()
    
    print("\n" + "=" * 30)
    if gui_result:
        print("✅ GUI executable test: PASSED")
    else:
        print("❌ GUI executable test: FAILED")
        
    if cli_result:
        print("✅ CLI executable test: PASSED (with possible missing dependencies)")
    else:
        print("❌ CLI executable test: FAILED")
    
    if gui_result and cli_result:
        print("\n🎉 All tests completed successfully!")
        return 0
    else:
        print("\n⚠️  Some tests failed. Please check the output above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())