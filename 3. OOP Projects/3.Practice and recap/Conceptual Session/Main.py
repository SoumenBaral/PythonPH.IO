from abc import ABC , abstractmethod
# we use Abstractmethod for base class and take some must taking method in inherit class
# __init or anything __ is called Dander method

# First we need a company's blueprint that why we can use it any where
class RideSharing :
    def __init__(self,company_name) -> None: 
        self.company_name = company_name
        self.drivers = []
        self.riders = []
    def addDriver(self,driver):
        self.drivers.append(driver)
    def addRider(self,rider):
        self.riders.append(rider)
    
    def __repr__(self) -> str:
        return f'{self.company_name} has  Driver :{len(self.drivers)} and Riders : {len(self.riders)}'



uber = RideSharing("UBER")
uber.addDriver("monu")
uber.addRider("janu")
print(uber)
        