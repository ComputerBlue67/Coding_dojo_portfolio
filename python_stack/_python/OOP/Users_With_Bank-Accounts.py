class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate=int_rate
        self.balance=balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount 
        else:
            self.balance -= 5 
            print("Insufficient Funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print(f"Balance:${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.int_rate
        return self


class User:
    def __init__ (self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self,):
        self.account.display_account_info()
        return self

Mike = User("michael","michael@gmail.com")
Mike.make_deposit(300).make_deposit(500).make_deposit(400).make_withdrawal(450).display_user_balance()
Mike.make_deposit(4500).account.yield_interest().display_account_info()
Mike.display_user_balance()