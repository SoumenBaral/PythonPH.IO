# Inheritance VS composition

class Cpu:
    def __init__(self,cores) -> None:
        self.cores = cores

class RAM :
    def __init__(self,size) -> None:
        self.size = size 
class HardDrive :
    def __init__(self,capacity) -> None:
        self.capacity = capacity
    
# Computer has a cpu
# Computer has RAM 
# Computer has a HardDrive

class Computer:
    def __init__(self,cores,rmSize,hdCapacity) -> None:
        self.cores = Cpu(cores)
        self.rmSize = RAM(rmSize)
        self.hdCapacity = HardDrive(hdCapacity)
    
Mac = Computer(8, 16,512)