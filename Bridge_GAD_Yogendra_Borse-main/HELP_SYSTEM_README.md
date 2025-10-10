# 🆘 Bridge_GAD Help System

This document describes the integrated help system implemented for Bridge_GAD.

## 🎯 Overview

The help system provides users with easy access to the user manual directly from within the application through the "Help → User Manual" menu option.

## 🧩 Components

### 1. Menu Integration
- Added "User Manual" option to the Help menu
- Maintains existing "About" option with separator

### 2. Manual Opening Methods
- **Embedded Viewer**: When PDF and tkPDFViewer are available
- **External Viewer**: Opens with system default PDF/Markdown viewer

### 3. Fallback Mechanisms
- Searches for manual in multiple possible locations
- Falls back to Markdown version if PDF is not available
- Shows error message if no manual is found

## 📁 Manual Locations

The system searches for the manual in the following locations:
1. `docs/Bridge_GAD_User_Manual.pdf` (relative to project root)
2. `docs/Bridge_GAD_User_Manual.md` (relative to project root)
3. `docs/Bridge_GAD_User_Manual.pdf` (relative to current directory)
4. `docs/Bridge_GAD_User_Manual.md` (relative to current directory)

## 🔄 Process

1. User selects "Help → User Manual" from the menu
2. System searches for available manual (PDF preferred)
3. If PDF is found and tkPDFViewer is available, shows embedded viewer
4. Otherwise opens with system default application
5. If no manual is found, shows error message

## 📦 Dependencies

### Required for Embedded Viewer
- **tkPDFViewer**: Python library for PDF viewing in tkinter

### Installation
```bash
pip install -r requirements.txt
```

This installs all required dependencies including tkPDFViewer.

## 🛠️ Implementation Details

### File: `src/bridge_gad/gui.py`

#### New Methods Added:
- `open_user_manual()`: Main method to open the manual
- `show_embedded_manual(pdf_path)`: Shows manual in embedded viewer

#### Menu Update:
- Added "User Manual" command to Help menu
- Maintained existing "About" command

### File: `build_exe.bat`

#### Build Configuration:
- Added `--add-data` parameters to include manuals in executable
- Includes both PDF and Markdown versions when available

## 🧪 Testing

The help system has been tested and verified to:

1. Open PDF manuals in embedded viewer when available
2. Fall back to external viewer when embedded viewer is not available
3. Open Markdown manuals when PDF is not available
4. Show appropriate error messages when no manual is found
5. Work correctly in both development and packaged environments

## ✅ Features

- **Graceful Degradation**: Works without PDF dependencies
- **Multiple Formats**: Supports both PDF and Markdown manuals
- **Embedded Viewing**: Shows PDF directly in application when possible
- **External Fallback**: Opens with system viewer when embedded viewing is not available
- **Error Handling**: Provides clear error messages when manual is not found
- **Cross-Platform**: Works on any system with Python and tkinter

## 📈 Benefits

- **User Experience**: Easy access to documentation without leaving the application
- **Flexibility**: Works with different manual formats and viewing methods
- **Reliability**: Multiple fallback mechanisms ensure manual is always accessible
- **Maintainability**: Simple implementation that's easy to update and modify