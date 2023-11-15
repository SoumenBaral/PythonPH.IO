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

class SpecialAccount(Account):
    def __init__(self, name, accountNumber, Password,limit) -> None:
        super().__init__(name, accountNumber, Password, "special")
        self.limit = limit
    
   
    def Withdrew(self, amount):
        if amount > 0 and (self.balance - amount) >= self.limit:
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



currentUser=None

while(True):
    if currentUser==None:
        print("\n--> No user logged in !")
        ch=input("\n--> Register/Login (R/L) : ")
        if ch=="R":
            name=input("Name:")
            no=input("Account Number:")
            pa=input("Password:")
            a=input("Savings Account or special Account (sv/sp) :")
            if a=="sv":
                ir=int(input("Interest rate:"))
                currentUser=SavingsAccount(name,no,pa,ir)
            else:
                lm=int(input("Overdraft Limit:"))
                currentUser=SpecialAccount(name,no,pa,lm)
        else:
            no=int(input("Account Number:"))
            for account in Account.accounts:
                
                if account.accountNo==no:
                    currentUser=account
                    break
                
    else:
        print(f"\nWelcome {currentUser.name} !\n")
        
        if currentUser.type=="savings":
            
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Show Info")
            print("4. change Info")
            print("5. Apply Interset")
            print("6. Logout\n")
            
            op=int(input("Chhose Option:"))
            
            if op==1:
                amount=int(input("Enter withdraw amount:"))
                currentUser.withdraw(amount)
                
            elif op==2:
                amount=int(input("Enter deposit amount:"))
                currentUser.deposit(amount)
            
            elif op==3:
                currentUser.showInfo()
            
            elif op==4:
                print("Homework")
            
            elif op==5:
                currentUser.apply_interest()
            
            elif op==6:
                currentUser=None
            else:
                print("Invalid Option")
        
        else:
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Show Info")
            print("4. change Info")
            print("5. Logout\n")
            
            
            op=int(input("Chhose Option:"))
            
            if op==1:
                amount=int(input("Enter withdraw amount:"))
                currentUser.Withdrew(amount)
                
            elif op==2:
                amount=int(input("Enter deposit amount:"))
                currentUser.deposit(amount)
            
            elif op==3:
                currentUser.showInfo()
            
            elif op==4:
                print("Homework")
            
            elif op==5:
                # currentUser=None
                break # when we use break it will be out of the system 
            
            
            else:
                print("Invalid Option")