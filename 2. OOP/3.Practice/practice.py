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



"""Inheritance:
Inheritance is a fundamental concept in object-oriented programming (OOP) that allows one class (the derived or child class) to inherit properties and behaviors from another class (the base or parent class). Inheritance promotes code reusability and the creation of a hierarchical structure of classes, with more specialized classes inheriting from more generalized ones.

Inheritance is achieved in Python through class definition and the use of the class keyword. Here's an example:"""

# Example:

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Buddy")
print(dog.speak())  # Output: Woof!

cat = Cat("Whiskers")
print(cat.speak())  # Output: Meow!


