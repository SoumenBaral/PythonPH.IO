class Book:
    def __init__(self,name) -> None:
        self.name = name 
    def read (self):
        raise NotImplementedError

class physics(Book):
    def __init__(self, name,lab) -> None:
        self.lab = lab
        super().__init__(name)
    def read(self):
        print('reading is a good habit')

topon = physics("Topon",True)

print(issubclass(physics,Book))
print(isinstance(topon,physics)) # is instance means is it make by class physics
print(isinstance(topon,Book)) # is it make by it
topon.read()