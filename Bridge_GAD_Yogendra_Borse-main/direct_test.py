#!/usr/bin/env python3
"""Direct test of our functions."""

print("Script is running...")  # Debug print

import sys
import os

# Add the src directory to the path so we can import bridge_gad modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from bridge_gad.geometry import compute_bending_moment, compute_shear_force, compute_deflection
from bridge_gad.config import DEFAULT_E, DEFAULT_I

def main():
    print("Testing Bridge GAD functions directly...")
    
    # Test parameters
    span = 20.0
    load = 15.0
    E = DEFAULT_E
    I = DEFAULT_I
    
    print(f"Parameters: span={span}m, load={load}kN/m, E={E}kN/m², I={I}m⁴")
    
    # Compute results
    bending_moment = compute_bending_moment(span, load)
    shear_force = compute_shear_force(load, span)
    deflection = compute_deflection(span, load, E, I)
    
    print("\n=== Bridge_GAD Results ===")
    print(f"{'Parameter':<15} {'Value':<12} {'Unit':<10}")
    print("-" * 35)
    print(f"{'Span Length':<15} {span:<12.2f} {'m':<10}")
    print(f"{'Load':<15} {load:<12.2f} {'kN/m':<10}")
    print(f"{'E-Modulus':<15} {E:<12.2e} {'kN/m²':<10}")
    print(f"{'Moment I':<15} {I:<12.2e} {'m⁴':<10}")
    print("-" * 35)
    print(f"{'Bending Moment':<15} {bending_moment:<12.2f} {'kN*m':<10}")
    print(f"{'Shear Force':<15} {shear_force:<12.2f} {'kN':<10}")
    print(f"{'Deflection':<15} {deflection:<12.6f} {'m':<10}")

if __name__ == "__main__":
    main()