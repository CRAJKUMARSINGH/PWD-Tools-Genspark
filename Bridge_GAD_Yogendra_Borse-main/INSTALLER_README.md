# 📦 Bridge_GAD Windows Installer

This document describes the professional Windows installer for Bridge_GAD.

## 🎯 Overview

The installer provides a professional installation experience for Bridge_GAD with branding, license agreement, and proper application integration with the Windows operating system.

## 🧩 Features

### 1. Professional Branding
- Custom installer icon
- Application name and version display
- Publisher information
- Professional installation wizard

### 2. License Agreement
- Integrated license agreement display
- User must accept terms before installation
- Uses the project's LICENSE file

### 3. Application Integration
- Start Menu shortcuts
- Optional desktop shortcut
- Uninstaller integration
- File associations

### 4. Components Installed
- Bridge_GAD CLI executable
- Bridge_GAD GUI executable
- User Manual (PDF)
- Application icon

## 📁 Installation Structure

```
Program Files\Bridge_GAD\
├── Bridge_GAD.exe          # Command-line interface
├── Bridge_GAD_GUI.exe      # Graphical user interface
├── bridge.ico              # Application icon
├── LICENSE                 # License agreement
└── docs\
    └── Bridge_GAD_User_Manual.pdf  # User manual
```

## 🔄 Installation Process

1. **Welcome Screen**: Introduction to the installer
2. **License Agreement**: Display and acceptance of terms
3. **Installation Directory**: Selection of install location
4. **Start Menu Folder**: Selection of Start Menu folder
5. **Additional Tasks**: Optional desktop shortcut
6. **Ready to Install**: Confirmation of installation settings
7. **Installation**: Copying of files
8. **Finish**: Completion with option to launch application

## ⚙️ Installer Script

### File: `Bridge_GAD_Installer.iss`

#### Sections:
- **[Setup]**: Installation configuration
- **[Languages]**: Language support
- **[Tasks]**: Installation tasks (desktop shortcut)
- **[Files]**: Files to be installed
- **[Icons]**: Start Menu and desktop icons
- **[Run]**: Post-installation actions

#### Key Features:
- Version detection from VERSION.txt
- License file integration
- Desktop shortcut option
- Start Menu integration
- Automatic application launch option

## 🛠️ Building the Installer

### Prerequisites
- Inno Setup Compiler
- Built executables in dist/ directory
- Documentation files in docs/ directory

### Build Process
1. Ensure all required files are built:
   - `dist/Bridge_GAD.exe`
   - `dist/Bridge_GAD_GUI.exe`
   - `docs/Bridge_GAD_User_Manual.pdf`
   - `bridge.ico`
   - `LICENSE`
   - `VERSION.txt`

2. Open `Bridge_GAD_Installer.iss` in Inno Setup Compiler

3. Click **Compile (F9)** or select **Build** from the menu

4. Installer will be generated in the `dist/` directory as `Bridge_GAD_Setup.exe`

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

## 🔧 Post-Installation

### Launch Options
- Automatic launch after installation (optional)
- Start Menu shortcuts
- Desktop shortcut (if selected)

### Uninstallation
- Control Panel → Programs and Features
- Start Menu → Bridge_GAD → Uninstall
- Removes all installed files and shortcuts

## 🧪 Testing

The installer has been tested and verified to:

1. Display proper branding and version information
2. Show license agreement and require acceptance
3. Install all components correctly
4. Create Start Menu shortcuts
5. Create desktop shortcut when selected
6. Launch application after installation
7. Uninstall cleanly

## ✅ Benefits

- **Professional Appearance**: Polished installer with branding
- **User Experience**: Clear installation process with options
- **Integration**: Proper Windows integration with shortcuts
- **Legal Compliance**: License agreement display and acceptance
- **Flexibility**: Optional components and installation locations
- **Reliability**: Tested installation and uninstallation process