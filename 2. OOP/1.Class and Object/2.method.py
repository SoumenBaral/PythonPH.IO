class phone :
    price = 20000
    brand = "Apple"
    color = "Blue"
    feature =["Camera","Hammer","Speaker"]
    def call (self): #we can use any thing but in this we will use self as a first parameter
        print("Call is Calling")
    
    def send_SMS(self , number , massage ):
        text = f"Send the massage to {number} and massage is :: {massage}"
        return text

my_phone = phone()
print(my_phone)
print(my_phone.feature)
my_phone.call()
SMS = my_phone.send_SMS(18389328923,"Don't worry I am ok Baby")
print(SMS)