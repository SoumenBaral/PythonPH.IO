import random
class Account:
    accounts = []
    def __init__(self,name,email,address,type) -> None:
        self.name = name 
        self.email = email
        self.address = address
        self.type = type
        self.balance = 0
        self.ID = random.randint(1000,9999)
        Account.accounts.append(self)

    def withdraw(self,amount):
        if amount >= 0 and amount >= self.balance:
            self.balance -= amount
            print(f'\n After withdrawing ${amount} , your current Balance is : {self.balance}\n')
        else:
            print("\n Withdrawal amount exceeded \n")

    def Deposit(self,amount):
        self.balance += amount
        print(f'\n After Deposit ${amount} , your current Balance is : {self.balance}\n')
    
    def AvailableBalance(self):
        print(f'\n Current Balance is : {self.balance} \n')
        