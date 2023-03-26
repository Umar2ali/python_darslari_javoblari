# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 18:11:58 2023

@author: LENOVO
"""

#juft_son = int(input(f"Juft son kiriting: "))

#son = juft_son%2

# if son == 0:
#     print(f"Raxmat!")
# else:
#     print(f"Iltimos juft son kiriting!")

# ikkinchi topshiriq

# foydalanuvchining_yoshi = int(input(f"Yoshiniz nechida? - "))

# if foydalanuvchining_yoshi <= 4 or foydalanuvchining_yoshi >=60:
#     narh = "bepul"
# elif foydalanuvchining_yoshi <= 18:
#     narh = "10000 so'm"
# else:
#     narh = "20000 so'm"

# print(f"Sizga hayvonot bog'iga kirish {narh}")

# uchunchi topshiriq

# birinchi_son = input(f"Birinchi sonni kiriting: ")

# ikkinchi_son = input(f"Ikkinchi sonni kiriting: ")

# if birinchi_son > ikkinchi_son:
#     print(f"{birinchi_son} > {ikkinchi_son}")
# else:
#     print(f"{birinchi_son} < {ikkinchi_son}")

# to'rtinchi topshiriq

# mahsulotlar = ["olma", "banan", "pomidor", "kartoshka", "gilos", "guruch", "makaron", "mosh", "karam", "bodiring"]

# savat = []

# for n in range(5):
#     savat.append(input(f"{n+1} - mahsulot nomini kiriting: ")) 

# for buyurtma in savat:
#     if buyurtma in mahsulotlar:
#         print(f"Do'konimizda {buyurtma} bor")
#     else:
#         print(f"Do'konimizda {buyurtma} yo'q")

# beshinchi topshiriq

# mahsulotlar = ["olma", "banan", "pomidor", "kartoshka", "gilos", "guruch", "makaron", "mosh", "karam", "bodiring"]

# savat = []

# for n in range(5):
#      savat.append(input(f"{n+1} - mahsulot nomini kiriting: ")) 

# bor_mahsulotlar = []

# mavjud_emas = []

# for buyurtma in savat:
#     if buyurtma in mahsulotlar:
#         bor_mahsulotlar.append(buyurtma)
#     else:
#         mavjud_emas.append(buyurtma)

# if mavjud_emas:
#     print("Do'konimizda quyidagi mahsulotlar yo'q: ")
#     for uzunlik in range(len(mavjud_emas)):
#         print(f"{mavjud_emas[uzunlik]}")
# else:
#     print("Siz so'ragan barcha mahsulotlar bizning do'donda bor!")

# oltinchi topshiriq

# foydalanuvchilar = ["Ahmadulloh", "Behruz", "Xushnudbek", "Mubina", "Risolat"]

# yangi_foydalanuvchi = input(f"Yangi login kiriting: ")

# if yangi_foydalanuvchi in foydalanuvchilar:
#     print("Assalomu alaykum. Bu nomdagi foydalanuvchi bor. Boshqa nom tanlang!")
# else:
#     print("Assalomu alaykum. Xush kelibsiz!")

# yettinchi topshiriq

ixtiyoriy_son = int(input(f"Istalgan butun son kiriting: "))

for son in range(2,11):
    qoldiq = ixtiyoriy_son%son
    if qoldiq == 0:
        print(f"{ixtiyoriy_son} sonni {son}ga qoldiqsiz bo'linadi")











