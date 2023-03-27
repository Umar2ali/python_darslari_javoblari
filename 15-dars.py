# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 08:53:06 2023

@author: LENOVO
"""

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
# Birinchi topshiriq

# for kalit, qiymat in python_lug_at.items():
#     print(f"{kalit.title()} - {qiymat}")

# Ikkinchi topshiriq

# davlatlar_va_poytaxtlar = {"O'zbekiston":"Toshkent",
#                            "Qozog'iston":"Olmaota",
#                            "Qirg'iziston":"Bishkek",
#                            "Tojikiston":"Dushanbe",
#                            "Turkmaniston":"Ashhaobod",
#                            "Rossiya":"Moskova",
#                            "Xitoy":"Pekin",
#                            "Avg'oniston":"Kobul",
#                            "Eron":"Tehron",
#                            "Turkiya":"Anqara",
#                            "Pokiston":"Islomobod"}

# print("Duyo davlatlari: ")

# for kalit in sorted(davlatlar_va_poytaxtlar):
#     print(f"{kalit}")

# print("Dunyo davlatlari poytahtlari:")

# for qiymat in sorted(davlatlar_va_poytaxtlar.values()):
#     print(f"{qiymat}")

# Uchinchi topshiriq

# ixtiyoriy_davlat = input(f"Qaysi davlatning poytaxtini bilishni istaysiz? ")

# print(davlatlar_va_poytaxtlar.get(ixtiyoriy_davlat, "Kechirasiz, bizda bu haqida ma'lumot yo'q!"))

# To'rtinchi topshiriq

restaran_taomlari = {"osh":15000,
                     "xonim":7000,
                     "sho'rva":14000,
                     "beshbarmoq":20000,
                     "chuchvara":18000,
                     "go'ja":20000,
                     "lavash":16000,
                     "tovuqli somsa":8000,
                     "ko'ksomsa":27000,
                     "jizzax somsa":25000}

buyurtmalar = []

print("Uchta taom buyurtma qiling!")

for n in range(3):
    buyurtmalar.append(input(f"{n+1} - taomni kiriting: "))


for buyurtma in buyurtmalar:
    if buyurtma in restaran_taomlari:
        print(f"{buyurtma}ning narhi : {restaran_taomlari[buyurtma]}")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q")






