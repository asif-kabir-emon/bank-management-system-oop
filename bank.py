from user import User

class Bank:
    def __init__(self, name):
        self.name = name
        self.__users = []
        self.__loans = {}
        self.__loan_feature = True
        self.__is_bankrupt = False
    
    def generate_account_number(self):
        account_number = 1000000000 + len(self.__users) + 1
        return str(account_number)
    
    def add_new_user(self, user):
        self.__users.append(user)
        
    def create_user(self, name, email, address, account_type):
        account_number = self.generate_account_number()
        user = User(name, email, address, account_type, account_number)
        self.add_new_user(user)
        print(f"Account created successfully. Account number: {account_number}")
        return user
    
    def delete_user(self, account_number):
        for user in self.__users:
            if user.account_number == account_number:
                self.__users.remove(user)
                print(f"Account with account number {account_number} has been deleted")
                return
        print("Account not found")
    
    def view_users(self):
        if len(self.__users) == 0:
            print("No User Account!!!")
        else:
            for user in self.__users:
                print(f"---- Account number: {user.account_number} ----")
                print(f"Name: {user.name} \nAccount number: {user.account_number} \nAccount type: {user.account_type} \nBalance: {user.check_balance()} \nEmail: {user.email} \nAddress: {user.address}")
    
    def total_available_balance(self):
        total = 0
        for user in self.__users:
            total += user.check_balance()
        return total
    
    def total_loan_amount(self):
        total = 0
        for loan in self.__loans.values():
            for item in loan:
                total += item["loan_amount"]
        return total
    
    def toggle_loan_feature(self):
        self.__loan_feature = not self.__loan_feature
        if self.__loan_feature:
            print("Loan feature is now enabled.")
        else:
            print("Loan feature is now disabled.")
    
    def check_account(self, account_number):
        for user in self.__users:
            if user.account_number == account_number:
                return user
        return None
    
    def check_loan_feature(self):
        return self.__loan_feature
    
    def check_bankruptcy(self):
        return self.__is_bankrupt
    
    def change_bankruptcy_status(self):
        self.__is_bankrupt = not self.__is_bankrupt
        if self.__is_bankrupt:
            print("Bank is now bankrupt")
        else:
            print("Bank is now out of bankruptcy")
    
    def request_loan(self, user, amount):
        if self.__loan_feature:
            # { user_account_number: [ {loan_amount: 1}  ] }
            have_already_loan = self.__loans.get(user.account_number)
            
            if have_already_loan:
                if len(have_already_loan) > 2:
                    print("You have already taken the maximum number of loans.")
                    return False
                else:
                    self.__loans[user.account_number].append({"loan_amount": amount})
                    return True
            else:
                self.__loans[user.account_number] = [{"loan_amount": amount}]
                return True
            
        else:
            print("Loan feature is disabled")