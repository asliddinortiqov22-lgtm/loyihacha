class Soat:
    def __init__(self, soat, daqiqa):
        self.__soat = soat
        self.__daqiqa = daqiqa

    def korsat(self):
        print(f"{self.__soat:02d}:{self.__daqiqa:02d}")

    def soatni_ber(self, soat):
        if 0 <= soat <= 23:
            self.__soat = soat
        else:
            print("Soat 0-23 oralig'ida bo'lishi kerak")

    def oshir(self, daqiqa):
        jami_daqiqa = self.__soat * 60 + self.__daqiqa + daqiqa

        jami_daqiqa %= 24 * 60

        self.__soat = jami_daqiqa // 60
        self.__daqiqa = jami_daqiqa % 60
            
s = Soat(23, 45)
s.korsat()
s.oshir(30)
s.korsat()
s.soatni_ber(25)
s.soatni_ber(9)
s.korsat()
s.oshir(150)
s.korsat()