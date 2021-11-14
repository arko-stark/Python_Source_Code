class Account():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance = self.balance+amount
    def withdrawl(self,amount):
        if self.balance < amount :
            print('Insufficient Balance')
        else :
            self.balance = self.balance-amount

myacc1 = Account('Arko',800)
myacc1.deposit(200)
print(myacc1.balance)
myacc1.withdrawl(10000)
print(myacc1.balance)