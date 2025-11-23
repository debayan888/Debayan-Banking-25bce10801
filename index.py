import random
import time

ac_list = []



def find_ac(acno):
    
    """Finds account by number."""
    for ac in ac_list:
        if ac['id'] == acno:
            return ac 
    return None 

def safe_input(txt, type, tries = 3):
    """Gets input safely with retries."""
    for i in range(tries):
        try:
            inp = input(txt).strip()
            
            if type == float:
                val = float(inp)
                if val <= 0:
                    print("Error: Amount must be > 0.")
                    continue
                return val
            
            return type(inp)
        
        except ValueError:
            print(f"Error: Wrong input format.")
            if i < tries - 1:
                print(f"Try again. {tries - 1 - i} tries left.")
            else:
                print("Failed. Restarting transaction.")
    return None  

def login():
    """Checks ID and PIN."""
    print("\n--- Login ---")
    
    # Get ID
    acno = safe_input("Enter Account No (4 digit): ", str)
    if acno is None: 
        return None

    # Find account
    ac = find_ac(acno)
    if ac is None:
        print("Error: Account not found.")
        return None

    # Get PIN
    p = safe_input("Enter PIN (4 digit): ", str)
    if p is None: 
        return None
    
    # Match PIN
    if ac['pin'] == p:
        print(f"Success! Welcome, {ac['name']}.")
        return ac
    else:
        print("Error: Wrong PIN.")
        return None

def new_ac():
    """Makes a new account."""
    print("\n--- New Account ---")
    
    nm = input("Enter Name: ")
    if not nm: 
        return print("Failed.")
    
    print("Min balance is ₹ 500.00")
    bal=0
    bal = safe_input("Enter Deposit: ₹", float)
    if not bal or bal < 500:
        return print("Failed.")
    
    p = input("Set 4-digit PIN: ").strip()
    if len(p) != 4 or not p.isdigit():
        print("Error: PIN must be 4 digits.")
        return print("Failed.")
    
    """Generates a unique 4-digit account number."""
    while True:
        num = str(random.randint(1000, 9999))
        
        # Check if ID is unique
        if not find_ac(num):
            id = num
            break
        
    data = {"id": id,"pin": p,"name": nm,"bal": bal}
    
    ac_list.append(data)
    
    print("\nCreated!")
    print(f"Ac No: {id}")
    print(f"Name: {nm}")
    print(f"Bal: ₹ {bal:,.2f}")

def show_bal():
    """Shows balance."""
    ac = login()
    if ac is not None:
        print("\n--- Balance Info ---")
        print(f"Name: {ac['name']}")
        print(f"Ac No: {ac['id']}")
        print(f"Balance: ₹ {ac['bal']:,.2f}")
        
def add_money():
    """Deposit money."""
    ac = login()
    if ac is None: return print("Failed.")
    
    print(f"\n--- Deposit to {ac['id']} ---")
    
    amt = safe_input("Amount to add: ₹", float)
    if amt is None: return print("Failed.")
    
    ac['bal'] += amt
    print(f"\nDone. Added ₹ {amt:,.2f}.")
    print(f"New Bal: ₹ {ac['bal']:,.2f}")

def wdraw():
    """Withdraw money."""
    ac = login()
    if ac is None: return print("Failed.")
    
    print(f"\n--- Withdraw from {ac['id']} ---")
    
    amt = safe_input("Amount to take: ₹", float)
    if amt is None: return print("Failed.")
    
    if amt > ac['bal']:
        print("Error: Not enough money.")
        print(f"Bal is: ₹ {ac['bal']:,.2f}")
        return print("Failed.")
        
    ac['bal'] -= amt
    print(f"\nDone. Took ₹ {amt:,.2f}.")
    print(f"New Bal: ₹ {ac['bal']:,.2f}")

def trans():
    """Transfer money."""
    me = login()
    if me is None: return print("Failed.")
    
    print(f"\n--- Transfer from {me['id']} ---")
    
    other_no = input("To Account No: ").strip()
    other = find_ac(other_no)
    
    if other is None:
        return print("Error: Receiver not found.")
    
    if me['id'] == other['id']:
        return print("Error: Can't send to self.")

    amt = safe_input("Amount to send: ₹", float)
    if amt is None: return print("Failed.")

    if amt > me['bal']:
        print("Error: Not enough money.")
        return print("Failed.")

    #Money transfer process (+ on receiver, - on sender)
    me['bal'] -= amt
    other['bal'] += amt
    
    #Print the account transfer details and money transfer confirmation
    print("\nSent Successfully.")
    print(f"Amount: ₹ {amt:,.2f}")
    print(f"To: {other['name']}")
    print(f"My New Bal: ₹ {me['bal']:,.2f}")


def main():
    while True:
        print()
        print("="*40)
        print("             BANKING SYSTEM         ")
        print("="*40)
        print("Welcome to the Customer Banking Services!")
        print("-"*40)
        print("Please choose an option below:")
        print("-"*40)
        print("1. New Account")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer")
        print("6. Exit")
        print("-" * 30)

        opt = input("Choose (1-6): ").strip()
        
        if opt == '1':
            new_ac()
        elif opt == '2':
            show_bal()
        elif opt == '3':
            add_money()
        elif opt == '4':
            wdraw()
        elif opt == '5':
            trans()
        elif opt == '6':
            print("\nBye! Good to see you and have a nice day.")
            break 
        else:
            print("Invalid Choice Please try again!")
            
        if opt in ['1', '2', '3', '4', '5']:
            print("\n")
            time.sleep(1) 

main()