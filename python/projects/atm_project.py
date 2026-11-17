def atm_system():
    # Default Account Data
    account = {
        "name": "Aarav Sharma",
        "pin": "1234",
        "balance": 100000.0,
        "transactions": []
    }

    print("====================================")
    print("      WELCOME TO PYTHON BANK ATM    ")
    print("====================================")

    # PIN Verification (3 Attempts)
    attempts = 3
    while attempts > 0:
        entered_pin = input("\nEnter your 4-digit PIN: ")
        if entered_pin == account["pin"]:
            print(f"\nLogin Successful! Welcome, {account['name']}.")
            break
        else:
            attempts -= 1
            print(f"Incorrect PIN. Attempts left: {attempts}")
            if attempts == 0:
                print("Card blocked due to too many failed attempts.")
                return

    # Main ATM Menu
    while True:
        print("\n------------------------------------")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Mini Statement")
        print("5. Change PIN")
        print("6. Exit")
        print("------------------------------------")

        choice = input("Select an option (1-6): ")

        if choice == '1':
            print(f"\nCurrent Balance: ₹{account['balance']:.2f}")

        elif choice == '2':
            try:
                amount = float(input("\nEnter amount to deposit: ₹"))
                if amount > 0:
                    account["balance"] += amount
                    account["transactions"].append(f"Deposited: +₹{amount:.2f}")
                    print(f"₹{amount:.2f} deposited successfully!")
                    print(f"Updated Balance: ₹{account['balance']:.2f}")
                else:
                    print("Invalid amount. Please enter a positive value.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")

        elif choice == '3':
            try:
                amount = float(input("\nEnter amount to withdraw: ₹"))
                if amount <= 0:
                    print("Invalid amount. Please enter a positive value.")
                elif amount > account["balance"]:
                    print("Insufficient balance!")
                else:
                    account["balance"] -= amount
                    account["transactions"].append(f"Withdrawn: -₹{amount:.2f}")
                    print(f"Please collect your cash: ₹{amount:.2f}")
                    print(f"Remaining Balance: ₹{account['balance']:.2f}")
            except ValueError:
                print("Invalid input. Please enter numbers only.")

        elif choice == '4':
            print("\n--- MINI STATEMENT ---")
            if not account["transactions"]:
                print("No transactions yet.")
            else:
                for txn in account["transactions"][-5:]:  # Shows last 5 transactions
                    print(txn)
            print(f"Available Balance: ₹{account['balance']:.2f}")

        elif choice == '5':
            old_pin = input("\nEnter current PIN: ")
            if old_pin == account["pin"]:
                new_pin = input("Enter new 4-digit PIN: ")
                if len(new_pin) == 4 and new_pin.isdigit():
                    account["pin"] = new_pin
                    print("PIN changed successfully!")
                else:
                    print("PIN must be exactly 4 digits.")
            else:
                print("Incorrect current PIN.")

        elif choice == '6':
            print("\nThank you for using Python Bank ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please select between 1 and 6.")

if __name__ == "__main__":
    atm_system()