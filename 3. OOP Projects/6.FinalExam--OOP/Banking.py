import random

"""YOUR_BANK"""

class Account:
    accounts = []
    total_Balance = 0
    total_Loan = 0
    lonStatus = True
    isBankrupt = False

    def __init__(self,name,email,address,AcType,password) -> None:
        self.name = name 
        self.email = email
        self.address = address
        self.password = password
        self.AcType = AcType
        self.balance = 0
        self.ID = random.randint(1000,9999)
        self.Transaction = []
        self.loanCount = 2
        Account.accounts.append(self)


    def withdraw(self,amount):
        if not self.isBankrupt:
            if amount >= 0 and amount >= self.balance:
                self.balance -= amount
                Account.total_Balance -=amount
                resit = f"withdraw balance is :{amount} and Current Balance is :  {self.balance} "
                self.Transaction.append(resit)
                print(f'\n After withdrawing ${amount} , your current Balance is : {self.balance}\n')
            else:
                print("\n Withdrawal amount exceeded \n")
        else:
            print("the bank is bankrupt")

    def Deposit(self,amount):
        self.balance += amount
        Account.total_Balance +=amount
        resit = f"withdraw balance is :{amount} and Current Balance is :  {self.balance} "
        self.Transaction.append(resit)
        print(f'\n After Deposit ${amount} , your current Balance is : {self.balance}\n')
    
    def AvailableBalance(self):
        print(f'\n Current Balance is : {self.balance} \n')

    def TransactionHistory(self):
        if len(self.Transaction)>0:
           for trans in self.Transaction:
                print(trans)

        else:
           print("There is no Transaction history ")
        

    def TakeLoan(self,amount):
        if self.loanCount>0 and Account.lonStatus:
            Account.total_Loan +=amount
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

    def TransferBalance(self,name , amount):
        if len(Account.accounts) >= 2:
            for user in Account.accounts:
                if name == user.name:
                    print('user found')
                    if self.balance >= amount:
                        user.balance += amount
                        self.balance -= amount
                        history = history = f"\n-->Balance successfully transferred to {name} from {self.name}, and the amount is {amount}\n"
                        self.Transaction.append(history)
                        print(history)
                        break
            
                    else:
                        print("You don't have enough money to transfer ")
                else:
                    print('user is not found')

        else:
            print("Not More user there you can transfer your money")
                                

class Admin:
    name = "admin"
    password = "1234"


    def create_user(self, name, email, address, account_type,password):
        user =Account(name, email, address, account_type,password)
        Account.accounts.append(user)
        return user
    
    def delete_user(self, account_number):
        for user in Account.accounts:
            if user.account_number == account_number:
                Admin.user.remove(user)
                print(f"User account number {account_number} has been deleted.")
        print("User account not found. Deletion failed.")
    
    def show_users(self):
        if len(Account.accounts) > 0:
            print(f"\n-->Available users down below\n")
            for user in Account.accounts:
                print(
                    f"-->Name: {user.name}, Account No: {user.ID}, Email: {user.email}, Address: {user.address}, Account Type: {user.AcType}"
                )
                print()
        else:
            print(f"\n-->No user found.\n")

    
    def totalBalanceOfTheBank(self):
        print(f'This Bank total Current Balance is : {Account.total_Balance}')
    
    def check_bank_loan(self):
        print(f"\n-->Total loan of the  bank is ${Account.total_Loan}\n")

    def loanControl(self ,status=1):
        if status == "off" or status == 0:
            Account.lonStatus = False
            print("You just Off the Loan Status ")
        else:
            Account.lonStatus = True
            print("loan status on")

    def setBankrupt(self,status=0):
        if status == "on" or status == 1:
            Account.isBankrupt = True
            print("You Bank in now  Bankrupt ")
        else:
            Account.lonStatus = False
            print("Bank is now Open for all")

   






currentUser=None


while(True):
    if currentUser==None:
        print("\n-----> No user logged in !<--------\n")
        ch=input("\n--> Register/Login (R/L) : ")
        if ch=="R" or ch =='r':
            name= input("name : ")
            email = input("Email : ")
            address = input("address : ")
            accountType = input("account Type: ")
            password = input("Password : ")
            currentUser = Account(name,email,address,accountType,password)

        elif ch == "L" or 'l':
            LogInAs =input("Log in as User or Admin  U/A : " )

            if LogInAs == 'U' or LogInAs == 'u':
                name=int(input("Account Name : "))
                for account in Account.accounts:
                    if account.name==name:
                        currentUser=account
                        break
            elif LogInAs == 'A' or LogInAs == 'a':
                name=input("Account Name : ")
                password = input("PassWord : ")
                if(name==Admin.name and password == Admin.password):
                    print("Take the control of the bank")
                    currentUser = Admin
                else:
                    print("you not UserName or password is wrong")
            else:
                print("Press The valid key ")

    else:
        print(f"\nWelcome {currentUser.name} Account number {currentUser.ID}!\n  ")
        break



