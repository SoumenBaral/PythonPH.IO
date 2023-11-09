class User:
    def __init__(self,name,age , money) -> None:
        self.name = name
        self.age = age 
        self.__money = money

samsu = User("Kopa",21,1000)
print(samsu.__money)