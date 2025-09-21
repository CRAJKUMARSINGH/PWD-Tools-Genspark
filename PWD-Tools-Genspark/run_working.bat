@echo off
REM PWD Tools Desktop - Working Version Launcher
REM Maintains exact same landing page design with proper tool linking

echo.
echo ========================================
echo   PWD Tools Desktop - Working Version
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python 3.9+ from https://python.org
    echo.
    pause
    exit /b 1
)

echo ✅ Python is available
echo.

REM Check if dependencies are installed
python -c "import customtkinter, pandas, openpyxl, reportlab, numpy, PIL" >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  WARNING: Some dependencies may be missing
    echo Please run INSTALL_DEPS.bat to install all dependencies
    echo.
    echo Continuing anyway...
    echo.
)

echo 🚀 Launching PWD Tools Desktop (Working Version)...
echo.

REM Run the working version
python pwd_tools_working.py

echo.
echo 👋 Application closed. Thank you for using PWD Tools!
pause
