# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 14:37:01 2023

@author: LENOVO
"""

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']

#for car in cars:
#    if car == 'gm':
#        print(car.upper())
#    else:
#        print(car.title())


#for car in cars:
#    if car != 'gm':
#        print(car.title())
#    else:
#        print(car.upper())


#ism = input(f"Ismingiz: ")

#if ism.lower() == 'admin':
#    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
#else:
#    print(f"Xush kelibsix, {ism.title()}")


#son1, son2 = input(f"Birinchi sonni kiriting: "), input(f"Ikkinchi sonni kiriting: ")

#if son1 == son2:
#    print("Sonlar teng")
#else:
#    if son1 <= son2:
#        print(f"{son1}, {son2} dan kichkina")
#    else:
#        print(f"{son1}, {son2} dan katta")

ixtiyoriy_son = int(input(f"Istalgan sonni kiriting: "))

#if ixtiyoriy_son < 0:
#    print(f"{ixtiyoriy_son} - manfiy")
#else:
#    if ixtiyoriy_son == 0:
#        print(f"son nolga teng")
#    else:
#        print(f"{ixtiyoriy_son} - musbat")

if ixtiyoriy_son < 0:
    print(f"Musbat son kiriting!")
else:
    print(f"{ixtiyoriy_son} ning kvadrat ildizi {int(ixtiyoriy_son**(1/2))}")






