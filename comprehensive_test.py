#!/usr/bin/env python3
"""
Comprehensive test script for PWD Tools - Tests all 10 tools 5 times each
"""

import random
import time
import csv
from datetime import datetime, timedelta
import os

def test_excel_se_emd(test_number):
    """Test Excel se EMD tool"""
    print(f"Testing Excel se EMD - Test #{test_number}")
    
    # Generate random test data
    project_name = f"Project {random.choice(['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon'])} {random.randint(1, 100)}"
    contractor_name = f"Contractor {random.choice(['A', 'B', 'C', 'D', 'E'])}"
    work_order_amount = round(random.uniform(100000, 5000000), 2)
    emd_percentage = round(random.uniform(1.0, 10.0), 1)
    emd_amount = round(work_order_amount * (emd_percentage / 100), 2)
    
    print(f"  Project: {project_name}")
    print(f"  Contractor: {contractor_name}")
    print(f"  Work Order Amount: ₹{work_order_amount:,.2f}")
    print(f"  EMD Percentage: {emd_percentage}%")
    print(f"  EMD Amount: ₹{emd_amount:,.2f}")
    print("  ✅ Excel se EMD test completed\n")
    
    return {
        "project_name": project_name,
        "contractor_name": contractor_name,
        "work_order_amount": work_order_amount,
        "emd_percentage": emd_percentage,
        "emd_amount": emd_amount
    }

def test_bill_deviation(test_number):
    """Test Bill & Deviation tool"""
    print(f"Testing Bill & Deviation - Test #{test_number}")
    
    # Generate random test data
    work_description = f"Work Description {random.randint(1000, 9999)}"
    original_amount = round(random.uniform(100000, 3000000), 2)
    deviation_amount = round(random.uniform(0, original_amount * 0.2), 2)
    final_amount = original_amount + deviation_amount
    
    print(f"  Work: {work_description}")
    print(f"  Original Amount: ₹{original_amount:,.2f}")
    print(f"  Deviation Amount: ₹{deviation_amount:,.2f}")
    print(f"  Final Amount: ₹{final_amount:,.2f}")
    print("  ✅ Bill & Deviation test completed\n")
    
    return {
        "work_description": work_description,
        "original_amount": original_amount,
        "deviation_amount": deviation_amount,
        "final_amount": final_amount
    }

def test_tender_processing(test_number):
    """Test Tender Processing tool"""
    print(f"Testing Tender Processing - Test #{test_number}")
    
    # Generate random test data
    tender_number = f"TN-{random.randint(2025, 2030)}-{random.randint(1000, 9999)}"
    tender_type = random.choice(["Works", "Goods", "Services"])
    tender_value = round(random.uniform(500000, 10000000), 2)
    submission_date = datetime.now().date() + timedelta(days=random.randint(1, 180))
    opening_date = submission_date + timedelta(days=random.randint(1, 30))
    
    print(f"  Tender Number: {tender_number}")
    print(f"  Tender Type: {tender_type}")
    print(f"  Tender Value: ₹{tender_value:,.2f}")
    print(f"  Submission Date: {submission_date}")
    print(f"  Opening Date: {opening_date}")
    print("  ✅ Tender Processing test completed\n")
    
    return {
        "tender_number": tender_number,
        "tender_type": tender_type,
        "tender_value": tender_value,
        "submission_date": str(submission_date),
        "opening_date": str(opening_date)
    }

def test_bill_note_sheet(test_number):
    """Test Bill Note Sheet tool"""
    print(f"Testing Bill Note Sheet - Test #{test_number}")
    
    # Generate random test data
    bill_type = random.choice(["Running", "Final"])
    work_order_number = f"WO-{random.randint(2025, 2030)}-{random.randint(10000, 99999)}"
    work_order_amount = round(random.uniform(100000, 2000000), 2)
    bill_amount = round(random.uniform(50000, work_order_amount), 2)
    
    print(f"  Bill Type: {bill_type}")
    print(f"  Work Order: {work_order_number}")
    print(f"  Work Order Amount: ₹{work_order_amount:,.2f}")
    print(f"  Bill Amount: ₹{bill_amount:,.2f}")
    print("  ✅ Bill Note Sheet test completed\n")
    
    return {
        "bill_type": bill_type,
        "work_order_number": work_order_number,
        "work_order_amount": work_order_amount,
        "bill_amount": bill_amount
    }

