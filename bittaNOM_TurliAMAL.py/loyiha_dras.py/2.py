class Mahsulot:
    def __init__(self, nomi, narx, soni):
        self.nomi = nomi
        self.__narx = narx
        self.__soni = soni

    def narxni_ol(self):
        return self.__narx

    def sonini_ol(self):
        return self.__soni    

    def narxni_ber(self, narx):
        if narx > 0:
            self.__narx = narx
        else:
            print("Narx musbat bolishi kerak")

    def sotish(self, miqdor):
        if miqdor > self.__soni:
            print(f"Omborda faqat {self.__soni} ta bor")
        else:
            self.__soni -= miqdor
            jami = miqdor * self.__narx
            print(f"{miqdor} ta sotildi. Jami: {jami} som")

m = Mahsulot("Daftar", 5000, 20)
m.sotish(3)
m.narxni_ber(-100)
m.narxni_ber(6000)
m.sotish(30)
m.sotish(17)
print(m.sonini_ol())                
