"""
Security Refund Tool - SIMPLE VERSION
Display only in HTML format like the original repository
"""

import webbrowser
import tempfile
import os


def open_security_refund_html():
    """Open Security Refund in HTML format"""
    
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Security Deposit Refund</title>
    <style>
        :root {
            --primary-color: #1a365d;
            --secondary-color: #3182ce;
            --success-color: #38a169;
            --error-color: #e53e3e;
            --warning-color: #ed8936;
            --info-color: #4299e1;
            --light-bg: #f7fafc;
            --dark-text: #2d3748;
            --light-text: #ffffff;
            --border-radius: 8px;
            --gradient-primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            --gradient-secondary: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        }
        
        body {
            font-family: Arial, sans-serif;
            line-height: 1.5;
            color: var(--dark-text);
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        .form-container {
            background: linear-gradient(145deg, #ffffff 0%, #f8fafc 100%);
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            margin-bottom: 20px;
            max-width: 800px;
            margin: 20px auto;
        }
        .form-container h2 {
            color: white;
            font-size: 2.2rem;
            margin-bottom: 35px;
            text-align: center;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            padding: 30px 20px;
            background: var(--gradient-primary);
            border-radius: 15px;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
            box-shadow: var(--shadow);
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #333;
        }
        input[type="text"], input[type="number"], input[type="date"] {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
            font-size: 14px;
            transition: border-color 0.3s ease;
        }
        input[type="text"]:focus, input[type="number"]:focus, input[type="date"]:focus {
            outline: none;
            border-color: #2196F3;
            box-shadow: 0 0 0 2px rgba(33, 150, 243, 0.1);
        }
        .bill-controls {
            display: flex;
            gap: 15px;
            margin-bottom: 20px;
        }
        .bill-controls button {
            flex: 1;
            max-width: 200px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            font-size: 15px;
        }
        button {
            background: var(--gradient-secondary);
            color: var(--light-text);
            border: none;
            padding: 15px 30px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            font-weight: 600;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 12px;
            transition: all 0.3s ease;
            box-shadow: var(--shadow);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        button:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 20px -5px rgba(0, 0, 0, 0.2);
            background: linear-gradient(135deg, #f5576c 0%, #f093fb 100%);
        }
        .result {
            display: none;
            margin-top: 20px;
            padding: 20px;
            background-color: white;
            border: 1px solid #ddd;
            line-height: 1.215;
        }
        .document-title {
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 20px;
            text-decoration: underline;
        }
        .item-table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 15px;
        }
        .item-table td {
            padding: 5px;
            vertical-align: top;
        }
        .deposit-table {
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
        }
        .deposit-table th, .deposit-table td {
            border: 1px solid #000;
            padding: 5.4px;
            text-align: left;
        }
        .deposit-table th {
            background-color: #f2f2f2;
        }
        .signature-block {
            display: flex;
            justify-content: space-between;
            margin-top: 60px;
        }
        .signature {
            text-align: center;
            width: 30%;
        }
        .remove-bill {
            background-color: #c62828;
            padding: 10px 20px;
            font-size: 14px;
        }
        .remove-bill:hover {
            background-color: #b71c1c;
        }
        .action-buttons {
            display: flex;
            gap: 15px;
            margin-top: 30px;
            justify-content: center;
        }
        .action-buttons button {
            min-width: 180px;
        }
        .report-item {
            margin-bottom: 2.43px;
            text-indent: -1.5em;
            padding-left: 1.5em;
        }
        @media print {
            body {
                background-color: white;
                padding: 0;
                margin: 0;
                font-size: 11pt;
                line-height: 1.2;
            }
            .form-container, button, .action-buttons, .bill-controls {
                display: none !important;
            }
            .result {
                display: block !important;
                margin: 0;
                padding: 20px;
                border: none;
                line-height: 0.972;
                box-sizing: border-box;
                width: 100%;
            }
            @page {
                size: A4 portrait;
                margin: 0;
                @top-center { content: none !important; }
                @top-left { content: none !important; }
                @top-right { content: none !important; }
                @bottom-center { content: none !important; }
                @bottom-left { content: none !important; }
                @bottom-right { content: none !important; }
            }
            .result * {
                page-break-inside: avoid;
            }
            .deposit-table {
                page-break-inside: auto;
            }
            .deposit-table tr {
                page-break-inside: avoid;
                page-break-after: auto;
            }
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>Security Deposit Refund Form</h2>
        <div class="form-group">
            <label for="contractorName">1. Name of Contractor</label>
            <input type="text" id="contractorName">
        </div>
        <div class="form-group">
            <label for="workName">2. Name of Work</label>
            <input type="text" id="workName">
        </div>
        <div class="form-group">
            <label for="agreementNo">3. Agreement No.</label>
            <input type="text" id="agreementNo">
        </div>
        <div class="form-group">
            <label for="commencementDate">4. Date of Commencement</label>
            <input type="date" id="commencementDate">
        </div>
        <div class="form-group">
            <label for="stipulatedDate">5. Stipulated date of Completion</label>
            <input type="date" id="stipulatedDate">
        </div>
        <div class="form-group">
            <label for="actualDate">6. Actual Date of Completion</label>
            <input type="date" id="actualDate">
        </div>
        <div class="form-group">
            <label for="mbNo">7. MB No.</label>
            <input type="text" id="mbNo">
        </div>
        <div class="form-group">
            <label for="inspectionDate">8. Date of Inspection (for certification)</label>
            <input type="date" id="inspectionDate">
        </div>
        <div class="form-group">
            <label for="finalBillDate">9. Date of Payment of final bill</label>
            <input type="date" id="finalBillDate">
        </div>
        <div class="form-group">
            <label for="dlpExpiryDate">10. Date of Expiry of 3/6 months/DLP</label>
            <input type="date" id="dlpExpiryDate">
        </div>
        <div class="form-group">
            <label>11. Was work satisfactory</label>
            <input type="text" value="Yes" readonly>
        </div>
        <div class="form-group">
            <label>12. Any tools outstanding against contractor</label>
            <input type="text" value="Nil" readonly>
        </div>
        <div class="form-group">
            <label>13. Any recovery due from contractor after payment of final bill</label>
            <input type="text" value="Nil" readonly>
        </div>
        <h3>14. Details of Security Deposit</h3>
        <div class="bill-controls">
            <button type="button" onclick="addBill()" id="addBillBtn">Add Bill (+)</button>
            <button type="button" onclick="removeBill()" class="remove-bill" id="removeBillBtn">Remove Bill (-)</button>
        </div>
        <table class="deposit-table" id="depositTable">
            <thead>
                <tr>
                    <th width="20%">Bill Type</th>
                    <th width="30%">MB No.</th>
                    <th width="20%">SD Type</th>
                    <th width="20%">Amount (₹)</th>
                    <th width="10%"></th>
                </tr>
            </thead>
            <tbody id="depositRows">
                <tr>
                    <td><input type="text" value="I RB" class="bill-type" readonly></td>
                    <td><input type="text" class="bill-mb"></td>
                    <td><input type="text" value="SD II" class="bill-sd" readonly></td>
                    <td><input type="number" class="bill-amount"></td>
                    <td></td>
                </tr>
            </tbody>
        </table>
        <div class="action-buttons">
            <button type="button" onclick="generateReport()">Generate Report</button>
            <button type="button" onclick="printReport()">Print Report</button>
        </div>
    </div>
    <div class="result" id="result">
        <div class="document-title">ORDER FOR REFUND OF SECURITY DEPOSIT [RWMF 119]</div>
        <p class="report-item"><strong>1. Name of Contractor:</strong> <span id="result-contractor"></span></p>
        <p class="report-item"><strong>2. Amount of Deposit:</strong> ₹<span id="result-deposit-amount"></span></p>
        <p class="report-item"><strong>3. Name of Work:</strong> <span id="result-work"></span></p>
        <p class="report-item"><strong>4. Agreement No.:</strong> <span id="result-agreement"></span></p>
        <p class="report-item"><strong>5. Reference for granting refunds:</strong> <span id="result-reference"></span></p>
        <p class="report-item"><strong>6. Date of Commencement:</strong> <span id="result-commencement"></span></p>
        <p class="report-item"><strong>7. Stipulated date of Completion:</strong> <span id="result-stipulated"></span></p>
        <p class="report-item"><strong>8. Actual Date of Completion:</strong> <span id="result-actual"></span></p>
        <p class="report-item"><strong>9. MB No.:</strong> <span id="result-mbno"></span></p>
        <p class="report-item"><strong>10. Date of Payment of final bill:</strong> <span id="result-final-bill-date"></span></p>
        <p class="report-item"><strong>11. Date of Expiry of 3/6 months/DLP:</strong> <span id="result-dlp-expiry-date"></span></p>
        <p class="report-item"><strong>12. Was work satisfactory:</strong> <span>Yes</span></p>
        <p class="report-item"><strong>13. Any tools outstanding against contractor:</strong> <span>Nil</span></p>
        <p class="report-item"><strong>14. Any recovery due from contractor after payment of final bill:</strong> <span>Nil</span></p>
        <p class="report-item"><strong>15. Extension of time limit sanctioned vide</strong></p>
        <p class="report-item"><strong>16. Assistant Engineer Signature's Recommending refund</strong></p>
        <p class="report-item"><strong>17. Accountant's Remarks</strong></p>
        <h4 class="report-item"><strong>18. Details of Security Deposit</strong></h4>
        <table class="deposit-table" id="result-deposit">
            <thead>
                <tr>
                    <th></th>
                    <th>MB No.</th>
                    <th>SD Type</th>
                    <th>Amount (₹)</th>
                </tr>
            </thead>
            <tbody id="result-deposit-rows">
            </tbody>
            <tfoot>
                <tr>
                    <td colspan="3" style="text-align: right;"><strong>Total:</strong></td>
                    <td><strong>₹<span id="result-total"></span></strong></td>
                </tr>
            </tfoot>
        </table>
        <p><strong>Certified That:-</strong></p>
        <p>1. The Work has been completed as per G-schedule.</p>
        <p>2. The work has been inspected by the undersigned as on <span id="result-inspection-date"></span> and it stood satisfactory.</p>
        <p>3. No Defect found during DLP Period.</p>
        <p>4. The final time extension granted upto <span id="extension-date"></span> With/without compensation by the competent authority.</p>
        <p>5. The defects pointed out by higher authorities or other authorized authorities during inspection etc have been removed by the contractor and compliance has been refund.</p>
        <div class="signature-block">
            <div class="signature">
                <p>Divisional Accountant</p>
            </div>
            <div class="signature">
                <p>Assistant Engineer</p>
            </div>
            <div class="signature">
                <p>Executive Engineer</p>
                <p>PWD Electric Div.- Udaipur</p>
            </div>
        </div>
    </div>
    <script>
        let billCount = 1;
        const maxBills = 10;

        function addBill() {
            if (billCount >= maxBills) {
                alert(`Maximum ${maxBills} bills allowed`);
                return;
            }
            billCount++;
            const tbody = document.getElementById('depositRows');
            const newRow = document.createElement('tr');
            let billType = '';
            const romanNumerals = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X'];
            if (billCount <= romanNumerals.length) {
                billType = romanNumerals[billCount-1] + ' RB';
            } else {
                billType = 'Bill ' + billCount;
            }
            newRow.innerHTML = `
                <td><input type="text" value="${billType}" class="bill-type" readonly></td>
                <td><input type="text" class="bill-mb"></td>
                <td><input type="text" value="SD II" class="bill-sd" readonly></td>
                <td><input type="number" class="bill-amount"></td>
                <td><button type="button" onclick="removeThisBill(this)" class="remove-bill">X</button></td>
            `;
            tbody.appendChild(newRow);
            document.getElementById('removeBillBtn').disabled = billCount <= 1;
        }

        function removeBill() {
            if (billCount <= 1) {
                alert("At least one bill is required");
                return;
            }
            const tbody = document.getElementById('depositRows');
            tbody.removeChild(tbody.lastElementChild);
            billCount--;
            document.getElementById('removeBillBtn').disabled = billCount <= 1;
        }

        function removeThisBill(button) {
            if (billCount <= 1) {
                alert("At least one bill is required");
                return;
            }
            const row = button.closest('tr');
            row.parentNode.removeChild(row);
            billCount--;
            const rows = document.querySelectorAll('#depositRows tr');
            const romanNumerals = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X'];
            rows.forEach((row, index) => {
                const typeInput = row.querySelector('.bill-type');
                if (index < romanNumerals.length) {
                    typeInput.value = romanNumerals[index] + ' RB';
                } else {
                    typeInput.value = 'Bill ' + (index + 1);
                }
            });
            document.getElementById('removeBillBtn').disabled = billCount <= 1;
        }

        function generateReport() {
            const contractorName = document.getElementById('contractorName').value;
            const workName = document.getElementById('workName').value;
            const agreementNo = document.getElementById('agreementNo').value;
            const commencementDate = document.getElementById('commencementDate').value;
            const stipulatedDate = document.getElementById('stipulatedDate').value;
            const actualDate = document.getElementById('actualDate').value;
            const mbNo = document.getElementById('mbNo').value;
            const inspectionDate = document.getElementById('inspectionDate').value;
            const finalBillDate = document.getElementById('finalBillDate').value;
            const dlpExpiryDate = document.getElementById('dlpExpiryDate').value;

            const formatDate = (dateString) => {
                if (!dateString) return '';
                const date = new Date(dateString);
                const day = String(date.getDate()).padStart(2, '0');
                const month = String(date.getMonth() + 1).padStart(2, '0');
                const year = date.getFullYear();
                return `${day}/${month}/${year}`;
            };

            const depositRows = document.querySelectorAll('#depositRows tr');
            let total = 0;
            const depositDetails = [];
            depositRows.forEach((row, index) => {
                const typeInput = row.querySelector('.bill-type');
                const mbInput = row.querySelector('.bill-mb');
                const sdInput = row.querySelector('.bill-sd');
                const amountInput = row.querySelector('.bill-amount');
                let billType = typeInput.value;
                if (index === depositRows.length - 1) {
                    if (billType.includes('RB')) {
                        billType = billType.replace('RB', 'RB & Final Bill');
                    } else {
                        billType += ' & Final Bill';
                    }
                }
                const amount = amountInput.value ? parseFloat(amountInput.value) : 0;
                total += amount;
                depositDetails.push({
                    type: billType,
                    mb: mbInput.value || '',
                    sd: sdInput.value || 'SD II',
                    amount: amount ? amount.toLocaleString('en-IN') : ''
                });
            });

            document.getElementById('result-contractor').textContent = contractorName || '';
            document.getElementById('result-work').textContent = workName || '';
            document.getElementById('result-agreement').textContent = agreementNo || '';
            document.getElementById('result-commencement').textContent = formatDate(commencementDate);
            document.getElementById('result-stipulated').textContent = formatDate(stipulatedDate);
            document.getElementById('result-actual').textContent = formatDate(actualDate);
            document.getElementById('result-mbno').textContent = mbNo || '';
            document.getElementById('result-deposit-amount').textContent = total ? total.toLocaleString('en-IN') : '';
            document.getElementById('result-total').textContent = total ? total.toLocaleString('en-IN') : '';
            document.getElementById('result-inspection-date').textContent = formatDate(inspectionDate);
            document.getElementById('result-final-bill-date').textContent = formatDate(finalBillDate);
            document.getElementById('result-dlp-expiry-date').textContent = formatDate(dlpExpiryDate);

            const resultDepositRows = document.getElementById('result-deposit-rows');
            resultDepositRows.innerHTML = '';
            depositDetails.forEach(detail => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${detail.type}</td>
                    <td>${detail.mb}</td>
                    <td>${detail.sd}</td>
                    <td>${detail.amount ? '₹' + detail.amount : ''}</td>
                `;
                resultDepositRows.appendChild(row);
            });

            document.getElementById('result').style.display = 'block';
        }

        function printReport() {
            const resultDiv = document.getElementById('result');
            if (resultDiv.style.display !== 'block') {
                alert('Please generate the report first by clicking "Generate Report".');
                return;
            }
            setTimeout(() => {
                window.print();
            }, 100);
        }
    </script>
</body>
</html>'''
    
    # Create temporary HTML file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8') as f:
        f.write(html_content)
        temp_file = f.name
    
    # Open in browser
    webbrowser.open(f'file://{temp_file}')
    
    print("Security Refund opened in browser")


if __name__ == "__main__":
    open_security_refund_html()
