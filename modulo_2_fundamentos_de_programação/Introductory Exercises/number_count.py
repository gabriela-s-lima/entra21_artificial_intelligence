sum_numbers = 0  # Initializes the sum
entered_numbers = []  # Initializes the list to store the numbers

# Infinite loop to read numbers until the user enters zero
while True:
    number = int(input("Enter a random number: "))
    if number == 0:  # If the number entered is zero, exit the loop
        break

    entered_numbers.append(number)  # Adds the entered number to the list
    sum_numbers += number  # Adds the entered number to the total sum

# After exiting the loop, displays the total quantity of numbers entered
print("Total number of numbers entered:", len(entered_numbers))

# Displays the complete list of entered numbers
print("Entered numbers:", entered_numbers)

# Displays the total sum of the entered numbers
print(f"The sum of the entered numbers is {sum_numbers}")
