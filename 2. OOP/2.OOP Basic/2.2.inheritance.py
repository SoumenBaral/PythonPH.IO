# Base Class , Parent Class , Common Attribute , functionality Class
# Child class , derivate class ,uncommon attribute + Functionality class 
class Gadget:
    def __init__(self,brand,color, price ) -> None:
        self.brand = brand
        self.color = color 
        self.price = price
        pass
class laptop:
    def __init__(self,memory) -> None:
        
        self.memory = memory

    def run (self):
        print(f'Running laptop: {self.brand}')

    def coding(self):
        print(f"learning and practicing the via my {self.color} {self.brand} laptop")

class Phone:
    def __init__(self,brand,color, price , dual_sim) -> None:
        self.brand = brand
        self.color = color 
        self.price = price
        self.dual_sim = dual_sim
        

    def run (self):
        print(f'Running Phone: {self.brand}')

    def phone_call(self,number ,text):
        print(f"Number : {number}  and SMS : {text}")

class Camera:
    def __init__(self, brand, price, color, pixel) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.pixel = pixel

    def run(self):
        pass

    def change_lens(self):
        pass
