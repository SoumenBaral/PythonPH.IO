class Person :
    def __init__(self,name,age,height ,weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def eat(self):
        print("vat , meat , fish, water .")
    def exercise(self):
        raise NotImplementedError

class Cricketer(Person):
    def __init__(self, name, age, height, weight,team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)
        # Child class method over write the parent class same method 
    def eat(self):
        print("vegetable")
    def exercise(self):
        print("Gym is mandatory")

    # + sign operator Overload   
    def __add__(self,other):
        return self.age+other.age
    # * sign operator Overload
    def __mul__(self,other):
        return(self.height * other.height)
    # length overloading
    def __len__(self):
        return self.weight
    
    # Gater then Overloading

    def __gt__(self,other):
        return self.age>other.age
    

Shakib = Cricketer("Shakib all Hasan", 35, 5.6,70,"Bangladesh") 
Mushi = Cricketer("mushi",34,5.4,50,"Bangladesh")
# Shakib.eat()
# Shakib.exercise()

#---------------- Overloading........................
# =====================================================

# plus sign overloading

print(3 + 5)
print("Shakib"+"Rakib")
print([32,53,533]+ [3,4,6,2,10])

print(Shakib+Mushi)
print(Shakib*Mushi)
print(len(Shakib))
print(Shakib>Mushi)
# print(dir(int))