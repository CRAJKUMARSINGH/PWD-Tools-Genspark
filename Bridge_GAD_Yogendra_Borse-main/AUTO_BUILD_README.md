# Bridge GAD Auto Build System

This folder contains the auto-build system for the Bridge GAD application that automates the entire build process.

## Features

- Automatically extracts version information from source files
- Builds both CLI and GUI executables
- Creates Windows installer
- Outputs all deliverables in one go
- Consistent versioning across all components

## Usage

### One-Click Build

Run the auto-build script:

```
auto_build.bat
```

This will:
1. Extract current version from `src/bridge_gad/__init__.py`
2. Build both CLI and GUI executables using PyInstaller
3. Create the Windows installer using Inno Setup
4. Output all deliverables to the `dist` folder

### Output Files

The build process will generate the following files in the `dist` folder:
- `Bridge_GAD.exe` - Command-line interface version
- `Bridge_GAD_GUI.exe` - Graphical user interface version
- `Bridge_GAD_Setup.exe` - Windows installer

## Version Management

The system automatically extracts version information from:
- `src/bridge_gad/__init__.py` - Main package version
- `pyproject.toml` - Package metadata version
- `VERSION.txt` - Simple version file

All version numbers are kept in sync automatically.

## Prerequisites

1. **PyInstaller** - Installed via `pip install pyinstaller`
2. **Inno Setup** - Download from [https://jrsoftware.org/isinfo.php](https://jrsoftware.org/isinfo.php)

## Customization

You can customize the build process by modifying:
- `auto_build.bat` - Main build script
- `build_all.bat` - Executable build script
- `Bridge_GAD_Installer.iss` - Installer configuration

## Troubleshooting

### Inno Setup Compiler not found

If you get an error that ISCC is not found:
1. Install Inno Setup from [https://jrsoftware.org/isinfo.php](https://jrsoftware.org/isinfo.php)
2. Add Inno Setup to your PATH environment variable
3. Or update the path in `auto_build.bat` to match your installation

### PyInstaller not found

If PyInstaller is not found:
```
pip install pyinstaller
```

### Missing source files

Ensure all source files are in their correct locations:
- `src/bridge_gad/__init__.py` - Package initialization
- `src/bridge_gad/cli.py` - Command-line interface
- `src/bridge_gad/gui.py` - Graphical user interface