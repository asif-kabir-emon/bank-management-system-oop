from user import User
from bank import Bank

class Admin:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
    def delete_user(self, Bank, account_number):
        Bank.delete_user(account_number)
    
    def view_users(self, Bank):
        Bank.view_users()
        
    def total_available_balance(self, Bank):
        total = Bank.total_available_balance()
        return total
    
    def total_loan_amount(self, Bank):
        total = Bank.total_loan_amount()
        return total
    
    def toggle_loan_feature(self, Bank):
        Bank.toggle_loan_feature()
        

# admin = Admin()
# abc_bank = Bank("ABC Bank")

# admin.create_user(abc_bank, "John Doe", "joe@gmail.com", "123, Baker Street", "Savings")
# admin.create_user(abc_bank, "Von Doe", "von@gmail.com", "123, Baker Street", "Savings")

# print(admin.total_available_balance(abc_bank))
# print(admin.total_loan_amount(abc_bank))
# admin.toggle_loan_feature(abc_bank)
# admin.toggle_loan_feature(abc_bank)

# print(abc_bank.check_account("10000000013"))

# admin.view_users(abc_bank)