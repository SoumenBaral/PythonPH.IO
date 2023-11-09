"""Hierarchical Inheritance"""
class Parent :
    def __init__(self,name) -> None:
        self.name = name 
    
    def showInfo(self):
        print(f"the name of the parent is {self.name}")

class Child1(Parent):
    def __init__(self, name,hobby) -> None:
        super().__init__(name)
        self.hobby = hobby
    def showInfo(self):
        super().showInfo()
        print(f"{self.name}'s child's  hobby is {self.hobby}")
    
class Child2(Parent):
    def __init__(self, name,school) -> None:
        super().__init__(name)
        self.school = school
    def showInfo(self):
        super().showInfo()
        print(f"{self.name}'s child's school is {self.school}")
    
# Creating instances of the classes
parent = Parent("John")
child1 = Child1("Alice", "Painting")
child2 = Child2("Bob", "XYZ School")

parent.showInfo()
child1.showInfo()
child2.showInfo()

