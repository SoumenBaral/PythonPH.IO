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