from Menu import Pizza , Burger,Drinks,Menu 
from Restaurant import Restaurant
from Users import Chef,Server,Customer,Manager
from Order import Order
def main ():
    menu = Menu()

    # add Pizza to the menu
    pizza1 = Pizza("Shutkhi pizza",1200,"large",["shutki","onion","oil"])
    menu.addMenuItems("pizza",pizza1)
    pizza2 = Pizza("Potato pizza",3992 ,"medium",["potato","oil","turmeric"])
    menu.addMenuItems("pizza",pizza2)
    pizza3 = Pizza("dal pizza",499,"large",["Dal","chile","chrisPe"])
    menu.addMenuItems("pizza",pizza3)

    # Add Burger to the menu 

    burger1 = Burger("naga burger",2352,"chicken",["chicken","bread","chili"])
    menu.addMenuItems("burger",burger1)
    burger2 = Burger("nagin burger",2352,"chicken",["snake","bread","chili"])
    menu.addMenuItems("burger",burger2)

    # add Drinks to the menu 

    drinks1 = Drinks("funTa",30,True)
    menu.addMenuItems("drink",drinks1)
    drinks2 = Drinks("MunTa",30,False)
    menu.addMenuItems("drink",drinks2)

    menu.showMenu()


    # Restaurant :

    restaurant = Restaurant("Sai Baba ",1800,menu)


    # Add Employee to the restaurant
    manager = Manager("Kala chan",12000,"30 jan 2022","Core",34,"kala@Omuk.com","kaloPur")

    restaurant.addEmployee("manager",manager)

    chef = Chef("Rustum Baburci",3400,"3 fed 2016","kahi",3432,"kahidai@baburchi.com","BaburchiPara","mular jhol")
    restaurant.addEmployee("chef",chef)

    server = Server("chtu server",3400,"22 fed 2023","givenTake",3432,"chotu@server.com","BePara")
    restaurant.addEmployee("server",server)

    # showing employees:
    restaurant.ShowEmployee()


    # Customer:
    customer1 = Customer("Dudu mia ",10009,23424,"dudu32@gmail.com","buk bazar")
    customer2 = Customer("kodu mia ",20002,523424,"kodu342@gmail.com","koku bazar")
    customer3 = Customer("chodu mia ",13002,623424,"chodu32@gmail.com","Jomjom")
    customer4 = Customer("Modu mia ",50002,8923424,"Modu32@gmail.com","buk bazar")
    customer5 = Customer("Bidu mia ",67002,123424,"Bidu32@gmail.com","buk bazar")

    # Customer one placing Order 
    order1 = Order(customer1,[pizza3,drinks2,pizza3,drinks2])
    customer1.placeAOrder(order1)
    restaurant.AddOrder(order1)

    restaurant.receivePayment(55220,order1,customer1)
    print("Revenue and Balance after first Customer: ",restaurant.revenue,restaurant.balance)

    # Customer two placing Order 
    order2 = Order(customer2,[pizza3,burger1,drinks2,burger2,pizza2])
    customer2.placeAOrder(order2)
    restaurant.AddOrder(order2)

    restaurant.receivePayment(105022,order2,customer2)
    print("Revenue and Balance after second Customer: ",restaurant.revenue,restaurant.balance)

    #  pay rant 

    restaurant.payExpense(restaurant.rent,"Rent")
    print("Revenue and Balance after pay Rent: ",restaurant.revenue,restaurant.balance ,restaurant.expense)
    restaurant.PaySalary(chef)
    print("Revenue and Balance after pay Rent and salary : ",restaurant.revenue,restaurant.balance ,restaurant.expense)

#Call the main  
if __name__ == '__main__':
    main()