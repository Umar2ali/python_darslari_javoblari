# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 10:22:32 2023

@author: LENOVO
"""

ismlar =["Ibrohim", "Anvar", "Yusuf", "Jamol", "Kamol"]

#for ism in ismlar:
#    print(f"Assalomu alaykum {ism}")
#print("Kod ", len(ismlar), "marta takrorlandi")

o_ndan_yuzgacha_toq_sonlar = list(range(11,100,2))

#for son in o_ndan_yuzgacha_toq_sonlar:
#    print(f"{son}ning kubi {son**3} ga teng")

kinolar = []

#print("5 ta eng yaxshi ko'rgan kinongiz qaysi?")

#for kino in range(5):
#    kinolar.append(input(f"{kino+1}-eng yaxshi ko'rgan kinongizni kiriting: "))
#print(kinolar)



kishilar_soni = input("Bugun necha kishi bilan uchrashdingiz: ")

uchrashgan_kishilar_ismi = []

for son in range(int(kishilar_soni)):
    uchrashgan_kishilar_ismi.append(input(f"{son+1}-uchrashgan odamingiz kim: "))

print(uchrashgan_kishilar_ismi)

