# Hindi Bill Note Tool - SIMPLE VERSION
## For Lower Divisional Clerks

### 🎯 **NO COMPLEXITY - JUST HINDI BILL NOTES**

This is the **simplified Hindi bill note tool** designed specifically for lower divisional clerks. Handles both **Running Bills** and **Final Bills** in proper Hindi format as per original repository.

---

## 🚀 **How to Run**

### **Windows (Easiest)**
```bash
# Just double-click this file:
run_hindi_bill.bat
```

### **Manual**
```bash
python run_hindi_bill.py
```

---

## 🛠️ **Available Bill Types**

### 1. **रनिंग बिल (Running Bill)** - Simple Fields
- **वर्क ऑर्डर राशि (₹)** - Enter work order amount
- **अब तक की बिल राशि (₹)** - Enter upto date bill amount
- **Extra Items शामिल** - Yes/No
- **Extra Items राशि (₹)** - Enter extra amount (if applicable)
- **Click "नोट शीट जनरेट करें"** - Generate Hindi note!

### 2. **फाइनल बिल (Final Bill)** - Additional Fields
- **वर्क ऑर्डर राशि (₹)** - Enter work order amount
- **अब तक की बिल राशि (₹)** - Enter upto date bill amount
- **Extra Items शामिल** - Yes/No
- **Extra Items राशि (₹)** - Enter extra amount (if applicable)
- **प्रारंभ तिथि (DD/MM/YYYY)** - Enter start date
- **निर्धारित समापन तिथि (DD/MM/YYYY)** - Enter scheduled completion date
- **वास्तविक समापन तिथि (DD/MM/YYYY)** - Enter actual completion date
- **मरम्मत कार्य** - Yes/No
- **अधिक मात्रा (Excess Quantity)** - Yes/No
- **बिल देर से जमा (>6 माह)** - Yes/No
- **Click "नोट शीट जनरेट करें"** - Generate Hindi note!

---

## ✨ **Features**

- ✅ **Proper Hindi Format** - Exactly as per original repository
- ✅ **Running & Final Bills** - Handles both bill types
- ✅ **Automatic Calculations** - Percentage work done, delays, etc.
- ✅ **Smart Logic** - Different notes based on completion percentage
- ✅ **Extra Items Handling** - 5% rule implementation
- ✅ **Delay Calculations** - Automatic delay day calculations
- ✅ **Local Database** - All notes saved locally
- ✅ **No Internet Required** - Works completely offline
- ✅ **Simple Interface** - Easy for lower divisional clerks

---

## 📁 **Files**

- `hindi_bill_note.py` - Main Hindi bill note application
- `run_hindi_bill.py` - Simple launcher
- `run_hindi_bill.bat` - Windows batch file
- `hindi_bills.db` - Simple database (created automatically)

---

## 🎯 **Usage Examples**

### **Running Bill Example:**
1. Select "रनिंग बिल" (Running Bill)
2. Enter: "100000" (वर्क ऑर्डर राशि)
3. Enter: "75000" (अब तक की बिल राशि)
4. Select "हाँ" (Extra Items शामिल)
5. Enter: "5000" (Extra Items राशि)
6. Click "नोट शीट जनरेट करें" - See Hindi note!

### **Final Bill Example:**
1. Select "फाइनल बिल" (Final Bill)
2. Enter: "100000" (वर्क ऑर्डर राशि)
3. Enter: "105000" (अब तक की बिल राशि)
4. Enter: "01/01/2024" (प्रारंभ तिथि)
5. Enter: "31/03/2024" (निर्धारित समापन तिथि)
6. Enter: "15/04/2024" (वास्तविक समापन तिथि)
7. Select "नहीं" (मरम्मत कार्य)
8. Select "हाँ" (अधिक मात्रा)
9. Click "नोट शीट जनरेट करें" - See Hindi note!

---

## 🔧 **System Requirements**

- **Windows 10+** (or any OS with Python)
- **Python 3.9+** (if running manually)
- **CustomTkinter** (installed automatically)

---

## 🆘 **Troubleshooting**

**If the application doesn't start:**
1. Make sure Python is installed
2. Run: `pip install customtkinter`
3. Try running: `python run_hindi_bill.py`

**If you get errors:**
- Check that all required fields are filled
- Make sure dates are in DD/MM/YYYY format
- Make sure amounts are numbers only
- For final bills, fill all date fields

---

## 📞 **Support**

This simple version is designed to be **error-free** and **easy to use**. If you encounter any issues, check that:

1. All required fields are filled
2. Dates are in correct format (DD/MM/YYYY)
3. Amounts are valid numbers
4. Python and CustomTkinter are installed

---

**🎉 Simple, Fast, and Easy to Use in Hindi!**

*Perfect for lower divisional clerks - no complexity, just proper Hindi bill notes as per original repository!*
