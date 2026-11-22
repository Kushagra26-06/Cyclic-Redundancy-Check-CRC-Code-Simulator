"""
Unit tests for CRC GUI
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import tkinter as tk
from unittest.mock import Mock, patch


def test_gui_initialization():
    """Test GUI initialization"""
    try:
        # Create a mock root window
        root = tk.Tk()
        root.withdraw()  # Hide the window
        
        # Import and create GUI
        from crc_gui import CompleteCRCGUI
        app = CompleteCRCGUI(root)
        
        # Check that key components exist
        assert hasattr(app, 'simulator')
        assert hasattr(app, 'notebook')
        assert hasattr(app, 'results_text')
        
        root.destroy()
        print("✓ GUI initialization test passed")
        return True
    except Exception as e:
        print(f"GUI initialization test failed: {e}")
        return False


def test_polynomial_update():
    """Test polynomial update functionality"""
    try:
        root = tk.Tk()
        root.withdraw()
        
        from crc_gui import CompleteCRCGUI
        app = CompleteCRCGUI(root)
        
        # Test polynomial update
        app.update_poly('custom')
        assert app.simulator.polynomial_length == len(app.simulator.polynomial)
        
        root.destroy()
        print("✓ Polynomial update test passed")
        return True
    except Exception as e:
        print(f"Polynomial update test failed: {e}")
        return False


def test_field_clearing():
    """Test field clearing functionality"""
    try:
        root = tk.Tk()
        root.withdraw()
        
        from crc_gui import CompleteCRCGUI
        app = CompleteCRCGUI(root)
        
        # Test field clearing
        app.clear_field('custom')
        assert app.custom_data_entry.get() == "1011001"
        
        root.destroy()
        print("✓ Field clearing test passed")
        return True
    except Exception as e:
        print(f"Field clearing test failed: {e}")
        return False


def run_all_tests():
    """Run all GUI tests"""
    print("Running CRC GUI Tests...")
    print("="*50)
    
    tests = [
        test_gui_initialization,
        test_polynomial_update,
        test_field_clearing
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("="*50)
    if all(results):
        print("All GUI tests passed! ✓")
        return True
    else:
        print("Some GUI tests failed.")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
