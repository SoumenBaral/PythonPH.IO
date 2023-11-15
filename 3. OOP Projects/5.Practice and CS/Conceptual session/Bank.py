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


class SavingsAccount(Account):
    def __init__(self, name, accountNumber, Password,interestRate) -> None:
        super().__init__(name, accountNumber, Password, "SavingsAccount")
        self.interestRate = interestRate
    
    def Withdrew(self, amount):
        if amount > 0 and (self.balance - amount) >= -self.limit:
            self.balance -= amount
            print(f"\n--> Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("\n--> Invalid withdrawal amount or overdraft limit reached")
        

    def showInfo(self):
        print(f"Infos of {self.type} account of {self.name}:\n")
        print(f'\n\tAccount Type : {self.type}')
        print(f'\tName : {self.name}')
        print(f'\tAccount No : {self.accountNo}')
        print(f'\tCurrent Balance : {self.balance}\n')

class SpecialAccount(Account):
    def __init__(self, name, accountNumber, Password,limit) -> None:
        super().__init__(name, accountNumber, Password, "special")
        self.limit = limit
    
    def applyInterest(self):
        Interest = self.balance*(self.interestRate/100)
        print("\n--> Interest is applied !")
        self.deposit(Interest)


    def showInfo(self):
        print(f"Infos of {self.type} account of {self.name}:\n")
        print(f'\n\tAccount Type : {self.type}')
        print(f'\tName : {self.name}')
        print(f'\tAccount No : {self.accountNo}')
        print(f'\tCurrent Balance : {self.balance}\n')
