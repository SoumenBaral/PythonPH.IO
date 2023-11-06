# when the function is into the class we will call it method 
# we can call method into the method 

class Bank:
    def __init__(self,balance):
        self.balance = balance
        self.minimum_withdraw = 100
        self.maximum_withdraw = 100000 # we can make the variable in own .

    def get_balance(self):
        return self.balance
    

    def deposit (self,amount):
        if(amount>0):
            self.balance += amount
        print(f'your new balance is : {self.balance}')

    def withdraw (self, amount):
        if(amount<self.minimum_withdraw):
            print(f"you are a verger you have to withdraw minimum : {self.minimum_withdraw}")

        elif(amount>self.maximum_withdraw):
            print(f'Bank will be veger man please withdraw less then {self.maximum_withdraw}')
        
        else:
            self.balance -=amount
            print(f"after withdrawing {amount} you have rest : {self.get_balance()}")


brac = Bank(15000)
brac.withdraw(25)
brac.withdraw(50000000)
brac.withdraw(1000)

dbbl = Bank(5000)
dbbl.deposit(2000)
dbbl.deposit(2000)
print(dbbl.get_balance())