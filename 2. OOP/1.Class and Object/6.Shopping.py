class Shopping:

    def __init__(self,name):
        self.name = name 
        self.cart = [] # instance cart individual cart 

    def add_to_cart(self,item ,price ,quantity):
        product = {"Item " : item , "price":price, "Quantity": quantity}
        self.cart.append(product)
    
    def remove_form_cart(self,item):
        for product in self.cart:
            if item in product.values():
                print(f"found the item --> {item} from the product --->{product}")
                self.cart.remove(product)
                print(self.cart)
                break
            else:
                print('Not found')    


    
    def checkout(self ,amount):
        total = 0
        for product in self.cart:
            # print(type(product['price']))
            total += product['price']*product['Quantity']
        print(total)
        if(total==amount):
            print("Thank you , you may go now ")

        elif(total>amount):
            extra = total-amount
            print(f"you have to pay extra : {extra} Tk")
        else:
            extra = amount-total
            print(f"take your extra money : {extra} tk and Thank you for visiting my shop come again sir, {self.name}")

swapan = Shopping('Alan Swapon')
swapan.add_to_cart('alu', 50, 6)
swapan.add_to_cart('dim', 12, 24)
swapan.add_to_cart('rice', 50, 5)

print(swapan.cart)    
swapan.checkout(600)

swapan.checkout(1600)
swapan.remove_form_cart('alu')

