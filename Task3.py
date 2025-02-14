class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ₱{amount}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ₱{amount}")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")
    
    def display_balance(self):
        print(f"Account Balance: ₱{self.balance}")
# Creating a bank account object
account = BankAccount("123456789", "Asher James", 1000)
# Performing transactions
account.deposit(500)  # Deposit ₱500
account.withdraw(200)  # Withdraw ₱200
account.withdraw(1500)  # Attempt to withdraw more than balance
account.display_balance()  # Display the account balance