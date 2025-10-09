@echo off
echo Starting CustomTkinter Magenta Button Demo...
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

REM Check if required files exist
if not exist "customtkinter_magenta_demo.py" (
    echo Error: customtkinter_magenta_demo.py not found
    pause
    exit /b 1
)

REM Run the demo
echo Launching Magenta Button Demo...
python customtkinter_magenta_demo.py

if %errorlevel% neq 0 (
    echo Error: Failed to launch the demo
    echo Make sure all dependencies are installed:
    echo pip install -r requirements.txt
    pause
    exit /b 1
)

echo.
echo Demo application closed.
pause