# read only --> you can not set the value. value can not be changed
# getter --> get a value of a property through a method. Most of the time, you will get the value of a private attribute.
# setter --> set a value of a property through a method. Most of the time, you will set the value of a private property.


class User:
    def __init__(self,name,age , money) -> None:
        self._name = name
        self._age = age 
        self.__money = money

        # getter without any setter is readonly attribute
    @property 
    # @ is present in anything then we will call it a Decorator
    
    def age(self):
        return self._age
    
    # Getter
    @property
    def salary (self):
        return self.__money
    

    # Setter
    @salary.setter
    def salary(self,value):
        if value<0:
            print("you are a cheater ")
        self.__money += value

samsu = User("Kopa",21,1000)
# print(samsu.__money)

# print(samsu.age())
print(samsu.age)

# print(samsu.salary())

samsu.salary = 3400
print(samsu.salary)