class Odam:
    def __init__(self, ism):
        self.ism = ism

    def gapir(self):
        return f"Mening ismim {self.ism}"


class Xaridor(Odam):
    def __init__(self, ism):
        self.ism = ism
        self.xarid_savati = Savat()  

    def gapir(self):
        return f"Xaridor: {self.ism}"


class Savat:
    def __init__(self):
        self.buyumlar = []  
    def solish(self, buyum):
        self.buyumlar.append(buyum)

    def hisobla(self):
        jamul_jam = 0
        for har_bir_buyum in self.buyumlar:
            jamul_jam += har_bir_buyum.narxni_korsat()
        return jamul_jam


class Buyum:
    def __init__(self, nomi, narxi):
        self.nomi = nomi
        self.__narxi = narxi  

    def narxni_korsat(self):
        return self.__narxi

    def __str__(self):
        return f"{self.nomi} - {self.__narxi} so'm"

b1 = Buyum("Noutbuk", 10000000)
b2 = Buyum("Sichqoncha", 120000)

xaridor = Xaridor("Ali")

xaridor.xarid_savati.solish(b1)
xaridor.xarid_savati.solish(b2)

print(xaridor.gapir())
print("Birinchi buyum:", b1)
print("Birinchi buyum:", b2)
print("Jami to'lov:", xaridor.xarid_savati.hisobla(), "so'm")
