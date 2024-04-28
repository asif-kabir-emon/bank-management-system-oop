from bank import Bank
from user import User
from admin import Admin

abc_bank = Bank("ABC Bank")

def Admin_Access():
    admin = Admin()
    print("\nWelcome Admin")
    
    while True:
        print("\n")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. View All Accounts")
        print("4. Total Available Balance")
        print("5. Total Loan Amount")
        print("6. Toggle Loan Feature")
        print("7. Exit")
        
        choice = int(input("\nEnter your choice: "))
        print("\n")
        
        if choice == 1:
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            account_type = "Savings"
            while True:
                account_type_choice = input("Enter account type (1. Savings , 2. Current ) : ")
                if account_type_choice == '1':
                    account_type = "Savings"
                    break
                if account_type_choice == '2':
                    account_type = "Current"
                    break
                else:
                    print("Invalid Account Type!!! Please enter again!\n")
                    
            admin.create_user(abc_bank, name, email, address, account_type)
        
        elif choice == 2:
            account_number = str(input("Enter account number: "))
            admin.delete_user(abc_bank, account_number)
        
        elif choice == 3:
            admin.view_users(abc_bank)
        
        elif choice == 4:
            total = admin.total_available_balance(abc_bank)
            print(f"Total available balance: {total}")
        
        elif choice == 5:
            total = admin.total_loan_amount(abc_bank)
            print(f"Total loan amount: {total}")
        
        elif choice == 6:
            admin.toggle_loan_feature(abc_bank)
        
        elif choice == 7:
            break

def User_Access(user):
    print(f"\nWelcome {user.name}")
    
    while True:
        print("\n")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Check Transaction History")
        print("5. Send Money")
        print("6. Request Loan")
        print("7. Exit")
        
        choice = int(input("\nEnter your choice: "))
        print("\n")
        
        if choice == 1:
            amount = int(input("Enter amount to deposit: "))
            deposit = user.deposit(amount)
            if deposit:
                print(deposit)
        
        elif choice == 2:
            amount = int(input("Enter amount to withdraw: "))
            withdraw = user.withdraw(amount)
            if withdraw:
                print(withdraw)
        
        elif choice == 3:
            balance = user.check_balance()
            print(f"Balance: {balance}")
        
        elif choice == 4:
            user.check_transaction_history()
        
        elif choice == 5:
            amount = int(input("Enter amount to send: "))
            recipient_account_number = str(input("Enter recipient account number: "))
            user.send_money(abc_bank, amount, recipient_account_number)
        
        elif choice == 6:
            amount = int(input("Enter loan amount: "))
            user.request_loan(abc_bank, amount)
        
        elif choice == 7:
            break

while True:
    print("\nWelcome to ABC Bank\n")
    
    print("1. Admin")
    print("2. User")
    print("3. Exit")
    
    choice = int(input("\nEnter your choice: "))
    
    if choice == 1:
        Admin_Access()
    elif choice == 2:
        account_number = str(input("Enter account number: "))
        user = abc_bank.check_account(account_number)
        if user:
            User_Access(user)
        else:
            print("Account not found!!!")
    elif choice == 3:
        break
    else:
        print("Invalid choice!!!")