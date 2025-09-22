# 🚀 HOW TO RUN - PWD Tools Desktop Application

## 📋 Prerequisites

### System Requirements
- **Operating System**: Windows 10/11, macOS, or Linux
- **Python Version**: Python 3.9 or higher
- **Memory**: Minimum 4GB RAM
- **Storage**: 100MB free space

### Check Python Installation
```bash
python --version
```
**Expected Output**: `Python 3.9.x` or higher

---

## 🛠️ Installation Steps

### Method 1: Quick Start (Recommended)
1. **Download/Clone** the repository
2. **Run the installer**:
   ```bash
   # Windows
   INSTALL_DEPS.bat
   
   # macOS/Linux
   chmod +x install.sh
   ./install.sh
   ```

### Method 2: Manual Installation
1. **Navigate** to the project directory:
   ```bash
   cd PWD-Tools-Genspark
   ```

2. **Install dependencies** (if any):
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation**:
   ```bash
   python --version
   ```

---

## 🎯 Running the Application

### Quick Launch
```bash
# Windows
START_APP.bat

# macOS/Linux
chmod +x start.sh
./start.sh
```

### Manual Launch
```bash
python pwd_tools_simple.py
```

### Alternative Launch Methods
```bash
# Using the main application
python main.py

# Using the run script
python run_app.py
```

---

## 🛠️ Available Tools

The application provides **10 comprehensive tools**:

| Tool | Type | Description |
|------|------|-------------|
| 🔧 **Bill Note Sheet** | Web | Professional bill generation |
| 🔧 **EMD Refund** | Web | Earnest money refund calculator |
| 🔧 **Deductions Table** | Web | Tax and deduction calculations |
| 🔧 **Delay Calculator** | Web | Project delay analysis |
| 🔧 **Financial Progress** | Desktop | Progress tracking with HTML output |
| 🔧 **Security Refund** | Desktop | Security deposit refund calculator |
| 🔧 **Stamp Duty** | Desktop | Stamp duty calculation tool |
| 🔧 **Excel se EMD** | Web | Excel-based EMD processing |
| 🔧 **Bill & Deviation** | Web | Combined bill and deviation generator |
| 🔧 **Faster Performance** | Info | Performance features information |

---

## 🔧 Tool Usage Guide

### Desktop Tools (Local Processing)
1. **Click** the tool button
2. **Follow** the on-screen instructions
3. **Enter** required data
4. **View** results in the application

### Web Tools (Browser Redirect)
1. **Click** the tool button
2. **Browser** opens automatically
3. **Use** the web-based interface
4. **Close** browser when done

---

## 🆘 Troubleshooting

### Common Issues

#### ❌ **"Python not found"**
**Solution**:
- Install Python 3.9+ from [python.org](https://python.org)
- Add Python to PATH during installation
- Restart command prompt/terminal

#### ❌ **"Module not found"**
**Solution**:
```bash
pip install -r requirements.txt
```

#### ❌ **"Application won't start"**
**Solution**:
- Check Python version: `python --version`
- Ensure all files are in correct location
- Check console for error messages

#### ❌ **"Permission denied" (Unix/macOS)**
**Solution**:
```bash
chmod +x *.sh
chmod +x *.bat
```

### Performance Issues

#### ⚠️ **Slow startup**
- Close other applications
- Ensure sufficient RAM available
- Check for antivirus interference

#### ⚠️ **Tool not responding**
- Check internet connection (for web tools)
- Restart the application
- Check browser compatibility

---

## 🔒 Security Notes

### Data Privacy
- ✅ **Local Processing**: All desktop tools process data locally
- ✅ **No Data Transmission**: Desktop tools don't send data anywhere
- ✅ **Web Tools**: Only web-based tools use external services

### Safe Usage
- ✅ **Offline Capable**: Desktop tools work without internet
- ✅ **No Malware**: Uses only standard Python libraries
- ✅ **Open Source**: Code is transparent and auditable

---

## 📞 Support

### Getting Help
1. **Check** this documentation first
2. **Review** console output for errors
3. **Verify** system requirements
4. **Contact** technical support if needed

### System Information
When reporting issues, include:
- Operating System and version
- Python version (`python --version`)
- Error messages from console
- Steps to reproduce the issue

---

## 🎉 Success Indicators

### ✅ **Application Started Successfully**
- Window opens with colorful interface
- All 10 tool buttons are visible
- No error messages in console

### ✅ **Tools Working Correctly**
- Desktop tools open new windows
- Web tools open browser automatically
- All calculations produce correct results

---

## 📝 Additional Notes

### Development
- **Main File**: `pwd_tools_simple.py`
- **Configuration**: No external config files needed
- **Dependencies**: Standard library only

### Updates
- **Version**: Current version is stable and production-ready
- **Updates**: Check repository for latest versions
- **Compatibility**: Maintains backward compatibility

---

**Last Updated**: $(date)  
**Version**: 1.0  
**Status**: ✅ **PRODUCTION READY**
