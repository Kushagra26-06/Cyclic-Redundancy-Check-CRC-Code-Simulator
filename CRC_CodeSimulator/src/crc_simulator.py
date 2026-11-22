"""
CRC Code Simulator
Demonstrates error detection and correction using Cyclic Redundancy Check (CRC)
"""

class CRCSimulator:
    """
    A comprehensive CRC simulator that demonstrates error detection and correction.
    Supports multiple polynomial generators and provides detailed analysis.
    """
    
    def __init__(self, polynomial="1101"):
        """
        Initialize the CRC simulator with a generator polynomial.
        
        Args:
            polynomial (str): Binary string representing the generator polynomial
                             Default: "1101" (CRC-3)
        """
        self.polynomial = polynomial
        self.polynomial_length = len(polynomial)
        
    def xor_operation(self, a, b):
        """Perform XOR operation on two binary strings"""
        result = []
        for i in range(1, len(b)):
            if a[i] == b[i]:
                result.append('0')
            else:
                result.append('1')
        return ''.join(result)
    
    def mod2_division(self, data, polynomial, show_steps=False):
        """
        Perform modulo-2 binary division to calculate CRC.
        
        Args:
            data (str): Binary data string
            polynomial (str): Generator polynomial
            show_steps (bool): Whether to show step-by-step process
            
        Returns:
            tuple: (remainder, steps_list) if show_steps else remainder
        """
        pick = len(polynomial)
        tmp = data[:pick]
        steps = []
        quotient = []
        
        if show_steps:
            # Generate long division format matching traditional style
            divisor_width = len(polynomial)
            dividend_width = len(data)
            
            lines = []
            
            # Line 1: Dividend at top
            lines.append(f"{' ' * (divisor_width + 2)}{data}")
            
            # Line 2: Divisor symbol with quotient (will be updated later)
            lines.append(f"{polynomial})")
            
            # Line 3: Divider line under dividend
            lines.append(f"{' ' * (divisor_width + 2)}{'-' * dividend_width}")
            
            current_pos = 0
            
            while pick < len(data):
                # Determine divisor (polynomial or zeros) based on first bit
                if tmp[0] == '1':
                    current_divisor = polynomial
                    quotient.append('1')
                else:
                    current_divisor = '0' * divisor_width
                    quotient.append('0')
                
                # Show divisor being XORed (only show polynomial for cleaner output)
                if current_divisor == polynomial:
                    lines.append(f"{' ' * (divisor_width + 2 + current_pos)}{current_divisor}")
                    lines.append(f"{' ' * (divisor_width + 2 + current_pos)}{'-' * divisor_width}")
                
                # Perform XOR
                xor_result = self.xor_operation(current_divisor, tmp)
                
                # Show result with next bit brought down
                lines.append(f"{' ' * (divisor_width + 2 + current_pos)}{xor_result}{data[pick]}")
                
                # Update tmp for next iteration
                tmp = xor_result + data[pick]
                current_pos += 1
                pick += 1
            
            # Final step - XOR with the remaining tmp (no more bits to bring down)
            if tmp[0] == '1':
                current_divisor = polynomial
                quotient.append('1')
            else:
                current_divisor = '0' * divisor_width
                quotient.append('0')
            
            # Show final divisor
            if current_divisor == polynomial:
                lines.append(f"{' ' * (divisor_width + 2 + current_pos)}{current_divisor}")
                lines.append(f"{' ' * (divisor_width + 2 + current_pos)}{'-' * divisor_width}")
            
            # Final XOR result (remainder)
            xor_result = self.xor_operation(current_divisor, tmp)
            lines.append(f"{' ' * (divisor_width + 2 + current_pos)}{xor_result}")
            tmp = xor_result
            
            # Insert quotient in line 2
            quotient_str = ''.join(quotient)
            lines[1] = f"{polynomial}){' ' * (dividend_width - len(quotient_str))}{quotient_str}"
            
            lines.append("")
            lines.append(f"Quotient: {quotient_str}")
            lines.append(f"Remainder: {tmp}")
            lines.append("")
            
            steps.append("LONG DIVISION FORMAT:")
            steps.extend(lines)
            steps.append("")
            return tmp, steps
        else:
            # Perform calculation without steps
            while pick < len(data):
                if tmp[0] == '1':
                    tmp = self.xor_operation(polynomial, tmp) + data[pick]
                else:
                    tmp = self.xor_operation('0'*pick, tmp) + data[pick]
                pick += 1
            
            if tmp[0] == '1':
                tmp = self.xor_operation(polynomial, tmp)
            else:
                tmp = self.xor_operation('0'*pick, tmp)
            
            return tmp
    
    def calculate_crc(self, data, show_steps=False):
        """
        Calculate CRC checksum for given data.
        
        Args:
            data (str): Binary data string
            show_steps (bool): Whether to show step-by-step process
            
        Returns:
            tuple: (data_with_crc, crc_checksum, steps) if show_steps else (data_with_crc, crc_checksum)
        """
        # Append zeros to data (length of polynomial - 1)
        appended_data = data + '0' * (self.polynomial_length - 1)
        
        if show_steps:
            steps = []
            steps.append(f"CRC CALCULATION PROCESS")
            steps.append(f"")
            steps.append(f"Step 1: Append Zeros")
            steps.append(f"  Original Data: {data}")
            steps.append(f"  Polynomial Length: {self.polynomial_length}")
            steps.append(f"  Zeros to append: {self.polynomial_length - 1}")
            steps.append(f"  Appended Data: {appended_data}")
            steps.append(f"")
            
            # Calculate remainder with steps
            remainder, division_steps = self.mod2_division(appended_data, self.polynomial, show_steps=True)
            steps.extend(division_steps)
            
            steps.append(f"")
            steps.append(f"Step 2: Replace Zeros with Remainder")
            steps.append(f"  Original Data: {data}")
            steps.append(f"  Remainder (CRC): {remainder}")
            steps.append(f"  Final Encoded Data: {data + remainder}")
            
            # Replace appended zeros with remainder
            data_with_crc = data + remainder
            
            return data_with_crc, remainder, steps
        else:
            # Calculate remainder
            remainder = self.mod2_division(appended_data, self.polynomial)
            
            # Replace appended zeros with remainder
            data_with_crc = data + remainder
            
            return data_with_crc, remainder
    
    def verify_crc(self, received_data, show_steps=False):
        """
        Verify if received data has errors using CRC.
        
        Args:
            received_data (str): Binary data string with CRC
            show_steps (bool): Whether to show step-by-step process
            
        Returns:
            tuple: (is_valid, remainder, steps) if show_steps else (is_valid, remainder)
        """
        if show_steps:
            steps = []
            steps.append(f"CRC VERIFICATION PROCESS")
            steps.append(f"")
            steps.append(f"Received Data: {received_data}")
            steps.append(f"Generator Polynomial: {self.polynomial}")
            steps.append(f"")
            
            # Perform division with steps
            remainder, division_steps = self.mod2_division(received_data, self.polynomial, show_steps=True)
            steps.extend(division_steps)
            
            steps.append(f"")
            steps.append(f"VERIFICATION RESULT:")
            is_valid = all(bit == '0' for bit in remainder)
            if is_valid:
                steps.append(f"  Remainder is all zeros: {remainder}")
                steps.append(f"  [OK] No errors detected - Data is VALID")
            else:
                steps.append(f"  Remainder is NOT all zeros: {remainder}")
                steps.append(f"  [ERROR] Errors detected - Data is CORRUPTED")
            
            return is_valid, remainder, steps
        else:
            remainder = self.mod2_division(received_data, self.polynomial)
            is_valid = all(bit == '0' for bit in remainder)
            return is_valid, remainder
    
    def introduce_error(self, data, error_positions):
        """
        Introduce errors at specific bit positions.
        
        Args:
            data (str): Binary data string
            error_positions (list): List of bit positions to flip (0-indexed)
            
        Returns:
            str: Data with errors introduced
        """
        data_list = list(data)
        for pos in error_positions:
            if 0 <= pos < len(data_list):
                data_list[pos] = '1' if data_list[pos] == '0' else '0'
        return ''.join(data_list)
    
    def demonstrate_transmission(self, original_data, error_positions=None, show_steps=False):
        """
        Demonstrate complete CRC transmission process with error detection.
        
        Args:
            original_data (str): Original binary data
            error_positions (list): Optional list of positions to introduce errors
            show_steps (bool): Whether to show detailed step-by-step process
            
        Returns:
            dict: Complete transmission details
        """
        all_steps = []
        
        if show_steps:
            all_steps.append("CRC TRANSMISSION DEMONSTRATION")
            all_steps.append("")
        
        # Step 1: Calculate CRC
        if show_steps:
            all_steps.append("STEP 1: TRANSMITTER - CRC CALCULATION")
        
        if show_steps:
            data_with_crc, crc_checksum, calc_steps = self.calculate_crc(original_data, show_steps=True)
            all_steps.extend(calc_steps)
        else:
            data_with_crc, crc_checksum = self.calculate_crc(original_data)
            if show_steps:
                all_steps.append(f"Original Data: {original_data}")
                all_steps.append(f"Generator Polynomial: {self.polynomial}")
                all_steps.append(f"CRC Checksum: {crc_checksum}")
                all_steps.append(f"Transmitted Data (Data + CRC): {data_with_crc}")
        
        if show_steps:
            all_steps.append("")
        
        # Step 2: Introduce errors if specified
        if show_steps:
            all_steps.append("STEP 2: TRANSMISSION CHANNEL")
        
        if error_positions:
            if show_steps:
                all_steps.append(f"Introducing errors at positions: {error_positions}")
            received_data = self.introduce_error(data_with_crc, error_positions)
            if show_steps:
                all_steps.append(f"Transmitted Data: {data_with_crc}")
                all_steps.append(f"Received Data (with errors): {received_data}")
        else:
            if show_steps:
                all_steps.append("No errors introduced")
            received_data = data_with_crc
            if show_steps:
                all_steps.append(f"Transmitted Data: {data_with_crc}")
                all_steps.append(f"Received Data: {received_data}")
        
        if show_steps:
            all_steps.append("")
        
        # Step 3: Verify CRC
        if show_steps:
            all_steps.append("STEP 3: RECEIVER - CRC VERIFICATION")
        
        if show_steps:
            is_valid, remainder, verify_steps = self.verify_crc(received_data, show_steps=True)
            all_steps.extend(verify_steps)
        else:
            is_valid, remainder = self.verify_crc(received_data)
            if show_steps:
                all_steps.append(f"Verifying CRC at receiver...")
                all_steps.append(f"Remainder after division: {remainder}")
                if is_valid:
                    all_steps.append("[OK] RESULT: No errors detected - Data is valid")
                else:
                    all_steps.append("[ERROR] RESULT: Errors detected - Data is corrupted")
                    all_steps.append(f"  Non-zero remainder indicates errors")
        
        if show_steps:
            all_steps.append("")
            all_steps.append("TRANSMISSION COMPLETE")
        
        result = {
            'original_data': original_data,
            'crc_checksum': crc_checksum,
            'transmitted_data': data_with_crc,
            'error_positions': error_positions,
            'received_data': received_data,
            'is_valid': is_valid,
            'remainder': remainder
        }
        
        if show_steps:
            result['steps'] = all_steps
        
        return result
    
    def burst_error_detection(self, data, burst_length):
        """
        Demonstrate burst error detection capability.
        
        Args:
            data (str): Binary data
            burst_length (int): Length of burst error to introduce
            
        Returns:
            dict: Burst error detection results
        """
        print("\n" + "="*60)
        print("BURST ERROR DETECTION DEMONSTRATION")
        print("="*60)
        
        data_with_crc, crc_checksum = self.calculate_crc(data)
        print(f"\nOriginal Data with CRC: {data_with_crc}")
        
        # Introduce burst error
        start_pos = len(data) // 2
        error_positions = list(range(start_pos, start_pos + burst_length))
        received_data = self.introduce_error(data_with_crc, error_positions)
        
        print(f"Burst error of length {burst_length} at position {start_pos}")
        print(f"Received Data: {received_data}")
        
        is_valid, remainder = self.verify_crc(received_data)
        
        print(f"\nRemainder: {remainder}")
        if is_valid:
            print("[ERROR] Burst error NOT detected (rare case)")
        else:
            print(f"[OK] Burst error of length {burst_length} detected")
        
        return {
            'burst_length': burst_length,
            'error_positions': error_positions,
            'is_detected': not is_valid,
            'remainder': remainder
        }


