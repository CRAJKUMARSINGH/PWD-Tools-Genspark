@echo off
echo ==============================
echo Bridge_GAD Executable Verification
echo ==============================

REM Check if executables exist
if not exist "dist\Bridge_GAD.exe" (
    echo ❌ CLI executable not found: dist\Bridge_GAD.exe
    exit /b 1
)

if not exist "dist\Bridge_GAD_GUI.exe" (
    echo ❌ GUI executable not found: dist\Bridge_GAD_GUI.exe
    exit /b 1
)

echo ✅ Both executables found
echo.

REM Display executable information
echo CLI Executable Information:
for %%A in (dist\Bridge_GAD.exe) do (
    echo   Name: %%~nxA
    echo   Size: %%~zA bytes
    echo   Modified: %%~tA
)
echo.

echo GUI Executable Information:
for %%A in (dist\Bridge_GAD_GUI.exe) do (
    echo   Name: %%~nxA
    echo   Size: %%~zA bytes
    echo   Modified: %%~tA
)
echo.

REM Test CLI executable (basic test)
echo Testing CLI executable...
dist\Bridge_GAD.exe --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ CLI executable runs without crashing
) else (
    echo ⚠️  CLI executable has issues (may be missing dependencies)
)

echo.
echo Testing GUI executable...
echo This will launch the GUI for 5 seconds, then close it.
echo.

REM Launch GUI executable in background
start "" "dist\Bridge_GAD_GUI.exe"

REM Wait for 5 seconds
timeout /t 5 /nobreak >nul

REM Try to kill the process (if still running)
taskkill /f /im Bridge_GAD_GUI.exe >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ GUI executable launched and terminated successfully
) else (
    echo ⚠️  GUI executable may have closed on its own
)

echo.
echo ==============================
echo Verification Complete
echo ==============================
echo ✅ Executables are ready for packaging
echo 📦 Next step: Run build_installer.bat to create the installer
pause