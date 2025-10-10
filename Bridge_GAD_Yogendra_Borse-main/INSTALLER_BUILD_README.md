# 📦 Bridge_GAD Installer Build Guide

This document describes how to build the professional Windows installer for Bridge_GAD.

## 🎯 Overview

The installer provides a professional installation experience for Bridge_GAD with branding, license agreement, and proper application integration with the Windows operating system.

## 🧩 Prerequisites

### 1. Inno Setup Compiler
- Download from: [https://jrsoftware.org/isinfo.php](https://jrsoftware.org/isinfo.php)
- Install the latest version of Inno Setup
- Ensure `ISCC.exe` is available in your PATH

### 2. Built Executables
- `dist/Bridge_GAD.exe` (CLI version)
- `dist/Bridge_GAD_GUI.exe` (GUI version)
- These are created by running `build_exe.bat`

### 3. Documentation
- `docs/Bridge_GAD_User_Manual.pdf`
- This is created by running `build_manual.bat`

### 4. Supporting Files
- `bridge.ico` (Application icon)
- `LICENSE` (License agreement)
- `VERSION.txt` (Version information)

## 🛠️ Building the Installer

### Method 1: Using the Batch Script (Recommended)
```cmd
build_installer.bat
```

This script will:
1. Check for all required prerequisites
2. Verify that all required files exist
3. Build the installer using Inno Setup Compiler
4. Output the installer to `dist/Bridge_GAD_Setup.exe`

### Method 2: Manual Build
1. Open `Bridge_GAD_Installer.iss` in Inno Setup Compiler
2. Click **Compile (F9)** or select **Build** from the menu
3. The installer will be generated in the `dist/` directory

### Method 3: Command Line Build
```cmd
ISCC Bridge_GAD_Installer.iss
```

## 📁 Required Files

### Executables (Created by build_exe.bat)
```
dist/
├── Bridge_GAD.exe          # Command-line interface
├── Bridge_GAD_GUI.exe      # Graphical user interface
```

### Documentation (Created by build_manual.bat)
```
docs/
└── Bridge_GAD_User_Manual.pdf  # User manual
```

### Supporting Files (Included in repository)
```
├── bridge.ico              # Application icon
├── LICENSE                 # License agreement
├── VERSION.txt             # Version information
├── Bridge_GAD_Installer.iss  # Installer script
```

## ⚙️ Installer Features

### Branding
- Custom installer icon
- Application name and version display
- Publisher information
- Professional installation wizard

### License Agreement
- Integrated license agreement display
- User must accept terms before installation

### Application Integration
- Start Menu shortcuts
- Optional desktop shortcut
- Uninstaller integration

### Components Installed
- Bridge_GAD CLI executable
- Bridge_GAD GUI executable
- User Manual (PDF)
- Application icon

## 📤 Output

### Generated File
- `dist/Bridge_GAD_Setup.exe`: Professional Windows installer

### Installation Directory
- Default: `C:\Program Files\Bridge_GAD\`

### Start Menu
- Group: `Bridge_GAD`
- Shortcuts:
  - Bridge_GAD (CLI)
  - Bridge_GAD (GUI)
  - Bridge_GAD User Manual

### Desktop
- Optional shortcut for Bridge_GAD (GUI)

## 🔧 Troubleshooting

### "Inno Setup Compiler not found"
- Ensure Inno Setup is installed
- Add Inno Setup directory to your PATH environment variable
- Or run the compiler directly from its installation directory

### "Required files not found"
- Ensure you've run `build_exe.bat` to create the executables
- Ensure you've run `build_manual.bat` to create the user manual
- Verify all supporting files are present

### "Installation fails"
- Run the installer as Administrator
- Ensure you have write permissions to the installation directory
- Check Windows Event Viewer for detailed error information

## 🧪 Testing

Before distributing the installer, test it on a clean system to ensure:

1. All prerequisites are properly checked
2. Installation completes successfully
3. All components are installed correctly
4. Start Menu shortcuts work
5. Desktop shortcut (if selected) works
6. Application launches correctly
7. User manual opens correctly
8. Uninstallation works properly

## ✅ Benefits

- **Professional Appearance**: Polished installer with branding
- **User Experience**: Clear installation process with options
- **Integration**: Proper Windows integration with shortcuts
- **Legal Compliance**: License agreement display and acceptance
- **Flexibility**: Optional components and installation locations
- **Reliability**: Tested installation and uninstallation process

## 🔄 Post-Build Steps

After building the installer:

1. **Test the installer** on a clean system
2. **Sign the installer** with your code signing certificate:
   ```cmd
   signtool sign /f BridgeGAD_SignCert.pfx /p yourpassword /tr http://timestamp.digicert.com /td sha256 /fd sha256 dist\Bridge_GAD_Setup.exe
   ```
3. **Verify the signature**:
   ```cmd
   signtool verify /pa dist\Bridge_GAD_Setup.exe
   ```
4. **Upload to GitHub** as part of your release process