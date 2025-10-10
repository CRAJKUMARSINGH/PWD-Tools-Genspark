# Bridge GAD Code Signing and Auto-Update

This document explains how to add digital signatures to Bridge GAD executables and implement auto-update functionality.

## Digital Signature (Code Signing)

### Why Code Signing Matters

Without code signing, Windows may show:
> "Windows protected your PC"

With code signing, it shows:
> "Verified publisher: Er. Rajkumar Singh Chauhan"

### Option 1: Self-Signed Certificate (for testing)

#### Create a Self-Signed Certificate

Run this command in **PowerShell (Admin)**:

```powershell
New-SelfSignedCertificate -Type CodeSigningCert -Subject "CN=BridgeGAD" -CertStoreLocation "Cert:\CurrentUser\My"
```

#### Export the Certificate

1. Open **Manage User Certificates** (certmgr.msc)
2. Navigate to **Personal** → **Certificates**
3. Find your new *BridgeGAD* certificate
4. Right-click → **All Tasks** → **Export**
5. Choose "Yes, export the private key"
6. Select **Personal Information Exchange (.PFX)**
7. Set a strong password
8. Save as `BridgeGAD_SignCert.pfx`

### Option 2: Official Code-Signing Certificate

For production use, purchase an official certificate from:
- Sectigo
- DigiCert
- GlobalSign
- Comodo

Official certificates remove SmartScreen warnings completely.

### Signing Your Executables

#### Prerequisites

1. Certificate file (`.pfx`)
2. `signtool` (included with Windows SDK or Visual Studio)

#### Manual Signing

```bash
signtool sign /f BridgeGAD_SignCert.pfx /p yourpassword /tr http://timestamp.digicert.com /td sha256 /fd sha256 dist\Bridge_GAD.exe
signtool sign /f BridgeGAD_SignCert.pfx /p yourpassword /tr http://timestamp.digicert.com /td sha256 /fd sha256 dist\Bridge_GAD_GUI.exe
signtool sign /f BridgeGAD_SignCert.pfx /p yourpassword /tr http://timestamp.digicert.com /td sha256 /fd sha256 dist\Bridge_GAD_Setup.exe
```

#### Automated Signing

Run the provided batch script:

```
sign_executables.bat
```

This script will:
1. Check for the certificate file
2. Verify signtool availability
3. Prompt for certificate password
4. Sign all executables in the dist folder

## Auto-Update Functionality

### How It Works

The GUI application automatically checks for updates on startup by:
1. Querying the GitHub Releases API
2. Comparing the latest version with the current version
3. Prompting the user to download if a newer version is available

### Implementation Details

The auto-update feature is implemented in `src/bridge_gad/gui.py`:

```python
def check_for_updates(current_version: str):
    try:
        response = requests.get(LATEST_RELEASE_URL, timeout=5)
        if response.status_code == 200:
            latest_release = response.json()
            latest_version = latest_release["tag_name"]
            # Compare versions and prompt user
    except Exception as e:
        print("Update check failed:", e)
```

### Update Check URL

The application checks:
```
https://api.github.com/repos/CRAJKUMARSINGH/Bridge_GAD_Yogendra_Borse/releases/latest
```

### Version Comparison

The system compares:
- Current version (from `src/bridge_gad/__init__.py`)
- Latest GitHub release tag

### User Experience

When a new version is available:
1. A dialog box appears after 1 second
2. Shows current and latest versions
3. Offers to open the download page in the browser

## Testing Auto-Update

### Prerequisites

The `requests` library must be available:
```bash
pip install requests
```

### Manual Testing

1. Build the GUI executable
2. Run it to see the update check
3. Modify the version in `__init__.py` to test different scenarios

### GitHub Release Testing

1. Create a new release on GitHub with a higher version number
2. Run the GUI application
3. Verify the update prompt appears

## Troubleshooting

### Certificate Issues

**Error: "File not found"**
- Ensure the `.pfx` file is in the correct location
- Verify the file name matches what's in the script

**Error: "Password incorrect"**
- Double-check the certificate password
- Ensure there are no extra spaces

### Signing Tool Issues

**Error: "signtool not found"**
- Install Windows SDK or Visual Studio Build Tools
- Add the SDK bin directory to your PATH

### Update Check Issues

**Error: "Update check failed"**
- Check internet connectivity
- Verify the GitHub repository URL
- Ensure the GitHub API is accessible

## Best Practices

1. **Always timestamp signatures** - Prevents expiration issues
2. **Use strong passwords** - Protect your private key
3. **Backup certificates** - Store securely in multiple locations
4. **Test updates regularly** - Ensure the mechanism works
5. **Monitor certificate expiration** - Renew before expiration
6. **Use HTTPS for update checks** - Ensure secure communication

## Security Considerations

1. **Private key protection** - Never share your `.pfx` file
2. **Certificate storage** - Keep in secure locations
3. **Password management** - Use strong, unique passwords
4. **Update verification** - Always verify downloads from official sources
5. **Network security** - Use trusted timestamp servers