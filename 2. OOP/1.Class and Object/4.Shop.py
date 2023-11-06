class shop:
    cart = [] # Cart is a class attribute that's means it will share every object
    def __init__(self,buyer):
        self.buyer = buyer

    def add_to_Cart(self,product):
        self.cart.append(product)