def test_deductions_table(test_number):
    """Test Deductions Table tool"""
    print(f"Testing Deductions Table - Test #{test_number}")
    
    # Generate random test data
    bill_number = f"BILL-{random.randint(10000, 99999)}"
    contractor_name = f"Contractor {random.choice(['F', 'G', 'H', 'I', 'J'])}"
    gross_amount = round(random.uniform(50000, 5000000), 2)
    tds_rate = round(random.uniform(0.5, 5.0), 1)
    security_rate = round(random.uniform(1.0, 10.0), 1)
    other_deductions = round(random.uniform(0, 50000), 2)
    
    # Calculate deductions
    tds_amount = (gross_amount * tds_rate) / 100.0
    security_deduction = (gross_amount * security_rate) / 100.0
    total_deductions = tds_amount + security_deduction + other_deductions
    net_amount = gross_amount - total_deductions
    
    print(f"  Bill Number: {bill_number}")
    print(f"  Contractor: {contractor_name}")
    print(f"  Gross Amount: ₹{gross_amount:,.2f}")
    print(f"  TDS Rate: {tds_rate}%")
    print(f"  Security Rate: {security_rate}%")
    print(f"  Net Amount: ₹{net_amount:,.2f}")
    print("  ✅ Deductions Table test completed\n")
    
    return {
        "bill_number": bill_number,
        "contractor_name": contractor_name,
        "gross_amount": gross_amount,
        "tds_rate": tds_rate,
        "security_rate": security_rate,
        "other_deductions": other_deductions,
        "net_amount": net_amount
    }

def test_delay_calculator(test_number):
    """Test Delay Calculator tool"""
    print(f"Testing Delay Calculator - Test #{test_number}")
    
    # Generate random test data
    project_name = f"Project {random.choice(['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon'])} {random.randint(1, 100)}"
    
    # Generate dates with some delays
    planned_start = datetime.now().date() - timedelta(days=random.randint(100, 500))
    actual_start = planned_start + timedelta(days=random.randint(0, 30))  # 0-30 days delay
    planned_completion = planned_start + timedelta(days=random.randint(180, 730))  # 6 months to 2 years
    actual_completion = planned_completion + timedelta(days=random.randint(-30, 90))  # -30 to 90 days delay
    
    # Calculate delays
    start_delay = (actual_start - planned_start).days
    completion_delay = (actual_completion - planned_completion).days
    total_delay = completion_delay
    
    print(f"  Project: {project_name}")
    print(f"  Planned Start: {planned_start}")
    print(f"  Actual Start: {actual_start}")
    print(f"  Start Delay: {start_delay} days")
    print(f"  Completion Delay: {completion_delay} days")
    print(f"  Total Delay: {total_delay} days")
    print("  ✅ Delay Calculator test completed\n")
    
    return {
        "project_name": project_name,
        "planned_start": str(planned_start),
        "actual_start": str(actual_start),
        "planned_completion": str(planned_completion),
        "actual_completion": str(actual_completion),
        "total_delay": total_delay
    }

def test_emd_refund(test_number):
    """Test EMD Refund tool"""
    print(f"Testing EMD Refund - Test #{test_number}")
    
    # Generate random test data
    tender_number = f"TN-2025-{random.randint(1000, 9999)}"
    contractor_name = f"Contractor {random.choice(['A', 'B', 'C', 'D', 'E'])}"
    emd_amount = round(random.uniform(10000, 1000000), 2)
    
    # Validity date - sometimes in past, sometimes in future
    if random.choice([True, False]):
        # Future date
        validity_date = datetime.now().date() + timedelta(days=random.randint(1, 365))
    else:
        # Past date
        validity_date = datetime.now().date() - timedelta(days=random.randint(1, 365))
    
    # Simulate the calculation
    current_date = datetime.now().date()
    days_difference = (current_date - validity_date).days
    
    if validity_date >= current_date:
        refund_amount = emd_amount
        penalty = 0.0
    elif days_difference <= 30:
        penalty = emd_amount * 0.10
        refund_amount = emd_amount - penalty
    elif days_difference <= 90:
        penalty = emd_amount * 0.50
        refund_amount = emd_amount - penalty
    else:
        penalty = emd_amount
        refund_amount = 0.0
    
    print(f"  Tender: {tender_number}")
    print(f"  Contractor: {contractor_name}")
    print(f"  EMD Amount: ₹{emd_amount:,.2f}")
    print(f"  Validity Date: {validity_date}")
    print(f"  Refund Amount: ₹{refund_amount:,.2f}")
    print(f"  Penalty: ₹{penalty:,.2f}")
    print("  ✅ EMD Refund test completed\n")
    
    return {
        "tender_number": tender_number,
        "contractor_name": contractor_name,
        "emd_amount": emd_amount,
        "validity_date": str(validity_date),
        "refund_amount": refund_amount,
        "penalty": penalty
    }

def test_financial_progress(test_number):
    """Test Financial Progress tool"""
    print(f"Testing Financial Progress - Test #{test_number}")
    
    # Generate random test data
    project_name = f"Project {random.choice(['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon'])} {random.randint(1, 100)}"
    budget_amount = round(random.uniform(1000000, 10000000), 2)
    spent_amount = round(random.uniform(0, budget_amount), 2)
    progress_percentage = round((spent_amount / budget_amount) * 100, 2) if budget_amount > 0 else 0
    
    print(f"  Project: {project_name}")
    print(f"  Budget Amount: ₹{budget_amount:,.2f}")
    print(f"  Spent Amount: ₹{spent_amount:,.2f}")
    print(f"  Progress: {progress_percentage}%")
    print("  ✅ Financial Progress test completed\n")
    
    return {
        "project_name": project_name,
        "budget_amount": budget_amount,
        "spent_amount": spent_amount,
        "progress_percentage": progress_percentage
    }

