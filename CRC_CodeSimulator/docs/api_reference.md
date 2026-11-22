# CRC Code Simulator - API Reference

## CRCSimulator Class

### Constructor

```python
CRCSimulator(polynomial="1101")
```

Initialize the CRC simulator with a generator polynomial.

**Parameters:**
- `polynomial` (str): Binary string representing the generator polynomial
  - Default: "1101" (CRC-3)
  - Options: "1101", "10011", "100000111", "10001000000100001"

**Example:**
```python
simulator = CRCSimulator(polynomial="10011")  # CRC-4
```

### Methods

#### xor_operation

```python
xor_operation(a, b) -> str
```

Perform XOR operation on two binary strings.

**Parameters:**
- `a` (str): First binary string
- `b` (str): Second binary string

**Returns:**
- `str`: Result of XOR operation

**Example:**
```python
result = simulator.xor_operation("1010", "1100")
# Returns "0110"
```

#### mod2_division

```python
mod2_division(data, polynomial, show_steps=False) -> tuple
```

Perform modulo-2 binary division to calculate CRC.

**Parameters:**
- `data` (str): Binary data string
- `polynomial` (str): Generator polynomial
- `show_steps` (bool): Whether to show step-by-step process

**Returns:**
- If `show_steps=False`: `str` (remainder)
- If `show_steps=True`: `tuple` (remainder, steps_list)

**Example:**
```python
remainder = simulator.mod2_division("10110010000", "10011")
remainder, steps = simulator.mod2_division("10110010000", "10011", show_steps=True)
```

#### calculate_crc

```python
calculate_crc(data, show_steps=False) -> tuple
```

Calculate CRC checksum for given data.

**Parameters:**
- `data` (str): Binary data string
- `show_steps` (bool): Whether to show step-by-step process

**Returns:**
- If `show_steps=False`: `tuple` (data_with_crc, crc_checksum)
- If `show_steps=True`: `tuple` (data_with_crc, crc_checksum, steps)

**Example:**
```python
data_with_crc, checksum = simulator.calculate_crc("1011001")
data_with_crc, checksum, steps = simulator.calculate_crc("1011001", show_steps=True)
```

#### verify_crc

```python
verify_crc(received_data, show_steps=False) -> tuple
```

Verify if received data has errors using CRC.

**Parameters:**
- `received_data` (str): Binary data string with CRC
- `show_steps` (bool): Whether to show step-by-step process

**Returns:**
- If `show_steps=False`: `tuple` (is_valid, remainder)
- If `show_steps=True`: `tuple` (is_valid, remainder, steps)

**Example:**
```python
is_valid, remainder = simulator.verify_crc("101100101010")
is_valid, remainder, steps = simulator.verify_crc("101100101010", show_steps=True)
```

#### introduce_error

```python
introduce_error(data, error_positions) -> str
```

Introduce errors at specific bit positions.

**Parameters:**
- `data` (str): Binary data string
- `error_positions` (list): List of bit positions to flip (0-indexed)

**Returns:**
- `str`: Data with errors introduced

**Example:**
```python
corrupted_data = simulator.introduce_error("1011001", [2, 5])
# Flips bits at positions 2 and 5
```

#### demonstrate_transmission

```python
demonstrate_transmission(original_data, error_positions=None, show_steps=False) -> dict
```

Demonstrate complete CRC transmission process with error detection.

**Parameters:**
- `original_data` (str): Original binary data
- `error_positions` (list, optional): List of positions to introduce errors
- `show_steps` (bool): Whether to show detailed step-by-step process

**Returns:**
- `dict`: Complete transmission details
  - `original_data`: Original data
  - `crc_checksum`: Calculated CRC
  - `transmitted_data`: Data + CRC
  - `error_positions`: Error positions (if any)
  - `received_data`: Data after transmission
  - `is_valid`: Whether data is valid
  - `remainder`: Verification remainder
  - `steps`: Step-by-step process (if show_steps=True)

**Example:**
```python
result = simulator.demonstrate_transmission("1011001", error_positions=[2])
result = simulator.demonstrate_transmission("1011001", show_steps=True)
```

#### burst_error_detection

```python
burst_error_detection(data, burst_length) -> dict
```

Demonstrate burst error detection capability.

**Parameters:**
- `data` (str): Binary data
- `burst_length` (int): Length of burst error to introduce

**Returns:**
- `dict`: Burst error detection results
  - `burst_length`: Length of burst error
  - `error_positions`: Positions of errors
  - `is_detected`: Whether error was detected
  - `remainder`: Verification remainder

**Example:**
```python
result = simulator.burst_error_detection("1011001", burst_length=3)
```

## Properties

### polynomial

```python
simulator.polynomial
```

Current generator polynomial (string).

### polynomial_length

```python
simulator.polynomial_length
```

Length of the current polynomial (integer).

## Usage Examples

### Basic CRC Calculation

```python
from crc_simulator import CRCSimulator

# Initialize with CRC-4
simulator = CRCSimulator(polynomial="10011")

# Calculate CRC
data = "1011001"
data_with_crc, checksum = simulator.calculate_crc(data)

print(f"Original: {data}")
print(f"CRC: {checksum}")
print(f"Transmitted: {data_with_crc}")
```

### Error Detection

```python
# Transmit data
data_with_crc, _ = simulator.calculate_crc("1011001")

# Introduce error
corrupted = simulator.introduce_error(data_with_crc, [3])

# Verify
is_valid, remainder = simulator.verify_crc(corrupted)

if is_valid:
    print("Data is valid")
else:
    print("Error detected!")
```

### Step-by-Step Analysis

```python
# Get detailed steps
result = simulator.demonstrate_transmission("1011001", show_steps=True)

# Print each step
for step in result['steps']:
    print(step)
```

## Error Handling

The simulator validates inputs and will raise exceptions for:

- Invalid binary data (contains characters other than 0 and 1)
- Empty data strings
- Invalid polynomial strings
- Out-of-range error positions

## Performance Considerations

- Large data sets (>1000 bits) may take longer to process
- Step-by-step mode is slower than calculation-only mode
- Memory usage scales with data length
