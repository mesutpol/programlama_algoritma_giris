# Kullanıcıdan üç sayıyı al
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))
sayi3 = float(input("Üçüncü sayıyı girin: "))

# Sayıları sırala
en_buyuk = max(sayi1, sayi2, sayi3)
en_kucuk = min(sayi1, sayi2, sayi3)
ortanca = sayi1 + sayi2 + sayi3 - en_buyuk - en_kucuk

print("Büyükten küçüğe sıralama: {}, {}, {}".format(en_buyuk, ortanca, en_kucuk))