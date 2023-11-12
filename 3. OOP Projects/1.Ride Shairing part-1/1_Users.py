from abc import ABC , abstractmethod
from datetime import datetime
 
class User(ABC):
    def __init__(self,name,email,NID) -> None:
        self.name = name
        self.email = email
        # TODO: Set User Id dynamically 
        self.__Id = 0
        self.__NID = NID
        self.wallet = 0
    
    @abstractmethod
    def displayProfile(self):
        raise NotImplementedError

class Rider(User):
    def __init__(self, name, email, NID,CurrentLocation) -> None:
        self.CurrentRide = None
        self.wallet = 0
        self.CurrentLocation = CurrentLocation
        super().__init__(name, email, NID)


    def displayProfile(self):
        print(f"Rider Name : {self.name} and his Email: {self.email}")
    
    def requestRide(self,currentLocation,destination):
        if not self.CurrentRide:

            # TODO: set ride request property ------> Done 
            # TODO: Set current via ride match------> Done
            
            ride_request = RideRequest(self,destination)
            rideMatcher = RideMatching()
            self.CurrentRide = rideMatcher.findDriver(ride_request)
    def LoadCash (self,loadMoney):
        if loadMoney>0:
            self.wallet += loadMoney
    def updateLocation(self,currentLocation):
        self.CurrentLocation = currentLocation

class Driver(User):
    def __init__(self, name, email, NID,CurrentLocation) -> None:
        super().__init__(name, email, NID)
        self.CurrentLocation = CurrentLocation
        self.wallet = 0
    
    def displayProfile(self):
        print(f"Rider Name : {self.name} and his Email: {self.email}")
    
    def acceptRide(self,ride):
        ride.setDriver(self)

class Ride:
    def __init__(self,startLocation,EndLocation) -> None:
        self.startLocation = startLocation
        self.endLocation   = EndLocation
        self.driver = None
        self.rider = None
        self.StartingTime = None 
        self.EndingTime  = None
        self.EstimatedFare = None

    def setDriver(self,driver):
        self.driver = driver

    def StartRide(self):
        self.StartingTime = datetime.now()
    
    def EndRide(self,rider,payment):
        self.payment = payment
        self.rider.wallet -= self.EstimatedFare
        self.driver.wallet += self.EstimatedFare

class RideRequest:
    def __init__(self,rider,endLocation) -> None:
        self.rider = rider
        self.endLocation = endLocation


class RideMatching :
    def __init__(self) -> None:
        self.AvailableDrivers = []

    def findDriver(self, rideRequest):
        # TODO: find the closest driver from the rider 
        if len(self.AvailableDrivers)>0:
            driver = self.AvailableDrivers[0]
            ride  = Ride(rideRequest.rider.currentLocation,rideRequest.endLocation)
            driver.acceptRide(ride)
            return ride
        


        
