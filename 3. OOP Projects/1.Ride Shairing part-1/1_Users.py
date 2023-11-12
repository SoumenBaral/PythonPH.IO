from abc import ABC , abstractmethod
from datetime import datetime
 
class Ride_Sharing:
    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []

    def add_rider(self, rider):
        self.riders.append(rider)
    
    def add_driver(self, driver):
        self.drivers.append(driver)

    def __repr__(self) -> str:
        return f'{self.company_name} with riders: {len(self.riders)} and drivers: {len(self.drivers)}'

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
    def __init__(self, name, email, NID,CurrentLocation,initialAmount) -> None:
        self.CurrentRide = None
        self.wallet = initialAmount
        self.CurrentLocation = CurrentLocation
        super().__init__(name, email, NID)


    def displayProfile(self):
        print(f"Rider Name : {self.name} and his Email: {self.email}")
    
    
    def request_ride(self, ride_sharing, destination):
        if not self.CurrentRide:
            
            ride_request = RideRequest(self, destination)
            ride_matcher = RideMatching(ride_sharing.drivers)
            ride = ride_matcher.findDriver(ride_request)
            print('got the ride, yay', ride)
            self.CurrentRide = ride

    def LoadCash (self,loadMoney):
        if loadMoney>0:
            self.wallet += loadMoney
    def updateLocation(self,currentLocation):
        self.CurrentLocation = currentLocation
    def show_current_ride(self):
        print(self.CurrentRide)

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
    def __init__(self,drivers) -> None:
        self.AvailableDrivers = drivers

    
    def findDriver(self, ride_request):
        if len(self.AvailableDrivers) > 0:
            # TODO: find  the closest driver of the rider
            print('looking for a driver')
            driver = self.AvailableDrivers[0]
            ride = Ride(ride_request.rider.current_location, ride_request.end_location)
            driver.accept_ride(ride)
            return ride
        


        
class Vehicles(ABC):
    speed = {
        'car': 50,
        'bike': 60,
        'cng': 15
    }

    def __init__(self,vehicles_type , licensePlate , rate ) -> None:
        self.vehicles_type = vehicles_type
        self.licensePlate = licensePlate
        self.rate = rate
        self.Status = "Available"
        super().__init__()
    @abstractmethod
    def startDrive(self):
        pass

class Car(Vehicles):
    def __init__(self, vehicles_type, licensePlate, rate) -> None:
        super().__init__(vehicles_type, licensePlate, rate)
    def startDrive(self):
        self.status = 'unavailable'

class Bike (Vehicles):
    def __init__(self, vehicles_type, licensePlate, rate) -> None:
        super().__init__(vehicles_type, licensePlate, rate)
    def startDrive(self):
        self.status = 'unavailable'

# check the class integration

niye_jao = Ride_Sharing('Niye Jao')
sakib = Rider("sakib Khan", 'sakib@khan.com', 1254, 'mohakhali',1000)
niye_jao.add_rider(sakib)
kala_pakhi = Driver('Kala Pakhi', 'kala@sada.com', 5648, 'gulshan 1')
niye_jao.add_driver(kala_pakhi)
print(niye_jao)
sakib.request_ride(niye_jao,"uttora")
sakib.show_current_ride()
    

        # git problem 