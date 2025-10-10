# Bridge_GAD - Professional Bridge Design Engineering Software

![Bridge_GAD](bridge_logo.png)

**Version 2.0.0** | **Developed by Er. Rajkumar Singh Chauhan**

Bridge_GAD is a comprehensive Python-based engineering software suite designed for professional bridge design and analysis. It provides engineers with tools to generate detailed bridge drawings, perform structural calculations, and create professional documentation.

## Key Features

### Core Engineering Tools
- Generate professional bridge general arrangement drawings
- Support for multiple bridge types (slab, beam, box culvert, PSC girder)
- DXF, PDF, HTML, SVG, PNG output formats
- Excel-based parameter input system
- Interactive 3D visualization capabilities

### Advanced Professional Features
- **Plugin Architecture**: Modular design with custom bridge modules
- **Auto-Update System**: Silent background updates for core and plugins
- **Marketplace Integration**: Install new modules directly from GitHub/Google Drive
- **Sandbox Security**: Safe plugin isolation using multiprocessing
- **Telemetry System**: Anonymous usage analytics for feature improvement
- **Error Logging**: Comprehensive diagnostic export system
- **Professional Installer**: Standalone Windows executable with setup wizard

## System Requirements

- Windows 7 or higher (64-bit recommended)
- 2 GB RAM minimum (4 GB recommended)
- 100 MB available disk space
- No Python installation required for end users

## Installation

1. Download `Bridge_GAD_Setup.exe` from the latest release
2. Run the installer as administrator
3. Follow the setup wizard prompts
4. Launch Bridge_GAD from desktop shortcut or Start menu

## Usage

### Quick Start
1. Launch Bridge_GAD GUI application
2. Enter bridge parameters (span, load, material properties)
3. Click "Compute" to generate results
4. Use "Export to Excel" to save results

### Advanced Features
- Access plugins through the Plugins menu
- View user manual via Help → User Manual
- Check for updates via Help → Check for Updates
- Export diagnostics via Help → Export Diagnostics

## Development

### Prerequisites
- Python 3.8 or higher
- Required packages in `requirements.txt`
- PyInstaller for building executables
- Inno Setup for creating Windows installer

### Building from Source
```bash
# Install dependencies
pip install -r requirements.txt

# Build executables
pyinstaller Bridge_GAD.spec
pyinstaller Bridge_GAD_GUI.spec

# Or use the provided build script
.\build_exe.bat

# Create installer
.\build_installer.bat
```

## Documentation

- [User Manual](docs/Bridge_GAD_User_Manual.pdf)
- [Release Manual](BRIDGE_GAD_v2.0_RELEASE_MANUAL.md)
- [Build Instructions](BUILD_INSTRUCTIONS.md)

## Project Structure

```
Bridge_GAD/
├── src/bridge_gad/          # Core application code
│   ├── __main__.py          # CLI entry point
│   ├── gui.py               # GUI application
│   ├── plugins/             # Plugin modules
│   └── ...                  # Other modules
├── docs/                    # Documentation
├── dist/                    # Build output
├── tests/                   # Unit tests
└── assets/                  # Icons and images
```

## 31-Step Development Journey

This project evolved through 31 comprehensive development steps into a professional engineering software suite:

1. **Foundation**: Basic CLI structure, core calculations, DXF generation
2. **Enhancement**: Multi-format output, advanced bridge types, visualization
3. **Professional Features**: Plugin architecture, auto-updates, marketplace
4. **Final Polish**: Security sandboxing, telemetry, release packaging

## Support

- Report issues on GitHub
- Contact developer: Er. Rajkumar Singh Chauhan
- Institution of Engineers (India), Udaipur Local Centre

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

*"Bridging Engineering Excellence with Modern Software Solutions"*

**Developed with ❤️ by Er. Rajkumar Singh Chauhan**  
**Institution of Engineers (India)**  
**Udaipur Local Centre Initiative (2025)**