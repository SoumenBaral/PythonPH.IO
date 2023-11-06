class pen:
    manufacture = "Bangladesh"

    def __init__(self,name,price):
        self.name = name 
        self.price = price

my_pen = pen("kopa Samsu ",20)
print(my_pen.name,my_pen.price)

her_pen = pen("metaDow" ,5)
print(her_pen.name,her_pen.price)