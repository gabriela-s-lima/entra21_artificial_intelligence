# Asks for the student's name
name = input("Enter the student's name: ")

# List to store the 4 grades
grades = []

# Loop to collect exactly 4 valid grades
for i in range(1, 5):
    while True:
        try:
            # Asks for each grade with validation
            grade = float(input(f"Enter the {i}st grade for {name}: "))
            
            # Checks if the grade is between 0 and 10
            if 0 <= grade <= 10:
                grades.append(grade)
                break
            else:
                print("Invalid grade. Please enter a value between 0 and 10.")
        
        # Handles invalid input that can't be converted to float
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Calculates the average of the grades
average = sum(grades) / len(grades)

# Determines the student's status
status = "Approved" if average >= 7 else "Failed"

# Displays the result
print("\nStudent's result:")
print(f"Name: {name}")
print(f"Grades: {grades}")
print(f"Average: {average:.2f}")
print(f"Status: {status}")