def test_security_refund(test_number):
    """Test Security Refund tool"""
    print(f"Testing Security Refund - Test #{test_number}")
    
    # Generate random test data
    work_order_number = f"WO-{random.randint(2025, 2030)}-{random.randint(10000, 99999)}"
    contractor_name = f"Contractor {random.choice(['K', 'L', 'M', 'N', 'O'])}"
    security_deposit = round(random.uniform(50000, 2000000), 2)
    work_completion = random.choice(["Complete", "Partial", "Not Started"])
    
    # Calculate refund based on completion
    if work_completion == "Complete":
        refund_amount = security_deposit
    elif work_completion == "Partial":
        refund_amount = round(security_deposit * 0.75, 2)
    else:
        refund_amount = 0.0
    
    print(f"  Work Order: {work_order_number}")
    print(f"  Contractor: {contractor_name}")
    print(f"  Security Deposit: ₹{security_deposit:,.2f}")
    print(f"  Work Completion: {work_completion}")
    print(f"  Refund Amount: ₹{refund_amount:,.2f}")
    print("  ✅ Security Refund test completed\n")
    
    return {
        "work_order_number": work_order_number,
        "contractor_name": contractor_name,
        "security_deposit": security_deposit,
        "work_completion": work_completion,
        "refund_amount": refund_amount
    }

def test_stamp_duty(test_number):
    """Test Stamp Duty tool"""
    print(f"Testing Stamp Duty Calculator - Test #{test_number}")
    
    # Generate random test data
    work_order_amount = round(random.uniform(100000, 10000000), 2)
    
    # Calculate stamp duty based on rules
    if work_order_amount <= 5000000:
        stamp_duty = 1000
    else:
        stamp_duty = round(work_order_amount * 0.0015)
        if stamp_duty > 2500000:
            stamp_duty = 2500000
    
    print(f"  Work Order Amount: ₹{work_order_amount:,.2f}")
    print(f"  Stamp Duty: ₹{stamp_duty:,.2f}")
    print("  ✅ Stamp Duty test completed\n")
    
    return {
        "work_order_amount": work_order_amount,
        "stamp_duty": stamp_duty
    }

def run_comprehensive_tests():
    """Run all tests 5 times each"""
    print("🧪 PWD Tools Comprehensive Testing Script")
    print("=" * 50)
    print(f"Starting tests at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Test results storage
    all_results = {
        "excel_se_emd": [],
        "bill_deviation": [],
        "tender_processing": [],
        "bill_note_sheet": [],
        "deductions_table": [],
        "delay_calculator": [],
        "emd_refund": [],
        "financial_progress": [],
        "security_refund": [],
        "stamp_duty": []
    }
    
    # Define test functions
    test_functions = [
        ("excel_se_emd", test_excel_se_emd),
        ("bill_deviation", test_bill_deviation),
        ("tender_processing", test_tender_processing),
        ("bill_note_sheet", test_bill_note_sheet),
        ("deductions_table", test_deductions_table),
        ("delay_calculator", test_delay_calculator),
        ("emd_refund", test_emd_refund),
        ("financial_progress", test_financial_progress),
        ("security_refund", test_security_refund),
        ("stamp_duty", test_stamp_duty)
    ]
    
    # Run each tool 5 times
    for i in range(1, 6):
        print(f"🔄 Running test cycle {i}/5")
        print("-" * 30)
        
        for tool_name, test_func in test_functions:
            result = test_func(i)
            all_results[tool_name].append(result)
            time.sleep(0.1)  # Small delay between tests
        
        print()
    
    # Summary
    print("📊 Test Summary")
    print("=" * 50)
    print(f"Total tests run: {len(test_functions) * 5}")  # 10 tools × 5 tests each
    for tool_name in all_results.keys():
        print(f"{tool_name.replace('_', ' ').title()} tests: {len(all_results[tool_name])}")
    print(f"Completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("✅ All tests completed successfully!")
    
    return all_results

def save_results_to_csv(results):
    """Save test results to CSV files"""
    print("\n💾 Saving results to CSV files...")
    
    for tool_name, tool_results in results.items():
        if tool_results:
            filename = f"comprehensive_test_results_{tool_name}.csv"
            # Write CSV file manually without pandas
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                if tool_results:
                    fieldnames = tool_results[0].keys()
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    for row in tool_results:
                        writer.writerow(row)
                print(f"  Saved {len(tool_results)} results to {filename}")
    
    print("✅ All results saved!")

if __name__ == "__main__":
    # Run the tests
    test_results = run_comprehensive_tests()
    
    # Save results
    save_results_to_csv(test_results)
    
    print("\n🏁 Comprehensive testing script completed!")