# CRC Code Simulator - User Manual

## Table of Contents

1. [Introduction](#introduction)
2. [System Requirements](#system-requirements)
3. [Installation Guide](#installation-guide)
4. [Getting Started](#getting-started)
5. [Using the Simulator](#using-the-simulator)
6. [Understanding CRC](#understanding-crc)
7. [Troubleshooting](#troubleshooting)
8. [Advanced Usage](#advanced-usage)

---

## Introduction

The CRC Code Simulator is an educational tool designed to demonstrate how Cyclic Redundancy Check (CRC) codes work for error detection in data transmission. This manual provides step-by-step instructions for installation, usage, and understanding of the simulator.

### What is CRC?

Cyclic Redundancy Check (CRC) is an error-detecting code used to detect changes to raw data in digital networks and storage devices. It works by treating data as a binary number and dividing it by a predetermined polynomial using modulo-2 arithmetic.

### Purpose of This Simulator

This simulator helps you:
- Understand how CRC codes are calculated
- Visualize error detection mechanisms
- Test different error scenarios
- Experiment with various generator polynomials
- Learn about burst error detection

---

## System Requirements

### Minimum Requirements

- **Operating System**: Windows 7/8/10/11, Linux, or macOS
- **Python Version**: Python 3.6 or higher
- **RAM**: 256 MB minimum
- **Disk Space**: 10 MB free space
- **Processor**: Any modern processor

### Recommended Requirements

- **Operating System**: Windows 10/11, Ubuntu 20.04+, macOS 10.15+
- **Python Version**: Python 3.8 or higher
- **RAM**: 512 MB or more
- **Disk Space**: 50 MB free space
- **IDE**: VS Code, PyCharm, or similar Python IDE

### Software Dependencies

This project uses only Python standard library. No external packages are required.

**Optional Dependencies** (for enhanced features):
- PyPDF2 (for PDF processing)
- numpy (for advanced operations)

---

## Installation Guide

### Step 1: Verify Python Installation

Open a command prompt/terminal and check Python version:

```bash
python --version
```

Or:

```bash
python3 --version
```

**Expected Output**: Python 3.6.0 or higher

If Python is not installed, download from [python.org](https://www.python.org/downloads/)

### Step 2: Navigate to Project Directory

```bash
cd "C:\Users\harsh\OneDrive\Desktop\College\Semester V\CN\Project"
```

### Step 3: Install Dependencies (Optional)

```bash
pip install -r requirements.txt
```

### Step 4: Verify Installation

Run the demonstration to verify everything works:

```bash
python src/crc_simulator.py
```

You should see output showing various CRC scenarios.

---

## Getting Started

### Quick Start Guide

1. **Run the demonstration**:
   ```bash
   python src/crc_simulator.py
   ```

2. **Run interactive mode**:
   ```bash
   python src/interactive_crc.py
   ```

3. **Test with your own data**:
   - Choose option 1 in interactive mode
   - Enter binary data (e.g., `1011001`)
   - Specify error positions or leave blank for no errors

### First Run Example

```
CRC CODE SIMULATOR
============================================================
Demonstrating Error Detection and Correction using CRC
============================================================

SCENARIO 1: Error-Free Transmission
------------------------------------------------------------

Step 1: Original Data: 1011001
Generator Polynomial: 1101
CRC Checksum: 001
Transmitted Data (Data + CRC): 1011001001

Step 2: No errors introduced
Received Data: 1011001001

Step 3: Verifying CRC at receiver...
Remainder after division: 000
✓ RESULT: No errors detected - Data is valid
```

---

## Using the Simulator

### Mode 1: Demonstration Mode

**File**: `src/crc_simulator.py`

**Purpose**: Automatically runs pre-defined scenarios

**How to Run**:
```bash
python src/crc_simulator.py
```

**Scenarios Included**:
1. Error-free transmission
2. Single bit error
3. Multiple bit errors
4. Burst error detection
5. Different polynomial (CRC-4)

**Output**: Step-by-step explanation of each scenario with results

### Mode 2: Interactive Mode

**File**: `src/interactive_crc.py`

**Purpose**: User-driven testing with custom inputs

**How to Run**:
```bash
python src/interactive_crc.py
```

**Menu Options**:

#### Option 1: Test with Custom Data
- Enter your own binary data
- Specify error positions
- See detailed transmission process

**Example**:
```
Enter binary data: 110101
Enter error positions (0-8, separated by spaces): 3 5
```

#### Option 2: Test with Random Data
- Specify data length
- Specify number of errors
- System generates random test case

**Example**:
```
Enter data length (8-32 recommended): 16
Enter number of random errors to introduce (0-5): 2
```

#### Option 3: Change Polynomial
- Choose from common polynomials
- Enter custom polynomial
- Update simulator settings

**Common Polynomials**:
- CRC-3: `1101`
- CRC-4: `10011`
- CRC-8: `100000111`
- CRC-16: `10001000000100001`

#### Option 4: Demonstrate Burst Error Detection
- Enter binary data
- Specify burst error length
- See how burst errors are detected

#### Option 5: View Current Settings
- Display current polynomial
- Show error detection capabilities
- View configuration details

#### Option 6: Run All Demo Scenarios
- Execute all demonstration scenarios
- Press Enter between scenarios
- Comprehensive overview

### Mode 3: Library Mode

**Purpose**: Import and use in your own Python code

**Example**:
```python
from src.crc_simulator import CRCSimulator

# Create simulator instance
sim = CRCSimulator(polynomial="1101")

# Calculate CRC
data = "1011001"
encoded, checksum = sim.calculate_crc(data)

# Verify
valid, remainder = sim.verify_crc(encoded)

# Introduce error
corrupted = sim.introduce_error(encoded, [2])
valid, remainder = sim.verify_crc(corrupted)
```

---

## Understanding CRC

### CRC Calculation Process

#### Step 1: Append Zeros
```
Original Data: 1011001
Polynomial: 1101 (length 4)
Append (4-1) = 3 zeros: 1011001000
```

#### Step 2: Modulo-2 Division
```
Divide 1011001000 by 1101 using XOR
```

#### Step 3: Get Remainder
```
Remainder: 001
```

#### Step 4: Replace Zeros with Remainder
```
Transmitted Data: 1011001 + 001 = 1011001001
```

### CRC Verification Process

#### Step 1: Receive Data
```
Received: 1011001001
```

#### Step 2: Divide by Polynomial
```
Divide 1011001001 by 1101
```

#### Step 3: Check Remainder
```
Remainder = 000 → No errors
Remainder ≠ 000 → Errors detected
```

### Error Detection Capabilities

| Error Type | Detection Rate | Notes |
|------------|---------------|-------|
| Single-bit | 100% | Always detected |
| Double-bit | ~99% | Depends on polynomial |
| Odd-number bits | 100% | Always detected |
| Burst errors | Up to polynomial length | CRC-3 detects 3-bit bursts |

### Polynomial Selection

**Choose polynomial based on**:
- Required error detection capability
- Data length
- Performance requirements
- Standard compliance

**Guidelines**:
- Short data → CRC-3 or CRC-4
- Medium data → CRC-8
- Long data → CRC-16 or CRC-32

---

## Troubleshooting

### Common Issues and Solutions

#### Issue 1: Python Not Recognized

**Error**: `'python' is not recognized as an internal or external command`

**Solutions**:
1. Install Python from python.org
2. Add Python to system PATH
3. Use `python3` instead of `python`
4. Use full path to Python executable

#### Issue 2: Module Not Found

**Error**: `ModuleNotFoundError: No module named 'crc_simulator'`

**Solutions**:
1. Ensure you're in the project directory
2. Use correct import: `from src.crc_simulator import CRCSimulator`
3. Add project directory to PYTHONPATH

#### Issue 3: Invalid Binary Input

**Error**: Program rejects your input

**Solutions**:
1. Enter only 0s and 1s
2. No spaces or other characters
3. Example: `1011001` (correct), `10 11 01` (incorrect)

#### Issue 4: Error Position Out of Range

**Error**: Program says position is invalid

**Solutions**:
1. Positions are 0-indexed
2. Maximum position = data length - 1
3. For data `1011001` (length 7), valid positions: 0-6

#### Issue 5: Permission Denied

**Error**: Cannot write to files or directories

**Solutions**:
1. Run command prompt as administrator
2. Check folder permissions
3. Ensure project directory is not read-only

### Debug Mode

To enable detailed error messages, modify the code:

```python
import sys
try:
    # Your code here
    pass
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    import traceback
    traceback.print_exc()
```

---

## Advanced Usage

### Custom Polynomial Testing

Test your own polynomial:

```python
from src.crc_simulator import CRCSimulator

# Custom polynomial
custom_poly = "101010101"
sim = CRCSimulator(polynomial=custom_poly)

# Test with various data
test_data = ["1011001", "1101011", "1110000"]
for data in test_data:
    encoded, checksum = sim.calculate_crc(data)
    print(f"Data: {data}, CRC: {checksum}")
```

### Batch Testing

Test multiple scenarios automatically:

```python
from src.crc_simulator import CRCSimulator

sim = CRCSimulator(polynomial="1101")

# Test data
test_cases = [
    ("1011001", []),
    ("1011001", [2]),
    ("1011001", [1, 4]),
    ("1101011", [0, 3, 5]),
]

for data, errors in test_cases:
    result = sim.demonstrate_transmission(data, errors)
    print(f"Valid: {result['is_valid']}")
```

### Performance Analysis

Measure CRC calculation time:

```python
import time
from src.crc_simulator import CRCSimulator

sim = CRCSimulator(polynomial="1101")

# Large data
large_data = "1" * 1000

start = time.time()
encoded, checksum = sim.calculate_crc(large_data)
end = time.time()

print(f"Time: {end - start:.6f} seconds")
```

### Integration with Other Projects

Use CRC in your own applications:

```python
from src.crc_simulator import CRCSimulator

class DataTransmitter:
    def __init__(self, polynomial="1101"):
        self.crc = CRCSimulator(polynomial)
    
    def send_data(self, data):
        encoded, _ = self.crc.calculate_crc(data)
        return encoded
    
    def receive_data(self, received):
        valid, remainder = self.crc.verify_crc(received)
        return valid, received[:-self.crc.polynomial_length+1]

# Usage
transmitter = DataTransmitter()
original = "1011001"
sent = transmitter.send_data(original)
valid, decoded = transmitter.receive_data(sent)
```

---

## Appendix

### A. CRC Polynomial Reference

| Name | Polynomial | Hex | Length | Common Use |
|------|------------|-----|--------|------------|
| CRC-3 | 1101 | 0xD | 3 | Simple checks |
| CRC-4 | 10011 | 0x13 | 4 | Telecom |
| CRC-8 | 100000111 | 0x107 | 8 | SMBus, WWBN |
| CRC-16 | 10001000000100001 | 0x11021 | 16 | USB, Bluetooth |
| CRC-32 | 100000100110000010001110110110111 | 0x104C11DB7 | 32 | Ethernet, ZIP |

### B. Binary Conversion Reference

| Decimal | Binary | Hex |
|---------|--------|-----|
| 0 | 0000 | 0 |
| 1 | 0001 | 1 |
| 2 | 0010 | 2 |
| 3 | 0011 | 3 |
| 4 | 0100 | 4 |
| 5 | 0101 | 5 |
| 6 | 0110 | 6 |
| 7 | 0111 | 7 |
| 8 | 1000 | 8 |
| 9 | 1001 | 9 |
| 10 | 1010 | A |
| 11 | 1011 | B |
| 12 | 1100 | C |
| 13 | 1101 | D |
| 14 | 1110 | E |
| 15 | 1111 | F |

### C. Quick Reference Commands

```bash
# Run demonstration
python src/crc_simulator.py

# Run interactive mode
python src/interactive_crc.py

# Check Python version
python --version

# Install dependencies
pip install -r requirements.txt

# Run specific test
python -c "from src.crc_simulator import CRCSimulator; CRCSimulator().demonstrate_transmission('1011001')"
```

---

## Contact and Support

For questions related to:
- **Usage**: Refer to this manual
- **Installation**: Check System Requirements section
- **Errors**: See Troubleshooting section
- **Project details**: Contact your instructor

---

**Document Version**: 1.0  
**Last Updated**: 2026-09-23  
**Project**: CRC Code Simulator  
**Course**: Computer Networks - Semester V
