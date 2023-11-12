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
    def __init__(self, name, email, NID) -> None:
        self.CurrentRide = None
        super().__init__(name, email, NID)

    def displayProfile(self):
        print(f"Rider Name : {self.name} and his Email: {self.email}")
    
    def requestRide(self,currentLocation,destination):
        if not self.CurrentRide:

            # TODO: set ride request property
            # TODO: Set current via ride match
            ride_request = None
            self.CurrentRide = None

class Driver(User):
    def __init__(self, name, email, NID,CurrentLocation) -> None:
        super().__init__(name, email, NID)
        self.CurrentLocation = CurrentLocation
    
    def displayProfile(self):
        print(f"Rider Name : {self.name} and his Email: {self.email}")
    
    def acceptRide(self,ride):
        ride.setDriver(self)

class Ride:
    def __init__(self,startLocation,EndLocation) -> None:
        self.startLocation = startLocation
        self.endLocation   = EndLocation
        self.driver = None
        self.StartingTime = None 
        self.EndingTime  = None
        self.EstimatedFee = None

    def setDriver(self,driver):
        self.driver = driver

    def StartRide(self):
        self.StartingTime = datetime.now()