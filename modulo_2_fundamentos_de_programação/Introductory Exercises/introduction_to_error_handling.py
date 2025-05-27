# Infinite loop to keep asking for input until manually stopped
while True:
    try:
        # Asks the user to input the first number
        number_1 = int(input("Enter the first number: "))
        
        # Asks the user to input the second number
        number_2 = int(input("Enter the second number: "))
        
        # Performs the division and displays the result
        print("Result:", number_1 / number_2)

    # Handles division by zero error
    except ZeroDivisionError:
        print("It is not possible to divide by zero.")

    # Handles invalid input when the user does not enter an integer
    except ValueError:
        print("The input is not a valid integer.")

    # Handles any other unexpected errors
    except Exception as error:
        print("Oops, an unexpected error occurred!", error)