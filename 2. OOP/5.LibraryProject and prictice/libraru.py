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
    def  borrowBook(self,user,token):
        for book in self.books:
            if book.id == token:
                if book in user.borrowBooks:
                    print("\n\t---> Already borrowed !")
                    return
                elif book.quantity==0:
                    print("\n\t---> No Copy Available !")
                    return
                else:
                    user.borrowedBooks.append(book)
                    book.quantity-=1
                    print(f"\n\t---> Borrowed {book.name} Succesfully !")
                    return
        print(f"\n\t---> Not found any book with id: {token} !")
               


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

            for user in bsk.users:
                if user.id==id:
                   print(f"this {id} Id is already Exist in library")
                   break
            user = bsk.addUser(name,id,password)
            currentUser = user
            changeOfUser = True

    else:
        if changeOfUser:
            print("\n------------------------------------")
            print(f"\tWelcome Back {currentUser.name} !")
            print("------------------------------------")
            changeOfUser=False
        else:
            print("\n\t<---------------------------->")

        if currentUser.name == "Admin":

            print("Options:\n")
            print("1: Add book")
            print("2: Show users")
            print("3: Show all books")
            print("4: Logout")


            ch = int(input("Enter Options : "))

            if ch == 1:
                id=int(input("\tEnter book id:"))
                name=input("\tEnter book name:")
                quantity=int(input("\tEnter No of books:"))
                author = input("Enter the Author Name : ")

                bsk.addBook(id,name,quantity,author)

            elif ch == 2 :
                print("\n\tUsers:\n")
                print(f'\tName\tReading Now\tAlready Read')
            
                for user in bsk.users:
                    if user.name!="admin":
                        print(f'\t{user.name}\t\t{len(user.borrowedBooks)}\t\t{len(user.returnedBooks)}')
                  
            elif ch == 3:
                print("\n\tBook List:\n")

                for book in bsk.books:
                    print(f'\t{book.id}\t{book.name}\t{book.quantity}')
            elif ch==4:
                currentUser=None
             
            else:
                print("\n\t---> !!! Choose Valid Option\n")

        else:
            print("Options:\n")
            print("1: Borrow Book")
            print("2: Return Book")
            print("3: Show All Books")
            print("4: Show Borrowed books")
            print("5: Show History")
            print("6: Logout") 

        


             