def main():
    """Main function to demonstrate CRC simulator with various scenarios."""
    
    print("CRC CODE SIMULATOR")
    print("="*60)
    print("Demonstrating Error Detection and Correction using CRC")
    print("="*60)
    
    # Initialize simulator with CRC-3 polynomial
    simulator = CRCSimulator(polynomial="1101")
    
    # Scenario 1: Error-free transmission
    print("\n\nSCENARIO 1: Error-Free Transmission")
    print("-"*60)
    simulator.demonstrate_transmission("1011001", error_positions=None)
    
    # Scenario 2: Single bit error
    print("\n\nSCENARIO 2: Single Bit Error")
    print("-"*60)
    simulator.demonstrate_transmission("1011001", error_positions=[2])
    
    # Scenario 3: Multiple bit errors
    print("\n\nSCENARIO 3: Multiple Bit Errors")
    print("-"*60)
    simulator.demonstrate_transmission("1011001", error_positions=[1, 4, 6])
    
    # Scenario 4: Burst error detection
    print("\n\nSCENARIO 4: Burst Error Detection")
    print("-"*60)
    simulator.burst_error_detection("1011001", burst_length=3)
    
    # Scenario 5: Different polynomial (CRC-4)
    print("\n\nSCENARIO 5: Using Different Polynomial (CRC-4)")
    print("-"*60)
    simulator_crc4 = CRCSimulator(polynomial="10011")
    simulator_crc4.demonstrate_transmission("1101011011", error_positions=[3, 7])
    
    print("\n" + "="*60)
    print("DEMONSTRATION COMPLETE")
    print("="*60)


if __name__ == "__main__":
    main()
