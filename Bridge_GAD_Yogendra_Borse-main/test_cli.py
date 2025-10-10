#!/usr/bin/env python3
"""Test script for the CLI functionality."""

import sys
import os

# Add the src directory to the path so we can import bridge_gad modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from bridge_gad.cli import main

if __name__ == "__main__":
    # Simulate command line arguments
    sys.argv = ['test_cli.py', '--span', '20', '--load', '15']
    main()