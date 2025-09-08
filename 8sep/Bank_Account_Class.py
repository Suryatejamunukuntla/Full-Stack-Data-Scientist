class bankAccount:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if(self.balance<amount):
            print("No Balance")
        else:
            self.balance=self.balance-amount
    def get_balance(self):
        return self.balance
acc=bankAccount(100)

acc.deposit(200)
n1=acc.get_balance()
print("Balance",n1)
acc.withdraw(200)
n2=acc.get_balance()
print("Balance",n2)
