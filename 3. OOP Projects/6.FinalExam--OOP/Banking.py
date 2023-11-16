import random

class Bank:
    def __init__(self, Name, Location) -> None:
        self.Name = Name
        self.Location = Location
        self.Users = []
        self.total_Balance = 0
        self.total_Loan = 0
        self.Bankrupt = False
        self.Loan_System = True



class Account:
    accounts = []
    total_Balance = 0
    total_Loan = 0

    def __init__(self,name,email,address,type) -> None:
        self.name = name 
        self.email = email
        self.address = address
        self.type = type
        self.balance = 0
        self.ID = random.randint(1000,9999)
        self.Transaction = []
        self.loanCount = 2
        self.isBankrupt = False
        Account.accounts.append(self)


    def withdraw(self,amount):
        if not self.isBankrupt:
            if amount >= 0 and amount >= self.balance:
                self.balance -= amount
                Account.total_Balance -=amount
                resit = {"Withdraw" : amount ,"CurrentBalance":self.balance }
                self.Transaction.append(resit)
                print(f'\n After withdrawing ${amount} , your current Balance is : {self.balance}\n')
            else:
                print("\n Withdrawal amount exceeded \n")
        else:
            print("the bank is bankrupt")

    def Deposit(self,amount):
        self.balance += amount
        resit = {"Deposit" : amount ,"CurrentBalance":self.balance }
        self.Transaction.append(resit)
        print(f'\n After Deposit ${amount} , your current Balance is : {self.balance}\n')
    
    def AvailableBalance(self):
        print(f'\n Current Balance is : {self.balance} \n')

    def TransactionHistory(self):
        if len(self.Transaction)>0:
           for trans in self.Transaction:
                for key, value in trans.items():
                    print(f"{key} : {value}", end=" ")

        else:
           print("There is no Transaction history ")
        

    def TakeLoan(self,amount):
        if self.loanCount>0 and amount>=10000:
            self.balance += amount
            self.loanCount -=1
            if self.loanCount == 1 :
                print("you can take loan another time enjoy")
            else:
                print("Last time of your loan , Pay the previous loan ")
        else:
            print("your loan limit exceeded")
    
    def isAccount(self,id):
        for acc in Account.accounts:
            if id in acc["ID"]:
                return True

    def TransferBalance(self,id , amount):
        flag = False
        if self.balance>amount:
            for acc in Account.accounts:
                for isAc in acc:
                    if isAc["ID"] == self.id:
                        isAc["balance"] += amount
                        self.balance -= amount
                        flag= True
                        print(f'Transfer Successful to-- {isAc["name"]} and Balance is {isAc["balance"] }')
                        break
            if not flag:
                print("Your Searching Account is invalid ,Thank you")
        else:
            print("You don't have enough money to transfer ")
                       

class Admin(Account):
    def __init__(self, name, email, address, type) -> None:
        super().__init__(name, email, address, type)

    






