# 11. Bank Class for Managing Customer Accounts and Transactions
# Write a Python program to create a class representing a bank. 
# Include methods for managing customer accounts and transactions.

class Account:
    def __init__(self, customer_name, cash, account_type):
        self.name = customer_name
        self.balance = float(cash)
        self.type = account_type 

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False
        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.balance:
            print(f"Insufficient funds for {self.name}.")
            return False
        self.balance -= amount
        return True


class Bank:
    def __init__(self, account=None):
        self.accounts = {}   # {name: Account}
        self.size = 0
        if account is not None:
            self.add_account(account)

    def add_account(self, account):
        """Add a new account to the bank."""
        if account.name in self.accounts:
            print(f"Account for {account.name} already exists.")
            return False
        self.accounts[account.name] = account
        self.size += 1
        return True

    def close_account(self, name):
        """Remove an account by customer name."""
        if name not in self.accounts:
            print(f"No account found for {name}.")
            return False
        del self.accounts[name]
        self.size -= 1
        return True

    def deposit(self, name, amount):
        """Deposit money into a customer's account."""
        account = self.accounts.get(name)
        if account is None:
            print(f"No account found for {name}.")
            return False
        return account.deposit(amount)

    def withdraw(self, name, amount):
        """Withdraw money from a customer's account."""
        account = self.accounts.get(name)
        if account is None:
            print(f"No account found for {name}.")
            return False
        return account.withdraw(amount)

    def transfer(self, from_name, to_name, amount):
        """Transfer money from one account to another."""
        from_acc = self.accounts.get(from_name)
        to_acc = self.accounts.get(to_name)

        if from_acc is None:
            print(f"No account found for {from_name}.")
            return False
        if to_acc is None:
            print(f"No account found for {to_name}.")
            return False

        if not from_acc.withdraw(amount):
            # withdraw() already prints the error
            return False

        to_acc.deposit(amount)
        return True

    def get_balance(self, name):
        """Return the balance for a customer's account (or None if not found)."""
        account = self.accounts.get(name)
        if account is None:
            print(f"No account found for {name}.")
            return None
        return account.balance

    def print_accounts(self):
        """Display all accounts and balances."""
        if self.size == 0:
            print("No accounts in the bank.")
            return
        for name, acc in self.accounts.items():
            print(f"{name} ({acc.type}) - Balance: ${acc.balance:.2f}")

# if __name__ == "__main__":
acc1 = Account("Alice", 500, "checking")
acc2 = Account("Bob", 1000, "savings")

bank = Bank(acc1)
bank.add_account(acc2)

print("Initial accounts:")
bank.print_accounts()

print("\nDepositing 200 to Alice...")
bank.deposit("Alice", 200)
print("Withdrawing 150 from Bob...")
bank.withdraw("Bob", 150)

print("\nAfter transactions:")
bank.print_accounts()

print("\nTransferring 300 from Alice to Bob...")
bank.transfer("Alice", "Bob", 300)

print("\nFinal state:")
bank.print_accounts()
