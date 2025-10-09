print("Testing EMD Refund tool...")

# Test import
try:
    from gui.tools.emd_refund import EMDRefundTool
    print("Import successful!")
except Exception as e:
    print(f"Import failed: {e}")

# Test number to words function directly
def convert_number_to_words(num):
    """Convert number to words in Indian numbering system"""
    if num == 0:
        return "Zero"

    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    crore = " Crore "
    lakh = " Lakh "
    thousand = " Thousand "
    hundred = " Hundred "
    and_ = " and "

    words = ""

    # Crores
    if num // 10000000:
        crores = num // 10000000
        if crores > 9:
            words += convert_number_to_words(crores) + crore
        else:
            words += ones[crores] + crore
        num %= 10000000

    # Lakhs
    if num // 100000:
        lakhs = num // 100000
        if lakhs > 9:
            words += convert_number_to_words(lakhs) + lakh
        else:
            words += ones[lakhs] + lakh
        num %= 100000

    # Thousands
    if num // 1000:
        thousands = num // 1000
        if thousands > 9:
            words += convert_number_to_words(thousands) + thousand
        else:
            words += ones[thousands] + thousand
        num %= 1000

    # Hundreds
    if num // 100:
        hundreds = num // 100
        if hundreds > 9:
            words += convert_number_to_words(hundreds) + hundred
        else:
            words += ones[hundreds] + hundred
        num %= 100

    # Tens and ones
    if num > 0:
        if words:
            words += and_
        if num < 10:
            words += ones[num]
        elif num < 20:
            words += teens[num - 10]
        else:
            words += tens[num // 10]
            if num % 10:
                words += " " + ones[num % 10]

    return words.strip()

# Test the function
test_numbers = [0, 1, 15, 25, 100, 1000, 15000, 250000, 1500000, 25000000]
for num in test_numbers:
    result = convert_number_to_words(num)
    print(f"{num:,} -> {result}")