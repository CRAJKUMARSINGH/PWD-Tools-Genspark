import sys
import os
import importlib.util

def test_import(module_name, file_path):
    """Test if a module can be imported without errors"""
    try:
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        if spec is not None and spec.loader is not None:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            print(f"✓ {module_name} imported successfully")
            return True
        else:
            print(f"✗ {module_name} could not be loaded")
            return False
    except Exception as e:
        print(f"✗ {module_name} import failed: {e}")
        return False

def main():
    print("Testing PWD Tools imports...")
    print("=" * 40)
    
    # Test main applications
    tests = [
        ("app", "app.py"),
        ("pwd_tools_simple", "pwd_tools_simple.py"),
        ("pwd_tools_optimized", "pwd_tools_optimized.py"),
        ("launcher", "launcher.py"),
        ("emd_refund_simple", "emd_refund_simple.py"),
        ("delay_calculator_simple", "delay_calculator_simple.py"),
        ("hindi_bill_simple", "hindi_bill_simple.py"),
    ]
    
    success_count = 0
    for module_name, file_path in tests:
        if os.path.exists(file_path):
            if test_import(module_name, file_path):
                success_count += 1
        else:
            print(f"✗ {module_name} file not found: {file_path}")
    
    print("=" * 40)
    print(f"Import test results: {success_count}/{len(tests)} successful")
    
    # Test dependencies
    print("\nTesting dependencies...")
    print("-" * 20)
    dependencies = [
        "tkinter",
        "sqlite3",
        "subprocess",
        "webbrowser",
        "datetime",
        "os",
        "sys",
        "reportlab",
        "pandas",
    ]
    
    dep_success = 0
    for dep in dependencies:
        try:
            __import__(dep)
            print(f"✓ {dep} available")
            dep_success += 1
        except ImportError:
            print(f"✗ {dep} not available")
        except Exception as e:
            print(f"✗ {dep} error: {e}")
    
    print("-" * 20)
    print(f"Dependency test results: {dep_success}/{len(dependencies)} available")

if __name__ == "__main__":
    main()