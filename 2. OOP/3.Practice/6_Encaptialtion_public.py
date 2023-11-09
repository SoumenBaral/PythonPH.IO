"""
What is Encapsulation: 
   Ans: Data and Method are binding in a single unit
   Encapsulation = single Unit(Data + method)

"""

class Student :
    def __init__(self,name , Id) -> None:
        self.name = name 
        self.Id = Id
    
    def details(self):
 
       print(f"Name : {self.name} ID : {self.Id}")


obStudent = Student("Rahim",25)

print("Before Re-assign")
obStudent.details()

print("After Re-assign")
obStudent.id = -30 #reassign and dont show any error

obStudent.details()