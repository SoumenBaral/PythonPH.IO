from abc import ABC ,abstractstaticmethod

class User(ABC):
    def __init__(self,name,phone ,email,address) -> None:
        self.name = name 
        self.phone = phone 
        self.email = email
        self.address = address
        super().__init__()
class Customer(User):
    def __init__(self, name,money,phone ,email,address) -> None:
        self.money = money
        self.__order = None
        self.due_bill = 0
        super().__init__(name,phone ,email,address)

        # getter
    @property
    def Order (self):
        return self.__order

    # Setter

    @Order.setter
    def Order(self,order):
        self.__order = order
    
    def EatFood(self,order):
        print(f'{self.name} is now enjoying his food : {order.items}')

    def placeAOrder(self,order):
        self.order = order
        self.due_bill =order.bill
        print(f"{self.name} place with the a Bill of : {order.bill} taka")
    
    def PayForOrder(self,amount):
        # TODO : Submit the money to the manager 
        pass
    def giftTips(self,amount):
        pass

class Employee(User):
    def __init__(self, name,salary , StartingDate,department,phone ,email,address) -> None:
        self.salary = salary
        self.startingDate = StartingDate
        self.due = salary
        self.department = department
        super().__init__(name,phone ,email,address)
    
    def receiveSalary(self):
        self.due = 0

class Chef(Employee):
    def __init__(self, name, salary, StartingDate, department, phone, email, address,CookingItem) -> None:
        super().__init__(name, salary, StartingDate, department, phone, email, address)
        self.CookingItem = CookingItem

class Server(Employee):
    def __init__(self, name, salary, StartingDate, department, phone, email, address) -> None:
        super().__init__(name, salary, StartingDate, department, phone, email, address)
        self.TipsEarning = 0 

    def takeOrder(self,order):
        pass
    def transferOrder(self,order):
        pass
    def serverOrder(self,order):
        pass
    def receiveTips(self,amount ):
        pass

class Manager(Employee):
    def __init__(self, name, salary, StartingDate, department, phone, email, address) -> None:
        super().__init__(name, salary, StartingDate, department, phone, email, address)
