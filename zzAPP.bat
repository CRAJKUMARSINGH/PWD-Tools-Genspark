@echo off
echo Starting PWD Tools Desktop Application...
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
if exist "run_app.py" (
    echo Launching PWD Tools Desktop via run_app.py...
    python run_app.py
    goto :end
)

if exist "app.py" (
    echo Launching PWD Tools Desktop via app.py...
    python app.py
    goto :end
)

if exist "main.py" (
    echo Launching PWD Tools Desktop via main.py...
    python main.py
    goto :end
)

if exist "launcher.py" (
    echo Launching PWD Tools Desktop via launcher.py...
    python launcher.py
    goto :end
)

echo Error: No valid entry point found
echo Please make sure one of the following files exists:
echo   - run_app.py
echo   - app.py
echo   - main.py
echo   - launcher.py
pause
exit /b 1

:end
if %errorlevel% neq 0 (
    echo.
    echo Error: Failed to launch PWD Tools application
    echo Make sure all dependencies are installed:
    echo pip install -r requirements.txt
    pause
    exit /b 1
)

echo.
echo PWD Tools application closed.
pause