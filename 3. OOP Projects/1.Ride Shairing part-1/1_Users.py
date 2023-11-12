from abc import ABC , abstractmethod

class Users(ABC):
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

class Rider(Users):
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