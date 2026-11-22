"""
CRC Code Simulator - Demo Script
Demonstrates all CRC scenarios with comprehensive output
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from crc_simulator import CRCSimulator


def run_comprehensive_demo():
    """Run comprehensive CRC demonstration"""
    
    print("="*70)
    print("CRC CODE SIMULATOR - COMPREHENSIVE DEMONSTRATION")
    print("="*70)
    print("Demonstrating Error Detection and Correction using CRC")
    print("="*70)
    
    # Scenario 1: Error-free transmission with CRC-3
    print("\n" + "="*70)
    print("SCENARIO 1: Error-Free Transmission (CRC-3)")
    print("="*70)
    simulator = CRCSimulator(polynomial="1101")
    simulator.demonstrate_transmission("1011001", error_positions=None, show_steps=True)
    
    # Scenario 2: Single bit error with CRC-3
    print("\n" + "="*70)
    print("SCENARIO 2: Single Bit Error Detection (CRC-3)")
    print("="*70)
    simulator.demonstrate_transmission("1011001", error_positions=[2], show_steps=True)
    
    # Scenario 3: Multiple bit errors with CRC-3
    print("\n" + "="*70)
    print("SCENARIO 3: Multiple Bit Errors Detection (CRC-3)")
    print("="*70)
    simulator.demonstrate_transmission("1011001", error_positions=[1, 4, 6], show_steps=True)
    
    # Scenario 4: Burst error detection with CRC-3
    print("\n" + "="*70)
    print("SCENARIO 4: Burst Error Detection (CRC-3)")
    print("="*70)
    simulator.burst_error_detection("1011001", burst_length=3)
    
    # Scenario 5: Different polynomial (CRC-4)
    print("\n" + "="*70)
    print("SCENARIO 5: Using Different Polynomial (CRC-4)")
    print("="*70)
    simulator_crc4 = CRCSimulator(polynomial="10011")
    simulator_crc4.demonstrate_transmission("1101011011", error_positions=[3, 7], show_steps=True)
    
    # Scenario 6: CRC-8 demonstration
    print("\n" + "="*70)
    print("SCENARIO 6: CRC-8 Demonstration")
    print("="*70)
    simulator_crc8 = CRCSimulator(polynomial="100000111")
    simulator_crc8.demonstrate_transmission("1101011011001010", error_positions=[5, 12], show_steps=True)
    
    # Scenario 7: Comparison of polynomials
    print("\n" + "="*70)
    print("SCENARIO 7: Polynomial Comparison")
    print("="*70)
    test_data = "1011001101"
    test_errors = [3, 7]
    
    polynomials = [
        ("CRC-3", "1101"),
        ("CRC-4", "10011"),
        ("CRC-8", "100000111")
    ]
    
    print(f"Test Data: {test_data}")
    print(f"Error Positions: {test_errors}")
    print()
    
    for name, poly in polynomials:
        sim = CRCSimulator(polynomial=poly)
        result = sim.demonstrate_transmission(test_data, test_errors, show_steps=False)
        print(f"{name} ({poly}):")
        print(f"  CRC Checksum: {result['crc_checksum']}")
        print(f"  Valid: {'Yes' if result['is_valid'] else 'No'}")
        print(f"  Remainder: {result['remainder']}")
        print()
    
    print("="*70)
    print("DEMONSTRATION COMPLETE")
    print("="*70)
    print("\nKey Observations:")
    print("- CRC successfully detects single and multiple bit errors")
    print("- Burst errors are detected when within polynomial capability")
    print("- Different polynomials offer different error detection capabilities")
    print("- Longer polynomials generally provide better error detection")
    print("="*70)


if __name__ == "__main__":
    run_comprehensive_demo()
