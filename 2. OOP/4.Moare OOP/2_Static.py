# static attribute (class attribute)
# static method @staticmethod
# class method @classmethod
# differences between static method and class method


class Shopping:
    
    cart = [] # class Attribute or Static Attribute 
    Origin = "japan"
    def __init__(self,name ,location ) -> None:
        self.name = "Jamuna City" # Instance Attribute 
        self.location = "near to all janina"
    def purchase(self,item ,price ,amount):
        remaining = amount - price
        print(f"Buying {item} for Price {price} and remaining {remaining}")
    
    @classmethod
    # when we just call the class and it's method for ignoring the self parameter we have to use @classmethod
    def hudaiDakhi(self,item):
        print("hudai daktachi but kisui kintam na Ac ar hawa khaibar aschii",item)

    @staticmethod
    # When we use it we don't need any self keyword to derive it
    def Multiply(a,b):
        print(a*b)



basundara = Shopping('basu en dhara', 'not popular location')
# basundara.purchase('lungi', 500, 1000)
basundara.hudaiDakhi('lungi')
# Shopping.purchase(3,3,5,6)
Shopping.hudaiDakhi("lungi")
Shopping.Multiply(2,3)