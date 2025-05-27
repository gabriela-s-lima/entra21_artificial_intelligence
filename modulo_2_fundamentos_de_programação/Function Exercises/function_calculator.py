# High Order Function Calculator

def apply_operation(a, b, operation):
    """
    High-order function that takes two values (a, b) 
    and a function (operation). Applies the operation and returns the result.
    """
    return operation(a, b)


# Basic math operations
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: division by zero!"
    return x / y


# Function to display the menu
def show_menu():
    print("\n--- MENU ---")
    print("0 - Exit")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")


# Main program loop
while True:
    show_menu()
    option = input("Choose an option: ")

    if option == '0':
        print("Exiting the program...")
        break

    # Mapping options to functions (High Order)
    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide
    }

    if option in operations:
        try:
            # Asking for input values
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        chosen_function = operations[option]  # Gets the corresponding function
        result = apply_operation(a, b, chosen_function)
        print(f"Result: {result}")

    else:
        print("Invalid option! Please try again.")
