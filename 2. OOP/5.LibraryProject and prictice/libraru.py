class Book :
    def __init__(self,name,id,author,quantity) -> None:
        self.name     = name
        self.id       = id
        self.author   = author
        self.quantity = quantity

class User:
    def __init__(self,name,id,password) -> None:
        self.name        = name 
        self.id          = id
        self.password    = password
        self.borrowBooks = []
        self.returnBooks = []

class Library:
    def __init__(self,name) -> None:
        self.name = name
        self.users = []
        self.books = []

    def addBook(self,id,name,quantity,author):
        for book in self.books:
            if book.id == id:
                print(f"\n\t---> !! Book Id {book.id} already exists")
                return
        book = Book(name,id,author,quantity)
        self.books.append(book)
        print(f"{book.quantity} of book : {book.name}  added in the library successfully")


    def addUser(self,name,id,password):

        for user in self.users:
            if user.id == id:
                print(f'{id} user is Already exist')
                return
        user = User(name,id,password)
        self.users.append(user)
        print(f" Welcome to our library MemberShip sir, {user.name}")
        return user

bsk = Library("Waste of time ")
bsk.addBook(101,"cp_Boss",4,"Dane Danial")
Soumen = bsk.addUser("Soumen",111,"func") 
Admin  = bsk.addUser("Admin",102,"lucky")

currentUser  = Admin
changeOfUser = True

while True:
    if currentUser == None :
        print("\n\t--->!!! No logged in user\n")

        option = input("Login or Register (L/R) : ")

        if option == "L":
            id       = int(input("Enter you Id : "))
            password = input("Enter your Password : ")

            match = False
            for user in bsk.users:
                if user.id == id and user.password == password:
                    currentUser  = user
                    changeOfUser = True
                    match        = True
                    break
            if match == False:
                print("\n\t---> No user Found !\n")
        
        elif option == "R":
            id   = int(input("Enter a new Id : "))
            name = input("Enter your Name : ")
            password = input("Enter a Strong Password : ")
                   

