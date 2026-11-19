import os

FILE_NAME = "contacts.txt"

def load_contacts():
    contacts = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()
                if "," in line:
                    name, phone = line.split(",", 1)
                    contacts[name] = phone
    return contacts

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name},{phone}\n")

def contact_book():
    contacts = load_contacts()

    while True:
        print("\n====================================")
        print("        PYTHON CONTACT BOOK         ")
        print("====================================")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Phone Number")
        print("5. Delete Contact")
        print("6. Exit")
        print("------------------------------------")

        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            name = input("\nEnter Name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            if name in contacts:
                print("Contact already exists! Use Option 4 to update.")
            else:
                phone = input("Enter 10-digit Phone Number: ").strip()
                if phone.isdigit() and len(phone) == 10:
                    contacts[name] = phone
                    save_contacts(contacts)
                    print(f"Contact '{name}' saved!")
                else:
                    print("Invalid phone number. Please enter 10 digits.")

        elif choice == '2':
            print("\n--- ALL CONTACTS ---")
            if not contacts:
                print("Contact book is empty.")
            else:
                for name, phone in sorted(contacts.items()):
                    print(f"{name:<20} : {phone}")

        elif choice == '3':
            query = input("\nEnter name to search: ").strip().lower()
            found = False
            for name, phone in contacts.items():
                if query in name.lower():
                    print(f"Found -> {name}: {phone}")
                    found = True
            if not found:
                print("No matching contact found.")

        elif choice == '4':
            name = input("\nEnter exact name to update: ").strip()
            if name in contacts:
                new_phone = input("Enter new 10-digit Phone Number: ").strip()
                if new_phone.isdigit() and len(new_phone) == 10:
                    contacts[name] = new_phone
                    save_contacts(contacts)
                    print(f"Updated '{name}' successfully!")
                else:
                    print("Invalid phone number.")
            else:
                print("Contact not found.")

        elif choice == '5':
            name = input("\nEnter exact name to delete: ").strip()
            if name in contacts:
                del contacts[name]
                save_contacts(contacts)
                print(f"Deleted '{name}' successfully!")
            else:
                print("Contact not found.")

        elif choice == '6':
            print("\nContacts saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    contact_book()