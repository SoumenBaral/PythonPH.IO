from Menu import Pizza , Burger,Drinks,Menu 

def main ():
    menu = Menu()

    # add Pizza to the menu
    pizza1 = Pizza("Shutkhi pizza",1200,"large",["shutki","onion","oil"])
    menu.addMenuItems("pizza",pizza1)
    pizza2 = Pizza("Potato pizza",399 ,"medium",["potato","oil","turmeric"])
    menu.addMenuItems("pizza",pizza2)
    pizza3 = Pizza("dal pizza",499,"large",["Dal","chile","chrisPe"])
    menu.addMenuItems("pizza",pizza3)

    # Add Burger to the menu 

    burger1 = Burger("naga burger",235,"chicken",["chicken","bread","chili"])
    menu.addMenuItems("burger",burger1)
    burger2 = Burger("nagin burger",235,"chicken",["snake","bread","chili"])
    menu.addMenuItems("burger",burger2)

    # add Drinks to the menu 

    drinks1 = Drinks("funTa",30,True)
    menu.addMenuItems("drinks",drinks1)
    drinks2 = Drinks("MunTa",30,False)
    menu.addMenuItems("drinks",drinks2)

#Call the main  
if __name__ == '__main__':
    main()