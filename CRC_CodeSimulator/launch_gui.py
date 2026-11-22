"""
Launch script for CRC Code Simulator GUI
Run this file to start the professional GUI application
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from crc_gui import main

if __name__ == "__main__":
    print("Starting CRC Code Simulator GUI...")
    main()
