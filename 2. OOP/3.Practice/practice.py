class Product:
   def __init__(self,product) -> None:
        self.product = product
        self.products = []
    

class Shop(Product):
    def __init__(self, product) -> None:
        super().__init__(product)


    def add_product(self,product):
        self.products.append(product)

    def byProduct(self,product):
       
        if(product in self.products):
            print("Thank you so much For visiting and buying some thing from our shop ")



watch = Shop("Watch")
watch.add_product("Watch")
watch.add_product("Add nothing ")
print(watch.products)
watch.byProduct("Watch")