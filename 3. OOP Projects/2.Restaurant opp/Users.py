from abc import ABC ,abstractstaticmethod

class User(ABC):
    def __init__(self,name) -> None:
        self.name = name 
        super().__init__()
class Customer(User):
    def __init__(self, name,money) -> None:
        self.money = money
        self.__order = None
        super().__init__(name)

        # getter
    @property
    def Order (self):
        return self.__order

    # Setter
    
    @Order.setter
    def Order(self,order):
        self.__order = order