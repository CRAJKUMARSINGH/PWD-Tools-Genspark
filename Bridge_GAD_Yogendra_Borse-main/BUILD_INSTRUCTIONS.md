# Bridge_GAD v2.0.0 - Build and Release Instructions

## Overview

This document provides step-by-step instructions to build the final standalone Windows executable installer for Bridge_GAD, a professional bridge design engineering software suite.

## Prerequisites

1. Python 3.8 or higher installed
2. PyInstaller installed (`pip install pyinstaller`)
3. Inno Setup installed (https://jrsoftware.org/isinfo.php)
4. All project dependencies installed (`pip install -r requirements.txt`)

## Step 1: Build Executables with PyInstaller

### CLI Version
```bash
pyinstaller --onefile ^
    --name Bridge_GAD ^
    --hidden-import=yaml ^
    --hidden-import=ezdxf ^
    --hidden-import=reportlab ^
    --hidden-import=pygame ^
    --hidden-import=numpy ^
    --hidden-import=pandas ^
    --hidden-import=matplotlib ^
    --hidden-import=openpyxl ^
    --hidden-import=scipy ^
    --hidden-import=requests ^
    --hidden-import=xlrd ^
    --hidden-import=PIL ^
    --add-data "src\bridge_gad\*.py;bridge_gad" ^
    src\bridge_gad\cli.py
```

### GUI Version
```bash
pyinstaller --onefile --noconsole ^
    --name Bridge_GAD_GUI ^
    --icon=bridge.ico ^
    --version-file file_version_info.txt ^
    --hidden-import=yaml ^
    --hidden-import=ezdxf ^
    --hidden-import=reportlab ^
    --hidden-import=pygame ^
    --hidden-import=numpy ^
    --hidden-import=pandas ^
    --hidden-import=matplotlib ^
    --hidden-import=openpyxl ^
    --hidden-import=scipy ^
    --hidden-import=requests ^
    --hidden-import=xlrd ^
    --hidden-import=PIL ^
    --hidden-import=tkPDFViewer ^
    --add-data "docs\Bridge_GAD_User_Manual.md;docs" ^
    --add-data "docs\Bridge_GAD_User_Manual.pdf;docs" ^
    src\bridge_gad\gui.py
```

## Step 2: Build Windows Installer with Inno Setup

1. Ensure both executables are built and located in the `dist` folder
2. Run the Inno Setup compiler:
   ```bash
   ISCC "Bridge_GAD_Installer.iss"
   ```

## Step 3: Verify Installation

1. Run the generated installer (`dist\Bridge_GAD_Setup.exe`)
2. Verify that:
   - Both CLI and GUI versions launch correctly
   - All plugins load and function
   - Auto-update system works
   - Telemetry and error logging function
   - Desktop shortcuts are created
   - Documentation is accessible

## Expected Output

After successful completion, you should have:
- `dist\Bridge_GAD.exe` - Command-line interface
- `dist\Bridge_GAD_GUI.exe` - Graphical user interface
- `dist\Bridge_GAD_Setup.exe` - Windows installer

## Version Information

Current version: 2.0.0
Release date: October 2025

## Features Included

- Core auto-update system
- Plugin marketplace & auto-install
- Sandbox isolation for plugins
- Telemetry, error logging, and diagnostics
- Modular architecture with scaffolding for new bridge modules
- Professional installer with desktop shortcuts
- Comprehensive documentation

## Troubleshooting

### PyInstaller Issues
- Ensure all dependencies are installed
- Check that hidden imports match project requirements
- Verify data files are correctly included

### Inno Setup Issues
- Ensure ISCC is in PATH
- Verify all source files exist
- Check file permissions

### Execution Issues
- Run as administrator if needed
- Disable antivirus temporarily during build
- Ensure sufficient disk space

## Distribution

The final installer (`Bridge_GAD_Setup.exe`) is ready for distribution to end users and contains all necessary components for a complete Bridge_GAD installation.