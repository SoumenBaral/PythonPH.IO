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
    
    