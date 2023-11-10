class Engine:
    def __init__(self) -> None:
        pass
    def start(self):
        print("Engine Started") 
class Driver:
    def __init__(self) -> None:
        pass

# Car has a Engine 

class car:
    def __init__(self) -> None:
        self.engine = Engine()
        self.driver = Driver()
    
    def start(self):
        self.engine.start()

vulate = car()

vulate.start()
