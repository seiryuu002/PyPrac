class Account:

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print('Money Deposited...')
        print('Current Available balance: {}'.format(self.balance))

    def withdraw(self, amount):
        if (self.balance - amount) < 0:
            print("Sorry you don't have enough balance...")
        else:
            self.balance -= amount
            print('Cash withdrawn...')
            print('Current Available balance: {}'.format(self.balance))
    
    def __str__(self):
        return f'Account Owner: {self.owner} \nAccount balance: {self.balance}'

account1 = Account('Apurv', 3408)

print('\n'*2)
print(account1)

account1.deposit(1000)
account1.withdraw(2500)
account1.withdraw(3000)
