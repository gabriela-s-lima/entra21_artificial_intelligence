# Menu dictionary with dish names as keys and prices as values
menu = {
    "Chicken Milanese": 25.0,
    "Onion Steak": 28.0,
    "Fish Fillet": 30.0,
    "Feijoada": 25.0,  # Brazilian black bean stew
    "Stroganoff": 25.0,
    "Tacacá": 30.0,    # Amazonian soup
    "Vatapá": 28.0,    # Afro-Brazilian seafood dish
    "Maniçoba": 30.0,  # Brazilian traditional dish made from manioc leaves
    "Açaí": 32.0,
    "Juice": 12.0,
    "Water": 5.0
}

# List to store selected dishes' prices
order = []

print("=== MENU: ===")
# Loop through the menu items and print each dish with its price
for dish, price in menu.items():
    print(f"- {dish}: $ {price:.2f}")

while True:
    # Ask the user to type the dish they want or type EXIT to finish
    choice = input("Enter the desired dish or type EXIT to finish: ")

    # If user types 'exit', break the loop and end ordering
    if choice.lower() == "exit":
        break

    # Normalize the input to title case and check if it's in the menu
    if choice.title() in menu:
        # Add the selected dish price to the order list
        order.append(menu[choice.title()])
        print(f"{choice.title()} added to the order.")
    else:
        # Inform the user if the dish does not exist or is unavailable
        print("Dish does not exist or is unavailable.")

# Calculate the total sum of the order
total = sum(order)
print("Total order amount: $", total)
