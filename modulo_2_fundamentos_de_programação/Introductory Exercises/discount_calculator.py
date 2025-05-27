# Ask the user for the purchase amount and apply a discount based on the amount.
purchase_amount = float(input("Enter the purchase amount: "))

# If the amount is less than $100, no discount applies
if purchase_amount < 100:
    print("No discount applies.")
    print("Total amount: $ ", purchase_amount)
    exit()

# Apply discount based on the purchase range
if  100 <= purchase_amount < 200:
    discount = 0.05

elif 200 <= purchase_amount < 500: 
    discount = 0.1

else:
    discount = 0.2
total_amount = purchase_amount - (purchase_amount*discount)
print ("Purchase amount: $ ", purchase_amount)
print ("Discount amount: $ ", purchase_amount*discount)
print ("Total amount with discount: $ ", total_amount)
