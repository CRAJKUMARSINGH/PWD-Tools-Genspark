@echo off
echo ==============================
echo Bridge_GAD Git Tag Creator
echo ==============================

REM Check if git is available
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Git not found. Please install Git to create tags.
    pause
    exit /b 1
)

REM Get current version from VERSION.txt
if not exist "VERSION.txt" (
    echo ❌ VERSION.txt not found.
    echo Please create a VERSION.txt file with the version number.
    pause
    exit /b 1
)

set /p VERSION=<VERSION.txt
echo Current version from VERSION.txt: %VERSION%

REM Ask for version confirmation or custom version
set /p CUSTOM_VERSION=Enter version number (or press Enter to use %VERSION%): 
if "%CUSTOM_VERSION%"=="" (
    set TAG_VERSION=%VERSION%
) else (
    set TAG_VERSION=%CUSTOM_VERSION%
)

REM Validate version format (should start with v or be a number)
echo %TAG_VERSION% | findstr /R "^v[0-9]*\.[0-9]*\.[0-9]*$">nul
if %errorlevel% equ 0 (
    set FULL_TAG=%TAG_VERSION%
) else (
    echo %TAG_VERSION% | findstr /R "^[0-9]*\.[0-9]*\.[0-9]*$">nul
    if %errorlevel% equ 0 (
        set FULL_TAG=v%TAG_VERSION%
    ) else (
        echo Invalid version format. Please use format: v1.0.0 or 1.0.0
        pause
        exit /b 1
    )
)

REM Check if tag already exists
git rev-parse "%FULL_TAG%" >nul 2>&1
if %errorlevel% equ 0 (
    echo ❌ Tag %FULL_TAG% already exists.
    pause
    exit /b 1
)

REM Ask for confirmation
echo.
echo Tag to be created: %FULL_TAG%
set /p CONFIRM=Create this tag? (y/N): 
if /i not "%CONFIRM%"=="y" (
    echo Tag creation cancelled.
    pause
    exit /b 0
)

REM Create and push tag
echo Creating tag %FULL_TAG%...
git tag %FULL_TAG% -m "Release version %FULL_TAG%"

echo Pushing tag to remote repository...
git push origin %FULL_TAG%

echo.
echo ✅ Tag %FULL_TAG% created and pushed successfully!
echo The GitHub release workflow will start automatically.
echo Check the Actions tab for build progress.
pause