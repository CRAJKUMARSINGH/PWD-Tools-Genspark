# 🚀 Bridge_GAD GitHub Release Workflow

This document describes the automated release workflow for Bridge_GAD that builds, signs, and publishes releases to GitHub.

## 🎯 Overview

When a Git tag is pushed to the repository (e.g., `v1.0.0`), GitHub Actions automatically:

1. Builds standalone Windows executables
2. Generates user documentation
3. Digitally signs the executables (if certificate is provided)
4. Creates a professional Windows installer
5. Publishes a new GitHub Release with all assets

## ⚙️ Workflow Details

### Trigger
The workflow is triggered when a tag matching the pattern `v*` is pushed to the repository.

### Jobs
1. **Build Job** (Windows):
   - Sets up Python environment
   - Installs dependencies
   - Builds executables with PyInstaller
   - Generates documentation
   - Signs executables (if certificate available)
   - Builds Windows installer
   - Archives build artifacts

2. **Release Job** (Ubuntu):
   - Downloads build artifacts
   - Creates release notes
   - Publishes GitHub Release

## 📁 Files

### Workflow File
- `.github/workflows/release.yml` - Main release workflow

### Build Artifacts
- `Bridge_GAD_GUI.exe` - Graphical User Interface (standalone)
- `Bridge_GAD.exe` - Command Line Interface (standalone)
- `Bridge_GAD_Setup.exe` - Professional Windows Installer
- `Bridge_GAD_User_Manual.pdf` - Complete User Manual

## 🔧 Setup Instructions

### 1. Code Signing (Optional)
To enable automatic code signing:

1. Convert your `.pfx` certificate to base64:
   ```bash
   base64 -i certificate.pfx -o cert_base64.txt
   ```

2. Add the following secrets to your GitHub repository:
   - `SIGNING_CERT` - Base64 content of your certificate
   - `SIGNING_PASS` - Password for your certificate

### 2. Tagging a Release
To create a new release:

```bash
# Create and push a new tag
git tag v1.0.1 -m "Release version 1.0.1"
git push origin v1.0.1
```

## 🔄 Process

1. **Tag Creation**: Developer creates and pushes a new tag
2. **Workflow Trigger**: GitHub Actions workflow starts automatically
3. **Build Phase**: Windows runner builds all executables
4. **Documentation**: User manual is generated in PDF format
5. **Signing**: Executables are signed with provided certificate
6. **Packaging**: Windows installer is created
7. **Release**: Ubuntu runner publishes the GitHub Release
8. **Notification**: Release is available in the GitHub Releases tab

## 📤 Output

### GitHub Release
- **Title**: Bridge_GAD v[version]
- **Assets**:
  - `Bridge_GAD_GUI.exe` - GUI executable
  - `Bridge_GAD.exe` - CLI executable
  - `Bridge_GAD_Setup.exe` - Windows installer
  - `Bridge_GAD_User_Manual.pdf` - User manual

### Release Notes
Automatically generated release notes include:
- Version information
- Key features
- Installation instructions
- Asset descriptions

## 🧪 Testing

The workflow has been tested and verified to:

1. Build executables correctly on Windows runners
2. Generate documentation in PDF format
3. Sign executables when certificate is provided
4. Create Windows installer with Inno Setup
5. Publish releases with proper assets and notes

## ✅ Benefits

- **Automation**: No manual steps required for release publishing
- **Consistency**: Standardized build and release process
- **Security**: Optional code signing for verified executables
- **Documentation**: Automatic generation of user manuals
- **Distribution**: Professional installer for easy deployment
- **Transparency**: Clear release notes and asset descriptions

## 🛠️ Troubleshooting

### "Inno Setup not found"
- Ensure you're using a Windows runner
- The workflow uses `windows-latest` which includes Inno Setup

### "Certificate signing failed"
- Verify `SIGNING_CERT` and `SIGNING_PASS` secrets are correctly set
- Check certificate validity and password

### "Build failed"
- Check dependencies in `requirements.txt`
- Verify PyInstaller build options
- Ensure all source files are included in the repository

## 🔄 Post-Release

After a successful release:

1. **Verify**: Check GitHub Releases tab for new release
2. **Test**: Download and test the executables
3. **Announce**: Share the release with users
4. **Monitor**: Watch for any issues reported by users