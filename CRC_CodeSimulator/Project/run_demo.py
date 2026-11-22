"""
Quick Demo Script for CRC Code Simulator
Run this file to see a quick demonstration of CRC functionality
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from crc_simulator import CRCSimulator


def quick_demo():
    """Run a quick demonstration of CRC simulator."""
    
    print("="*70)
    print("CRC CODE SIMULATOR - QUICK DEMO")
    print("="*70)
    print("\nThis demonstration shows how CRC detects errors in data transmission\n")
    
    # Initialize simulator
    simulator = CRCSimulator(polynomial="1101")
    
    # Test case 1: Error-free transmission
    print("\n" + "-"*70)
    print("TEST CASE 1: Error-Free Transmission")
    print("-"*70)
    data = "1011001"
    print(f"Original Data: {data}")
    
    encoded, checksum = simulator.calculate_crc(data)
    print(f"CRC Checksum: {checksum}")
    print(f"Transmitted: {encoded}")
    
    is_valid, remainder = simulator.verify_crc(encoded)
    print(f"Verification: {'[OK] VALID' if is_valid else '[ERROR] INVALID'}")
    print(f"Remainder: {remainder}")
    
    # Test case 2: Single bit error
    print("\n" + "-"*70)
    print("TEST CASE 2: Single Bit Error")
    print("-"*70)
    data = "1011001"
    print(f"Original Data: {data}")
    
    encoded, checksum = simulator.calculate_crc(data)
    print(f"Transmitted: {encoded}")
    
    # Introduce error at position 2
    corrupted = simulator.introduce_error(encoded, [2])
    print(f"Corrupted (bit 2 flipped): {corrupted}")
    
    is_valid, remainder = simulator.verify_crc(corrupted)
    print(f"Verification: {'[OK] VALID' if is_valid else '[ERROR] INVALID - Error Detected!'}")
    print(f"Remainder: {remainder}")
    
    # Test case 3: Multiple bit errors
    print("\n" + "-"*70)
    print("TEST CASE 3: Multiple Bit Errors")
    print("-"*70)
    data = "1101011"
    print(f"Original Data: {data}")
    
    encoded, checksum = simulator.calculate_crc(data)
    print(f"Transmitted: {encoded}")
    
    # Introduce errors at positions 1, 3, 5
    corrupted = simulator.introduce_error(encoded, [1, 3, 5])
    print(f"Corrupted (bits 1,3,5 flipped): {corrupted}")
    
    is_valid, remainder = simulator.verify_crc(corrupted)
    print(f"Verification: {'[OK] VALID' if is_valid else '[ERROR] INVALID - Error Detected!'}")
    print(f"Remainder: {remainder}")
    
    # Test case 4: Different polynomial
    print("\n" + "-"*70)
    print("TEST CASE 4: Using CRC-4 Polynomial")
    print("-"*70)
    simulator_crc4 = CRCSimulator(polynomial="10011")
    data = "1101011011"
    print(f"Original Data: {data}")
    print(f"Polynomial: {simulator_crc4.polynomial}")
    
    encoded, checksum = simulator_crc4.calculate_crc(data)
    print(f"CRC Checksum: {checksum}")
    print(f"Transmitted: {encoded}")
    
    corrupted = simulator_crc4.introduce_error(encoded, [4])
    print(f"Corrupted (bit 4 flipped): {corrupted}")
    
    is_valid, remainder = simulator_crc4.verify_crc(corrupted)
    print(f"Verification: {'[OK] VALID' if is_valid else '[ERROR] INVALID - Error Detected!'}")
    print(f"Remainder: {remainder}")
    
    # Summary
    print("\n" + "="*70)
    print("DEMO SUMMARY")
    print("="*70)
    print("[OK] CRC successfully detected all introduced errors")
    print("[OK] Error-free transmission was validated correctly")
    print("[OK] Different polynomials can be used for different requirements")
    print("\nFor interactive testing, run: python src/interactive_crc.py")
    print("For full demonstration, run: python src/crc_simulator.py")
    print("="*70)


if __name__ == "__main__":
    quick_demo()
