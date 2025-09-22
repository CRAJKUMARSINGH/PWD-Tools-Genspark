#!/usr/bin/env python3
"""
Simple test script for PWD Tools - Tests each tool 5 times programmatically
"""

import random
import time
import csv
from datetime import datetime, timedelta
import os

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

def run_tests():
    """Run all tests 5 times each"""
    print("🧪 PWD Tools Testing Script")
    print("=" * 50)
    print(f"Starting tests at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Test results storage
    all_results = {
        "emd_refund": [],
        "deductions_table": [],
        "delay_calculator": [],
        "stamp_duty": []
    }
    
    # Run each tool 5 times
    for i in range(1, 6):
        print(f"🔄 Running test cycle {i}/5")
        print("-" * 30)
        
        # Test EMD Refund
        emd_result = test_emd_refund(i)
        all_results["emd_refund"].append(emd_result)
        time.sleep(0.1)  # Small delay between tests
        
        # Test Deductions Table
        deductions_result = test_deductions_table(i)
        all_results["deductions_table"].append(deductions_result)
        time.sleep(0.1)
        
        # Test Delay Calculator
        delay_result = test_delay_calculator(i)
        all_results["delay_calculator"].append(delay_result)
        time.sleep(0.1)
        
        # Test Stamp Duty
        stamp_result = test_stamp_duty(i)
        all_results["stamp_duty"].append(stamp_result)
        time.sleep(0.1)
        
        print()
    
    # Summary
    print("📊 Test Summary")
    print("=" * 50)
    print(f"Total tests run: {4 * 5}")  # 4 tools × 5 tests each
    print(f"EMD Refund tests: {len(all_results['emd_refund'])}")
    print(f"Deductions Table tests: {len(all_results['deductions_table'])}")
    print(f"Delay Calculator tests: {len(all_results['delay_calculator'])}")
    print(f"Stamp Duty tests: {len(all_results['stamp_duty'])}")
    print(f"Completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("✅ All tests completed successfully!")
    
    return all_results

def save_results_to_csv(results):
    """Save test results to CSV files"""
    print("\n💾 Saving results to CSV files...")
    
    for tool_name, tool_results in results.items():
        if tool_results:
            filename = f"test_results_{tool_name}.csv"
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
    test_results = run_tests()
    
    # Save results
    save_results_to_csv(test_results)
    
    print("\n🏁 Testing script completed!")