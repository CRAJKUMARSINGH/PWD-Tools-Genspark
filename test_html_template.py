import os
import webbrowser
import urllib.parse

def test_html_template():
    """Test the EMD Refund HTML template with sample data"""
    # Sample data
    payee_name = "Test Contractor"
    amount = 12500
    work_description = "Road Construction Work"
    
    # URL encode the parameters
    encoded_payee = urllib.parse.quote(payee_name)
    encoded_work = urllib.parse.quote(work_description)
    
    # Create URL with parameters
    html_file = os.path.abspath("emd-refund.html")
    if os.path.exists(html_file):
        url = f"file://{html_file}?payee={encoded_payee}&amount={amount}&work={encoded_work}"
        print(f"Opening URL: {url}")
        
        # Open in browser
        webbrowser.open(url)
        print("HTML template opened in browser successfully!")
        return True
    else:
        print(f"HTML file not found: {html_file}")
        return False

if __name__ == "__main__":
    test_html_template()