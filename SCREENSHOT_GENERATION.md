# Screenshot Generation for PWD Tools

This document explains how to generate screenshots for the PWD Tools application.

## For Desktop Application Screenshots

The desktop application uses CustomTkinter and requires the following steps:

1. **Install required dependencies**:
   ```bash
   pip install customtkinter Pillow
   ```

2. **Run the screenshot generation script**:
   ```bash
   python auto_run_tools.py
   ```

3. **Screenshots will be saved in the `screenshots/` directory**:
   - Each tool will have 3 screenshots in `screenshots/<tool_name>/run_<n>.png`
   - Main landing page screenshot in `screenshots/landing/main.png`

## For Streamlit Application Screenshots

The Streamlit application can be screenshot using browser tools or automated tools:

1. **Run the Streamlit application**:
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** at http://localhost:8501

3. **Take screenshots manually** or use automated tools:
   - Browser developer tools (F12) → More tools → Screenshot
   - Extensions like Full Page Screen Capture
   - Automated tools like Selenium WebDriver

## Screenshot Requirements

### Desktop Application
- Each tool window should be captured 3 times
- Main landing page should be captured
- Screenshots should show the color templates and UI design

### Streamlit Application
- Landing page/dashboard
- Each individual tool page
- Results pages after calculations
- Error states (if applicable)

## Troubleshooting

### Common Issues

1. **Pillow not installed**:
   ```bash
   pip install Pillow
   ```

2. **CustomTkinter not installed**:
   ```bash
   pip install customtkinter
   ```

3. **Streamlit not installed**:
   ```bash
   pip install streamlit
   ```

4. **Permission errors**:
   - Run command prompt as administrator
   - Ensure write permissions in the project directory

### Manual Screenshot Process

If automated screenshot generation fails:

1. **For Desktop Application**:
   - Run `python main.py`
   - Open each tool manually
   - Take screenshots using Windows Snipping Tool or similar
   - Save in `screenshots/<tool_name>/` directory

2. **For Streamlit Application**:
   - Run `streamlit run app.py`
   - Navigate to http://localhost:8501
   - Open each tool page
   - Take screenshots using browser tools
   - Save in `streamlit_screenshots/` directory

## Directory Structure

After successful screenshot generation:

```
pwd-tools/
├── screenshots/
│   ├── excel_emd/
│   │   ├── run_1.png
│   │   ├── run_2.png
│   │   └── run_3.png
│   ├── bill_note/
│   │   ├── run_1.png
│   │   ├── run_2.png
│   │   └── run_3.png
│   └── landing/
│       └── main.png
├── streamlit_screenshots/
│   ├── landing_page.png
│   ├── hindi_bill_note.png
│   ├── stamp_duty_calculator.png
│   └── ... (other tool screenshots)
└── ... (other files)
```

## Support

For screenshot generation issues:
1. Ensure all dependencies are installed
2. Check that the application runs without errors
3. Verify write permissions in the project directory
4. Confirm that GUI operations are allowed in your environment