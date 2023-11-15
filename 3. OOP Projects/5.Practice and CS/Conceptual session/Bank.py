from abc import ABC ,abstractmethod
class Account:
    accounts = []
    def __init__(self,name,accountNumber,Password,type) -> None:
        self.name = name 
        self.accountNo = accountNumber
        self.password = Password
        self.type = type 
        self.balance = 0
        Account.accounts.append(self)
    def changeInfo(self,name):
        self.name = name
        print(f"\n--> Name is changed of {self.accountNo}")

    # Overloading of method change Info 

    def changeInfo(self,name,passWord):
        self.name = name 
        self.password = passWord
        print(f"\n--> Name is changed of {self.accountNo} -- and Name:{self.name} and PassWord :{self.password}")

    def deposit(self,amount,):
        if amount>0:
            self.balance += amount
            print(f"\n--> Deposited {amount}. New balance: ${self.balance}")

        else :
            print("\n Invalid Deposit \n ")
    def Withdrew(self,amount,):
        if amount>0 and self.balance>=amount:
            self.balance -= amount
            print(f"\n--> Withdrew  {amount}. New balance: ${self.balance}")

        else :
            print("\n Invalid Withdrew \n ")

    @abstractmethod
    def showInfo(self):
        pass


    

