import sys
import requests

# Contact lists
clients = []
suppliers = []

def search_cep():
    while True:
        cep = input("Enter the ZIP code to search (Brazilian CEP): ")
        url = f"https://viacep.com.br/ws/{cep}/json/"

        response = requests.get(url=url)
        status_code = response.status_code

        if status_code == 400:
            print("Error. Make sure you are entering only numbers "
                  "and that the ZIP code has exactly 8 digits.")
            continue

        response = response.json()

        if "erro" in response:
            print("Invalid ZIP code. Please try again.")
            continue
        else:
            return response

def apply_function(chosen_function):
    answer = input("Which list do you want to access? 'suppliers' or 'clients': ").lower()
    if answer == "clients":
        return chosen_function(clients)
    elif answer == "suppliers":
        return chosen_function(suppliers)
    else:
        print("Invalid list option. Try again.")
        return None

def menu():
    print("\nOptions Menu:")
    print(""" 
    0 - Exit
    1 - Register new contact
    2 - Edit a contact
    3 - Delete a contact
    4 - Show all registered contacts
    """)
    return input("Choose an option: ")

def register_contact(contact_list):
    contact = {}
    contact["code"] = len(contact_list) + 1  # Starts from 1
    contact["name"] = input("Enter the name: ")
    contact["email"] = input("Enter the email: ")
    contact["phone"] = input("Enter the phone: ")
    contact["address"] = search_cep()
    contact_list.append(contact)
    print("Contact successfully registered!")

def edit_contact(contact_list):
    code = int(input("Enter the code of the contact you want to edit: "))
    index = code - 1  # Adjust because code starts at 1
    if 0 <= index < len(contact_list):
        print("Current contact:", contact_list[index])
        name = input("Enter the new name (leave blank to keep current): ")
        email = input("Enter the new email (leave blank to keep current): ")
        phone = input("Enter the new phone (leave blank to keep current): ")
        address = input("Do you want to change the address? (press any key or leave blank to keep current): ")

        if name:
            contact_list[index]["name"] = name
        if email:
            contact_list[index]["email"] = email
        if phone:
            contact_list[index]["phone"] = phone
        if address:
            contact_list[index]["address"] = search_cep()

        print("Contact updated successfully!")
    else:
        print("Invalid code.")

def delete_contact(contact_list):
    code = int(input("Enter the code of the contact you want to delete: "))
    index = code - 1  # Adjust because code starts at 1
    if 0 <= index < len(contact_list):
        contact_list.pop(index)
        # Update codes after removal
        for i in range(len(contact_list)):
            contact_list[i]["code"] = i + 1  # Starts from 1
        print("Contact deleted successfully!")
    else:
        print("Invalid code.")

def show_contacts(contact_list):
    if contact_list:
        print("\nContact List:")
        for contact in contact_list:
            address = contact.get('address', {})
            print(f"""
- Code: {contact.get('code')}
- Name: {contact.get('name')}
- Email: {contact.get('email')}
- Phone: {contact.get('phone')}
- Address:
    Street: {address.get('logradouro')}
    Neighborhood: {address.get('bairro')}
    City: {address.get('localidade')}
    State: {address.get('uf')}
    ZIP Code: {address.get('cep')}
""")
    else:
        print("No contacts registered.")

# Main loop
while True:
    option = menu()

    if option == "0":
        print("Exiting the program.")
        break
    elif option == "1":
        apply_function(register_contact)
    elif option == "2":
        apply_function(edit_contact)
    elif option == "3":
        apply_function(delete_contact)
    elif option == "4":
        apply_function(show_contacts)
    else:
        print("Invalid option.")
