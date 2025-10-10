"""
Financial Progress Tool - SIMPLE VERSION
Display only in HTML format like the original repository
"""

import webbrowser
import tempfile
import os


def open_financial_progress_html():
    """Open Financial Progress Tracker in HTML format"""
    
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Financial Progress Tracker</title>
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
        
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: var(--dark-text);
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 900px;
            margin: 0 auto;
            background: linear-gradient(145deg, #ffffff 0%, #f8fafc 100%);
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
        }
        
        .header {
            text-align: center;
            margin-bottom: 30px;
            padding: 30px 20px;
            background: var(--gradient-primary);
            border-radius: 15px;
            color: white;
            box-shadow: var(--shadow);
        }
        
        h1 {
            color: white;
            margin-bottom: 15px;
            font-size: 2.5rem;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
            font-weight: 700;
        }
        
        h2 {
            color: rgba(255, 255, 255, 0.9);
            font-size: 1.3rem;
            margin-bottom: 0;
            font-weight: 400;
        }
        
        .form-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }
        
        .input-group {
            margin-bottom: 15px;
        }
        
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: var(--primary-color);
        }
        
        input, select {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: var(--border-radius);
            font-size: 16px;
            transition: border 0.3s;
        }
        
        input:focus, select:focus {
            outline: none;
            border-color: var(--secondary-color);
            box-shadow: 0 0 0 2px rgba(52, 152, 219, 0.2);
        }
        
        .button-group {
            display: flex;
            gap: 15px;
            margin-top: 25px;
        }
        
        button {
            padding: 15px 30px;
            background: var(--gradient-secondary);
            color: var(--light-text);
            border: none;
            border-radius: 12px;
            cursor: pointer;
            font-size: 16px;
            font-weight: 600;
            transition: all 0.3s ease;
            flex: 1;
            box-shadow: var(--shadow);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        button:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 20px -5px rgba(0, 0, 0, 0.2);
            background: linear-gradient(135deg, #f5576c 0%, #f093fb 100%);
        }
        
        button:active {
            transform: translateY(0);
        }
        
        #resetBtn {
            background: linear-gradient(135deg, #a8a8a8 0%, #8a8a8a 100%);
        }
        
        #resetBtn:hover {
            background: linear-gradient(135deg, #8a8a8a 0%, #6a6a6a 100%);
        }
        
        #printBtn {
            background: linear-gradient(135deg, #38a169 0%, #2f855a 100%);
        }
        
        #printBtn:hover {
            background: linear-gradient(135deg, #2f855a 0%, #276749 100%);
        }
        
        .error {
            color: var(--error-color);
            background-color: rgba(231, 76, 60, 0.1);
            padding: 10px;
            border-radius: var(--border-radius);
            margin-bottom: 15px;
            font-weight: 500;
            display: none;
        }
        
        .success {
            color: var(--success-color);
            background-color: rgba(39, 174, 96, 0.1);
            padding: 10px;
            border-radius: var(--border-radius);
            margin-top: 20px;
            font-style: italic;
            text-align: center;
        }
        
        .result {
            background-color: #f5f5f5;
            padding: 20px;
            border-radius: var(--border-radius);
            margin-top: 25px;
            margin-bottom: 20px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
            animation: fadeIn 0.5s;
            border-left: 5px solid var(--secondary-color);
        }
        
        .result h3 {
            margin-bottom: 12px;
            color: var(--primary-color);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .result span {
            font-weight: 700;
            color: var(--secondary-color);
        }
        
        .progress-bar-container {
            width: 100%;
            height: 25px;
            background-color: #ecf0f1;
            border-radius: var(--border-radius);
            margin: 15px 0;
            overflow: hidden;
        }
        
        .progress-bar {
            height: 100%;
            background: var(--gradient-primary);
            border-radius: var(--border-radius);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
            transition: width 0.8s ease-in-out;
            box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        
        .footer {
            margin-top: 30px;
            text-align: center;
            font-size: 0.9rem;
            border-top: 1px solid #ddd;
            padding-top: 20px;
            color: #777;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        @media (max-width: 768px) {
            .form-container {
                grid-template-columns: 1fr;
            }
            
            .button-group {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Financial Progress Tracker</h1>
            <h2>Liquidity Damages Calculator</h2>
        </div>
        
        <div class="error" id="errorMessages"></div>
        
        <div class="form-container">
            <div>
                <div class="input-group">
                    <label for="workOrderAmount">Work Order Amount (₹):</label>
                    <input type="number" id="workOrderAmount" min="1" value="1000000" placeholder="Enter amount in INR">
                </div>
                
                <div class="input-group">
                    <label for="startDate">Project Start Date:</label>
                    <input type="date" id="startDate" value="2024-12-15">
                </div>
                
                <div class="input-group">
                    <label for="endDate">Project Completion Date:</label>
                    <input type="date" id="endDate" value="2025-04-15">
                </div>
            </div>
            
            <div>
                <div class="input-group">
                    <label for="reviewDate">Review Date:</label>
                    <input type="date" id="reviewDate" value="2025-02-06">
                </div>
                
                <div class="input-group">
                    <label for="actualProgress">Actual Progress (₹):</label>
                    <input type="number" id="actualProgress" value="500000" placeholder="Enter amount in INR">
                </div>
                
                <div class="input-group">
                    <label for="penaltyScheme">Penalty Scheme:</label>
                    <select id="penaltyScheme">
                        <option value="standard">Standard PWF&AR Scheme</option>
                        <option value="custom">Custom Scheme</option>
                    </select>
                </div>
            </div>
        </div>
        
        <div class="button-group">
            <button id="calculateBtn" onclick="calculate()">Calculate</button>
            <button id="resetBtn" onclick="resetForm()">Reset</button>
            <button id="printBtn" onclick="printResults()">Print Report</button>
        </div>
        
        <div class="result" id="results" style="display: none;">
            <h3>Project Timeline:</h3>
            <div id="timelineInfo"></div>
            
            <div class="progress-bar-container">
                <div class="progress-bar" id="timeProgressBar">0%</div>
            </div>
            
            <h3>Required Financial Progress: <span id="requiredProgress"></span></h3>
            <h3>Actual Financial Progress: <span id="actualProgressResult"></span></h3>
            
            <div class="progress-bar-container">
                <div class="progress-bar" id="financialProgressBar">0%</div>
            </div>
            
            <h3>Unexecuted Work: <span id="unexecutedWork"></span></h3>
            <h3>Liquidity Damages (Penalty): <span id="penalty"></span></h3>
        </div>
        
        <div id="successMessages" class="success" style="display: none;"></div>
        
        <div class="footer">
            <p>An Initiative by Mrs. Premlata Jain, AAO, PWD, Udaipur, Rajasthan</p>
            <p>Based on prevailing PWF&AR</p>
        </div>
    </div>

    <script>
        // Format currency in Indian Rupees format
        function formatCurrency(amount) {
            return new Intl.NumberFormat('en-IN', {
                style: 'currency',
                currency: 'INR',
                maximumFractionDigits: 0
            }).format(amount);
        }
        
        // Format date to DD/MM/YYYY
        function formatDate(dateString) {
            const date = new Date(dateString);
            const day = String(date.getDate()).padStart(2, '0');
            const month = String(date.getMonth() + 1).padStart(2, '0');
            const year = date.getFullYear();
            return `${day}/${month}/${year}`;
        }
        
        // Validate inputs
        function validateInputs(workOrderAmount, startDate, endDate, reviewDate, actualProgressInr) {
            const errors = [];
            
            if (isNaN(workOrderAmount) || workOrderAmount <= 0) {
                errors.push("Work Order Amount must be a positive number.");
            }
            
            if (isNaN(actualProgressInr) || actualProgressInr < 0) {
                errors.push("Actual Progress must be a non-negative number.");
            }
            
            if (actualProgressInr > workOrderAmount) {
                errors.push("Actual Progress cannot exceed Work Order Amount.");
            }
            
            if (startDate >= endDate) {
                errors.push("Start date must be before the completion date.");
            }
            
            if (reviewDate < startDate) {
                errors.push("Review date cannot be before the project start date.");
            }
            
            return errors;
        }
        
        function calculate() {
            const workOrderAmount = parseFloat(document.getElementById("workOrderAmount").value);
            const startDateValue = document.getElementById("startDate").value;
            const endDateValue = document.getElementById("endDate").value;
            const reviewDateValue = document.getElementById("reviewDate").value;
            const actualProgressInr = parseFloat(document.getElementById("actualProgress").value);
            const penaltyScheme = document.getElementById("penaltyScheme").value;

            const errorMessages = document.getElementById("errorMessages");
            const resultsDiv = document.getElementById("results");
            const successDiv = document.getElementById("successMessages");

            // Reset display
            errorMessages.innerHTML = "";
            errorMessages.style.display = "none";
            resultsDiv.style.display = "none";
            successDiv.style.display = "none";

            // Parse dates
            const startDate = new Date(startDateValue);
            const endDate = new Date(endDateValue);
            const reviewDate = new Date(reviewDateValue);
            
            // Validate inputs
            const validationErrors = validateInputs(workOrderAmount, startDate, endDate, reviewDate, actualProgressInr);
            
            if (validationErrors.length > 0) {
                errorMessages.innerHTML = validationErrors.join("<br>");
                errorMessages.style.display = "block";
                return;
            }

            // Calculate timeline information
            const totalProjectDuration = (endDate - startDate) / (1000 * 60 * 60 * 24);
            const elapsedDays = (reviewDate - startDate) / (1000 * 60 * 60 * 24);
            const remainingDays = totalProjectDuration - elapsedDays;
            const percentComplete = Math.min(100, Math.max(0, (elapsedDays / totalProjectDuration) * 100));
            
            // Display timeline information
            document.getElementById("timelineInfo").innerHTML = `
                <p>Total project duration: ${Math.ceil(totalProjectDuration)} days</p>
                <p>Time elapsed: ${Math.ceil(elapsedDays)} days (${percentComplete.toFixed(1)}%)</p>
                <p>Time remaining: ${Math.ceil(remainingDays)} days</p>
            `;
            
            // Update time progress bar
            const timeProgressBar = document.getElementById("timeProgressBar");
            timeProgressBar.style.width = `${percentComplete}%`;
            timeProgressBar.textContent = `${percentComplete.toFixed(1)}%`;
            
            // Calculate required progress based on selected scheme
            let requiredProgress;
            let penaltyRate;
            
            if (penaltyScheme === "standard") {
                // Standard PWF&AR Scheme
                if (elapsedDays <= totalProjectDuration * 0.25) {
                    requiredProgress = workOrderAmount * 0.125;
                    penaltyRate = 0.025;
                } else if (elapsedDays <= totalProjectDuration * 0.50) {
                    requiredProgress = workOrderAmount * 0.375;
                    penaltyRate = 0.05;
                } else if (elapsedDays <= totalProjectDuration * 0.75) {
                    requiredProgress = workOrderAmount * 0.75;
                    penaltyRate = 0.075;
                } else {
                    requiredProgress = workOrderAmount;
                    penaltyRate = 0.10;
                }
            } else {
                // Custom linear progression
                requiredProgress = workOrderAmount * (elapsedDays / totalProjectDuration);
                
                // Custom penalty rates based on lag percentage
                const lagPercentage = (requiredProgress - actualProgressInr) / requiredProgress;
                
                if (lagPercentage <= 0) {
                    penaltyRate = 0;
                } else if (lagPercentage <= 0.25) {
                    penaltyRate = 0.025;
                } else if (lagPercentage <= 0.50) {
                    penaltyRate = 0.05;
                } else if (lagPercentage <= 0.75) {
                    penaltyRate = 0.075;
                } else {
                    penaltyRate = 0.10;
                }
            }

            // Calculate unexecuted work and penalty
            const unexecutedWork = Math.max(0, requiredProgress - actualProgressInr);
            const penalty = penaltyRate * unexecutedWork;
            
            // Calculate financial progress percentage
            const financialProgress = (actualProgressInr / requiredProgress) * 100;
            
            // Update financial progress bar
            const financialProgressBar = document.getElementById("financialProgressBar");
            const progressPercent = Math.min(100, Math.max(0, financialProgress));
            financialProgressBar.style.width = `${progressPercent}%`;
            financialProgressBar.textContent = `${progressPercent.toFixed(1)}%`;
            
            // Set color based on progress
            if (progressPercent >= 100) {
                financialProgressBar.style.backgroundColor = "#27ae60"; // Green
            } else if (progressPercent >= 75) {
                financialProgressBar.style.backgroundColor = "#2ecc71"; // Light green
            } else if (progressPercent >= 50) {
                financialProgressBar.style.backgroundColor = "#f39c12"; // Orange
            } else {
                financialProgressBar.style.backgroundColor = "#e74c3c"; // Red
            }

            // Update results in the main view
            document.getElementById("requiredProgress").textContent = formatCurrency(Math.ceil(requiredProgress));
            document.getElementById("actualProgressResult").textContent = formatCurrency(Math.ceil(actualProgressInr));
            document.getElementById("unexecutedWork").textContent = formatCurrency(Math.ceil(unexecutedWork));
            document.getElementById("penalty").textContent = formatCurrency(Math.ceil(penalty));

            // Show results
            resultsDiv.style.display = "block";
            successDiv.innerHTML = "An Initiative by Mrs. Premlata Jain, AAO, PWD, Udaipur, Rajasthan<br>Based on prevailing PWF&AR";
            successDiv.style.display = "block";
        }
        
        function resetForm() {
            const today = new Date();
            const defaultStartDate = new Date();
            defaultStartDate.setMonth(today.getMonth() - 1);
            const defaultEndDate = new Date();
            defaultEndDate.setMonth(today.getMonth() + 3);
            
            document.getElementById("workOrderAmount").value = "1000000";
            document.getElementById("startDate").value = defaultStartDate.toISOString().split('T')[0];
            document.getElementById("endDate").value = defaultEndDate.toISOString().split('T')[0];
            document.getElementById("reviewDate").value = today.toISOString().split('T')[0];
            document.getElementById("actualProgress").value = "500000";
            document.getElementById("penaltyScheme").value = "standard";
            
            document.getElementById("errorMessages").innerHTML = "";
            document.getElementById("errorMessages").style.display = "none";
            document.getElementById("results").style.display = "none";
            document.getElementById("successMessages").style.display = "none";
        }

        function printResults() {
            if (document.getElementById("results").style.display === "none") {
                alert("Please calculate results first before printing.");
                return;
            }
            
            window.print();
        }
        
        // Initialize with today's date for review date if not set
        window.onload = function() {
            if (!document.getElementById("reviewDate").value) {
                const today = new Date();
                document.getElementById("reviewDate").value = today.toISOString().split('T')[0];
            }
        };
    </script>
</body>
</html>'''
    
    # Create temporary HTML file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8') as f:
        f.write(html_content)
        temp_file = f.name
    
    # Open in browser
    webbrowser.open(f'file://{temp_file}')
    
    print("Financial Progress Tracker opened in browser")


if __name__ == "__main__":
    open_financial_progress_html()
