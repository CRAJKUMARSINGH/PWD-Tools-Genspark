@echo off
echo ===========================
echo Building Bridge_GAD .EXE
echo ===========================

REM Clean previous builds
if exist dist rmdir /s /q dist
if exist build rmdir /s /q build

REM Create standalone executable using CLI entrypoint
python -m PyInstaller --onefile src\bridge_gad\cli.py

echo.
echo ✅ Build complete! Executable located in: dist\cli.exe
pause