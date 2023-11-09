class Company :
    def __init__(self,cName,location) -> None:
        self.cName = cName
        self.location = location
    def company_details(self):
        print(f"Company Name is : {self.cName} Location : {self.location}")
class Person:
    def __init__(self,name ,age) -> None:
        self.name = name 
        self.age = age 

    def person_details(self):
        print(f"Name : {self.name}, Age : {self.age}")

class employee(Company, Person):
    def __init__(self, cmpName, location,pName,Age) -> None:
    # Initialize the parent classes separately.
       Company.__init__(self,cmpName,location)
       Person.__init__(self,pName,Age)
    def emp_details(self,Salary,skill):
        print(f"Salary {Salary}  skill {skill}")

# When creating an employee object, provide values for both company and person attributes.
ob_employee = employee("Asif", 25, "Google", "USA")

ob_employee.emp_details(1500000, "Python OOP")

ob_employee.person_details()
ob_employee.company_details()