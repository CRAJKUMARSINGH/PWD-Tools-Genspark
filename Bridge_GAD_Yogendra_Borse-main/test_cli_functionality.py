#!/usr/bin/env python3
"""
Test script to verify CLI functionality.
"""

import sys
import os

# Add the src directory to the path so we can import bridge_gad modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from bridge_gad.geometry import compute_bending_moment, compute_shear_force, compute_deflection

def test_functions():
    """Test the core functions."""
    print("Testing Bridge GAD functions...")
    
    # Test parameters
    span = 20.0
    load = 15.0
    E = 2.1e8
    I = 0.0025
    
    # Compute results
    bending_moment = compute_bending_moment(span, load)
    shear_force = compute_shear_force(load, span)
    deflection = compute_deflection(span, load, E, I)
    
    print(f"Span: {span} m")
    print(f"Load: {load} kN/m")
    print(f"E: {E} kN/m²")
    print(f"I: {I} m⁴")
    print(f"Bending Moment: {bending_moment} kN*m")
    print(f"Shear Force: {shear_force} kN")
    print(f"Deflection: {deflection} m")
    
    # Verify results
    expected_moment = (load * span ** 2) / 8.0
    expected_shear = load * span / 2.0
    expected_deflection = (5 * load * span ** 4) / (384 * E * I)
    
    assert abs(bending_moment - expected_moment) < 1e-10
    assert abs(shear_force - expected_shear) < 1e-10
    assert abs(deflection - expected_deflection) < 1e-10
    
    print("All tests passed!")

if __name__ == "__main__":
    test_functions()