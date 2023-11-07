# Base Class , Parent Class , Common Attribute , functionality Class
# Child class , derivate class ,uncommon attribute + Functionality class 
class Gadget:
    def __init__(self,brand,color, price ,origin ) -> None:
        self.brand = brand
        self.color = color 
        self.price = price
        self.origin = origin
     
    
    def run (self):
        print(f'Running laptop: {self.brand}')


class laptop:
    def __init__(self,memory,ssd) -> None:
        self.ssd = ssd
        self.memory = memory

    def coding(self):
        print(f"learning and practicing the via my {self.color} {self.brand} laptop")

class Phone(Gadget):
    def __init__(self ,brand,color,price,origin, dual_sim) -> None:
        self.dual_sim = dual_sim
        
        super().__init__(brand,color,price,origin)

    def phone_call(self,number ,text):
        print(f"Number : {number}  and SMS : {text}")

    def __repr__(self) -> str:
        return f'phone: {self.brand} {self.price} {self.dual_sim}'

class Camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel


    def change_lens(self):
        pass


# Inheritance 
my_phone = Phone('iphone', 120000, 'silver', 'china', True)

print(my_phone)
# my_phone.phone_call()
print(my_phone.brand)
print(my_phone)
