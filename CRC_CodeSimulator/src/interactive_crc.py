"""
Interactive CRC Simulator - Command Line Interface
Provides an interactive command-line experience for CRC operations
"""

from crc_simulator import CRCSimulator


def print_menu():
    """Display the main menu"""
    print("\n" + "="*60)
    print("INTERACTIVE CRC SIMULATOR")
    print("="*60)
    print("1. Calculate CRC for custom data")
    print("2. Verify data with CRC")
    print("3. Demonstrate transmission with errors")
    print("4. Test burst error detection")
    print("5. Compare different polynomials")
    print("6. Exit")
    print("="*60)


def get_binary_input(prompt):
    """Get valid binary input from user"""
    while True:
        data = input(prompt).strip()
        if not data:
            print("Error: Input cannot be empty")
            continue
        if not all(c in '01' for c in data):
            print("Error: Please enter only 0s and 1s")
            continue
        return data


def get_polynomial_choice():
    """Get polynomial choice from user"""
    print("\nAvailable Polynomials:")
    print("1. CRC-3 (1101)")
    print("2. CRC-4 (10011)")
    print("3. CRC-8 (100000111)")
    print("4. CRC-16 (10001000000100001)")
    
    while True:
        choice = input("Select polynomial (1-4): ").strip()
        if choice == '1':
            return "1101"
        elif choice == '2':
            return "10011"
        elif choice == '3':
            return "100000111"
        elif choice == '4':
            return "10001000000100001"
        else:
            print("Invalid choice. Please enter 1-4")


def calculate_crc_mode():
    """Mode 1: Calculate CRC for custom data"""
    print("\n--- CRC CALCULATION ---")
    data = get_binary_input("Enter binary data: ")
    polynomial = get_polynomial_choice()
    
    simulator = CRCSimulator(polynomial=polynomial)
    data_with_crc, crc_checksum = simulator.calculate_crc(data, show_steps=True)
    
    print(f"\nResult:")
    print(f"Original Data: {data}")
    print(f"CRC Checksum: {crc_checksum}")
    print(f"Transmitted Data: {data_with_crc}")


def verify_crc_mode():
    """Mode 2: Verify data with CRC"""
    print("\n--- CRC VERIFICATION ---")
    data = get_binary_input("Enter received data (with CRC): ")
    polynomial = get_polynomial_choice()
    
    simulator = CRCSimulator(polynomial=polynomial)
    is_valid, remainder = simulator.verify_crc(data, show_steps=True)
    
    print(f"\nResult:")
    print(f"Remainder: {remainder}")
    if is_valid:
        print("[OK] Data is VALID - No errors detected")
    else:
        print("[ERROR] Data is CORRUPTED - Errors detected")


def transmission_mode():
    """Mode 3: Demonstrate transmission with errors"""
    print("\n--- TRANSMISSION DEMONSTRATION ---")
    data = get_binary_input("Enter binary data: ")
    polynomial = get_polynomial_choice()
    
    error_input = input("Enter error positions (space-separated, or press Enter for none): ").strip()
    errors = []
    if error_input:
        try:
            # Convert from 1-based to 0-based indexing
            errors = [int(x) - 1 for x in error_input.split()]
        except ValueError:
            print("Invalid error positions. Proceeding without errors.")
    
    simulator = CRCSimulator(polynomial=polynomial)
    result = simulator.demonstrate_transmission(data, errors, show_steps=True)
    
    print(f"\nTransmission Result:")
    print(f"Original Data: {result['original_data']}")
    print(f"CRC Checksum: {result['crc_checksum']}")
    print(f"Transmitted Data: {result['transmitted_data']}")
    print(f"Received Data: {result['received_data']}")
    print(f"Valid: {'Yes' if result['is_valid'] else 'No'}")


def burst_error_mode():
    """Mode 4: Test burst error detection"""
    print("\n--- BURST ERROR DETECTION ---")
    data = get_binary_input("Enter binary data: ")
    
    while True:
        try:
            burst_length = int(input("Enter burst error length: "))
            if burst_length > 0:
                break
            print("Burst length must be positive")
        except ValueError:
            print("Please enter a valid number")
    
    polynomial = get_polynomial_choice()
    
    simulator = CRCSimulator(polynomial=polynomial)
    result = simulator.burst_error_detection(data, burst_length)
    
    print(f"\nBurst Error Result:")
    print(f"Burst Length: {result['burst_length']}")
    print(f"Error Positions: {result['error_positions']}")
    print(f"Detected: {'Yes' if result['is_detected'] else 'No'}")
    print(f"Remainder: {result['remainder']}")


def compare_polynomials_mode():
    """Mode 5: Compare different polynomials"""
    print("\n--- POLYNOMIAL COMPARISON ---")
    data = get_binary_input("Enter binary data: ")
    
    error_input = input("Enter error positions (space-separated, or press Enter for none): ").strip()
    errors = []
    if error_input:
        try:
            # Convert from 1-based to 0-based indexing
            errors = [int(x) - 1 for x in error_input.split()]
        except ValueError:
            print("Invalid error positions. Proceeding without errors.")
    
    polynomials = [
        ("CRC-3", "1101"),
        ("CRC-4", "10011"),
        ("CRC-8", "100000111"),
        ("CRC-16", "10001000000100001")
    ]
    
    print(f"\nComparing polynomials on data: {data}")
    print(f"Error positions: {errors if errors else 'None'}")
    print("-" * 60)
    
    for name, poly in polynomials:
        simulator = CRCSimulator(polynomial=poly)
        result = simulator.demonstrate_transmission(data, errors, show_steps=False)
        
        print(f"{name} ({poly}):")
        print(f"  CRC: {result['crc_checksum']}")
        print(f"  Valid: {'Yes' if result['is_valid'] else 'No'}")
        print(f"  Remainder: {result['remainder']}")
        print()


def main():
    """Main interactive loop"""
    print("Welcome to Interactive CRC Simulator!")
    print("This tool allows you to explore CRC error detection interactively.")
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            calculate_crc_mode()
        elif choice == '2':
            verify_crc_mode()
        elif choice == '3':
            transmission_mode()
        elif choice == '4':
            burst_error_mode()
        elif choice == '5':
            compare_polynomials_mode()
        elif choice == '6':
            print("\nThank you for using Interactive CRC Simulator!")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-6.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
