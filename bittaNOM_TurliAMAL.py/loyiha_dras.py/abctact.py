# from abc import ABC, abstractmethod

# class Shakl(ABC):
#     @abstractmethod   
#     def yuza(self):
#         pass

# class Kvadrat(Shakl):
#     def __init__(self, tomon):
#         self.tomon = tomon


#     def yuza(self):
#         return self.tomon ** 2

# class Doira(Shakl):
#     def __init__(self, raidus):
#         self.raidus = raidus


#     def yuza(self):
#         return 3.14 * self.raidus ** 2

# for x in [Kvadrat(4), Doira(5)]:
#     print(x.yuza())        
    










from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def gildirak(self):
        pass

class Mashina(Transport):
    def __init__(self, a):
        self.a = a

    def gildirak(self):
        return self.a  


class Velosiped(Transport):
    def __init__(self, a):
        self.a = a

    def gildirak(self):
        return self.a   


for x in [Mashina(4), Velosiped(2)]:
    print(x.gildirak())    