# CRC Code Simulator - User Guide

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Using the GUI](#using-the-gui)
4. [Understanding CRC](#understanding-crc)
5. [Advanced Features](#advanced-features)
6. [Troubleshooting](#troubleshooting)

## Introduction

The CRC Code Simulator is a professional educational tool for understanding Cyclic Redundancy Check (CRC) error detection algorithms. It provides both a graphical interface and command-line tools for exploring how CRC works.

## Getting Started

### First Steps

1. Launch the application using `run_gui.bat` (Windows) or `python launch_gui.py` (Mac/Linux)
2. The GUI will open with the CUSTOM_DATA tab selected
3. Enter binary data (e.g., "1011001") in the input field
4. Select a generator polynomial (default: CRC-4)
5. Click "RUN_SIMULATION" to see the calculation process

## Using the GUI

### Custom Data Tab

This tab allows you to test your own binary data:

1. **Binary Data**: Enter any binary string (0s and 1s only)
2. **Error Positions**: Optionally specify positions to introduce errors (space-separated)
3. **Generator Polynomial**: Choose from CRC-3, CRC-4, CRC-8, or CRC-16
4. **RUN_SIMULATION**: Execute the simulation with detailed steps
5. **CLEAR**: Reset the input fields

### Random Data Tab

Generate random test data:

1. **Data Length**: Specify how many bits to generate (8-32 recommended)
2. **Number of Random Errors**: How many random bit errors to introduce (0-5)
3. **Generator Polynomial**: Choose polynomial for testing
4. **GENERATE_TEST**: Run the random test

### Burst Error Tab

Test consecutive bit error detection:

1. **Binary Data**: Enter test data
2. **Burst Error Length**: Specify length of consecutive errors
3. **Generator Polynomial**: Choose polynomial
4. **TEST_BURST**: Run burst error test

### Polynomial Comparison Tab

Compare different CRC polynomials:

1. **Binary Data**: Enter test data
2. **Compare Different Polynomials**: Choose which polynomials to compare
3. **Error Positions**: Specify test error positions
4. **COMPARE_POLY**: Run comparison

### All Scenarios Tab

Run comprehensive demonstration:

1. Shows all predefined test scenarios
2. **RUN_ALL_SCENARIOS**: Execute complete demonstration
3. **CLEAR_RESULTS**: Clear the results panel

## Understanding CRC

### What is CRC?

Cyclic Redundancy Check is an error-detecting code used to detect accidental changes to raw data. It's commonly used in:

- Network communications (Ethernet, WiFi)
- Storage devices (hard drives, SSDs)
- File transfers
- Digital communications

### How CRC Works

1. **Data Preparation**: Append zeros to original data
2. **Division**: Perform modulo-2 binary division
3. **Remainder**: The remainder becomes the CRC checksum
4. **Transmission**: Send original data + CRC
5. **Verification**: Receiver performs same division

### Reading the Long Division Format

The simulator shows the traditional long division format:

```
    10110010000
10011)1010110
    10011
    -----
     01101
     00000
     -----
     11010
     10011
     -----
     10010
     10011
     -----
     00010
     00000
     -----
     00100
     00000
     -----
     01010    ← Remainder (CRC)
```

## Advanced Features

### Polynomial Selection

Different polynomials offer different error detection capabilities:

- **CRC-3**: Good for simple demonstrations
- **CRC-4**: Better error detection, still simple
- **CRC-8**: Common in many applications
- **CRC-16**: Strong error detection, used in critical systems

### Error Patterns

- **Single Bit Errors**: Always detected
- **Double Bit Errors**: Usually detected
- **Burst Errors**: Detected if within polynomial capability
- **Random Errors**: Detection depends on polynomial strength

## Troubleshooting

### Common Issues

**GUI won't start**: Ensure Python is installed and tkinter is available

**Invalid binary data**: Use only 0s and 1s, no spaces or other characters

**Calculation errors**: Check that data length is appropriate for selected polynomial

**Results not showing**: Try clicking CLEAR then RUN_SIMULATION again

### Getting Help

For additional help:
- Check the README.md for overview
- Review SETUP_GUIDE.md for installation issues
- See PROJECT_STRUCTURE.md for technical details
