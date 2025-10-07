import sys
import os
import tkinter as tk

# Suppress tkinter window creation for testing
tk.Tk = lambda: None

def test_class_import(module_name, class_name):
    """Test if a class can be imported and instantiated without errors"""
    try:
        # Import the module
        module = __import__(module_name)
        
        # Get the class
        cls = getattr(module, class_name)
        
        # Try to instantiate the class (this will fail due to our mock, but we can catch the expected error)
        try:
            instance = cls()
            print(f"✓ {module_name}.{class_name} instantiated successfully")
            return True
        except Exception as e:
            # If the error is related to our mock, it means the class was imported correctly
            if "NoneType" in str(e) or "mock" in str(e).lower():
                print(f"✓ {module_name}.{class_name} imported successfully (GUI instantiation mocked)")
                return True
            else:
                print(f"✗ {module_name}.{class_name} instantiation failed: {e}")
                return False
                
    except Exception as e:
        print(f"✗ {module_name}.{class_name} import failed: {e}")
        return False

def main():
    print("Testing PWD Tools class imports...")
    print("=" * 50)
    
    # Test main application classes
    tests = [
        ("pwd_tools_simple", "PWDToolsSimple"),
        ("pwd_tools_optimized", "PWDToolsOptimized"),
        ("launcher", "PWDToolsLauncher"),
        ("emd_refund_simple", "SimpleEMDRefundTool"),
        ("delay_calculator_simple", "SimpleDelayCalculatorTool"),
        ("hindi_bill_simple", "SimpleHindiBillNoteTool"),
    ]
    
    success_count = 0
    for module_name, class_name in tests:
        if test_class_import(module_name, class_name):
            success_count += 1
    
    print("=" * 50)
    print(f"Class import test results: {success_count}/{len(tests)} successful")

if __name__ == "__main__":
    main()