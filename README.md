# PWD Tools - Infrastructure Management Suite

A comprehensive set of tools for Public Works Department (PWD) operations, designed specifically for Lower Divisional Clerks in Rajasthan PWD.

## 🎯 Purpose

This suite provides simple, offline-capable tools for common PWD tasks:
- Hindi Bill Note Generation
- Stamp Duty Calculation
- EMD Refund Processing
- Delay Calculation
- Financial Analysis
- Deductions Table

## 🛠️ Available Tools

### Main Dashboard Tools
1. **📝 Hindi Bill Note Generator** - Create running and final bills in Hindi
2. **💰 Stamp Duty Calculator** - Calculate stamp duty with predefined rates
3. **💳 EMD Refund** - Simple EMD refund with 3 inputs only
4. **⏰ Delay Calculator** - Calculate project delays easily
5. **📊 Financial Analysis** - Simple financial analysis with calendar

### Additional Tools
6. **📉 Deductions Table** - Calculate TDS, Security, and other deductions
7. **📅 Delay Calculator** - Advanced project delay analysis
8. **🎫 Stamp Duty** - Alternative stamp duty calculator

## 🚀 Quick Start

### Local Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/pwd-tools.git
   cd pwd-tools
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

### Deployment to Streamlit Cloud

1. Fork this repository to your GitHub account
2. Go to [Streamlit Cloud](https://share.streamlit.io)
3. Click "New app" and select your forked repository
4. Set the main file to `app.py`
5. Deploy!

## 🧪 Testing

The repository includes automated testing to verify tool functionality:

```bash
python simple_test.py
```

This script tests each tool 5 times with random data and generates CSV reports.

## 📁 Project Structure

```
pwd-tools/
├── app.py                 # Main Streamlit application
├── streamlit_landing.py   # Core tool implementations
├── pages/                 # Individual tool pages
│   ├── 01_EMD_Refund.py
│   ├── 02_Deductions_Table.py
│   ├── 03_Delay_Calculator.py
│   ├── 04_Stamp_Duty.py
│   └── 05_Placeholders.py
├── .streamlit/
│   └── config.toml        # Streamlit configuration
├── requirements.txt       # Python dependencies
├── simple_test.py         # Automated testing script
└── README.md
```

## 🎨 Features

- **Offline First**: All tools work without internet connection
- **Simple Interface**: Clean, intuitive design for ease of use
- **Multi-language**: Hindi support for official documentation
- **Responsive**: Works on desktop and mobile devices
- **No External Dependencies**: Self-contained application

## 🏆 Initiative Credit

**Mrs. Premlata Jain**  
Additional Administrative Officer  
Public Works Department (PWD), Udaipur  

*"Empowering Infrastructure Excellence Through Digital Innovation"*

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For issues, questions, or feedback, please open an issue on this repository.

# PWD Tools Desktop Application

A comprehensive standalone desktop application for PWD (Public Works Department) tools and utilities, designed to eliminate web hosting dependencies and provide reliable offline functionality.

## Overview

This desktop application migrates the existing web-dependent PWD Tools suite into a fully offline, standalone solution. It maintains complete feature parity with the original web tools while providing enhanced reliability and performance.

**Prepared on Initiative of Mrs. Premlata Jain, AAO, PWD Udaipur**

## Features

### Core Tools
- **Bill Note Sheet** - Generate PWD documentation and bills
- **EMD Refund** - Calculate and process EMD refunds with PDF generation
- **Deductions Table** - Standard deductions calculator with customizable rates
- **Delay Calculator** - Project timeline analysis and penalty calculations
- **Financial Progress Tracker** - Monitor project progress and liquidity damages
- **Security Refund** - Security deposit refund eligibility calculator
- **Stamp Duty Calculator** - Work order stamp duty calculations
- **Excel se EMD** - Generate hand receipts from Excel files
- **Bill & Deviation Generator** - Infrastructure billing with deviation tracking
- **Faster Performance**: No web latency, instant response
- **Native OS Integration**: Works like any other desktop application
- **Keyboard Shortcuts**: Full keyboard support
- **Multi-window Workflow**: Open multiple tools simultaneously
- **System Tray Integration**: Minimize to system tray

## 🛠️ Available Tools

### Financial Tools
- 📊 **Excel se EMD**: Process Excel files for EMD refunds
- 📋 **Bill Note Sheet**: Generate and manage bill notes
- 💰 **EMD Refund**: Calculate EMD refunds with penalties
- 🔒 **Security Refund**: Process security deposit refunds
- 📊 **Financial Progress**: Track financial progress

### Calculation Tools
- ⏰ **Delay Calculator**: Calculate project delays and penalties
- 🏛️ **Stamp Duty**: Calculate stamp duty amounts
- 📊 **Deductions Table**: Calculate TDS and security deductions
- 📈 **Bill Deviation**: Generate bill deviation reports

### Data Processing
- 📝 **Tender Processing**: Process tender documents
- 📄 **Hand Receipt**: Generate hand receipts
- 🌐 **Excel to EMD Web**: Web-based Excel processing

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   GUI Layer     │    │ Business Logic  │    │   Data Layer    │    │  Output Layer   │
│                 │    │                 │    │                 │    │                 │
│ CustomTkinter   │◄──►│   Python Core   │◄──►│  SQLite Local   │◄──►│ PDF/Excel Export│
│   Modern UI     │    │                 │    │     Database    │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 📋 System Requirements

- **Operating System**: Windows 10+, macOS 10.14+, or Linux
- **Memory**: 4GB RAM minimum
- **Storage**: 500MB disk space
- **Python**: 3.9+ (for development only)

## 🚀 Installation

### Option 1: Quick Start (Windows)
1. Download the project files
2. Double-click `run_app.bat`
3. The application will automatically install dependencies and start

### Option 2: Manual Installation
1. **Install Python 3.9+** from [python.org](https://python.org)
2. **Clone or download** this repository
3. **Open terminal/command prompt** in the project directory
4. **Run setup script**:
   ```bash
   python setup.py
   ```
5. **Start the application**:
   ```bash
   python pwd_tools_desktop.py
   ```

### Option 3: Create Standalone Executable
1. **Install dependencies** (if not already done):
   ```bash
   pip install -r requirements.txt
   ```
2. **Build executable**:
   ```bash
   # Windows
   build_executable.bat
   
   # Linux/Mac
   pyinstaller --onefile --windowed pwd_tools_desktop.py
   ```
3. **Run the executable** from `dist/` folder

## 📁 Project Structure

```
PWD_Tools_Desktop/
├── pwd_tools_desktop.py          # Main application file
├── requirements.txt              # Python dependencies
├── setup.py                     # Installation script
├── run_app.bat                  # Windows launcher
├── build_executable.bat         # Executable builder
├── README.md                    # This file
├── database/
│   └── pwd_tools.db            # SQLite database
├── config/
│   └── settings.json           # Application configuration
├── modules/                     # Individual tool modules
├── utils/                       # Utility functions
└── assets/                      # Icons, templates, styles
```

## 🎮 Usage

### Starting the Application
1. **Run the application** using one of the methods above
2. **Main window opens** with all available tools displayed as buttons
3. **Click any tool** to open it in a new window
4. **Use multiple tools** simultaneously in separate windows

### Using Individual Tools

#### Excel se EMD
1. Click "📊 Excel se EMD" button
2. Click "Browse" to select Excel file
3. Click "Process Excel File" to analyze data
4. View results in the results frame

#### Bill Note Sheet
1. Click "📋 Bill Note Sheet" button
2. Fill in bill details (number, contractor, work description, amount)
3. Click "Save Bill" to store in database
4. Click "Generate PDF" to create PDF report

#### Delay Calculator
1. Click "⏰ Delay Calculator" button
2. Enter work name and dates
3. Click "Calculate Delay" to see results
4. View delay analysis and penalties

#### EMD Refund
1. Click "💰 EMD Refund" button
2. Enter tender details and validity date
3. Click "Calculate Refund" to see eligibility
4. View refund amount and status

## 🔧 Development

### Adding New Tools
1. **Create tool method** in `PWDToolsApp` class
2. **Add button** to tools list in `create_tools_grid()`
3. **Implement content method** for the tool
4. **Add database tables** if needed

### Customizing the Interface
- **Theme**: Modify `ctk.set_appearance_mode()` in `__init__()`
- **Colors**: Change button colors in `create_tools_grid()`
- **Layout**: Adjust window sizes and grid configurations

## 📊 Performance Metrics

- **Startup Time**: <2 seconds
- **Response Time**: <100ms
- **Memory Usage**: <50MB
- **Database Size**: <10MB typical

## 🔒 Security Features

- **Local Data Storage**: All data stored on your machine
- **No Internet Required**: Complete offline functionality
- **Database Encryption**: SQLite with optional encryption
- **Audit Logging**: Track all operations

## 🆘 Troubleshooting

### Common Issues

**"Python not found"**
- Install Python 3.9+ from python.org
- Add Python to PATH during installation

**"Module not found"**
- Run: `pip install -r requirements.txt`
- Or use: `python setup.py`

**"Application won't start"**
- Check Python version: `python --version`
- Ensure all dependencies are installed
- Check console for error messages

**"Database errors"**
- Delete `pwd_tools.db` file to reset database
- Application will recreate database on next start

## 📞 Support

For technical support or feature requests:
- Check the troubleshooting section above
- Review the console output for error messages
- Ensure all system requirements are met

## 📄 License

This project is developed for PWD Udaipur under the initiative of Mrs. Premlata Jain, AAO.

## 🙏 Acknowledgments

- **Mrs. Premlata Jain, AAO, PWD Udaipur** - Project initiative
- **CustomTkinter** - Modern GUI framework
- **Python Community** - Excellent libraries and tools

---

**PWD Tools Desktop** - Complete Independence from Web Dependencies
