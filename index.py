details = []

def create_account():
    global account
    name = input("Enter your ID registered name: ")
    deposit = float(input("Enter deposit amount: "))
    pin = input("Set a 4-digit PIN for your account: ")
    if len(details) != 0:
        ac = details[len(details)-1]['account'] + 1
    else:
        ac=1000
    account = {'name': name,'account':ac,'balance': deposit, 'pin':pin}
    details.append(account)
    print(f"Account created successfully for {name} having account number {ac} with balance Rs.{deposit:.2f}")

def view_balance(ac):
    if not details:
        print("No accounts found. Please create an account first.")
        return
    pin = input("Enter your 4-digit PIN: ")
    for acc in details:
        if acc['account'] == ac and pin==acc['pin']:
            print(f"Account Balance for {acc['name']}: Rs.{acc['balance']:.2f}")
            return
    print("Account not found.")
def show_accounts():
    print(details)

def transfer_funds():
    if not details:
        print("No accounts found. Please create an account first.")
        return
    ac = int(input("Enter your account number: "))
    pin = input("Enter your 4-digit PIN: ")
    for acc in details:
        if acc['account'] == ac and pin==acc['pin']:
            to_ac = int(input("Enter recipient's account number: "))
            if to_ac == ac:
                print("Cannot transfer to the same account.")
                #to_ac = int(input("Enter recipient's account number: "))
                continue
            amount = float(input("Enter amount to transfer: "))
            if acc['balance'] >= amount:
                for rec_acc in details:
                    print(f"Recipient Name: {rec_acc['name']}")
                    chs = input("Confirm name? (yes/no): ")
                    chs = chs.lower().strip()
                    if chs == 'yes':
                        acc['balance'] -= amount
                        rec_acc['balance'] += amount
                        print(f"Transferred Rs.{amount:.2f} from account {ac} to account {to_ac}.")
                        print(f"New balance for account {ac}: Rs.{acc['balance']:.2f}")
                    else:
                        print("Transfer cancelled by user.")
                    return
                print("Recipient account not found.")
                    
                return
            else:
                print("Insufficient balance.")
                return
    print("Account not found. or incorrect PIN.")



while True:
    print("----------------------------------------------------------------------------------------")
    print("Welcome to the Banking Page!")
    print("Here you can manage your bank accounts and view transactions.")
    print("Please choose an option from the menu below:")
    print("1. Create New Account")    
    print("2. View Account Balance")
    print("3. Transfer Funds")
    print("4. Exit")
    ch=input("Enter your choice (1-4): ")
    if ch=='1':
        create_account()
    elif ch=='2':
        ac=int(input("Enter your account number: "))
        view_balance(ac)
    elif ch=='3':
        transfer_funds()
    elif ch=='4':
        print("Exiting Banking Page. Have a great day!")
        break
    elif ch=='show':
        show_accounts()
    else:
        print("Invalid choice. Please try again; if you want to exit press 4")

