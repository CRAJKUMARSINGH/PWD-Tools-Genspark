@echo off
title PWD Tools One-Click Deployment

echo ========================================
echo PWD Tools One-Click Deployment
echo ========================================
echo.

REM Change to the application directory
cd /d "c:\Users\Rajkumar\PWD-Tools-Genspark"

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.9 or higher and add it to your PATH
    pause
    exit /b 1
)

echo Python is available
echo.

REM Check if required files exist
if not exist "requirements.txt" (
    echo Error: requirements.txt not found
    pause
    exit /b 1
)

echo Requirements file found
echo.

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Warning: Failed to install dependencies
    echo Continuing with deployment...
)

echo.
echo Dependencies installation completed
echo.

REM Show deployment options
echo Deployment Options:
echo ==================
echo 1. Run Streamlit Web App
echo 2. Run Desktop App
echo 3. Exit
echo.

choice /c 123 /m "Select deployment option"
if %errorlevel% equ 1 (
    echo Starting Streamlit Web App...
    echo Opening browser...
    start "" http://localhost:8501
    python -m streamlit run app.py
) else if %errorlevel% equ 2 (
    echo Starting Desktop App...
    python run_app.py
) else (
    echo Exiting...
    exit /b 0
)

echo.
echo Deployment completed.
pause