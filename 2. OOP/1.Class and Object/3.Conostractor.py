class phone :
    Manufacture = "Chain"

    def __init__(self,owner,brand,price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def sendMMS(self,number,mms):
        text = f'we got the number of CM that is {number} and send MMs :: {mms} '
        print(text)


my_phone = phone("kala Chan Pakhi", "Oppo",8900)
print(my_phone.owner,my_phone.brand,my_phone.price)

her_phone = phone("shada chani","Iphone",120000)
print(her_phone.owner,her_phone.brand,her_phone.price)