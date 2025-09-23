#!/usr/bin/env python3
"""
PWD Tools Desktop - Application Launcher
Proper entry point for the PWD Tools Desktop application
"""

import sys
import os
from pathlib import Path

def main():
    """Main application launcher"""
    try:
        # Add project root to Python path
        project_root = Path(__file__).parent
        sys.path.insert(0, str(project_root))
        
        # Import and run main application
        from main import PWDToolsApp
        app = PWDToolsApp()
        app.run()
        
    except ImportError as e:
        print(f"Import Error: {e}")
        print("Make sure all dependencies are installed:")
        print("pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"Application Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
