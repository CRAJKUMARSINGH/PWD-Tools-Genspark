#!/bin/bash
# PWD Tools Desktop - Unix Application Starter
# Launches the PWD Tools Desktop Application

echo ""
echo "========================================"
echo "  PWD Tools Desktop - Starting Application"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ ERROR: Python 3 is not installed"
    echo ""
    echo "Please run ./install.sh first to install Python 3"
    echo ""
    exit 1
fi

echo "✅ Python 3 is available"
echo ""

# Check if dependencies are installed
python3 -c "import customtkinter, pandas, openpyxl, reportlab, numpy, PIL" &> /dev/null
if [ $? -ne 0 ]; then
    echo "⚠️  WARNING: Some dependencies may be missing"
    echo "Please run ./install.sh to install all dependencies"
    echo ""
    echo "Continuing anyway..."
    echo ""
fi

echo "🚀 Launching PWD Tools Desktop..."
echo ""

# Try to run the main application
if [ -f "main.py" ]; then
    echo "📱 Starting Main Application..."
    python3 main.py
elif [ -f "run_app.py" ]; then
    echo "📱 Starting via Run Script..."
    python3 run_app.py
elif [ -f "pwd_tools_simple.py" ]; then
    echo "📱 Starting Simple Version..."
    python3 pwd_tools_simple.py
else
    echo "❌ ERROR: No application file found"
    echo ""
    echo "Expected files: main.py, run_app.py, or pwd_tools_simple.py"
    echo ""
    exit 1
fi

echo ""
echo "👋 Application closed. Thank you for using PWD Tools!"
