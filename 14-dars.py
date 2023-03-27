# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 17:00:18 2023

@author: LENOVO
"""

# birinchi topshiriq

# dadam = {"ism":"Mamatqobil", "tug_ulgan_yili":"1963", "tug_ulgan_joyi":"Jizzax viloyati Zomin tumani"}

# print(f"Dadamning ismi {dadam['ism']}, tug\'ulgan yili {dadam['tug_ulgan_yili']}-yil, tug\'ulgan joyi {dadam['tug_ulgan_joyi']}")

# ikkinchi topshiriq

# sevimli_taomlar = {"Dadam":"osh", "Opam":"xonim", "Sadoqat_opcham":"manti", "Sabohat_opcham":"dimlama","Nazira_opcham":"shashlik", "Akam":"g'ilmindi"}

# print(f"Dadamning yaxshi ko'rgan taomi: {sevimli_taomlar['Dadam']}")

# print(f"Opamning yaxshi ko'rgan taomi: {sevimli_taomlar['Opam']}")

# print(f"Sadoqat opchamning yaxshi ko'rgan taomi: {sevimli_taomlar['Sadoqat_opcham']}")

# uchunchi topshiriq

python_lug_at = {"integer":"Butun qiymatlar qabul qiladi",
                 "float":"O'nli va butun sonlarni qabul qiladi",
                 "string":"Faqat matlarni qabul qiladi",
                 "del":"List va lug'atlardan elementlarni o'chiradi",
                 "len":"Elementning uzunligi yoki ichidagi qiymatlarning sonini ko'rsatadi",
                 "range":"sonli list yaratish uchun ishlatiladi",
                 "apport":"listga elemet qo'shish uchun ishlatiladi",
                 "title":"Bosh har qilish uchun ishlar=tiladi",
                 "if":"yoki operatori ikki qiymat qabul qiladi",
                 "for":"uchun degan ma'noni bildiradi va takrorlash vazifasini bildiradi"
                 }

# to'rtinchi topshiriq

so_z = input(f"Kalit so'zni kiriting: ")

chiqish = python_lug_at.get("string", "Bunday so'z mavjud emas")

print(chiqish)

#print(f"{python_lug_at[f'{so_z}']}")

# beshinchi topshiriq

# so_z = input(f"Kalit so'zni kiriting: ")

# if so_z in python_lug_at:
#     print(f"{python_lug_at[f'{so_z}']}")
# else:
#     print("Bunday so'z mavjud emas!")






