# Asks the user for a number and informs whether it is even or odd.
number = int(input("Enter a number: \n"))

# Checks if the number is divisible by 2.
# If the remainder of the division is 0, the number is even; otherwise, it is odd.
if number % 2 == 0:
    print("The number entered is even")
else:
    print("The number entered is odd")
