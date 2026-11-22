# CRC Code Simulator - Setup Guide

## Quick Start

This guide will help you get the CRC Code Simulator up and running in minutes.

## Prerequisites

- Python 3.6 or higher installed
- Basic command line knowledge

## Installation Steps

### 1. Verify Python Installation

Open a command prompt/terminal and run:

```bash
python --version
```

Expected output: `Python 3.6.0` or higher

### 2. Navigate to Project Directory

```bash
cd "C:\Users\harsh\OneDrive\Desktop\College\Semester V\CN\Project"
```

### 3. Run the Quick Demo

```bash
python run_demo.py
```

You should see a demonstration of CRC error detection with 4 test cases.

## Running the Simulator

### Option 1: Professional GUI (Recommended)

**NEW**: Modern graphical interface with professional UI

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

### Option 2: Quick Demo

```bash
python run_demo.py
```

Shows 4 pre-configured test cases demonstrating different error scenarios.

### Option 3: Full Demonstration

```bash
python src/crc_simulator.py
```

Runs comprehensive demonstration with 5 scenarios including burst error detection.

### Option 4: Interactive Mode

```bash
python src/interactive_crc.py
```

Provides menu-driven interface for custom testing:
- Test with your own data
- Generate random test cases
- Change generator polynomials
- Demonstrate burst errors
- View current settings

## Project Structure

```
Project/
├── src/
│   ├── crc_simulator.py      # Core CRC engine
│   └── interactive_crc.py    # Interactive interface
├── docs/
│   └── USER_MANUAL.md        # Detailed documentation
├── tests/                    # Test directory (for future use)
├── README.md                 # Project overview
├── requirements.txt          # Dependencies (empty - uses std lib)
├── run_demo.py              # Quick demo script
├── PROJECT_STRUCTURE.md     # Structure documentation
└── SETUP_GUIDE.md          # This file
```

## Features

✅ **Error Detection**: Single-bit, multi-bit, and burst errors
✅ **Multiple Polynomials**: CRC-3, CRC-4, CRC-8, CRC-16 support
✅ **Interactive Testing**: Custom data input and random generation
✅ **Detailed Output**: Step-by-step transmission visualization
✅ **No Dependencies**: Uses only Python standard library

## Common Issues

### Issue: "Python is not recognized"

**Solution**: 
1. Install Python from [python.org](https://www.python.org/downloads/)
2. Add Python to system PATH during installation
3. Restart command prompt

### Issue: "Module not found"

**Solution**: 
1. Ensure you're in the project directory
2. Use the correct run commands as shown above
3. Don't run from inside the `src/` folder

### Issue: Script runs but shows errors

**Solution**: 
1. Check Python version (3.6+ required)
2. Ensure all files are in the correct directories
3. Try running the quick demo first

## Next Steps

1. **Run the quick demo** to understand basic functionality
2. **Read the README.md** for project overview
3. **Consult docs/USER_MANUAL.md** for detailed usage instructions
4. **Try interactive mode** to experiment with custom data
5. **Review the source code** to understand implementation

## Academic Use

This project is designed for Computer Networks coursework and includes:

- ✅ Executable Python scripts
- ✅ Well-commented source code
- ✅ Comprehensive documentation
- ✅ User manual with installation instructions
- ✅ Software requirements specification

## Support

For detailed information:
- **Quick Start**: This file
- **Overview**: README.md
- **Detailed Manual**: docs/USER_MANUAL.md
- **Structure**: PROJECT_STRUCTURE.md

## Verification

To verify your installation is correct:

```bash
# Test 1: Quick demo
python run_demo.py

# Test 2: Full demo
python src/crc_simulator.py

# Test 3: Import test
python -c "from src.crc_simulator import CRCSimulator; print('Import successful')"
```

All three tests should run without errors.

---

**Version**: 1.0  
**Last Updated**: 2026-09-23  
**Project**: CRC Code Simulator
