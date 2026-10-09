# class Kitob:
#     def __init__(self, nomi, muallif):
#         self.nomi = nomi
#         self.muallif = muallif
#         self.band = False

# class Azo:
#     def __init__(self, ism):
#         self.ism = ism

# class Kutubxona:
#     def __init__(self):
#         self.kitoblar = []

#     def kitob_qosh(self, kitob):   
#         self.kitoblar.append(kitob)

#     def topish(self, nomi):
#         for kitob in self.kitoblar:
#             if kitob.nomi == nomi:
#                 return kitob

#     def berish(self, kitob, azo):
#         if kitob.band:
#             print(f"'{kitob.nomi}' hozir band")
#         else:
#             kitob.band = True
#             print(f" {azo.ism} '{kitob.nomi}' kitobini oldi ")

#     def qaytarish(self, kitob):
#         kitob.band = False
#         print(f"'{kitob.nomi}' qaytarildi") 

#     def royxat(self):
#         for kitob in self.kitoblar:
#             holat = "band" if kitob.band else "bosh"
#             print(f"-{kitob.nomi}: {holat}") 

# kutubxona  = Kutubxona()

# kutubxona.kitob_qosh(Kitob("O'tkan kunlar", "Abdulla Qodiriy"))
# kutubxona.kitob_qosh(Kitob("Shum bola", "G'afur G'ulom"))

# ali = Azo("Ali")
# vali = Azo("Vali")

# kitob = kutubxona.topish("Shum bola")
# kutubxona.berish(kitob, ali)
# kutubxona.berish(kitob, vali)
# kutubxona.royxat()











