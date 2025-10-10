@echo off
echo ===============================
echo Bridge_GAD - Complete Build Script
echo ===============================

REM Read version from VERSION.txt
if exist VERSION.txt (
    set /p VERSION=<VERSION.txt
) else (
    set VERSION=1.0.0
)

echo Version: %VERSION%

echo.
echo Step 1: Cleaning previous builds...
if exist dist rmdir /s /q dist
if exist build rmdir /s /q build

echo.
echo Step 2: Building executables with PyInstaller...
python -m PyInstaller --onefile ^
    --name Bridge_GAD ^
    --add-data "src\bridge_gad\*.py;bridge_gad" ^
    src\bridge_gad\cli.py

python -m PyInstaller --onefile --noconsole ^
    --name Bridge_GAD_GUI ^
    --icon=bridge.ico ^
    src\bridge_gad\gui.py

echo.
echo Step 3: Building installer with Inno Setup...
REM Check if Inno Setup Compiler is available
where ISCC >nul 2>&1
if %errorlevel% == 0 (
    ISCC Bridge_GAD_Installer.iss
    echo.
    echo ✅ Installer built successfully!
    echo Installer located at: dist\Bridge_GAD_Setup.exe
) else (
    echo.
    echo ⚠️  Inno Setup Compiler not found in PATH
    echo Please install Inno Setup from https://jrsoftware.org/isinfo.php
    echo Then add it to your PATH or run the installer script manually
)

echo.
echo ===============================
echo Build Summary:
echo ===============================
echo Version: %VERSION%
echo ✅ CLI Executable: dist\Bridge_GAD.exe
echo ✅ GUI Executable: dist\Bridge_GAD_GUI.exe
echo ℹ️  Installer: dist\Bridge_GAD_Setup.exe (if Inno Setup is installed)

pause