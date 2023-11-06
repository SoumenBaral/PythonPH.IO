class shop:
    cart = [] # Cart is a class attribute that's means it will share every object
    def __init__(self,buyer):
        self.buyer = buyer

    def add_to_Cart(self,product):
        self.cart.append(product)


soumen = shop("Soumen")
soumen.add_to_Cart("Table")
soumen.add_to_Cart("chair")
Antora = shop("Antora")
Antora.add_to_Cart("Wordwrap")
Antora.add_to_Cart("Bike")

print(Antora.cart)