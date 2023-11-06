class phone :
    Manufacture = "Chain"

    def __init__(self,owner,brand,price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def sendMMS(self,number,mms):
        text = f'we got the number of CM that is {number} and send MMs :: {mms} '
        print(text)