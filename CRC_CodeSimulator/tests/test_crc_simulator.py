"""
Unit tests for CRC Simulator
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from crc_simulator import CRCSimulator


def test_initialization():
    """Test simulator initialization"""
    sim = CRCSimulator(polynomial="1101")
    assert sim.polynomial == "1101"
    assert sim.polynomial_length == 4
    print("✓ Initialization test passed")


def test_xor_operation():
    """Test XOR operation"""
    sim = CRCSimulator()
    result = sim.xor_operation("1010", "1100")
    assert result == "0110"
    print("✓ XOR operation test passed")


def test_crc_calculation():
    """Test CRC calculation"""
    sim = CRCSimulator(polynomial="10011")
    data_with_crc, checksum = sim.calculate_crc("1011001")
    assert len(checksum) == 4  # CRC-4 produces 4-bit remainder
    assert data_with_crc == "1011001" + checksum
    print("✓ CRC calculation test passed")


def test_crc_verification():
    """Test CRC verification"""
    sim = CRCSimulator(polynomial="10011")
    data_with_crc, _ = sim.calculate_crc("1011001")
    
    # Valid data should pass
    is_valid, _ = sim.verify_crc(data_with_crc)
    assert is_valid == True
    
    # Corrupted data should fail
    corrupted = sim.introduce_error(data_with_crc, [3])
    is_valid, _ = sim.verify_crc(corrupted)
    assert is_valid == False
    
    print("✓ CRC verification test passed")


def test_error_introduction():
    """Test error introduction"""
    sim = CRCSimulator()
    original = "1011001"
    corrupted = sim.introduce_error(original, [2])
    
    # Bit at position 2 should be flipped
    assert corrupted[2] != original[2]
    # Other bits should remain the same
    assert corrupted[:2] == original[:2]
    assert corrupted[3:] == original[3:]
    
    print("✓ Error introduction test passed")


def test_transmission_demo():
    """Test transmission demonstration"""
    sim = CRCSimulator(polynomial="10011")
    result = sim.demonstrate_transmission("1011001", error_positions=[2])
    
    assert result['original_data'] == "1011001"
    assert result['error_positions'] == [2]
    assert result['is_valid'] == False  # Error should be detected
    
    print("✓ Transmission demonstration test passed")


def test_burst_error_detection():
    """Test burst error detection"""
    sim = CRCSimulator(polynomial="10011")
    result = sim.burst_error_detection("1011001", burst_length=3)
    
    assert result['burst_length'] == 3
    assert len(result['error_positions']) == 3
    
    print("✓ Burst error detection test passed")


def test_different_polynomials():
    """Test different polynomials"""
    polynomials = ["1101", "10011", "100000111", "10001000000100001"]
    
    for poly in polynomials:
        sim = CRCSimulator(polynomial=poly)
        assert sim.polynomial == poly
        assert sim.polynomial_length == len(poly)
        
        # Test calculation works
        data_with_crc, checksum = sim.calculate_crc("1011001")
        assert len(checksum) == len(poly) - 1
    
    print("✓ Different polynomials test passed")


def run_all_tests():
    """Run all tests"""
    print("Running CRC Simulator Tests...")
    print("="*50)
    
    try:
        test_initialization()
        test_xor_operation()
        test_crc_calculation()
        test_crc_verification()
        test_error_introduction()
        test_transmission_demo()
        test_burst_error_detection()
        test_different_polynomials()
        
        print("="*50)
        print("All tests passed! ✓")
    except AssertionError as e:
        print(f"Test failed: {e}")
        return False
    except Exception as e:
        print(f"Error during testing: {e}")
        return False
    
    return True


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
