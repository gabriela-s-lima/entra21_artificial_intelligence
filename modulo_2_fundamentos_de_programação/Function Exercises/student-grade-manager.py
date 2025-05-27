# Student Grade Manager

# Dictionary to store student names and their grades
grades = {}

# Menu function
def menu():
    print("""
          1 - Register grades
          2 - Show all grades
          3 - Calculate averages
          4 - Exit
          """)

# Function to register student grades
def register_grades():
    student = input("Enter the student's name: ")
    grade1 = float(input("Enter the first grade: "))
    grade2 = float(input("Enter the second grade: "))
    grade3 = float(input("Enter the third grade: "))
    grade4 = float(input("Enter the fourth grade: "))
    
    # Save grades into the dictionary
    grades[student] = {
        "grade1": grade1,
        "grade2": grade2,
        "grade3": grade3,
        "grade4": grade4
    }
    print(f"Grades successfully registered for {student}!")

# Function to display all registered grades
def show_grades():
    if not grades:
        print("No grades registered yet.")
    else:
        for i, (student, info) in enumerate(grades.items(), start=1):
            print(f"\n{i}. {student}")
            print(f"   Grades: {info['grade1']}, {info['grade2']}, {info['grade3']}, {info['grade4']}")

# Function to calculate average grades and check if the student passed
def calculate_averages():
    if not grades:
        print("No grades registered yet.")
    else:
        for student, info in grades.items():
            total = info['grade1'] + info['grade2'] + info['grade3'] + info['grade4']
            average = total / 4
            average = round(average, 2)

            if average < 7.0:
                print(f"Average {average}. Student {student} FAILED.")
            else:
                print(f"Average {average}. Student {student} PASSED.")

# Main program loop
while True:
    menu()
    option = input("Choose an option: ")

    if option == "1":
        register_grades()

    elif option == "2":
        show_grades()

    elif option == "3":
        calculate_averages()

    elif option == "4":
        print("Exiting the system.")
        break

    else:
        print("Invalid option. Please try again.")
