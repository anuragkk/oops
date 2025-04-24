class BankAccount:
    def __init__(self, account_holder_name: str, balance: float = 0):
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount
        return self.balance

    def withdraw_money(self, amount: float):
        if amount > self.balance:
            print(f"Error, you don't have sufficient balance : Account_balance {self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")
            return self.balance

    def display_balance(self):
        print(f" your account balance is {self.balance}")


account_1 = BankAccount("paplu")
account_1.deposit_money(amount=5000)
account_1.withdraw_money(amount=2000)
account_1.withdraw_money(10000)
account_1.display_balance()