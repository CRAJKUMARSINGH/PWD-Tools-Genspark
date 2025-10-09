@echo off
echo Killing PWD Tools processes...
echo.

REM Kill any running Python processes related to PWD Tools
taskkill /f /im python.exe /fi "WINDOWTITLE eq PWD Tools*" 2>nul
taskkill /f /im pythonw.exe /fi "WINDOWTITLE eq PWD Tools*" 2>nul

REM Kill processes by name that might be running the app
taskkill /f /im "python.exe" /fi "COMMANDLINE eq *run_app.py*" 2>nul
taskkill /f /im "pythonw.exe" /fi "COMMANDLINE eq *run_app.py*" 2>nul
taskkill /f /im "python.exe" /fi "COMMANDLINE eq *main.py*" 2>nul
taskkill /f /im "pythonw.exe" /fi "COMMANDLINE eq *main.py*" 2>nul
taskkill /f /im "python.exe" /fi "COMMANDLINE eq *PWD Tools*" 2>nul
taskkill /f /im "pythonw.exe" /fi "COMMANDLINE eq *PWD Tools*" 2>nul

echo.
echo Process killing completed.
echo.
pause