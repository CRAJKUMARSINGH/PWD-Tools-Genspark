@echo off
REM PWD Tools Desktop - Windows Dependency Installer
REM Installs all required Python dependencies

echo.
echo ========================================
echo   PWD Tools Desktop - Installing Dependencies
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python 3.9+ from https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo ✅ Python is available
echo.

REM Install dependencies
echo 📦 Installing required packages...
echo.

pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo ❌ ERROR: Failed to install dependencies
    echo Please check your internet connection and try again
    echo.
    pause
    exit /b 1
)

echo.
echo ✅ All dependencies installed successfully!
echo.
echo 🚀 You can now run the application using START_APP.bat
echo.
pause