@echo off
echo ========================================
echo Bridge GAD - Install and Build Script
echo ========================================

echo.
echo Installing required dependencies...
python -m pip install -r requirements.txt
python -m pip install -r requirements-dev.txt
python -m pip install pyinstaller

echo.
echo Building executable...
python -m PyInstaller --onefile ^
    --name Bridge_GAD ^
    --add-data "src\bridge_gad\*.py;bridge_gad" ^
    src\bridge_gad\cli.py

echo.
echo Build complete!
echo Executable located in: dist\Bridge_GAD.exe
pause