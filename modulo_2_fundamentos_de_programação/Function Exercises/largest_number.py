# Program to find the largest number between two numbers using a function

def largest_number(num1, num2):
    # Check which number is greater
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "The numbers are equal."

# Input from the user
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))

# Call the function and display the result
result = largest_number(n1, n2)
print(f"The largest number is: {result}")
