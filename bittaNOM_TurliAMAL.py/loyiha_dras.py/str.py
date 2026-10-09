# class Kitob:
#     def __init__(self, nomi, muallif):
#         self.nomi = nomi
#         self.muallif = muallif

#     def __str__(self):
#         return f"{self.nomi}, {self.muallif}" 

# kitob = Kitob("O'tkan kunlar", "Abdulla Qodiriy")
# print(kitob)






# class Shaxs:
#     def __init__(self, ism, yosh):
#         self.ism = ism
#         self.yosh = yosh

#     def __add__(self, boshqa):
#         return self.yosh + boshqa.yosh

# p1 = Shaxs("Ali", 22)
# p2 = Shaxs("Vali", 19)

# print(p1 + p2)







# class Pul:
#     def __init__(self, summa):
#         self.summa = summa

#     def __add__(self, boshqa):
#         return self.summa + boshqa.summa

#     def __str__(self):
#         return f"{self.summa} so'm"

# m1 = Pul(50000)
# m2 = Pul(25000)        

# umumiy_qiymat = m1 + m2
# m3 = Pul(umumiy_qiymat)
# print(m3)









# class Masofa:
#     def __init__(self, km):
#         self.km = km

#     def __str__(self):
#         return f"{self.km} km"

#     def __add__(self, boshqa):
#         return Masofa(self.km + boshqa.km)  
        
        

# yosh1 = Masofa(12) 
# yosh2 = Masofa(30)  
# yosh3 = Masofa(8)

# masofa = Masofa(yosh1 + yosh2 + yosh3)



# print(masofa)












# class Pul:
#     def __init__(self, summa):
#         self.summa = summa

#     def __str__(self):
#         return f"{self.summa} so'm"

#     def __add__(self, boshqa):
#         return Pul(self.summa + boshqa.summa)

#     def __eq__(self, boshqa):
#         return self.summa ==  boshqa.summa

#     def __lt__(self, boshqa):
#         return self.summa < boshqa.summa

# m1 = Pul(30000)
# m2 = Pul(20000)
# m3 = Pul(50000)

# print(m1 + m2)
# print(m1 + m2 == m3)
# print(m2 < m1)
    




