class User:
    def __init__ (self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self,amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self,):
        print(self.name)
        print(self.account_balance)
        return self

Mike = User("Michael","mike@gmail.com")
Vinny = User("Vincent","vinny@hotmail.com")
Pauly = User("Paul","paul@gmail.com")

Mike.make_deposit(3000).make_deposit(1000).make_deposit(1000).make_withdrawal(1000).display_user_balance()
Vinny.make_deposit(750).make_deposit(800).make_withdrawal(300).make_withdrawal(450).display_user_balance()
Pauly.make_deposit(9000).make_withdrawal(2000).make_withdrawal(765).make_withdrawal(900).display_user_balance()