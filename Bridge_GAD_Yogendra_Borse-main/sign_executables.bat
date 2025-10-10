@echo off
echo =============================
echo Bridge_GAD Code Signing Tool
echo =============================

set CERT_FILE=BridgeGAD_SignCert.pfx
set TIMESTAMP_URL=http://timestamp.digicert.com

:: Check if certificate file exists
if not exist "%CERT_FILE%" (
    echo ❌ Certificate file not found: %CERT_FILE%
    echo.
    echo Please create a self-signed certificate or obtain an official code-signing certificate.
    echo.
    echo To create a self-signed certificate, run this in PowerShell (Admin):
    echo   New-SelfSignedCertificate -Type CodeSigningCert -Subject "CN=BridgeGAD" -CertStoreLocation "Cert:\CurrentUser\My"
    echo.
    echo Then export it as a .pfx file.
    pause
    exit /b 1
)

:: Check if signtool is available
where signtool >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ signtool not found in PATH
    echo.
    echo Please install Windows SDK or Visual Studio Build Tools to get signtool.
    pause
    exit /b 1
)

:: Prompt for certificate password
set /p CERT_PASSWORD=Enter certificate password: 

echo.
echo Signing executables...

:: Sign CLI executable
if exist "dist\Bridge_GAD.exe" (
    echo Signing Bridge_GAD.exe...
    signtool sign /f "%CERT_FILE%" /p "%CERT_PASSWORD%" /tr "%TIMESTAMP_URL%" /td sha256 /fd sha256 "dist\Bridge_GAD.exe"
    if %errorlevel% equ 0 (
        echo ✅ Bridge_GAD.exe signed successfully
    ) else (
        echo ❌ Failed to sign Bridge_GAD.exe
    )
) else (
    echo ⚠️  Bridge_GAD.exe not found in dist folder
)

:: Sign GUI executable
if exist "dist\Bridge_GAD_GUI.exe" (
    echo Signing Bridge_GAD_GUI.exe...
    signtool sign /f "%CERT_FILE%" /p "%CERT_PASSWORD%" /tr "%TIMESTAMP_URL%" /td sha256 /fd sha256 "dist\Bridge_GAD_GUI.exe"
    if %errorlevel% equ 0 (
        echo ✅ Bridge_GAD_GUI.exe signed successfully
    ) else (
        echo ❌ Failed to sign Bridge_GAD_GUI.exe
    )
) else (
    echo ⚠️  Bridge_GAD_GUI.exe not found in dist folder
)

:: Sign installer
if exist "dist\Bridge_GAD_Setup.exe" (
    echo Signing Bridge_GAD_Setup.exe...
    signtool sign /f "%CERT_FILE%" /p "%CERT_PASSWORD%" /tr "%TIMESTAMP_URL%" /td sha256 /fd sha256 "dist\Bridge_GAD_Setup.exe"
    if %errorlevel% equ 0 (
        echo ✅ Bridge_GAD_Setup.exe signed successfully
    ) else (
        echo ❌ Failed to sign Bridge_GAD_Setup.exe
    )
) else (
    echo ⚠️  Bridge_GAD_Setup.exe not found in dist folder
)

echo.
echo Code signing process completed!
pause