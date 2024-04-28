from bank import Bank

class User:
    def __init__(self, name, email, address, account_type, account_number):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.__balance = 0
        self.account_number = account_number
        self.__transaction_history = []
        self.__loan_attempts = 0
        self.__loan_taken = 0
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transaction_history.append(f"Deposit: +{amount}")
            return f"Deposit successful. \nCurrent balance: {self.__balance}"
        else:
            print("Invalid amount!!!")
            return None
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Withdrawal amount exceeded")
            return None
        else:
            self.__balance -= amount
            self.__transaction_history.append(f'Withdrawal: -{amount}')
            return f"Withdrawal successful. \nCurrent balance: {self.__balance}"

    def check_balance(self):
        return self.__balance
    
    def check_transaction_history(self):
        for transaction in self.__transaction_history:
            print(transaction)
    
    def send_money(self, Bank, amount, recipient_account_number):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            recipient = Bank.check_account(recipient_account_number)
            if recipient:
                recipient.deposit(amount)
                self.__balance -= amount
                self.__transaction_history.append(f"Sent {amount} to {recipient.name}")
                recipient.__transaction_history.append(f"Received {amount} from {self.name}")
            else:
                print("Account does not exist")
    
    def request_loan(self, Bank, amount):
        is_loan_feature_enabled = Bank.check_loan_feature()
        if is_loan_feature_enabled:
            if self.__loan_attempts < 2:
                loan = Bank.request_loan(self, amount)
                if loan:
                    self.__loan_taken += amount
                    self.__balance += amount
                    self.__transaction_history.append(f'Loan Taken: +{amount}')
                    self.__loan_attempts += 1
                    print(f"Loan request approved. \nCurrent balance: {self.__balance}")
                    return
                else:
                    print("Loan request denied.")
                    return
            else:
                print("You have already taken the maximum number of loans.")
        else:
            print("Loan feature is disabled.")
    