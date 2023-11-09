class Shopping:
    cart = [] # class Attribute or Static Attribute 
    Origin = "japan"
    def __init__(self,name ,location ) -> None:
        self.name = "Jamuna City" # Instance Attribute 
        self.location = "near to all janina"
    def purchase(self,item ,price ,amount):
        remaining = amount - price
        print(f"Buying {item} for Price {price} and remaining {remaining}")
    
    @classmethod # when we just call the class and it's method for ignoring the self parameter we have to use @classmethod
    def hudaiDakhi(self,item):
        print("hudai daktachi but kisui kintam na Ac ar hawa khaibar aschii",item)

# Shopping.purchase(3,3,5,6)
Shopping.hudaiDakhi("lungi")