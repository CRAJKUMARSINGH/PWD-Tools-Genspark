# PWD Tools Deployment to Streamlit Cloud

This document provides instructions for deploying the PWD Tools application to Streamlit Cloud.

## Prerequisites

1. A Streamlit Cloud account (free at [share.streamlit.io](https://share.streamlit.io))
2. This repository forked or cloned to your GitHub account

## Deployment Steps

1. Go to [https://share.streamlit.io](https://share.streamlit.io) and sign in
2. Click "New app" 
3. Select your repository containing the PWD Tools code
4. Set the following deployment options:
   - Branch: `main` (or your default branch)
   - Main file: `app.py`
   - App URL: Choose a memorable name (e.g., `pwd-tools`)
5. Click "Deploy!"

## Configuration

The application includes the following configuration files:

- `.streamlit/config.toml` - Streamlit configuration with theme and server settings
- `requirements.txt` - Python dependencies

## Application Structure

The deployed application includes:

1. Main dashboard (`app.py`) - Landing page with tool navigation
2. Individual tools in the `pages/` directory:
   - EMD Refund Calculator
   - Deductions Table Calculator
   - Delay Calculator
   - Stamp Duty Calculator
3. Core functionality in `streamlit_landing.py` - Contains the main tools

## Testing

The repository includes automated testing scripts:

- `simple_test.py` - Tests each tool 5 times with random data
- Generates CSV reports for each tool's test results

To run tests locally:
```bash
python simple_test.py
```

## Customization

To customize the application:

1. Modify tool parameters in the respective files in `pages/`
2. Update styling in `app.py` CSS sections
3. Add new tools by creating new files in `pages/`

## Troubleshooting

Common deployment issues:

1. **Missing dependencies**: Ensure all packages in `requirements.txt` are compatible with Streamlit Cloud
2. **File paths**: Streamlit Cloud uses Linux-style paths; avoid Windows-specific path separators
3. **Memory limits**: Large datasets or complex calculations may exceed Streamlit Cloud's resource limits

## Support

For issues with deployment or customization, contact the repository maintainers or refer to [Streamlit Cloud documentation](https://docs.streamlit.io/cloud).