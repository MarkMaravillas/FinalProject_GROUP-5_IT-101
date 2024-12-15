PIN = []
USERNAME_LIST = []
accounts = {} 

while True:
    print(f"""Choose an option:
    1 - Register
    2 - Sign in
    3 - Log Out""")
    
    User_Input = input("\nEnter an option: ")

    if User_Input == "1":
        print(f'You have selected "Register" option.')
        print("\nPlease Register a Username and a Pin.")
        username = input("\nEnter A Username: ")

        if username in USERNAME_LIST:
            print("Invalid, username already exists.")
            continue

        while True:
            pin = input("Enter A 6-digit Pin: ")

            if not pin.isdigit():
                print("Pin must only contain numbers.")
            elif len(pin) != 6:
                print("Invalid Pin, must contain exactly 6 digits.")
            else:
                USERNAME_LIST.append(username)
                PIN.append(pin)
                accounts[username] = {'CHECKINGS': 0, 'SAVINGS': 0}  
                print(f"Registration Complete! Welcome, {username}.")
                break

    elif User_Input == "2":
        username = input("Please Enter your USERNAME: ")

        if username not in USERNAME_LIST:
            print("Username does not exist. Please register first.")
            continue

        pin = input("Please Enter your PIN: ")

        if pin in PIN and PIN[USERNAME_LIST.index(username)] == pin:
            print(f"Welcome back, {username}!")
        else:
            print("Invalid PIN. Please try again.")
            continue
        
        while True:
            options = input("Please select an option ('1' for CHECKINGS, '2' for SAVINGS): ")

            if not options.isdigit():
                print("Error: Please enter a numeric option.")
                continue

            if options == '1' or options == '2':
                account_type = 'CHECKINGS' if options == '1' else 'SAVINGS'
                print(f"You selected {account_type}.")
                break
            else:
                print("Error: Invalid option. Please select only between '1' or '2'.")
                continue

        for _ in range(1):  
            print("\nSelect an operation:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check balance")
            print("4. Log out")

            operation = input("Please select an option (1, 2, 3, or 4): ")

            if operation == '1':
                amount = float(input(f"Enter the amount to deposit into your {account_type} account: "))
                if amount <= 0:
                    print("Error: Deposit amount must be positive.")
                else:
                    accounts[username][account_type] += amount
                    print(f"Successfully deposited {amount} into your {account_type} account.")
                    print(f"New {account_type} balance: {accounts[username][account_type]}")

            elif operation == '2':
                amount = float(input(f"Enter the amount to withdraw from your {account_type} account: "))
                if amount <= 0:
                    print("Error: Withdrawal amount must be positive.")
                elif amount > accounts[username][account_type]:
                    print("Error: Insufficient balance.")
                else:
                    accounts[username][account_type] -= amount
                    print(f"Successfully withdrew {amount} from your {account_type} account.")
                    print(f"New {account_type} balance: {accounts[username][account_type]}")

            elif operation == '3':
                print(f"Your {account_type} account balance is: {accounts[username][account_type]}")

            elif operation == '4':
                print("Logging out. Thank you and Goodbye!")
                break

            else:
                print("Invalid option. Please choose between 1, 2, 3, or 4.")
        
    elif User_Input == "3":
        print("Logging out. Thank you and Goodbye!")
        break

    else:
        print("Invalid option. Please choose a valid option (1, 2, or 3).")