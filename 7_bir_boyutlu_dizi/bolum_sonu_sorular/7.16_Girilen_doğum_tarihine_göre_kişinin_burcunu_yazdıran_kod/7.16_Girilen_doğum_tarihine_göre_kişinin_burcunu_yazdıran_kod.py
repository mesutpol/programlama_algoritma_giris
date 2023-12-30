
#1. Burçları bir diziye yerleştirin.
#2. Kullanıcıdan doğum tarihini isteyin.
#3. Doğum tarihinin gününü ve ayını alın.
#4. Doğum tarihine göre burcu bulun.
#5. Burcu ekrana yazdırın.


burçlar = ["Oğlak", "Kova", "Balık", "Koç", "Boğa", "İkizler", "Yengeç", "Aslan", "Başak", "Terazi", "Akrep", "Yay"]

# Kullanıcıdan doğum tarihini isteyin
gün = int(input("Doğum gününüzün gününü girin: "))
ay = int(input("Doğum gününüzün ayını girin: "))

# Doğum tarihine göre burcu bulun
if gün <= 20:
    burç = burçlar[ay - 1]
else:
    burç = burçlar[ay]

# Burcu ekrana yazdırın
print("Burcunuz:", burç)
