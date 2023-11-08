from abc import ABC , abstractmethod

# abstract base class 
class Animal(ABC):
    def __init__(self) -> None:
        super().__init__()
    @abstractmethod # enforce all the derived class to have the under method
    def eat (self):
        print("i Need food ")
    @abstractmethod
    def move (self) :
        pass


class Monkey(Animal):
    def __init__(self,name ) -> None:
        self.category = "Monkey"
        self.name = name 
        super().__init__()

    def eat(self):
        print('Hey na nana, I am eating banana')
    def move(self):
        print('Hanging on the branches')

layka = Monkey('lucky')
layka.eat()
layka.move()