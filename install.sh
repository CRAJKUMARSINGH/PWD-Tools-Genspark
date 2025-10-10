#!/bin/bash
# PWD Tools Desktop - Unix Dependency Installer
# Installs all required Python dependencies

echo ""
echo "========================================"
echo "  PWD Tools Desktop - Installing Dependencies"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ ERROR: Python 3 is not installed"
    echo ""
    echo "Please install Python 3.9+ using your package manager:"
    echo "  Ubuntu/Debian: sudo apt install python3 python3-pip"
    echo "  CentOS/RHEL:   sudo yum install python3 python3-pip"
    echo "  macOS:         brew install python3"
    echo ""
    exit 1
fi

echo "✅ Python 3 is available"
echo ""

# Check Python version
python3 --version

# Install dependencies
echo "📦 Installing required packages..."
echo ""

pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo ""
    echo "❌ ERROR: Failed to install dependencies"
    echo "Please check your internet connection and try again"
    echo ""
    exit 1
fi

echo ""
echo "✅ All dependencies installed successfully!"
echo ""
echo "🚀 You can now run the application using ./start.sh"
echo ""