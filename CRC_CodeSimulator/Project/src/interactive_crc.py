"""
Interactive CRC Simulator with Command Line Interface
Allows users to input custom data and test CRC error detection
"""

from crc_simulator import CRCSimulator


def print_menu():
    """Display the main menu."""
    print("\n" + "="*60)
    print("INTERACTIVE CRC SIMULATOR")
    print("="*60)
    print("1. Test with custom data")
    print("2. Test with random data")
    print("3. Change polynomial")
    print("4. Demonstrate burst error detection")
    print("5. View current settings")
    print("6. Run all demo scenarios")
    print("0. Exit")
    print("="*60)


def get_binary_input(prompt):
    """Get valid binary input from user."""
    while True:
        try:
            data = input(prompt).strip()
            if all(bit in '01' for bit in data):
                return data
            else:
                print("Error: Please enter only 0s and 1s")
        except KeyboardInterrupt:
            print("\nOperation cancelled")
            return None


def get_error_positions(data_length):
    """Get error positions from user."""
    while True:
        try:
            positions_input = input(f"Enter error positions (0-{data_length-1}, separated by spaces, or press Enter for none): ").strip()
            if not positions_input:
                return None
            positions = [int(pos.strip()) for pos in positions_input.split()]
            if all(0 <= pos < data_length for pos in positions):
                return positions
            else:
                print(f"Error: Positions must be between 0 and {data_length-1}")
        except ValueError:
            print("Error: Please enter valid numbers")
        except KeyboardInterrupt:
            print("\nOperation cancelled")
            return None


def custom_data_test(simulator):
    """Test CRC with custom user data."""
    print("\n--- Custom Data Test ---")
    data = get_binary_input("Enter binary data: ")
    if data is None:
        return
    
    error_positions = get_error_positions(len(data) + simulator.polynomial_length - 1)
    
    if error_positions is None:
        error_positions = []
    
    result = simulator.demonstrate_transmission(data, error_positions)
    return result


def random_data_test(simulator):
    """Test CRC with randomly generated data."""
    import random
    print("\n--- Random Data Test ---")
    
    length = int(input("Enter data length (8-32 recommended): "))
    data = ''.join(random.choice('01') for _ in range(length))
    print(f"Generated random data: {data}")
    
    # Random errors
    num_errors = int(input("Enter number of random errors to introduce (0-5): "))
    data_with_crc_length = length + simulator.polynomial_length - 1
    error_positions = random.sample(range(data_with_crc_length), min(num_errors, data_with_crc_length))
    
    print(f"Random error positions: {error_positions}")
    result = simulator.demonstrate_transmission(data, error_positions)
    return result


def change_polynomial(simulator):
    """Change the generator polynomial."""
    print("\n--- Change Polynomial ---")
    print("Common polynomials:")
    print("  CRC-3: 1101")
    print("  CRC-4: 10011")
    print("  CRC-8: 100000111")
    print("  CRC-16: 10001000000100001")
    
    new_poly = get_binary_input("Enter new polynomial (binary): ")
    if new_poly:
        simulator.polynomial = new_poly
        simulator.polynomial_length = len(new_poly)
        print(f"Polynomial changed to: {new_poly}")


def burst_error_demo(simulator):
    """Demonstrate burst error detection."""
    print("\n--- Burst Error Detection ---")
    data = get_binary_input("Enter binary data: ")
    if data is None:
        return
    
    burst_length = int(input("Enter burst error length: "))
    result = simulator.burst_error_detection(data, burst_length)
    return result


def view_settings(simulator):
    """Display current simulator settings."""
    print("\n--- Current Settings ---")
    print(f"Generator Polynomial: {simulator.polynomial}")
    print(f"Polynomial Length: {simulator.polynomial_length} bits")
    print(f"Can detect errors up to: {simulator.polynomial_length - 1} bits")


def run_all_demos(simulator):
    """Run all demonstration scenarios."""
    print("\n--- Running All Demo Scenarios ---")
    
    scenarios = [
        ("Error-free transmission", "1011001", None),
        ("Single bit error", "1011001", [2]),
        ("Double bit error", "1011001", [1, 4]),
        ("Multiple bit errors", "1011001", [1, 4, 6]),
    ]
    
    for name, data, errors in scenarios:
        print(f"\n{name.upper()}")
        print("-" * 60)
        simulator.demonstrate_transmission(data, errors)
        input("\nPress Enter to continue to next scenario...")


def main():
    """Main interactive loop."""
    simulator = CRCSimulator(polynomial="1101")
    
    print("Welcome to the Interactive CRC Simulator!")
    print("This tool demonstrates error detection using Cyclic Redundancy Check")
    
    while True:
        print_menu()
        choice = input("Enter your choice (0-6): ").strip()
        
        if choice == '1':
            custom_data_test(simulator)
        elif choice == '2':
            random_data_test(simulator)
        elif choice == '3':
            change_polynomial(simulator)
        elif choice == '4':
            burst_error_demo(simulator)
        elif choice == '5':
            view_settings(simulator)
        elif choice == '6':
            run_all_demos(simulator)
        elif choice == '0':
            print("\nThank you for using the CRC Simulator!")
            break
        else:
            print("Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
