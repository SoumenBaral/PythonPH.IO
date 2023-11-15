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
        self.Transaction = []
        Account.accounts.append(self)


    def withdraw(self,amount):
        if amount >= 0 and amount >= self.balance:
            self.balance -= amount
            resit = {"Withdraw" : amount ,"CurrentBalance":self.balance }
            self.Transaction.append(resit)
            print(f'\n After withdrawing ${amount} , your current Balance is : {self.balance}\n')
        else:
            print("\n Withdrawal amount exceeded \n")

    def Deposit(self,amount):
        self.balance += amount
        resit = {"Deposit" : amount ,"CurrentBalance":self.balance }
        self.Transaction.append(resit)
        print(f'\n After Deposit ${amount} , your current Balance is : {self.balance}\n')
    
    def AvailableBalance(self):
        print(f'\n Current Balance is : {self.balance} \n')

    def TransactionHistory(self):
       for trans in self.Transaction:
           for key, value in trans.items():
                print(f"{key} : {value}", end=" ")




my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

for key, value in my_dict.items():
    print(key, ":", value)

y_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Traverse the dictionary and print key-value pairs in a single line
for key, value in my_dict.items():
    print(f"{key}: {value}", end=" ")
