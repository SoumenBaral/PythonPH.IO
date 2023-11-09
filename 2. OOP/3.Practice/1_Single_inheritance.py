"""Single Inheritance """

class Animal :
    def __init__(self,name) -> None:
        self.name = name 
    def eat(self):
        print(f'{self.name} is eating')
        print(f'{self.name} is eating 2')
    
class Cat(Animal):
    def __init__(self, name) -> None:
        # self.name = name 
        Animal.__init__(self,name)
        # super().__init__(name)

cat = Cat("Cat")
cat.eat()