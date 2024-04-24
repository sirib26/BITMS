file=open("file.txt","r")
def withdraw(account, amount):
    if amount > account['balance']:
        print("Insufficient funds!")
    elif  account['count']>=3:
        print("transcation limit exceeded")
        
    else:
        account['balance'] -= amount
        account['transactions'].append(f"Withdrawal: ${amount}")
        account['count']+=1
        print(f"Withdrawal successful. Remaining balance: ${account['balance']}")

def deposit(account, amount):
    account['balance'] += amount
    account['transactions'].append(f"Deposit: ${amount}")
    print(f"Deposit successful. Remaining balance: ${account['balance']}")

def get_balance(account):
    return account['balance']

def get_transaction_history(account):
    return account['transactions']

# Create an account dictionary
account = {
    'balance': 1000,
    'transactions': [],
    'count':0
}

# Dictionary to map user choices to functions
choices = {
    '1': deposit,
    '2': withdraw,
    '3': get_balance,
    '4': get_transaction_history
}
details = {
    'user': ['siri','sanjana','uzma'],
    'pass' : ['1','2','3']
}
username = input("enter the username")
passwd = input("enter the password")
if username in details['user'] and passwd and details['pass']:
    print("successful")
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '5':
            print("Exiting program.")
            exit()

        if choice in choices:
            if choice == '1' or choice == '2':
                amount = float(input("Enter amount: "))
                choices[choice](account, amount)
            else:
                print(choices[choice](account))
        else:
            print("Invalid choice. Please try again.")
else:
    print("invalid")
    exit()
