class Vehicle:
    def __init__(self,name,price) -> None:
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f'{self.name} and It\'s price  {self.price}'
    
class Bus(Vehicle):
    def __init__(self, name, price,seat) -> None:
        self.seat = seat
        super().__init__(name, price)
    def __repr__(self) -> str:
        return super().__repr__()

EnaPoribohon = Bus("Ena PoriBohon ",1200,56)
print(EnaPoribohon)