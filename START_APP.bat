@echo off
REM PWD Tools Desktop - Windows Application Starter
REM Launches the PWD Tools Desktop Application

echo.
echo ========================================
echo   PWD Tools Desktop - Starting Application
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ ERROR: Python is not installed or not in PATH
    echo.
    echo Please run INSTALL_DEPS.bat first to install Python 3.9+
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

echo 🚀 Launching PWD Tools Desktop...
echo.

REM Try to run the main application
if exist "app.py" (
    echo 📱 Starting Optimized Application...
    python app.py
) else if exist "pwd_tools_optimized.py" (
    echo 📱 Starting Optimized PWD Tools...
    python pwd_tools_optimized.py
) else if exist "main.py" (
    echo 📱 Starting Main Application...
    python main.py
) else if exist "run_app.py" (
    echo 📱 Starting via Run Script...
    python run_app.py
) else if exist "pwd_tools_simple.py" (
    echo 📱 Starting Simple Version...
    python pwd_tools_simple.py
) else (
    echo ❌ ERROR: No application file found
    echo.
    echo Expected files: app.py, pwd_tools_optimized.py, main.py, run_app.py, or pwd_tools_simple.py
    echo.
    pause
    exit /b 1
)

echo.
echo 👋 Application closed. Thank you for using PWD Tools!
pause