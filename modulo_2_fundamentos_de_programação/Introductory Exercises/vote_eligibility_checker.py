# Asks the user to enter their age
age = int(input("Enter your age: "))

# Checks the age group and informs the type of voting right
if 16 <= age < 18:
    print("Eligible to vote (Optional Voting)")
elif 18 <= age < 60:
    print("Eligible to vote (Mandatory Voting)")
elif age >= 60:
    print("Eligible to vote (Optional Voting)")
else:
    print("Not eligible to vote (below minimum voting age)")
