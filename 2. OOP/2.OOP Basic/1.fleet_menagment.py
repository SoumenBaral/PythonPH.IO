# Ena Express

class company:
    def __init__(self,name,address) -> None:
        self.name = name
        self.address = address
        self.bus = []
        self.driver = []
        self.counter = []
        self.route = []
        self.supervisor = []
        self.manager = []

class Driver : 
    def __init__(self,name ,license,age) -> None:

        self.name = name 
        self.license = license
        self.age = age 
    def __repr__(self) -> str:
        return f"""
                   Name of the Driver is : {self.name}
                   license Number is : {self.license}
                   Age is           : {self.age}            
"""

class counter :
    def __init__(self) -> None:
        pass
    def purchase_a_ticket(self, start, destination):
        pass

class Passenger:
    pass

class Supervisor:
    pass

red_mia = Driver('a', '123',32)

print(red_mia)