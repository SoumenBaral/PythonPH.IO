class calculator:
    brand = "Casio"

    def add(self , x,y):
        print(x+y)
    def minus (self , x,y):
        print(x-y)
    def div (self , x,y):
        print(x/y)

    def mul(self,x,y):
        print(x*y)

my_calculator = calculator()

my_calculator.add(10,30)
my_calculator.minus(10,30)
my_calculator.div(10,30)
my_calculator.mul(10,30)
