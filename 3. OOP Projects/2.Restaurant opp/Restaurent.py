class Restaurant:
    def __init__(self,name,menu =[]) -> None:
        self.name = name 
        self.menu = menu
        self.server = None
        self.chef = None
        self.manager = None
        self.revenue = 0
        self.Profit  = 0
        self.expense = 0
        self.balance = 0
        self.Menu = []
    
    def addEmployee(self,employeeType , employee):
        self.employeeType = employeeType
        self.employee  = employee

        if self.employee =="chef":
            self.chef = employee
        elif self.employee == "server":
            self.server = employee
        elif self.employee == "manager":
            self.manager = employee
    def receivePayment(self,amount,order,customer):
        if amount>=order.bill:
            self.revenue += amount.bill
            self.balance += amount.bill
            self.dueAmount = 0
            return order - amount.bill
    
    def payExpense(self,amount,description):
        if amount<self.balance:
            self.expense += amount
            self.balance -= amount
            print(f"Amount {amount} for the reason of {description}")

        else:
            print(f"I don't have enough money for expanse {description}") 

    def PaySalary(self,employee):
        print(f'Paying salary for {employee.name} salary: {employee.salary}')
        if employee.salary<self.balance:
            employee.receiveSalary() 


