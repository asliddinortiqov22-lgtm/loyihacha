class Karta:
    def __init__(self, pin, balans=0):
        self.__pin = pin
        self.__balans = balans
        self.__urinshlar = 0
        self.__bloklangan = False

    def __pin_togri(self, pin):
        if self.__bloklangan:
            print("Karta bloklangan!")
            return False

        if pin == self.__pin:
            self.__urinshlar = 0
            return True
        else:
            self.__urinshlar += 1

            if self.__urinshlar >= 3:
                self.__bloklangan = True
                print("Karta bloklandi!")
            else:
                print("PIN noto'g'ri")

            return False

    def toldirish(self, summa):
        self.__balans += summa
        print(f"Balans: {self.__balans}")

    def yechish(self, pin, summa):
        if not self.__pin_togri(pin):
            return

        if summa > self.__balans:
            print("Mablag' yetarli emas")
        else:
            self.__balans -= summa
            print(f"{summa} so'm yechildi. Balans: {self.__balans}")

    def balansni_korish(self, pin):
        if self.__pin_togri(pin):
            print(f"Balans: {self.__balans}")


k = Karta("1234")

k.toldirish(500000)

k.yechish("1234", 200000)
k.yechish("0000", 1000)
k.yechish("1111", 1000)
k.balansni_korish("9999")
k.yechish("1234", 1000)