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
9. **📈 Financial Progress** - Track financial progress
10. **🔒 Security Refund** - Process security deposit refunds

## 🚀 Quick Start

### Local Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
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

The repository includes automated testing scripts:

```bash
python comprehensive_test.py
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
├── comprehensive_test.py  # Automated testing script
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

This project is licensed under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For issues, questions, or feedback, please open an issue on this repository.