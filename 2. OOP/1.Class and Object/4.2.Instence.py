class shop:
    Shopping_Mol = "Jumna"
    cart = []
    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = [] # it's an instance Attribute 
                       #thats means every buyer cart will be different
    def add_to_Cart(self,product):
        self.cart.append(product)


soumen = shop("Soumen")
soumen.add_to_Cart("Table")
soumen.add_to_Cart("chair")
print(soumen.cart)
Antora = shop("Antora")
Antora.add_to_Cart("Wordwrap")
Antora.add_to_Cart("Bike")

print(Antora.cart)
        