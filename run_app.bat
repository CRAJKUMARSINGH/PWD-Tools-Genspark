@echo off
echo.
echo ========================================
echo   PWD Tools Desktop - Launcher
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.9+ from https://python.org
    echo.
    pause
    exit /b 1
)

REM Check if requirements are installed
echo Checking dependencies...
python -c "import customtkinter, pandas, openpyxl, reportlab, numpy" >nul 2>&1
if errorlevel 1 (
    echo Installing required packages...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        echo Please run: pip install -r requirements.txt
        echo.
        pause
        exit /b 1
    )
)

REM Run the application
echo Starting PWD Tools Desktop...
python run_app.py

REM Keep window open if there's an error
if errorlevel 1 (
    echo.
    echo Application encountered an error.
    pause
)
