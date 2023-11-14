class Food:
    def __init__(self,name , price) -> None:
        self.name = name 
        self.price = price
        self.CookingTime = 12
    

class Burger(Food):
    def __init__(self, name, price,meat ,ingredients) -> None:
        super().__init__(name, price)
        self.meat = meat
        self.ingredients = ingredients
    
class Pizza(Food):
    def __init__(self, name, price,size ,topping) -> None:
        super().__init__(name, price)
        self.size = size
        self.topping = topping
    
class Drinks(Food):
    def __init__(self, name, price,isCold = True) -> None:
        super().__init__(name, price)
        self.isCold = isCold

# composition

class Menu:
    def __init__(self) -> None:
        self.pizzas = []
        self.burgers = []
        self.drinks = []

    def addMenuItems(self,ItemType,item):
        if ItemType == "pizza":
            self.pizzas.append(item)
        elif ItemType == "burger":
            self.burgers.append(item)
        elif ItemType == "drink":
            self.drinks.append(item)
    def removePizza(self,pizza):
        if pizza in self.pizzas:
            self.pizzas.remove(pizza)
    
    def showMenu(self):
        for pizza in self.pizzas:
            print(f'name: {pizza.name} price : {pizza.price}')
        for burger in self.burgers:
            print(f'Name : {burger.name } Price : {burger.price}')
        for drink in self.drinks:
            print(f'Name : {drink.name } price: {drink.price}')
        
        