class Restaurant:
    def __init__(self,name,rent,menu =[]) -> None:
        self.name = name 
        self.menu = menu
        self.rent = rent
        self.orders = []
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

        if self.employeeType =="chef":
            self.chef = employee
        elif self.employeeType == "server":
            self.server = employee
        elif self.employeeType == "manager":
            self.manager = employee

    def AddOrder(self,order):
        self.orders.append(order)
      
      
    def receivePayment(self,amount,order,customer):
        if amount>=order.bill:
            self.revenue += order.bill
            self.balance += order.bill
            customer.dueAmount = 0
            return amount - order.bill
        else:
            print("you don't have enough money ")
    
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
            self.balance -= employee.salary
            self.expense += employee.salary
            employee.receiveSalary() 
    
    def ShowEmployee(self):
        print("showing Employees: ")
        if self.chef is not None :
            print(f'Chef : {self.chef.name} with salary : {self.chef.salary}')
        if self.server is not None:
            print(f"Server : {self.server.name} with salary: {self.server.salary}")
        if self.manager is not None:
            print(f"Server : {self.manager.name} with salary: {self.manager.salary}")


