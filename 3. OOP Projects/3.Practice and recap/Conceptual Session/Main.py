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
        self.currentRide = None

    def display_Profile(self):
        print(f"Rider  name is {self.name} and mail is {self.email}")

    def rideRequest(self,ridingApp,destination):
        print("looking for Rides")
        if not self.currentRide :
            ob = RideMatcher(ridingApp.drivers)
            res = ob.hasDriver(self,destination)
            print("your Result is , ",res)
            self.currentRide = res
            return True


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
        return f"Start from {self.startLocation} to {self.endLocation}"         

class RideMatcher:
    def __init__(self,drivers) -> None:
        self.drivers = drivers

    def hasDriver(self,rider,destination):
        if(len(self.drivers))>0:
            ride = Ride(rider.currentLocation,destination)
            return ride
        else:
            return "Sorry, Driver not Found"

        

uber = RideSharing("UBER")
alice = Driver("Alice","alaice@gmil.com",12345,"Chittagong 1")
Soumen = Rider("soumen","sakib@gmail.com",1236,"Chittagong 2")
uber.addDriver(alice)
uber.addRider(Soumen)
print(uber)

if Soumen.rideRequest(uber,"Dhaka"):
    print("Traveling..")
else:
    print("No Ride found")

 

        