class Foydalanuvchi:
    def __init__(self, login, parol):
        self.login = login
        self.__parol = parol

    def parolni_tekshir(self, parol):
        return self.__parol == parol
            
    def parolni_ozgartir(self, eski, yangi):
        if not self.parolni_tekshir(eski):
            print("Eski parol notogri")
        elif len(yangi) < 6:
            print("Parol kamida 6 belgidan iborat bo'lishi kerak")
        else:
            self.__parol = yangi 
            print("Parol ozgartirildi")     


u = Foydalanuvchi("ali_01", "qwerty")
print(u.parolni_tekshir("12345"))
u.parolni_ozgartir("111111", "abcdef")
u.parolni_ozgartir("qwerty", "abc")
u.parolni_ozgartir("qwerty", "yangi123")
print(u.parolni_tekshir("yangi123"))