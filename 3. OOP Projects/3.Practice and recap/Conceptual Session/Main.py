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


class User(ABC):
    def __init__(self,name , email,nid) -> None:
        super().__init__()
        self.name = name 
        self.email = email
        self.nid = nid

    @abstractmethod
    def display_Profile(self):
        raise NotImplementedError

class Driver(User):
    def __init__(self, name, email, nid,currentLocation) -> None:
        super().__init__(name, email, nid)
        self.currentLocation = currentLocation
    def display_Profile(self):
        print(f"Driver name is {self.name} and mail is {self.email}")
class Rider(User):
    def __init__(self, name, email, nid ,currentLocation) -> None:
        super().__init__(name, email, nid)
        self.currentLocation = currentLocation
        self.destination = destination
        self.currentRide = None

    def display_Profile(self):
        print(f"Rider  name is {self.name} and mail is {self.email}")

    def rideRequest(self,ridingApp,destination):
        print("looking for Rides")
        if not self.currentRide :
            pass

class Ride :
    def __init__(self,startLocation,endLocation ) -> None:
        self.startLocation = startLocation
        self.endLocation = endLocation
        self.driver = None
        self.rider = None 
    def start_ride(self):
        pass
    def endRide(self):
        pass
    def __repr__(self) -> str:
        return f"Start from {self.start_location} to {self.endLocation}"         

uber = RideSharing("UBER")
uber.addDriver("monu")
uber.addRider("janu")
print(uber)
        