contact = {}

def display_contact():
    print("\nName\t\tContact number")
    print("-" * 30)
    for name, phone in contact.items():
        print(f"{name}\t\t{phone}")

while True:
    print("""
1. Add new contact
2. Search contact
3. Display contacts
4. Edit contact
5. Delete contact
6. Exit
""")

    choice = input("Enter your choice: ").strip()

    # 1. Add
    if choice == "1":
        name = input("Enter the contact name: ").strip()
        phone = input("Enter the mobile number: ").strip()
        contact[name] = phone
        print("Contact added successfully.")

    # 2. Search
    elif choice == "2":
        search_name = input("Enter the contact name: ").strip()
        if search_name in contact:
            print(f"{search_name}'s contact number is: {contact[search_name]}")
        else:
            print("Name is not found in contact book!")

    # 3. Display
    elif choice == "3":
        if not contact:
            print("Contact book is empty.")
        else:
            display_contact()

    # 4. Edit
    elif choice == "4":
        edit_name = input("Enter the contact name to edit: ").strip()
        if edit_name in contact:
            new_phone = input("Enter new mobile number: ").strip()
            contact[edit_name] = new_phone
            print("Contact updated successfully.")
            display_contact()
        else:
            print("Name is not found in contact book!")

    # 5. Delete
    elif choice == "5":
        del_name = input("Enter the contact name to delete: ").strip()
        if del_name in contact:
            confirm = input("Are you sure? (y/n): ").lower()
            if confirm == "y":
                contact.pop(del_name)
                print("Contact deleted.")
            display_contact()
        else:
            print("Name is not found in contact book!")

    # 6. Exit
    elif choice == "6":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
