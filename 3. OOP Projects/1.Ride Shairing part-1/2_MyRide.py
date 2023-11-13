from abc import ABC,abstractclassmethod
from datetime import datetime

class RideSharing:
    def __init__(self,companyName) -> None:
        self.companyName = companyName
        self.riders = []
        self.drivers = []
        self.rides = []

    def addRider(self,rider):
        self.riders.append(rider)
    
    def addDriver(self,driver):
        self.drivers.append(driver)
    def __repr__(self) -> str:
        return f'{self.companyName} with riders : {len(self.riders)} and drivers: {len(self.drivers)}'
    
class User(ABC):
    def __init__(self,name ,email,nid) -> None:
        self.name = name 
        self.email = email
        self.__id = 0
        self.__NID = nid
        self.wallet = 0

    @abstractclassmethod
    def displayProfile (self):
        raise NotImplementedError

class Rider(User):
    def __init__(self, name, email, nid,currentLocation,initialAmount) -> None:
        self.name = name 
        self.wallet = initialAmount
        self.currentLocation = currentLocation
        super().__init__(name, email, nid)
    def displayProfile(self):
        print(f'Rider: with name : {self.name} and email: {self.email}')
    def loadCash(self,amount):
        if amount>0:
            self.wallet +=amount
    def updateLocation (self,currentLocation):
        self.currentLocation = currentLocation
    
    def requestRide(self,rideSharing ,destination):
        if not self.currentRide:
            rideRequest = RideRequest(self,destination)
            rideMatcher = RideMatching(rideSharing.drivers)
            ride = rideMatcher.findDriver(rideRequest)
            print("got the ride, yoy",ride)
            self.currentRide = ride

    def showCurrentRide(self):
        print(self.currentRide)


class RideRequest :
    def __init__(self,rider,endLocation) -> None:
        self.rider = rider
        self.endLocation = endLocation

class RideMatching:
    def __init__(self,drivers) -> None:
        self.availableDrivers = drivers
    
    def findDriver(self,rideRequest):
        if len(self.availableDrivers)>0:
            print("looking for a driver ")
            driver = self.availableDrivers[0]
            ride = 0
    