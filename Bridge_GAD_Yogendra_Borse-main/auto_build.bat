@echo off
echo =============================
echo Bridge_GAD Auto Build System
echo =============================

setlocal enabledelayedexpansion

:: ----- Step 1: Extract current version -----
for /f "tokens=2 delims== " %%A in ('findstr /C:"__version__" src\bridge_gad\__init__.py') do set "ver=%%~A"
set ver=%ver:"=%
echo Current version: %ver%

:: ----- Step 2: Run PyInstaller builds -----
echo.
echo Building executables with PyInstaller...
call build_all.bat

:: ----- Step 3: Rebuild installer -----
echo.
echo Building installer...
if exist "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" (
    "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" Bridge_GAD_Installer.iss
    echo.
    echo ✅ Installer built successfully!
) else (
    echo.
    echo ⚠️  Inno Setup Compiler not found. Please install Inno Setup.
)

echo.
echo ✅ All builds complete!
echo Output: dist\Bridge_GAD.exe, Bridge_GAD_GUI.exe, Bridge_GAD_Setup.exe
pause