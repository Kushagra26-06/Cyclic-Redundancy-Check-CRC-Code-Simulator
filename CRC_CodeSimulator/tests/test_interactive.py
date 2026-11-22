"""
Unit tests for Interactive CRC
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from io import StringIO
from unittest.mock import patch


def test_binary_input_validation():
    """Test binary input validation"""
    from interactive_crc import get_binary_input
    
    # Test valid input
    with patch('builtins.input', return_value='1011001'):
        result = get_binary_input("Enter data: ")
        assert result == '1011001'
    
    # Test invalid input (should reject)
    with patch('builtins.input', side_effect=['1012', '1011001']):
        result = get_binary_input("Enter data: ")
        assert result == '1011001'
    
    print("✓ Binary input validation test passed")


def test_polynomial_choice():
    """Test polynomial choice selection"""
    from interactive_crc import get_polynomial_choice
    
    # Test valid choices
    with patch('builtins.input', return_value='1'):
        result = get_polynomial_choice()
        assert result == '1101'
    
    with patch('builtins.input', return_value='2'):
        result = get_polynomial_choice()
        assert result == '10011'
    
    with patch('builtins.input', return_value='3'):
        result = get_polynomial_choice()
        assert result == '100000111'
    
    with patch('builtins.input', return_value='4'):
        result = get_polynomial_choice()
        assert result == '10001000000100001'
    
    print("✓ Polynomial choice test passed")


def test_menu_display():
    """Test menu display"""
    from interactive_crc import print_menu
    
    # Capture print output
    captured_output = StringIO()
    with patch('sys.stdout', captured_output):
        print_menu()
    
    output = captured_output.getvalue()
    assert "INTERACTIVE CRC SIMULATOR" in output
    assert "Calculate CRC" in output
    assert "Verify data" in output
    
    print("✓ Menu display test passed")


def run_all_tests():
    """Run all interactive tests"""
    print("Running Interactive CRC Tests...")
    print("="*50)
    
    try:
        test_binary_input_validation()
        test_polynomial_choice()
        test_menu_display()
        
        print("="*50)
        print("All interactive tests passed! ✓")
        return True
    except AssertionError as e:
        print(f"Test failed: {e}")
        return False
    except Exception as e:
        print(f"Error during testing: {e}")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
