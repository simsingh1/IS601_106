# Name - Simranjit Singh
# UCID - ss2267
# Date - 17th Feb 2024

# Define the BankAccount class
class BankAccount:
    def __init__(self, account_number, balance, account_holder):
        self.account_number = account_number
        self.balance = balance
        self.account_holder = account_holder

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance

# Create an instance of BankAccount
account = BankAccount(account_number=12345, balance=1000, account_holder='John Doe')
# Perform deposit and withdraw operations
account.deposit(200)  # Deposit amount
account.withdraw(700)  # Withdraw amount
# Print the current balance
print(f"Total Balance (BankAccount): \n{account.get_balance()}")

# Define the CheckingAccount class
class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, account_holder, transaction_fees):
        super().__init__(account_number, balance, account_holder)
        self.transaction_fees = transaction_fees

    def apply_transaction_fees(self):
        self.balance -= self.transaction_fees

# Create an instance of CheckingAccount
checking_account = CheckingAccount(account_number=67890, balance=1000, account_holder='Alice Smith', transaction_fees=34.50)
# Apply transaction fees
checking_account.apply_transaction_fees()
# Print the current balance after transaction fees
print(f"Total Balance (CheckingAccount): \n{checking_account.get_balance()}")

# Define the SavingsAccount class
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, account_holder, interest_rate):
        super().__init__(account_number, balance, account_holder)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest

# Create an instance of SavingsAccount
savings_account = SavingsAccount(account_number=24680, balance=1000, account_holder='Bob Brown', interest_rate=0.12)
# Calculate and apply interest
savings_account.calculate_interest()
# Print the current balance after applying interest
print(f"Total Balance (SavingsAccount): \n{savings_account.get_balance()}")
