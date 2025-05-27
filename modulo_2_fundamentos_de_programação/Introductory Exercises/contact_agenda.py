contacts = [] # List to store all contacts

while True: 
    # Display menu options
    print ("\nMENU OPTIONS:")
    print (""" 
           1 - Create new contact
           2 - Edit a contact
           3 - Delete a contact
           4 - Show all contacts
           """) 
    option = input("Choose an option (enter only the number): ") # Ask user to choose an option

    if option == "1": 
        # Create a new contact
        name = input("Enter name: ") 
        email = input("Enter e-mail: ") 
        phone = input("Enter phone: ") 

        # Create a contact dictionary with the entered data
        contact = { 
            "name" : name,
            "email" : email,
            "phone" : phone
        }

        # Add the new contact to the contacts list
        contacts.append(contact) 
        

    elif option == "2":
        # Edit an existing contact
        print("\nContact List:")
        # Show all contacts with codes for selection
        for idx, contact in enumerate(contacts):
            print(f"Code: {idx + 1} - Name: {contact['name']} | E-mail: {contact['email']} | Phone: {contact['phone']}")

         # Ask user for the contact code to edit
        code = int(input("Enter the contact code to edit: ")) - 1

        # Get the selected contact
        contact = contacts[code]
        
        # Show current contact information
        print(f"Current contact: Name: {contacts[code]['name']} | Email: {contacts[code]['email']} | Phone: {contacts[code]['phone']}")

        # Ask for new data or keep old if blank  
        name = input("Enter the new name (or leave blank to keep the same): ")
        email = input("Enter the new e-mail (or leave blank to keep the same): ")
        phone = input("Enter the new phone (or leave blank to keep the same): ")

        # Update contact info if new data provided
        if name:
            contacts[code]["name"] = name
        if email:
            contacts[code]["email"] = email
        if phone:
            contacts[code]["phone"] = phone
            
            print("Contact updated successfully!")

        else:
            print("Invalid code")

    elif option == "3":
        # Delete a contact
        code = int(input("Enter the contact code to delete: ")) - 1
        
        # Check if code is valid
        if 0 <= code < len(contacts):
            deleted = contacts.pop(code) # Remove the contact from the list
            print(f"Contact {deleted['name']} deleted successfully!")

        else:
            print("Invalid code.")

    elif option == "4": 
            # Show all contacts
            if contacts:
                print("\nContact List:")
                for idx, contact in enumerate(contacts):
                    print(f"Code: {idx + 1} - Name: {contact['name']} | E-mail: {contact['email']} | Phone: {contact['phone']}")
            else:
                print("No contacts registered.")


 
    
    