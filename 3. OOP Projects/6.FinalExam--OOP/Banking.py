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
        if not Account.isBankrupt:
            if amount >= 0 and self.balance >= amount:
                self.balance -= amount
                Account.total_Balance -=amount
                resit = f"withdraw balance is : ${amount} and Current Balance is :  ${self.balance} "
                self.Transaction.append(resit)
                print(f'\n After withdrawing ${amount} , your current Balance is : ${self.balance}\n')
            else:
                print("\n Withdrawal amount exceeded \n")
        else:
            print("\nthe bank is bankrupt")

    def Deposit(self,amount):
        if not Account.isBankrupt:
            self.balance += amount
            Account.total_Balance +=amount
            resit = f"Deposit balance is :{amount} and Current Balance is :  {self.balance} "
            self.Transaction.append(resit)
            print(f'\n After Deposit ${amount} , your current Balance is : {self.balance}\n')

        else:
            print("\n the bank is bankrupt")


    def AvailableBalance(self):
        print(f'\n Current Balance is : {self.balance} \n')

    def TransactionHistory(self):
        if len(self.Transaction)>0:
           for trans in self.Transaction:
                print(trans)

        else:
           print("\n ---------=> There is no Transaction history ")
        

    def TakeLoan(self,amount):
        if self.loanCount>0 and Account.lonStatus:
            Account.total_Loan +=amount
            self.balance += amount
            self.loanCount -=1
            if self.loanCount == 1 :
                print("\n ---------=>  you can take loan another time enjoy")
            else:
                print("\n---------=> Last time of your loan , Pay the previous loan ")
        else:
            print("\n ------=>your loan limit exceeded<=----------\n")
    
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
                        print("\n -------->You don't have enough money to transfer <-------\n ")
                else:
                    print('\n----->user is not found<----------\n')

        else:
            print("\n--------->Not More user there you can transfer your money<-----------\n")
                                

class Admin:
    name = "admin"
    password = "1234"
    ID = "BOSS"


    def create_user(self, name, email, address, account_type, password):
        user = Account(name, email, address, account_type, password)
        # Account.accounts.append(user)
        print(f"\n------>Successfully create the Account , Name : {name} and AccountNumber : {user.ID} <--------\n")
        return user
    
    def delete_user(self, accountHolder):
        for user in Account.accounts:
            if user.name == accountHolder:
                Account.accounts.remove(user)
                print(f"\n-----=> {accountHolder}'s account has been deleted.<=-------- \n")
                return
        print("\n ------=>User account not found. Deletion failed.<=---- \n")
    
    def show_users(self):
        if len(Account.accounts) > 0:
            print(f"\n-->Available users down below\n")
            print(len(Account.accounts),"user's found \n")
            for user in Account.accounts:
                print(
                    f"\n -->Name: {user.name}, Account No: {user.ID}, Email: {user.email}, Address: {user.address}, Account Type: {user.AcType} \n"
                )
        else:
            print(f"\n-->No user found.\n")

    
    def totalBalanceOfTheBank(self):
        print(f'\n-------->This Bank total Current Balance is : {Account.total_Balance}<=-----\n')
    
    def check_bank_loan(self):
        print(f"\n--=>Total loan of the  bank is ${Account.total_Loan}<=--\n")

    def loanControl(self ,status=1):
        if status == "off" or status == 0:
            Account.lonStatus = False
            print("\n---------->You just Off the Loan Status<------------\n ")
        else:
            Account.lonStatus = True
            print("\n---------->loan status on<--------------\n")

    def setBankrupt(self,status=0):
        if status == "on" or status == 1:
            Account.isBankrupt = True
            print("\n------->You Bank in now  Bankrupt<----------------\n ")
        else:
            Account.lonStatus = False
            print("\n-------->Bank is now Open for all<-----------------\n")

   






currentUser=None


while(True):
    if currentUser==None:
        print("\n-----> No user logged in !<--------\n")
        ch = input("\n--> Register/Login (R/L) : ")
        if ch=="R" or ch =='r':
            name= input("Name : ")
            email = input("Email : ")
            address = input("address : ")
            accountType = input("Account Type: ")
            password = input("Password : ")
            currentUser = Account(name,email,address,accountType,password)

        elif ch == "L" or ch == 'l':
            LogInAs =input("Log in as User or Admin  U/A : " )

            if LogInAs == 'U' or LogInAs == 'u':
                name = input("Account Name : ") 
                password = input("Account Password : ")
                for account in Account.accounts:
                    if account.name==name and account.password == password:
                        currentUser=account
                    else:
                        print("\n ------------>your UserName or password is wrong<----------- \n")
            elif LogInAs == 'A' or LogInAs == 'a':
                name=input("Account Name : ")
                password = input("PassWord : ")
                if(name==Admin.name and password == Admin.password):
                    print("\n------->Take the control of the bank<----------\n")
                    currentUser = Admin
                else:
                    print("\n ------->your UserName or password is wrong<-------------- \n")
            else:
                print("\n ----->Press The valid key<----------- \n")

        else:
            print("\n Press The valid key \n")

    else:
        print("\n--------------------------------------------------------------------------\n")
        
        print(f"\n---------=> Welcome {currentUser.name} Account number {currentUser.ID}!<=-------------\n  ")
        
        if isinstance(currentUser, Account):
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Check balance")
            print("4. Transaction history")
            print("5. Loan")
            print("6. Transfer balance")
            print("7. Logout\n")
            
            op = int(input("Chose a Option : "))

            if op == 1:
                amount = int(input("Enter withdrawal amount: "))
                currentUser.withdraw(amount)

            elif op == 2:
                amount = int(input("Enter deposit amount:"))
                currentUser.Deposit(amount)

            elif op == 3:
                currentUser.AvailableBalance()

            elif op == 4:
                currentUser.TransactionHistory()

            elif op == 5:
                amount = int(input("Enter loan amount:"))
                currentUser.TakeLoan(amount)

            elif op == 6:
                receiverName = input("Enter the account Holder Name For  transfer :")
                amount = int(input("Enter transfer amount:"))
                currentUser.TransferBalance(receiverName , amount)

            elif op == 7:
                currentUser = None

            else:
                print("\n------->Invalid Option<----------\n")

        else:
            
            print("1. Create User")
            print("2. Delete User")
            print("3. View User Accounts")
            print("4. View Total Balance")
            print("5. View Total Loan Amount")
            print("6. Toggle Loan Feature")
            print("7. Logout \n")

            op = int(input("Choose Option : "))
            
            if op == 1:
                name = input("Name : ")
                email = input("Email : ")
                address = input("Address: ")
                account_type = input("account_type: ")
                password = input("password : ")
                currentUser.create_user(Admin,name,email,address,account_type,password)

            elif op == 2:
                acc = input("Enter account's Holder name to delete:")
                result = currentUser.delete_user(Admin,acc)

            elif op == 3:
                acc = currentUser.show_users(Admin)
            elif op == 4:
                currentUser.totalBalanceOfTheBank(Admin)

            elif op == 5:
                currentUser.check_bank_loan(Admin)

            elif op == 6:
                status = int(input("on for pass 1 and for off press 0 : "))

                result = currentUser.loanControl(Admin,status)

            elif op == 7:
                currentUser = None

            else:
                 print("\n------->Invalid Option<-----------\n")



