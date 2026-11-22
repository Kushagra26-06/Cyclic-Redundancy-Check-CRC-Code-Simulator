# CRC Code Simulator

A comprehensive Python-based simulator demonstrating error detection and correction using Cyclic Redundancy Check (CRC) codes.

## Project Overview

This project implements a CRC (Cyclic Redundancy Check) code simulator that demonstrates how errors are detected in data transmission. CRC is a widely used error-detecting code commonly used in digital networks and storage devices to detect accidental changes to raw data.

## Features

- **CRC Calculation**: Compute CRC checksums for any binary data
- **Error Detection**: Detect single-bit, multi-bit, and burst errors
- **Multiple Polynomial Support**: Support for various generator polynomials (CRC-3, CRC-4, CRC-8, CRC-16)
- **Interactive Mode**: Command-line interface for custom testing
- **Demonstration Mode**: Pre-built scenarios showing different error types
- **Detailed Output**: Step-by-step visualization of CRC operations

## Project Structure

```
Project/
├── src/
│   ├── crc_simulator.py      # Core CRC simulation engine
│   └── interactive_crc.py    # Interactive command-line interface
├── docs/
│   └── USER_MANUAL.md        # Detailed user manual
├── tests/
│   └── test_crc.py          # Unit tests (optional)
├── requirements.txt          # Python dependencies
├── README.md                # This file
└── Project GuideLines.pdf   # Project guidelines
```

## Installation

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

### Setup Instructions

1. **Clone or download the project**
   ```bash
   cd "C:\Users\harsh\OneDrive\Desktop\College\Semester V\CN\Project"
   ```

2. **Install dependencies (optional)**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation**
   ```bash
   python src/crc_simulator.py
   ```

## Usage

### Option 1: Professional GUI (Recommended)

**NEW**: Professional graphical interface with modern UI

```bash
python launch_gui.py
```

Or double-click `run_gui.bat` on Windows

**GUI Features:**
- Modern, professional interface
- Visual input controls
- Real-time simulation results
- Color-coded output
- Error injection controls
- Multiple polynomial support
- Step-by-step process visualization

### Option 2: Quick Demo

To run the quick demonstration:

```bash
python run_demo.py
```

### Option 3: Full Demonstration

To run the pre-built demonstration scenarios:

```bash
python src/crc_simulator.py
```

This will display:
- Error-free transmission
- Single bit error detection
- Multiple bit error detection
- Burst error detection
- Different polynomial demonstration

### Option 4: Interactive Command-Line Mode

To run the interactive command-line interface:

```bash
python src/interactive_crc.py
```

**Interactive Mode Features:**
1. Test with custom binary data
2. Test with randomly generated data
3. Change generator polynomial
4. Demonstrate burst error detection
5. View current settings
6. Run all demo scenarios

### Using as a Library

You can also import the CRC simulator in your own Python code:

```python
from src.crc_simulator import CRCSimulator

# Initialize with polynomial
simulator = CRCSimulator(polynomial="1101")

# Calculate CRC
data = "1011001"
data_with_crc, checksum = simulator.calculate_crc(data)
print(f"Data with CRC: {data_with_crc}")

# Verify data
is_valid, remainder = simulator.verify_crc(data_with_crc)
print(f"Valid: {is_valid}")

# Introduce errors
error_data = simulator.introduce_error(data_with_crc, [2])
is_valid, remainder = simulator.verify_crc(error_data)
print(f"Errors detected: {not is_valid}")
```

## CRC Background

### How CRC Works

1. **Generator Polynomial**: A predefined binary pattern used for division
2. **Data Division**: The data is divided by the polynomial using modulo-2 arithmetic
3. **Remainder**: The remainder becomes the CRC checksum
4. **Transmission**: Data + CRC checksum is transmitted
5. **Verification**: Receiver divides received data by polynomial
6. **Error Detection**: Non-zero remainder indicates errors

### Supported Polynomials

- **CRC-3**: `1101` - Can detect single-bit errors
- **CRC-4**: `10011` - Can detect single and double-bit errors
- **CRC-8**: `100000111` - Common in communication protocols
- **CRC-16**: `10001000000100001` - Used in USB, Bluetooth, etc.

## Examples

### Example 1: Error-Free Transmission

```
Original Data: 1011001
Generator Polynomial: 1101
CRC Checksum: 001
Transmitted Data: 1011001001
Received Data: 1011001001
Remainder: 000
✓ RESULT: No errors detected - Data is valid
```

### Example 2: Single Bit Error

```
Original Data: 1011001
Generator Polynomial: 1101
CRC Checksum: 001
Transmitted Data: 1011001001
Introducing errors at positions: [2]
Received Data (with errors): 1001001001
Remainder: 011
✗ RESULT: Errors detected - Data is corrupted
```

## Error Detection Capabilities

- **Single-bit errors**: Always detected
- **Double-bit errors**: Detected with most polynomials
- **Burst errors**: Detected up to polynomial length
- **Odd number of errors**: Always detected

## Software Requirements

- **Operating System**: Windows, Linux, or macOS
- **Python Version**: 3.6 or higher
- **IDE**: Any Python IDE (VS Code, PyCharm, IDLE) or command line
- **No additional libraries required**

## Project Submission Components

As per project guidelines, this project includes:

1. ✅ **Executable/Output File**: Python scripts that can be run directly
2. ✅ **Source Code**: Well-commented, properly indented Python code
3. ✅ **Documentation**: README.md and USER_MANUAL.md
4. ✅ **Software Requirements**: Listed in this README

## Troubleshooting

### Common Issues

**Issue**: "Python is not recognized"
- **Solution**: Install Python from python.org and add to PATH

**Issue**: "Module not found"
- **Solution**: Ensure you're running from the project directory

**Issue**: "Invalid binary input"
- **Solution**: Enter only 0s and 1s for binary data

## Future Enhancements

Potential improvements for the project:
- GUI interface using Tkinter or PyQt
- Support for hexadecimal input
- Real-time data transmission simulation
- Error correction capabilities (beyond detection)
- Performance benchmarking

## References

- Tanenbaum, A. S., & Wetherall, D. J. (2011). Computer Networks
- Forouzan, B. A. (2007). Data Communications and Networking
- IEEE 802.3 Ethernet CRC standards

## License

This project is created for educational purposes.

## Authors

Computer Networks Project
Semester V
College Project

## Contact

For questions or issues, please refer to the project documentation or contact your instructor.
