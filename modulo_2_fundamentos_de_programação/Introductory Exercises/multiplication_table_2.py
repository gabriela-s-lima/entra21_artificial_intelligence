# Asks the user to enter a number
number = int(input("Enter a number: "))

# Displays the multiplication table for the entered number
print(f"\nMultiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


