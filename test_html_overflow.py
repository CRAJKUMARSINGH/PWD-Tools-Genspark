import webbrowser
import urllib.parse
import os

def test_html_overflow():
    """Test the HTML template with long text to ensure no overflow"""
    # Sample data with long text that might cause overflow
    test_data = [
        {
            "payee": "Very Long Contractor Name That Might Cause Overflow Issues In The Template",
            "amount": 125000.50,
            "work": "Extremely Long Work Description That Should Not Overflow From The Right Margin Of The Page And Should Wrap Properly Within The Designated Area"
        },
        {
            "payee": "Another Contractor With A Very Long Name For Testing Purposes",
            "amount": 95000.75,
            "work": "Another Extremely Long Work Description That Tests The Limits Of Text Wrapping And Ensures That All Content Stays Within The Page Boundaries Without Overflowing"
        }
    ]
    
    # Get the absolute path to the HTML file
    html_file = os.path.abspath("emd-refund.html")
    
    print("Testing HTML template with long text to ensure no overflow...")
    print(f"HTML file path: {html_file}")
    
    # Test with the first set of data
    data = test_data[0]
    encoded_payee = urllib.parse.quote(data["payee"])
    encoded_amount = urllib.parse.quote(str(data["amount"]))
    encoded_work = urllib.parse.quote(data["work"])
    
    # Create URL with parameters
    url = f"file://{html_file}?payee={encoded_payee}&amount={encoded_amount}&work={encoded_work}"
    
    print(f"\nOpening test URL with long text:")
    print(f"Payee: {data['payee']}")
    print(f"Amount: {data['amount']}")
    print(f"Work: {data['work']}")
    
    # Open in browser
    webbrowser.open(url)
    
    print("\nCheck the browser to verify:")
    print("1. All text stays within the page margins")
    print("2. No text overflows from the right margin")
    print("3. Text wraps properly within the designated areas")
    print("4. The layout remains intact")

if __name__ == "__main__":
    test_html_overflow()