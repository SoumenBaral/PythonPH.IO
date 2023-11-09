"""Multilevel Inheritance """

class GrandPaa:
    def __init__(self) -> None:
        pass

    def property(self):
        print("I have 5 corer taka")
    
class father(GrandPaa):
    def __init__(self) -> None:
        super().__init__()
class child(father):
    def __init__(self) -> None:
        super().__init__()
    
ami = child()
ami.property()