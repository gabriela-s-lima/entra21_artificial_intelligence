contacts = []  # List to store all contacts

def show_menu():
    # Display the menu options to the user
    print("\nMENU OPTIONS:")
    print("""
           1 - Create new contact
           2 - Edit a contact
           3 - Delete a contact
           4 - Show all contacts
           5 - Exit
          """)

def create_contact():
    # Prompt user to enter contact details and add the new contact to the list
    name = input("Enter name: ")
    email = input("Enter e-mail: ")
    phone = input("Enter phone: ")
    
    contact = {
        "name": name,
        "email": email,
        "phone": phone
    }
    
    contacts.append(contact)  # Add contact dictionary to contacts list
    print("Contact created successfully!")

def show_contacts():
    # Display all contacts in the list with their corresponding codes
    if contacts:
        print("\nContact List:")
        for idx, contact in enumerate(contacts):
            print(f"Code: {idx + 1} - Name: {contact['name']} | E-mail: {contact['email']} | Phone: {contact['phone']}")
    else:
        print("No contacts registered.")

def edit_contact():
    # Allow user to edit an existing contact by selecting its code
    show_contacts()
    if not contacts:
        return  # No contacts to edit
    
    try:
        code = int(input("Enter the contact code to edit: ")) - 1  # Adjust for zero-based index
        if 0 <= code < len(contacts):
            contact = contacts[code]
            print(f"Current contact: Name: {contact['name']} | Email: {contact['email']} | Phone: {contact['phone']}")
            
            # Ask for new values or keep the old ones if input is blank
            name = input("Enter the new name (or leave blank to keep the same): ")
            email = input("Enter the new e-mail (or leave blank to keep the same): ")
            phone = input("Enter the new phone (or leave blank to keep the same): ")
            
            if name:
                contact["name"] = name
            if email:
                contact["email"] = email
            if phone:
                contact["phone"] = phone
                
            print("Contact updated successfully!")
        else:
            print("Invalid code.")
    except ValueError:
        print("Please enter a valid number.")

def delete_contact():
    # Allow user to delete a contact by selecting its code
    show_contacts()
    if not contacts:
        return  # No contacts to delete
    
    try:
        code = int(input("Enter the contact code to delete: ")) - 1  # Adjust for zero-based index
        if 0 <= code < len(contacts):
            deleted = contacts.pop(code)  # Remove the contact from the list
            print(f"Contact {deleted['name']} deleted successfully!")
        else:
            print("Invalid code.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    # Main loop to show the menu and handle user choices
    while True:
        show_menu()
        option = input("Choose an option (enter only the number): ")
        
        if option == "1":
            create_contact()
        elif option == "2":
            edit_contact()
        elif option == "3":
            delete_contact()
        elif option == "4":
            show_contacts()
        elif option == "5":
            print("Exiting program. Bye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
