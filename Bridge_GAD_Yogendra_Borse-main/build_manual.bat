@echo off
echo ==============================
echo Bridge_GAD User Manual Generator
echo ==============================

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python not found. Please install Python to generate the manual.
    pause
    exit /b 1
)

REM Run the manual generator script
echo Generating user manual...
python docs\build_manual.py

pause